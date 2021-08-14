import os

cur_path = os.path.realpath(__file__)
print(cur_path)

root_path = os.path.dirname(os.path.dirname(cur_path))
print(root_path)