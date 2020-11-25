import time

def get_current_time_in_millis():
  millis = int(round(time.time() * 1000))
  return millis
