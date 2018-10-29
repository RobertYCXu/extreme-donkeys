class Game:
  def __init__(self, key):
    self.key = key
    self.state = 'START'
    self.user = {}

  def add_user(self, user):
    if user.name in self.user or len(self.user) >= 3:
      return False

    self.user[user.name] = user
    return True

  def serialize(self):
    body = self.key + '\n'
    for k in self.user.keys():
      body += k + '\n'
    return body


