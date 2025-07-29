import os
import sys
import subprocess
import time

def run_update_check():
    update_exe = os.path.join(os.path.dirname(sys.executable), 'Update.exe')
    if not os.path.exists(update_exe):
        return
    
    try:
        subprocess.run([
            update_exe,
            '--update',
            'https://github.com/bennedi/velo-flask-app/releases/latest/download',
            '--waitForExit'
        ], check=True)
        print("Update applied successfully. Restarting...")
        time.sleep(2)
        subprocess.run([sys.executable, 'main.py'])
        sys.exit(0)
    except subprocess.CalledProcessError:
        print("Update check failed")

if __name__ == '__main__':
    run_update_check()
    from main import app
    app.run(host='0.0.0.0', port=5000)