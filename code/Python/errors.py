"""
Defines functions called when throwing errors
"""
import os
import sys

def checkexists(fname, dir=False):
  if dir:
    if not os.path.isdir(fname):
      print "error: Dir %s does not exist. Exiting." % fname
      sys.exit(1)
  else:
    if not os.path.exists(fname):
      print "Error: File %s does not exist. Exiting." % fname
      sys.exit(1)
