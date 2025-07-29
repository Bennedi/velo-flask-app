import os
import subprocess
import json
from datetime import datetime

# Build with PyInstaller
subprocess.run(['pyinstaller', '--onefile', '--name=MyApp', 'update_checker.py'], check=True)

# Prepare Velopack package
version = datetime.now().strftime("%Y.%m.%d.%H%M")
release_notes = "Automatic build"
channel = "stable"

# Create Velopack package
subprocess.run([
    'velo-pack', '--pack',
    f'--dir=dist',
    f'--version={version}',
    f'--notes="{release_notes}"',
    f'--channel={channel}'
], check=True)

# Create release info
release_info = {
    "version": version,
    "releaseDate": datetime.utcnow().isoformat() + "Z",
    "notes": release_notes
}

with open('dist/RELEASES.json', 'w') as f:
    json.dump(release_info, f)

print(f"Build complete: Version {version}")