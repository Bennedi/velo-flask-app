import os
import subprocess

# Install dependencies
subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)

# Run Velopack build
subprocess.run(['python', 'velopack_build.py'], check=True)

print("Build completed successfully. Output in dist/ folder")