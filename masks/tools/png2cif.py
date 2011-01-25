#!/usr/bin/python

import scipy
import readmagick
from mask_util import *

def stripe(x,y):
  for (z,k) in rle(x):
    print ' B %d %d %d %d;' % (2*k,2,2*z+k,2*y+1)

def layer(file,cif_name):
  try:
    img = readmagick.readimg(file)
  except:
    return
  print 'L '+cif_name+';'
  height,width,bytes = img.shape
  for y in xrange(0,height):
    stripe(img[y,:,0],height-y-1)

# CIF header
#   set CIF scale to 0.6 microns per pixel

print "( CIF conversion of visual6502 polygon data );"
print "DS 1 60 1;"
print "9 6502_chip;"

# CIF layers (NMOS)

layer("diffusion.png","ND")
layer("implant.png","NI")
layer("buried.png","NB")
layer("poly.png","NP")
layer("contact.png","NC")
layer("metal.png","NM")
layer("overglass.png","NG")

# CIF footer

print "DF;"
print "C 1;"
print "E"