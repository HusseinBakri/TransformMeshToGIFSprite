# TransformMeshIntoGIFandSprite
A Python 3 tool that transforms a 3D model / 3D Mesh from OBJ format or GLTF (need some changes in code) into a GIF file and into a CSS Sprite image file using the Blender Python API and other tools.

## Introduction
Ever wondered when you go to https://sketchfab.com/ on a browser that do not support WebGL, How you get sort of 360 view of the 3D model in a clever way. Well actually it is not like it is an actual 360 image but a clever technique called 3D Spriting.

A lot of similar repositories to Sketchfab (https://sketchfab.com/ ), provide such technique and it can be used to showcase or mimic a 3D model on less capable devices especially mobile devices just with a bunch of images taken from different venture points of a certain 3D model. I believe it is quite handy in a lot of cases.

Sketchfab normally produces an image Sprite of 15 small images of the 3D model, combined into one thin landscape image. A Javascript library can then receive this 3D sprite image from the server and renders it to create a somehow 360 effect. Please see section titled 'Javascript Viewers for 3D Sprites' later for suggestions of libraries I enjoyed using on GitHub that renders/shows a sprite image as a 360 image.

This current Python tool licensed under MIT License,  helps you out with this by taking as input a 3D model in OBJ (you can easily change the code to accommodate other 3D file formats like gLTF, Collada ...  - tell you later how). This tool then captures different venture points of the 3D model while spinning/rotating it and outputs a bunch of images (16 images to be precise) and a GIF file. It also outputs a CSS sprite image.

This tool is ideal to be integrated into a server side logic that can do this task in Batch for all 3D models.


## Requirements
* Install Blender (https://www.blender.org/) on the operating system in question and make sure it is runnable from the terminal/Command Line (explained in a later section for how to do that on Mac OS). On Linux, I beleive you won't encounter problems. I found Blender is easier to run on Linux in headless mode, than per example: Meshlab - http://www.meshlab.net/ - (which we can do the same task in).
* Install Python 3 Packages Pillow/Image inside Blender Python packages and maybe on the OS level also. 

Yes Blender uses its own Python Packages. Have a look at https://blender.stackexchange.com/questions/5287/using-3rd-party-python-modules. Non-common python modules are not recognized by Blender (even if installed on OS level) and thus need to be installed accordingly (please see in corresponding sections of Operating Systems).
* Installing graphicsmagick (http://www.graphicsmagick.org/) on the operating system in question.

### Mac OS
In Mac OS, Blender may be an unrecognized command so you need to create an alias so it can be used from terminal Normally Blender command or process is inside the blender.app folder. Do the following:
```
echo 'alias blender="/Applications/blender.app/Contents/MacOS/blender"' >> .bashrc
```
or normally in a folder in /Applications called also Blender
```
echo 'alias blender="/Applications/Blender/blender.app/Contents/MacOS/blender"' >> .bashrc
```
Now run this in terminal:
```
source ~/.bashrc
```
Finally check if blender can be invoked from terminal:
```
blender --version
```


### Python Packages
On Mac/Linnux Operating systems level:
```
sudo pip3 install pillow  
sudo pip3 install image
```
On Blender Level, in MacOS High Sierra usually all python modules are installed in the following directly. Please check if different. You won't have difficulities finding it
```
/Applications/Blender/blender.app/Contents/Resources/2.79/python/lib/python3.5
```

You can install the python modules inside Blender (so Blender can see them) using the following method:
```
pip3 install --target=/Applications/Blender/blender.app/Contents/Resources/2.79/python/lib/python3.5/ image
```
On Blender Level, in Linux, example Fedora, Python packages are located in:
```
XX
```

#### Other requirements
Install graphicsmagick which allows us to create a GIF file from a bunch of images files setting delay etc.... Of course there are other tools if you wish to use. On Mac OS, install it via HomeBrew:

```
brew install graphicsmagick
```

On Linux, depending on distros won't be a headache:
```
#Example: Fedora 27
sudo dnf install GraphicsMagick

#Example: Ubuntu 
sudo apt-get install graphicsmagick

```
Finally make sure it can be called from terminals
```
gm -version
```

## Usage
```
blender -b -P GIFandSpriteFromModel.py -- --inm 'Original_Mesh.obj'
```

## Example

```
blender -b -P GIFandSpriteFromModel.py -- --inm 'Hat.obj'
```

## Javascript Viewers for 3D Sprites
* First suggestion a lovely library found at 

## MIT License

This tool uses on another code that create a CSS Sprite (found at https://gist.github.com/gourneau/939252 ) which is based on Creative Commons Attribution 3.0 United. All rights reserved and my great appreciation.

My current tool adopts the MIT License as it did some minor changes to a third party code (cited previsouly) to work with the intended goal of this particular tool.

I expect adequate attribution of this work and all cited work. The attribution should include the title of the program, the author and the site or the document where the program is taken from.
