import time
import subprocess

while True:
  subprocess.call(['sh', 'ss9.sh'])
  time.sleep(250)
  subprocess.call(['nohup', 'python3', '19.py'])
  subprocess.call(['nohup', 'python3', '18.py'])
  break