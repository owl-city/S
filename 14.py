import time
import subprocess

while True:
  subprocess.call(['sh', 'ss6.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '13.py'])
  subprocess.call(['nohup', 'python3', '15.py'])
  break