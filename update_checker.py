import os
import sys
import subprocess
import time

def run_update_check():
    # Get path to Update.exe in same directory as executable
    update_exe = os.path.join(os.path.dirname(sys.executable), 'Update.exe')
    if not os.path.exists(update_exe):
        print("Update.exe not found. Skipping update check.")
        return
    
    try:
        print("Checking for updates...")
        subprocess.run([
            update_exe,
            '--update',
            'https://github.com/Bennedi/velo-flask-app/',
            '--waitForExit'
        ], check=True)
        print("Update applied successfully. Restarting...")
        time.sleep(2)
        subprocess.Popen([sys.executable, 'main.py'])
        sys.exit(0)
    except subprocess.CalledProcessError as e:
        print(f"Update failed: {e}")
    except Exception as e:
        print(f"Update check error: {e}")

if __name__ == '__main__':
    run_update_check()
    from main import app
    app.run(host='0.0.0.0', port=5000)