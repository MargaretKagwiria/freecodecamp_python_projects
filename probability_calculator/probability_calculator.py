import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for key, value in kwargs.items():
      for i in range(value):
        self.contents.append(key)
    self.copy = self.contents[:]

  def draw(self, num_balls):
    self.contents = self.copy[:]
    if num_balls >= len(self.contents):
      return self.contents

    picked_balls = []
    for i in range(num_balls):
      colour = random.choice(self.contents)
      picked_balls.append(colour)
      self.contents.remove(colour)
    return picked_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for n in range(num_experiments):
    actual = dict()
    result = hat.draw(num_balls_drawn)
    for color in result:
      if color in actual:
        actual[color] += 1
      else:
        actual[color] = 1
    if all(key in actual and actual[key] >= expected_balls[key] for key in expected_balls):
      count += 1
  probability = count/num_experiments
  return probability