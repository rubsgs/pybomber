class Bomb:
  TYPES = {
    'WEAK': 0,
    'MEDIUM': 1,
    'STRONG': 2
  }
  
  DAMAGES = {
    TYPES['WEAK']: 80,
    TYPES['MEDIUM']: 200,
    TYPES['STRONG']: 500
  }

  RANGES = {
    TYPES['WEAK']: 2,
    TYPES['MEDIUM']: 4,
    TYPES['STRONG']: 8
  }

  def __init__(self, type=TYPES['WEAK']):
    self.type = type
    self.damage = Bomb.DAMAGES[self.type]
    self.range = Bomb.RANGES[self.type]
