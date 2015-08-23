import numpy as np
import output
from time import sleep

class Zoo:
  # spire is considered a node at position zero
  NODE_COUNT = 89
  START_CHAR = "@"
  END_CHAR = "#"
  FRAME_DELAY = 0.0030

  def __init__(self):
    self.frame = self.init_frame()

  def init_frame(self):
    return np.zeros(shape=(self.NODE_COUNT, 3), dtype=np.uint8)

  def send_frame(self):
    serial_array = []

    serial_array.append(self.START_CHAR)

    for x, colors in enumerate(self.frame):
      # TODO: send zero address value to spire
      if x == 0:
        continue
      else:
        serial_array.append("{0:0>3}{1:0>3}{2:0>3}{3:0>3}".format(x, colors[0], colors[1], colors[2]))

    serial_array.append(self.END_CHAR)

    output.write("".join(serial_array))

    self.frame_delay()

  def update_node(self, pos, color=[0, 0, 0]):
    self.frame[pos] = color

  def update_frame(self, frame):
    pass

  def frame_delay(self):
    sleep(self.FRAME_DELAY)
