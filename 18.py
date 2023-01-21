import time
import subprocess

while True:
  subprocess.call(['sh', 'ss8.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '17.py'])
  subprocess.call(['nohup', 'python3', '19.py'])
  break