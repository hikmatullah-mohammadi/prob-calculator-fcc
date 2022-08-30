import random
import copy

class Hat:
  def __init__(self, **colors):
    self.contents = []
    # put all arguments in self.contents
    for i, j in colors.items():
      self.contents.extend([i]*j)

  def draw(self, n_balls):
    if n_balls >= len(self.contents):
      return self.contents
    rd_balls = []
    for i in range(n_balls):
      rd_ball = random.choice(self.contents)
      self.contents.remove(rd_ball)
      rd_balls.append(rd_ball)
    return rd_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  n_expected_outcome = 0
  for i in range(num_experiments):
    drawn_balls = copy.deepcopy(hat).draw(num_balls_drawn)
    for i, j in expected_balls.items():
      if drawn_balls.count(i) < j:
        break
    else:
      n_expected_outcome += 1
  return n_expected_outcome / num_experiments