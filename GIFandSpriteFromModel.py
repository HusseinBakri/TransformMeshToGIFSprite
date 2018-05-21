#!/usr/bin/python3
'''
Author: Hussein Bakri
License: MIT
Requirements: Blender on the OS (runnable from terminals/Command Lines)
            Package Pillow/Image: sudo pip3 install image in Blender
            Installing graphicsmahick

Usage: blender -b -P GIFandSpriteFromModel.py -- --inm 'Original_Mesh.obj'

'''

import argparse
from math import radians
from math import degrees
from random import uniform
import subprocess
import time
import bpy
import bmesh
from bmesh.ops import spin
from mathutils import Euler, Vector, Color
import os
import sys
#import image
#from PIL import Image
#import Image
#import glob

def get_args():
  parser = argparse.ArgumentParser()
 
  # get all script args
  _, all_arguments = parser.parse_known_args()
  double_dash_index = all_arguments.index('--')
  script_args = all_arguments[double_dash_index + 1: ]
 
  # add parser rules
  parser.add_argument('-in', '--inm', help="Original Model")
  parsed_script_args, _ = parser.parse_known_args(script_args)
  return parsed_script_args


args = get_args()

input_model = str(args.inm)
print(input_model)

print('\n Clearing blender scene (default garbage...)')
# deselect all
bpy.ops.object.select_all(action='DESELECT')

# selection
#bpy.data.objects['Camera'].select = True

# remove it
#bpy.ops.object.delete() 

# Clear Blender scene
# select objects by type
for o in bpy.data.objects:
    if o.type == 'MESH':
        o.select = True
    else:
        o.select = False

# call the operator once
bpy.ops.object.delete()


#importing the OBJ Model
bpy.ops.import_scene.obj(filepath=input_model)
print('\n Obj file imported successfully ...')

print('\n Creating and object list and adding meshes to it ...')
objectList=bpy.data.objects
meshes = []
for obj in objectList:
  if(obj.type == "MESH"):
    meshes.append(obj)

print("{} meshes".format(len(meshes)))

for i, obj in enumerate(meshes):
  bpy.context.scene.objects.active = obj
  print("{}/{} meshes, name: {}".format(i, len(meshes), obj.name))
  print("{} has {} verts, {} edges, {} polys".format(obj.name, len(obj.data.vertices), len(obj.data.edges), len(obj.data.polygons)))

print('\n Saving a .blend file of the scene')
bpy.ops.wm.save_as_mainfile(filepath="OBJscene.blend")



scene = bpy.context.scene
fp = os.path.dirname(os.path.realpath(__file__))
#fp = scene.render.filepath # get existing output path
print('\n Saving a .blend file of the scene: ')
print(fp)
scene.render.image_settings.file_format = 'PNG' # set output format to .png

frames = range(1,16)
x_rotation = radians(90)
y_rotation = radians(0)
z_rotation = radians(90)
# axis = (1,0,0)
# dvec = (0,0,0)
# angle = 2*math.pi
# steps = 20
# cent = obj.location


#bpy.ops.transform.rotate(value=2.56562, axis=(-0.818828, 0.361665, -0.445779), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)

print('\n begin rendering frames: ')
for frame_nr in frames:

    # set current frame to frame 5
    scene.frame_set(frame_nr)

    # set output path so render won't get overwritten
    context = bpy.context
    scene = context.scene
    ob = scene.objects.active # the newly added cylinder.
    ob.name = 'tree'
    # set the objects rotation
    ob.rotation_euler = Euler((x_rotation, y_rotation, z_rotation), 'XYZ')
    scene.render.filepath = fp + "/" + str(frame_nr)
    bpy.ops.render.render(write_still=True) # render still
    y_rotation = y_rotation + radians(20)

    
# restore the filepath
scene.render.filepath = fp

# need to install graphicsmagick 
# Mac OS brew install graphicsmagick
# Linux Ubuntu: sudo apt-get install graphicsmagick
print('\n Converting all the Images to a GIF at delay of 20')
subprocess.run("gm convert -delay 20 -loop 0 *.png animation.gif", shell=True, check=True)
#status = subprocess.call(['gm convert -delay 20 -loop 0 botimage*.png animation.gif'])
time.sleep(5)


print('\n Finished converting to GIF')

print('\n Moving on *******************')

print('\n Creating a sprite to be used for a 3D sprite effect on client side *******************')
subprocess.run("python3 ImagesSprite.py", shell=True, check=True)
print('\n Finished SPRITING')