import subprocess

print("Initializing git repository")

subprocess.call(['git','init'])
subprocess.call(['git','add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])