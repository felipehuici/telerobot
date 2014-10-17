import RPi.GPIO as io
import time

pins = [17, 18, 22, 23]
io.setmode(io.BCM)

# set up GPIO 
for p in pins:
  io.setup(p, io.OUT)

# run test
print "starting test..."
for p in pins:
  print "setting pin %s" % str(p)
  io.output(p, 1)
  time.sleep(3)
  print "unsetting pin %s" % str(p)
  io.output(p, 0)
  time.sleep(1)

