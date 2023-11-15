import subprocess

# Define the path to your requirements.txt file
requirements_file = 'requirements.txt'

# Run pip install for the requirements
subprocess.run(['pip', 'install', '-r', requirements_file])
