import tensorflow as tf 
import glob
import imageio
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
from tensorflow.keras import layers
import time
from IPython import display #Display images
import tensorflow_docs.vis.embed as embed #Creates gifs


BUFFER = 60000
BATCH = 256
EPOCHS = 50
NOISEDIM = 100 # decided seed
NUM_EXAMPLES_TO_GENERATE = 16

def makeGeneratorModel():
    """Function that creates the generative model."""
    model = tf.keras.Sequential()
    model.add(layers.Dense(7*7*256, use_bias=False, input_shape=(100,)))
    model.add(layers.BatchNormalization()) #Normalizes the batch being passed through
    model.add(layers.LeakyReLU()) #Different than ReLU (Small negative slope instead of 0)

    model.add(layers.Reshape((7,7,256)))
    assert model.output_shape == (None, 7, 7, 256) #Changes the shape of the output of each layer

    #strides = list of ints
    #padding = padding algorithm used
    model.add(layers.Conv2DTranspose(128, (5, 5), strides = (1,1), padding ="same", use_bias = False)) 
    assert model.output_shape == (None, 7, 7, 128) #Using convolutional layers
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
    assert model.output_shape == (None, 14, 14, 64)
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU())

    model.add(layers.Conv2DTranspose(1, (5,5), strides=(2,2), padding = "same", use_bias=False, activation = "tanh"))
    assert model.output_shape == (None, 28, 28, 1)
    
    return model
#makeGeneratorModel()


def makeDiscriminatorModel():
    """"Function that creates the discriminator model."""
    model = tf.keras.Sequential()
    model.add(layers.Conv2D(64, (5,5), strides=(2,2), padding="same", input_shape=[28,28,1]))

    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))

    model.add(layers.Conv2D(128, (5,5), strides=(2,2), padding="same"))
    model.add(layers.LeakyReLU())
    model.add(layers.Dropout(0.3))
    
    model.add(layers.Flatten())
    model.add(layers.Dense(1))
    return model
#makeDiscriminatorModel()


def discriminatorLoss(realOutput, fakeOutput, cross_entropy):
    """Function that calculates the loss of the discriminator."""
    real_loss = cross_entropy(tf.ones_like(realOutput), realOutput)
    fake_loss = cross_entropy(tf.zeros_like(fakeOutput), fakeOutput)
    totalLoss = real_loss + fake_loss
    return totalLoss
#discriminatorLoss()


def generatorLoss(fakeOutput, cross_entropy):
    """Function that calculates the loss of the genertaor."""
    return cross_entropy(tf.ones_like(fakeOutput), fakeOutput)
#generatorLoss()


#causes the function to be compiled.
@tf.function
def train_step(images, generator, discriminator, cross_entropy, generatorOptimizer, discriminatorOptimizer):
    """Function that works with the train function to help train the models."""
    noise = tf.random.normal([BATCH, NOISEDIM])

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)

        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)

        gen_loss = generatorLoss(fake_output, cross_entropy)
        disc_loss = discriminatorLoss(real_output, fake_output, cross_entropy)

        gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
        gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

        generatorOptimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
        discriminatorOptimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))
#train_step()

        
def train(dataset, epochs, discriminator, generator, seed, cross_entropy, generatorOptimizer, discriminatorOptimizer, checkpoint, checkpoint_prefix):
    """Function that trains the discriminator and the generator."""
    for epoch in range(epochs):
        start = time.time()

        for image_batch in dataset:
            train_step(image_batch, generator, discriminator, cross_entropy, generatorOptimizer, discriminatorOptimizer)

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
    generator.save("NumGenerator.model")
    discriminator.save("NumDiscriminator.model")
#train()
    

def generate_and_save_images(model, epoch, test_input):
    """Function that generates and saves an image of the model's output."""
    #Training is set to false
    #so all layers run in inference mode (batchnorm)(?)
    predictions = model(test_input, training=False)

    fig = plt.figure(figsize=(4,4))

    for i in range(predictions.shape[0]):
        plt.subplot(4,4, i+1)
        plt.imshow(predictions[i,:,:,0] * 127.5 + 127.5, cmap="gray")
        plt.axis("off")

    plt.savefig("image_at_epoch_{:04d}.png".format(epoch))
    plt.show()
#generate_and_save_image()
    

def displayImage(epochNum):
    """Displays an image using the epoch number."""
    return Image.open("image_at_epoch_{:04d}.png".format(epochNum))
#displayImage()

    
def main():
    """Main function."""
    print("Hello World!")

    (train_images, train_labels), (_,_) = tf.keras.datasets.mnist.load_data()
    train_images = train_images.reshape(train_images.shape[0], 28, 28, 1).astype('float32')
    train_images = (train_images - 127.5)/127.5 #Normalize images to a scale [-1,1]

    train_dataset = tf.data.Dataset.from_tensor_slices(train_images).shuffle(BUFFER).batch(BATCH)

    generator = makeGeneratorModel()

    noise = tf.random.normal([1, 100])
    generated_image = generator(noise, training=False)

    plt.imshow(generated_image[0,:,:,0], cmap="gray") #Creating an example of an untrained model.

    discriminator = makeDiscriminatorModel()
    decision = discriminator(generated_image)
    #print(decision)

    cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True) #Crossentropy used

    generatorOptimizer = tf.keras.optimizers.Adam(1e-4)
    discriminatorOptimizer = tf.keras.optimizers.Adam(1e-4)

    checkpoint_dir = './trainingCheckpoints' #Allows for the incremental saving of models
    checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
    checkpoint = tf.train.Checkpoint(generator_optimizer = generatorOptimizer,
                                     discriminator_optimizer = discriminatorOptimizer,
                                     generator=generator,
                                     discriminator=discriminator)

    seed = tf.random.normal([NUM_EXAMPLES_TO_GENERATE, NOISEDIM]) #Create the random seed
    
    train(train_dataset, EPOCHS, discriminator, generator, seed, cross_entropy, generatorOptimizer, discriminatorOptimizer, checkpoint, checkpoint_prefix)    
    checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir)) #Train the data
    displayImage(EPOCHS) #Display the final image.

    #Code that creates a gif
    anim_file = 'dcgan.gif'

    with imageio.get_writer(anim_file, mode='I') as writer:
      filenames = glob.glob('image*.png')
      filenames = sorted(filenames)
      for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)
    image = imageio.imread(filename)
    writer.append_data(image)

    embed.embed_file(anim_file)
    writer.close() #Close file
#main()

    
#tutorial used: https://www.tensorflow.org/tutorials/generative/dcgan


if __name__ == "__main__":
    main()
