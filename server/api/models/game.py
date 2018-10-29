class Game:
  def __init__(self, key):
    self.key = key

  def serialize(self):
    return self.key
