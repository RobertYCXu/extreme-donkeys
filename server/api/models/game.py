class Game:
  def __init__(self, key):
    self.key = key
    self.state = 'START'

  def serialize(self):
    return self.key

