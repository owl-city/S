import time
import subprocess

while True:
  subprocess.call(['sh', 'ss11.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '24.py'])
  subprocess.call(['nohup', 'python3', '21.py'])
  break