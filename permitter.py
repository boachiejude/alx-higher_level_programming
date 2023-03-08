import os

directory = './0x00-python-hello_world'

for filename in os.listdir(directory):
    if filename.endswith('.py'):
        filepath = os.path.join(directory, filename)
        os.system(f"chmod +x {filepath}")
        print(f"Permitted {filepath} to be executed")
