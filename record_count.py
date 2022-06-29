import time

class RecordCount:
  def __init__(self):
    self.counts = 300

  def increment_count(self):
    while True:
      time.sleep(6)
      self.counts += 1
  
