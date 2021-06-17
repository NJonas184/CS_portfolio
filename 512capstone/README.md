# My Capstone/Adjunct Project #

This is my Capstone/Adjuct project repository for my graduation. My goal was to create a GAN that could generate 
images of cats like the website [thiscatdoesnotexist.com](thiscatdoesnotexist.com). I have also included two other GANs to 
indicate my learning process. The Face Experiment GAN might not work though, as I stopped working on it midway to focus
on the main part of my Capstone/Adjunct.

### Requirements ###

These GANs require Python3 to run, below are the individual modules and links to their installation pages/instructions if they can be problematic (from my personal experience anyways).


* Install [Python3](https://www.python.org/downloads/)
* Install [pip](https://pip.pypa.io/en/stable/installing/)
* Install [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) (Just in case you don't already have it)
* Install [Tensorflow](https://www.tensorflow.org/install) or 
```
pip install --upgrade tensorflow
```
* MatPlotLib
```
pip install matplotlib
```
* Numpy
```
pip install numpy
```
* Imageio
```
pip install imageio
```
* Additional module to help generate gifs (as I copied the gif creation method from [this](https://www.tensorflow.org/tutorials/generative/dcgan) tensorflow guide)
```
pip install -q git+https://github.com/tensorflow/docs
```
* Tqdm
```
pip install tqdm
```
* cv2
```
pip install opencv-python
```
* IPython
```
pip install ipython
```
* glob
```
pip install glob3
```

### Installation ###

1.  Download the contents of this repository.
2.  Choose the Desired GAN:
    1.  For Face Experiment GAN:
        1.  Within the "Face Generator Experiment" folder, create an empy "output" folder. 
        2.  Within the "Face Generator Experiment" folder, download this [dataset](https://www.kaggle.com/gasgallo/faces-data-new) 
        and place it in a folder called "images". 
        3.  Run FaceGAN.py and enjoy!
    2.  For learningGANS: 
        1.  Run "learning Gans.py" and enjoy! 
    3.  For both catGAN.py and catGANColor.py: 
        1. Empty all folders within the "CatGAN" folder. 
        2.  Within the "CatGAN" folder, download this [dataset](https://www.kaggle.com/spandan2/cats-faces-64x64-for-generative-models)
        and place it within a folder called "cats". 
        3. Run either catGAN.py or catGANColor.py and enjoy! 


*Note that models do not come pretrained.*

### Author ###

* Nick Jonas

### Contributions ###

I won't be accepting any contributions, as this is just me documenting my Capstone/Adjunct project.
 I am also aware that it is significantly less efficient than it could be, as such I'll try to fix that if time allows.

### Different GANs ###
* FaceGAN.py: A GAN that generates images of faces
* "learnin Gans.py": A GAN that generates draws numbers
* catGAN.py: A GAN that generates images of cats in black and white
* catGANColor.py: A GAN that generates images of cats in color

### License ###

This project was created by Nick Jonas. It is a free software and may be redistributed under the terms 
specified in the LICENSE file.

If this project looks familiar, it's because I moved it from my school bitbucket repository.

### Inspirations ###
Here are a few places that helped me write this code:


* [Generating Faces with a Generative Adversarial Networks (GAN) in Keras/Tensorflow 2.0 (7.2)](https://www.youtube.com/watch?v=Nrsy6vF7rSw&t=2s)
* [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/tutorials/generative/dcgan)