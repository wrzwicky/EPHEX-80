#!/usr/bin/env python2.7
import sys
if sys.version_info < (3,0):
  sys.exit("EPHEX now requires Python 3 or later.")

import os
from ephex_core import *


fnum = 0
while os.path.exists("%s.svg" % (fnum,)):
  fnum += 1

outfile = None

def newfile ():
  global fnum
  global outfile
  outfile = open("%s.svg" % (fnum), "w")
  err_out("Opening %s" % (outfile))
  fnum += 1

def out (s):
  if not outfile: newfile()

  outfile.write(s)

def closefile ():
  global outfile
  if outfile:
    out(SVG_FOOTER)
    outfile.close()
    outfile = None

def formfeed (dummy):
  err_out("Form feed")
  closefile()

f = EPHEX()
f.form_feed_callback = formfeed

data = open(sys.argv[1], 'rb').read()
f.feed_input(data)

sys.stdout.write(f.save_to_string())
