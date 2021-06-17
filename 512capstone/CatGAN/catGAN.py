import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os
import time
import imageio
import glob
from tensorflow.keras import layers
from tqdm import tqdm
from PIL import Image
from IPython import display
import tensorflow_docs.vis.embed as embed

# A few global varibles to make for easy modification
BATCH = 512
EPOCHS = None
BUFFER = 60000
NOISEDIM = 100
GENERATE_RES = 2 #(1=32, 2=64, 3=96, 4=128, etc.)
IMGSIZE = 32 * GENERATE_RES #Size of images in the dataset
NUMEXAMPLES = 16

cross_entropy = tf.keras.losses.BinaryCrossentropy()




def createGenerator(seed, channels):
    """Method that creates a generative model.

        Parameters:
                seed (tf.Tensor) = the seed for the model to interpret.
                channels (int) = Noise dim variable used for filter.
        Returns:
        model (tensorflow.python.keras.engine.sequential.Sequential) = the generator
    """
    model = tf.keras.Sequential()
    model.add(layers.Dense(4 * 4 * 256, activation = "relu", input_dim = seed))
    model.add(layers.Reshape((4, 4, 256)))

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
    #check desired resolution to adjust output size and add complexity
    if GENERATE_RES > 1:
        model.add(layers.UpSampling2D(size=(GENERATE_RES, GENERATE_RES)))
        model.add(layers.Conv2D(128, kernel_size = 3, padding = "same"))
        model.add(layers.BatchNormalization(momentum = 0.8))
        model.add(layers.Activation("relu"))
    #if()

    #final Convolutional NN layer
    model.add(layers.Conv2D(channels, kernel_size = 3, padding = "same"))
    model.add(layers.Activation("tanh"))

    return model
#createGenerator()


def createDiscriminator(imgShape):
    """Function that creates the discriminator model.

        Parameters:
                imgShape (tuple) = desired shape of image.
        Returns:
                model (tensorflow.python.keras.engine.sequential.Sequential) = the discriminator

    """
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


def generate_and_save_images(model, epoch, test_input):
    """Generates screenshots of the models progress each epoch.

        Parameters:
                model (tensorflow.python.keras.engine.sequential.Sequential) =
                The generator to be tracked
                epoch (int) = the current local epoch
                test_input (tensorflow.python.framework.ops.EagerTensor) =
                The tracked seed to keep model results coherent
    """
    #Training is set to false
    #so all layers run in inference mode (batchnorm)(?)
    predictions = model(test_input, training=False)


    fig = plt.figure(figsize=(4,4))
    #plot predictions
    for i in range(predictions.shape[0]):
        plt.subplot(4,4, i+1)
        plt.imshow(predictions[i,:,:,0] * 127.5 + 127.5, cmap = "gray")
        plt.axis("off")
    #for()

    #update epoch_total or create a new tracker
    if os.path.exists(os.path.join("output","epoch_total.txt")):
        f = open(os.path.join("output","epoch_total.txt"),"r")
        epoch = int(f.readline()) + 1
        print("Total Epochs:{}".format(epoch))
        f = open(os.path.join("output","epoch_total.txt"),"w")
        f.write(str(epoch))
    #if()
    else:
        f = open(os.path.join("output","epoch_total.txt"),"w")
        f.write(str(epoch))
    #else()
    f.close()

    plt.savefig("image_at_epoch_{:04d}.png".format(epoch)) #save image
    #plt.show() # Turn on to show each new image after it's made
    plt.close()
#generate_and_save_images()
    

def discriminatorLoss(realOutput, fakeOutput):
    """Function to calculate discriminator loss.

    Indicates how well the discriminator can
    tell the difference between real and fake
    photos.

        Parameters:
                realOutput (tensorflow.python.framework.ops.Tensor) =
                The real images of cats
                fakeOutput (tensorflow.python.framework.ops.Tensor) =
                The fake images of cats generated by the generator
        Returns:
                totalLoss (tensorflow.python.framework.ops.Tensor) =
                The totalloss for the discriminator.
                
    """
    realLoss = cross_entropy(tf.ones_like(realOutput), realOutput)
    fakeLoss = cross_entropy(tf.zeros_like(fakeOutput), fakeOutput)
    totalLoss = realLoss + fakeLoss
    return totalLoss
#discriminatorLoss()


def generatorLoss(fakeOutput):
    """"Function to calculate generator loss.

    Indicates how well the generator can trick
    the discriminator into believing the fake
    images are real.

        Parameters:
                fakeOutput (tensorflow.python.framework.ops.Tensor) =
                The generated images of cats made by the generator
        Returns:
                cross_entropy(tf.ones_like(fakeOutput), fakeOutput)(tensorflow.python.framework.ops.Tensor) =
                The loss of the generator.
    """
    return cross_entropy(tf.ones_like(fakeOutput), fakeOutput)
#generatorLoss()


@tf.function #Improve performance
def train_step(images, generator, discriminator, generatorOptimizer, discriminatorOptimizer):
    """Function that helps train function train the models.

        Parameters:
                images (tensorflow.python.framework.ops.Tensor) = Selected images of cats for this current step of training
                generator (tensorflow.python.keras.engine.sequential.Sequential) =
                The generator model
                discriminator (tensorflow.python.keras.engine.sequential.Sequential) =
                The discriminator model
                generatorOptimizer (tensorflow.python.keras.optimizer_v2.adam.Adam) =
                The optimizer for the generator
                discriminatorOptimizer (tensorflow.python.keras.optimizer_v2.adam.Adam) =
                The optimizer for the discriminator
    """
    noise = tf.random.normal([BATCH, NOISEDIM])
    
    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generatedImages = generator(noise, training = True)

        realOutput = discriminator(images, training = True)
        fakeOutput = discriminator(generatedImages, training = True)
        #calculate loss
        gen_loss = generatorLoss(fakeOutput)
        disc_loss = discriminatorLoss(realOutput, fakeOutput)

        #Allow for generator and discriminator to be trained at the same time
        #but still essentially seperately
        gradients_of_generator = gen_tape.gradient(\
            gen_loss, generator.trainable_variables)
        gradients_of_discriminator = disc_tape.gradient(\
            disc_loss, discriminator.trainable_variables)
        generatorOptimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
        discriminatorOptimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))
    #with()
#train_step()
        

def train(dataset, epochs, discriminator, generator, generatorOptimizer, discriminatorOptimizer, seed, checkpoint, checkpoint_prefix):
    """Function that trains the model using train_step function.

        Parameters:
                dataset (tensorflow.python.data.ops.dataset_ops.BatchDataset) = dataset of cats
                epochs (int) = Number of epochs for training of model
                discriminator (tensorflow.python.keras.engine.sequential.Sequential) =
                The discriminator model
                generator (tensorflow.python.keras.engine.sequential.Sequential) =
                The generator model
                generatorOptimizer (tensorflow.python.keras.optimizer_v2.adam.Adam) =
                Optimizer for the generator
                discriminatorOptimizer (tensorflow.python.keras.optimizer_v2.adam.Adam) =
                Optimizer for the dscriminator
                seed (tensorflow.python.framework.ops.EagerTensor) = The tracked seed to
                keep generated results coherent
                checkpoint (tensorflow.python.training.tracking.util.Checkpoint) =
                The tensorflow checkpoint tracker to save the model
                checkpoint_prefix (str) = Filepath for checkpoint
    """
    for epoch in range(epochs):
        start = time.time()

        for image_batch in tqdm(dataset):
            train_step(image_batch, generator, discriminator, generatorOptimizer, discriminatorOptimizer)
        #2nd for()

        #Produce images for the GIF
        display.clear_output(wait=True)
        generate_and_save_images(generator, epoch + 1, seed)

        #save model every 5 epochs
        if (epoch + 1) % 5 == 0:
            print("Saving checkpoint.")
            checkpoint.save(file_prefix = checkpoint_prefix)
        #if()
            

        print("time for epoch {} is {} sec".format(epoch + 1, time.time()-start))
    #1st for()
        
    #Generate after final epoch
    display.clear_output(wait=True)
    generator.save("output/CatGenerator.model")
    discriminator.save("output/CatDiscriminator.model")
#train()
    

def displayImage():
    """Function that displays the latest generated image.

        Returns:
                Image.open("outputPhotos/image_at_epoch_{:04d}.png".format(epochNum))
                (PIL.PngImagePlugin.PngImageFile) = A pillow image to be opened
                
    """
    f = open(os.path.join("output","epoch_total.txt"),"r")
    epochNum = int(f.readline())
    f.close()
    return Image.open("outputPhotos/image_at_epoch_{:04d}.png".format(epochNum))
#displayImage()


def main():
    """Main function that executes the program."""
    print("Hello World!")


    EPOCHS = int(input("How many epochs shall this model train for?"))

    trainingData = []

    #create optimizers
    generator_optimizer = tf.keras.optimizers.Adam(1.5e-4,0.5)

    discriminator_optimizer = tf.keras.optimizers.Adam(1.5e-4,0.5)

    #gather all images of cats
    for filename in os.listdir("cats"):
        imgPath = os.path.join("cats", filename)
        img = Image.open(imgPath).resize((IMGSIZE, IMGSIZE), Image.ANTIALIAS)
        trainingData.append(np.asarray(img))
    #for()
        
    trainingData = np.reshape(trainingData, (-1, IMGSIZE, IMGSIZE, 3))
    trainingData = trainingData.astype(np.float32)
    trainingData = trainingData / 127.5 - 1
    
    np.save(os.path.join("output", "trainingData"), trainingData) #save trainingData

    trainDataset = tf.data.Dataset.from_tensor_slices(trainingData) \
                   .shuffle(BUFFER).batch(BATCH)
    #Create tensorflow compatible dataset

    ImgShape = (IMGSIZE, IMGSIZE, 3)

    generator = createGenerator(NOISEDIM, 3)#Uncomment this to make new generator

    discriminator = createDiscriminator(ImgShape)#Uncomment this to make new discriminator

    #Search for previous seed, or generate new one
    if os.path.exists(os.path.join("output", "seed.npy")):
        print("Using previous seed")
        seed = tf.convert_to_tensor(np.load(os.path.join("output","seed.npy")))
    #if()
        
    else:  
        print("Generating seed")
        seed = tf.random.normal([NUMEXAMPLES, NOISEDIM])
        np.save(os.path.join("output", "seed"), seed.numpy())
    #else()
    
    tf.print(seed)

    #Create a checkpoint saving system
    checkpoint_dir = './output'
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
    checkpoint = tf.train.Checkpoint(generator_optimizer = generator_optimizer,
                                 discriminator_optimizer = discriminator_optimizer,
                                 generator=generator,
                                 discriminator=discriminator)

    #Create a manager of the checkpoint
    manager = tf.train.CheckpointManager(checkpoint, directory = "output", max_to_keep = 3)

    #Restore to most recent checkpoint if available
    checkpoint.restore(manager.latest_checkpoint)
    if manager.latest_checkpoint:
        print("Restore from {}".format(manager.latest_checkpoint))
    #if()
        
    else:
        print("Starting from scratch...")
    #else()

    #train the models
    train(trainDataset, EPOCHS, discriminator, generator, generator_optimizer, discriminator_optimizer, seed, checkpoint, checkpoint_prefix)
    img = displayImage()
    img.show()
    
    anim_file = 'dcgancatbnw.gif'
    #Turn all images into gifs
    with imageio.get_writer(anim_file, mode='I') as writer: # I = multiple images
        filenames = glob.glob('image*.png') #find pathnames matching "image*.png" pattern
        filenames = sorted(filenames)
        for filename in filenames: #add the images to the gif
            image = imageio.imread(filename)
            writer.append_data(image)
            image = imageio.imread(filename)
            writer.append_data(image)
        #for()
    #with()

    embed.embed_file(anim_file)#create the gif
#main()
    

#New Dataset used: https://www.kaggle.com/spandan2/cats-faces-64x64-for-generative-models
#Inspiration 1: https://www.tensorflow.org/tutorials/generative/dcgan
#Inspiration 2: https://www.youtube.com/watch?v=Nrsy6vF7rSw&t=1212s

if __name__ == "__main__":
    main()
