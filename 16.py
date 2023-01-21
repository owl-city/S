import time
import subprocess

while True:
  subprocess.call(['sh', 'ss7.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '15.py'])
  subprocess.call(['nohup', 'python3', '14.py'])
  break