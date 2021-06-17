import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
import time
import tqdm
from tensorflow.keras import layers
from PIL import Image
from IPython import display
#See bottom for Dataset used
#Requires 2 folders: "output" and "images"(Data location)

def createGenerator(seed_size, channels, GEN_RESOLUTION):
    """Function that creates a generator model."""
    model = tf.keras.Sequential()
    model.add(layers.Dense(4 * 4 * 256, activation = "relu", input_dim = seed_size))
    model.add(layers.Reshape((4, 4, 256))) #shapes the layer

    model.add(layers.UpSampling2D())
    model.add(layers.Conv2D(256, kernel_size = 3,padding = "same"))
    model.add(layers.BatchNormalization(momentum = 0.8))
    model.add(layers.Activation("relu"))

    model.add(layers.UpSampling2D())
    model.add(layers.Conv2D(256, kernel_size = 3, padding = "same"))
    model.add(layers.BatchNormalization(momentum = 0.8))
    model.add(layers.Activation("relu"))

    model.add(layers.UpSampling2D())
    model.add(layers.Conv2D(128, kernel_size = 3, padding = "same"))
    model.add(layers.BatchNormalization(momentum = 0.8))
    model.add(layers.Activation("relu"))

    if GEN_RESOLUTION > 1:
        model.add(layers.UpSampling2D(size=(GEN_RESOLUTION, GEN_RESOLUTION)))
        model.add(layers.Conv2D(128, kernel_size = 3, padding = "same"))
        model.add(layers.BatchNormalization(momentum = 0.8))
        model.add(layers.Activation("relu"))

    #final Convolutional NN layer
    model.add(layers.Conv2D(channels, kernel_size = 3, padding = "same")) #Channel = number of output filters
    model.add(layers.Activation("tanh"))

    return model
#createGenerator()


def createDiscriminator(imgShape): #Kinda like a recognition model
    """Function that creates a discriminator model."""
    model = tf.keras.Sequential()

    model.add(layers.Conv2D(32, kernel_size = 3, strides = 2, input_shape = imgShape, padding = "same"))
    model.add(layers.LeakyReLU(alpha = 0.2))

    model.add(layers.Dropout(0.25))
    model.add(layers.Conv2D(64, kernel_size = 3, strides = 2, padding = "same"))
    model.add(layers.ZeroPadding2D(padding = ((0,1), (0,1))))
    model.add(layers.BatchNormalization(momentum = 0.8))
    model.add(layers.LeakyReLU(alpha = 0.2))

    model.add(layers.Dropout(0.25))
    model.add(layers.Conv2D(128, kernel_size = 3, strides = 2, padding = "same"))
    model.add(layers.BatchNormalization(momentum = 0.8))
    model.add(layers.LeakyReLU(alpha = 0.2))

    model.add(layers.Dropout(0.25))
    model.add(layers.Conv2D(256, kernel_size = 3, strides = 1, padding = "same"))
    model.add(layers.BatchNormalization(momentum = 0.8))
    model.add(layers.LeakyReLU(alpha = 0.2))

    model.add(layers.Dropout(0.25))
    model.add(layers.Conv2D(512, kernel_size = 3, strides = 1, padding = "same"))
    model.add(layers.BatchNormalization(momentum = 0.8))
    model.add(layers.LeakyReLU(alpha = 0.2))

    model.add(layers.Dropout(0.25))
    model.add(layers.Flatten())
    model.add(layers.Dense(1, activation = "sigmoid"))

    return model
#createDiscriminator()

"""
def saveImages(cnt, noise, PRE_ROWS, PRE_COLS, PRE_MARGIN, GEN_SQUARE, generator, DATA_PATH):
    '''Function that saves an image.'''
    imgArray = np.full((
        PRE_MARGIN + (PRE_ROWS * (GEN_SQUARE + PRE_MARGIN)),
        PRE_MARGIN + (PRE_COLS * (GEN_SQUARE + PRE_MARGIN)), 3), 255, dtype = np.uint8)

    generatedImages = generator.predict(noise)
    generatedImages = 0.5 * generatedImages + 0.5

    imgCount = 0
    for row in range(PRE_ROWS):
        for col in range(PRE_COLS):
            x = row * (GEN_SQUARE + 16) + PRE_MARGIN
            y = col * (GEN_SQUARE + 16) + PRE_MARGIN

            imgArray[x:x + GEN_SQUARE, y:y + GEN_SQUARE] \
                         = generatedImages[imgCount] * 255
            imgCount += 1

    outPath = os.path.join(DATA_PATH, 'output')

    filename = os.path.join(outPath, f"train-{cnt}.png")
    img = Image.fromarray(imageArray)
    img.save(filename)
#saveImages()
"""


def generate_and_save_images(model, epoch, test_input):
    #Training is set to false
    #so all layers run in inference mode (batchnorm)(?)
    predictions = model(test_input, training=False)

    fig = plt.figure(figsize=(4,4))

    for i in range(predictions.shape[0]):
        plt.subplot(4,4, i+1)
        plt.imshow(predictions[i,:,:,0] * 127.5 + 127.5, cmap = "gray")
        plt.axis("off")

    plt.savefig("image_at_epoch_{:04d}.png".format(epoch))
    #plt.show() # Turn on later
    plt.close()
#generate_and_save_images()


def discriminatorLoss(realOutput, fakeOutput, cross_entropy):
    """Function that calculates the loss of the discriminator."""
    realLoss = cross_entropy(tf.ones_like(realOutput), realOutput)
    fakeLoss = cross_entropy(tf.zeros_like(fakeOutput), fakeOutput)
    totalLoss = realLoss + fakeLoss
    return totalLoss
#discriminatorLoss()


def generatorLoss(fakeOutput, cross_entropy):
    """Function that calculates the loss of the generator."""
    return cross_entropy(tf.ones_like(fakeOutput), fakeOutput)
#generatorLoss()


@tf.function
def train_step(images, generator, discriminator, generatorOptimizer, discriminatorOptimizer, BATCH, NOISEDIM, cross_entropy):
    print("trainstep")
    noise = tf.random.normal([BATCH, NOISEDIM])

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generatedImages = generator(noise, training = True)

        realOutput = discriminator(images, training = True)
        fakeOutput = discriminator(generatedImages, training = True)

        gen_loss = generatorLoss(fakeOutput, cross_entropy)
        disc_loss = discriminatorLoss(realOutput, fakeOutput, cross_entropy)

        gradients_of_generator = gen_tape.gradient(\
            gen_loss, generator.trainable_variables)
        gradients_of_discriminator = disc_tape.gradient(\
            disc_loss, discriminator.trainable_variables)
        generatorOptimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
        discriminatorOptimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))
        print("done")
        #return gen_loss, disc_loss
#train_step()

'''
@tf.function
def train_step(images, generator, discriminator, cross_entropy, generatorOptimizer, discriminatorOptimizer, BATCH, SEED):
    """Function that works with the train function to train both models."""
    noise = tf.random.normal([BATCH, SEED])
    print("Step")

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training = True)

        realOutput = discriminator(images, training = True)
        fakeOutput = discriminator(generated_images, training = True)
        print("Outputs")

        gen_loss = generatorLoss(fakeOutput, cross_entropy)
        print(realOutput)
        disc_loss = discriminatorLoss(realOutput, fakeOutput, cross_entropy)

        gradients_of_generator = gen_tape.gradient(\
            gen_loss, generator.trainable_variables)
        gradients_of_discriminator = disc_tape.gradient(\
            disc_loss, discriminator.trainable_variables)
        print("Gradients")
        generatorOptimizer.apply_gradients(zip(
            gradients_of_generator, generator.trainable_variables))
        discriminatorOptimizer.apply_gradients(zip(
            gradients_of_discriminator, discriminator.trainable_variables))
        print("Optimizers")
        return gen_loss, disc_loss
#train_step()
'''

def train(dataset, epochs, discriminator, generator, generatorOptimizer, discriminatorOptimizer, seed, checkpoint, checkpoint_prefix, BATCH, NOISEDIM, cross_entropy):
    for epoch in range(epochs):
        start = time.time()

        for image_batch in dataset:
            train_step(image_batch, generator, discriminator, generatorOptimizer, discriminatorOptimizer, BATCH, NOISEDIM, cross_entropy)


        print("for loop done")

        #Produce images for the GIF
        display.clear_output(wait=True)
        generate_and_save_images(generator, epoch + 1, seed)

        #save model every 15 seconds
        if (epoch + 1) % 15 == 0:
            checkpoint.save(file_prefix = checkpoint_prefix)

        print("time for epoch {} is {} sec".format(epoch + 1, time.time()-start))
    #Generate after final epoch
    display.clear_output(wait=True)
    generate_and_save_images(generator,epochs,seed)
    generator.save("FaceGenerator.model")
    discriminator.save("FaceDiscriminator.model")
#train()

    
'''
def train(PRE_ROWS, PRE_COLS, PRE_MARGIN, GEN_SQUARE, DATA_PATH, SEED, dataset, epochs, generator, discriminator, cross_entropy, generatorOptimizer, discriminatorOptimizer, BATCH):
    """"Function that trains both models."""
    fixedSeed = np.random.normal(0, 1, (PRE_ROWS * PRE_COLS, SEED))
    start = time.time()
    print(dataset)
    for epoch in range(epochs):
        print("Epoch {}".format(epoch))
        Epochstart = time.time()
        """
        gen_loss_list = []
        disc_loss_list = []
        """
        for img_batch in dataset:
            train_step(img_batch, generator, discriminator, cross_entropy, generatorOptimizer, discriminatorOptimizer, BATCH, SEED)
            print("Done")
            """
            gen_loss_list.append(t[0])
            disc_loss_list.append(t[1])
            """
        """
        g_loss = sum(gen_loss_list) / len(gen_loss_list)
        d_loss = sum(disc_loss_list) / len(disc_loss_list)

        epochElapsed = time.time() - Epochstart
        print('Epoch {}, gen_loss = {}, disc_loss = {}, {}'.format(epoch + 1, g_loss, d_loss, epochElapsed))
        """
        saveImages(epoch, fixedSeed, PRE_ROWS, PRE_COLS, PRE_MARGIN, GEN_SQUARE, generator, DATA_PATH)
        print("Training time: {}".format(time.time()-start))
    generator.save("FaceGenerator.model")
    discriminator.save("FaceDiscriminator.model")
#train()
'''

def main():
    """Main function of the program."""
    print("Hello World!")
    GENERATE_RESOLUTION = 3
    GEN_SQUARE = 32 * GENERATE_RESOLUTION
    IMG_CHANNELS = 3

    #alt way of previewing images
    PRE_ROWS = 4
    PRE_COLS = 4
    PRE_MARGIN = 16

    #seed size
    SEED = 100
    BATCH = 32 #Smaller batch this time, look up later how different sizes affect training
    BUFFER = 60000 #Why this size?
    EPOCHS = 50
    PATH = "images"
    SAVEDATA = "numpyData"

    cross_entropy = tf.keras.losses.BinaryCrossentropy()
    imgShape = (GEN_SQUARE,GEN_SQUARE,IMG_CHANNELS)

    trainingData = []
    trainingBinPath = os.path.join(PATH,
        f'training_data_{GEN_SQUARE}_{GEN_SQUARE}.npy')
    SAVE_LOCATION = os.path.join(PATH, SAVEDATA)



    generator = createGenerator(SEED, IMG_CHANNELS, GENERATE_RESOLUTION)

    noise = tf.random.normal([1, SEED])
    generated_image = generator(noise, training=False)

    plt.imshow(generated_image[0, :, :, 0])



    generator_optimizer = tf.keras.optimizers.Adam(1.5e-4,0.5)

    discriminator_optimizer = tf.keras.optimizers.Adam(1.5e-4,0.5)
    
    for filename in os.listdir(PATH):
        if filename != "images" and filename != "numpyData" and filename != "numpyData.npy" and filename != "output":
            imgPath = os.path.join(PATH,filename)
            img = Image.open(imgPath).resize((GEN_SQUARE, GEN_SQUARE), Image.ANTIALIAS)
            trainingData.append(np.asarray(img))
    trainingData = np.reshape(trainingData,(-1, GEN_SQUARE, GEN_SQUARE, IMG_CHANNELS))
    trainingData = trainingData.astype(np.float32)
    trainingData = trainingData / 127.5 - 1 #Normalizing to a scale again

    #save the array for later
    np.save("./output",trainingData)

    #Load the images
    #trainingData = np.load(trainingBinPath)

    #How to shuffle without ImageDataGen
    trainDataset = tf.data.Dataset.from_tensor_slices(trainingData) \
                   .shuffle(BUFFER).batch(BATCH)



    generator = createGenerator(SEED, IMG_CHANNELS, GENERATE_RESOLUTION)

    discriminator = createDiscriminator(imgShape)

    checkpoint_dir = './output'
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
    checkpoint = tf.train.Checkpoint(generator_optimizer = generator_optimizer,
                                     discriminator_optimizer = discriminator_optimizer,
                                     generator=generator,
                                     discriminator=discriminator)
    seed = tf.random.normal([(PRE_ROWS * PRE_COLS), SEED])


    train(trainDataset, EPOCHS, discriminator, generator,
          generator_optimizer, discriminator_optimizer, seed, checkpoint, checkpoint_prefix, BATCH, SEED, cross_entropy)

    generator.save(os.path.join("./output","faceGenerator.h5"))
#main()
    

if __name__ == "__main__":
    main()


#Dataset used: https://www.kaggle.com/gasgallo/faces-data-new
#Inspiration: https://www.youtube.com/watch?v=Nrsy6vF7rSw&t=1212s
