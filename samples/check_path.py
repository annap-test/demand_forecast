import sys
import os
current_dir = os.path.abspath('.')
print(current_dir)
current_dir =os.getcwd()
print(current_dir)
value = os.environ.get('PYTHONPATH')
print(value)
for p in sorted(sys.path):
  print(f"->\t{p}")