import RPi.GPIO as io
pins = [17, 18, 22, 23]
io.setmode(io.BCM)
for p in pins:
  io.setup(p, io.OUT)
  io.output(p, 0)
