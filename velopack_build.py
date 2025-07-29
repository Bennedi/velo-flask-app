import os
import sys
import subprocess
import json
from datetime import datetime

def run_command(cmd):
    """Run command with error handling"""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Command failed with exit code {result.returncode}")
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        sys.exit(1)
    return result

# Build with PyInstaller using current Python
python_exe = sys.executable
run_command([python_exe, '-m', 'PyInstaller', '--onefile', '--name=MyApp', 'update_checker.py'])

# Prepare Velopack package
version = datetime.now().strftime("%Y.%m.%d.%H%M")
release_notes = "Automatic build"
channel = "stable"

# Create Velopack package
run_command([
    'velo-pack', '--pack',
    f'--dir=dist',
    f'--version={version}',
    f'--notes="{release_notes}"',
    f'--channel={channel}'
])

# Create release info
release_info = {
    "version": version,
    "releaseDate": datetime.utcnow().isoformat() + "Z",
    "notes": release_notes
}

with open('dist/RELEASES.json', 'w') as f:
    json.dump(release_info, f)

print(f"Build complete: Version {version}")
print("Upload .nupkg from dist/ folder to GitHub Releases")