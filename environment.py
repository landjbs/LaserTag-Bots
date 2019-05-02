import numpy as np
import matplotlib.pyplot as plt
import time

# set bounds
minX, maxX = 0, 10
minY, maxY = 0, 10

class player():
  """
  Any moving player in laser tag environment
  """
  def __init__(self):
    self.x = np.random.randint(minX, maxX)
    self.y = np.random.randint(minY, maxY)

  def loc(self):
    return (self.x, self.y)

  def move(self, xStep, yStep):
    """
    Moves X and Y by xStep and yStep clipping to boundaries of frame
    """
    def clip_move(step, minLim, maxLim):
      return min(max((minLim - 1), step), (maxLim - 1))
    x_move = clip_move((xStep + self.x), minX, maxX)
    y_move = clip_move((yStep + self.y), minY, maxY)
    self.x = x_move
    self.y = y_move

class board():
  """
  Board of the laser tag environment
  """
  def __init__(self):
    self.area = np.zeros((maxX, maxY))

  def edit_point(self, point, newVal=1):
    curX, curY = point
    if self.area[curX, curY] != newVal:
      self.area[curX, curY] = newVal
      return True
    else:
      raise ValueError

  def remove_point(self, point):
    self.edit_point(point, newVal=0)

  def add_points(self, pList):
    """
    Add list of points of type (x, y)
    """
    for point in pList:
      try:
        self.edit_point(point, 1)
      except:
        print("Unable to add point: {}".format(point))

  def display(self):
    plt.imshow(self.area)
    plt.show()

# simulate random walking of player
b = board()
p = player()

for _ in range(10):
  b.edit_point(p.loc())
  b.display()
  b.edit_point(p.loc(), 2)
  xMove, yMove = np.random.choice([-1,1], size=2)
  p.move(xMove, yMove)
