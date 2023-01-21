import time
import subprocess

while True:
  subprocess.call(['sh', 'ss10.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '21.py'])
  subprocess.call(['nohup', 'python3', '23.py'])
  break