import os

for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.py'):
            os.chmod(os.path.join(root, file), 0o755)
            print("Permitted: " + os.path.join(root, file))
