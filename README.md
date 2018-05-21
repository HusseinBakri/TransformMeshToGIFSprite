# TransformMeshIntoGIFandSprite
A Python 3 tool that transforms a 3D model / 3D Mesh from OBJ format or Collada (need some changes in code) into a GIF file and into a CSS Sprite image file using the Blender Python API and other tools.

## Introduction
Ever wondered when you go to https://sketchfab.com/ on a browser that do not support WebGL, How you get sort of 360 view of the 3D model in a clever way? Well, actually it is not like it is an actual 360 image but a clever technique called **3D Spriting** or **360 Spriting**.

A lot of similar repositories to Sketchfab (https://sketchfab.com/ ), provide such technique and it can be used to showcase or mimic a 3D model on less capable devices especially mobile devices just with a bunch of images taken from different venture points of a certain 3D model. I believe it is quite handy in a lot of cases.

Sketchfab normally produces an image Sprite of 15 small images of the 3D model, combined into one thin landscape image. A Javascript library can then receive this 3D sprite image from the server and renders it to create a somehow 360 effect. Please see section titled "Javascript Viewers for 3D Models' Sprite Images" later for suggestions of libraries I enjoyed using on GitHub that renders/shows a sprite image as a 360 image.

This current Python tool licensed under MIT License,  helps you out with this by taking as input a 3D model in OBJ (you can easily change the code to accommodate other 3D file formats like X3D, Collada ...  - tell you later how). This tool then captures different venture points of the 3D model while spinning/rotating it and outputs a bunch of images (16 images to be precise) and a GIF file. It also outputs a CSS sprite image.

This tool is ideal to be integrated into a server side logic that can do this task in Batch for all 3D models.

You can change my code, in a very simple manner, to import other types of 3D file formats as long as they are supported by Blender in the following manner [look for bpy.ops.import_scene.obj(filepath=input_model) and replace it with what you want]:
```
# Pay ATTENTION to extentions of files: Collada (.dae), FBX (.fbx), X3D (.x3d), Wavefront OBJ (.obj) etc...
# For OJB Format
# Importing a model in Wavefront OBJ (used in my Tool)
bpy.ops.import_scene.obj(filepath=input_model)

# For Collada Format
# Importing .collada 
bpy.ops.wm.collada_import(filepath=input_model)

# For Extensible 3D (.x3d)
# Importing X3D Format
bpy.ops.import_scene.x3d(filepath=input_model)

# For FBX (.fbx)
# Importing FBX
bpy.ops.import_scene.fbx(filepath=input_model)

```


## Requirements
* Install Blender (https://www.blender.org/) on the operating system in question and make sure it is runnable from the terminal/Command Line (explained in a later section for how to do that on Mac OS). On Linux, I beleive you won't encounter problems. I found Blender is easier to run on Linux in headless mode, than per example: Meshlab - http://www.meshlab.net/ - (which we can do the same task in).
* Install Python 3 Packages Pillow/Image inside Blender Python packages and maybe on the OS level also. 

Yes! Blender uses its own Python Packages! Have a look at https://blender.stackexchange.com/questions/5287/using-3rd-party-python-modules. Non-common python modules are not recognized by Blender (even if installed on OS level) and thus need to be installed accordingly (please see in corresponding sections of Operating Systems).
* Installing graphicsmagick (http://www.graphicsmagick.org/) on the operating system in question and make sure it is runnable from terminals.

### Mac OS
In Mac OS, Blender may be an unrecognized command so you need to create an alias so it can be used from the terminal. Normally Blender command or process is inside the blender.app folder. Do the following:
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
On Mac/Linux Operating systems level:
```
sudo pip3 install pillow  
sudo pip3 install image
```
On Blender Level, in MacOS High Sierra, usually all python modules are located in the following directory (Please check if different. You won't have difficulities finding it)
```
/Applications/Blender/blender.app/Contents/Resources/2.79/python/lib/python3.5
```

You can install the python modules inside Blender (so Blender can see them) using the --target method on pip3:
```
pip3 install --target=/Applications/Blender/blender.app/Contents/Resources/2.79/python/lib/python3.5/ image
```
Fortunately, for Linux OSs per examples Ubuntu Server 16.04/Fedora 27, it suffices if you install the Python package 'Pillow' on the OS level only like the following:
```
sudo pip3 install pillow  
```

Apperantly on Linux, Blender Python interpreter can see the system level python modules. Not sure if that is applicable to MS Windows 10. Did not try that yet!

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

## Javascript Viewers for 3D Models' Sprite Images
* 360-degrees-product-viewer, is a lovely resource found at https://github.com/CodyHouse/360-degrees-product-viewer that can do the job very well.


## MIT License

This tool uses on another code that create a CSS Sprite (found at https://gist.github.com/gourneau/939252 ) which is based on Creative Commons Attribution 3.0 United. All rights reserved and my great appreciation.

My current tool adopts the MIT License as it did some minor changes to a third party code (cited previsouly) to work with the intended goal of this particular tool.

I expect adequate attribution of this work and all cited work. The attribution should include the title of the program, the author and the site or the document where the program is taken from.
