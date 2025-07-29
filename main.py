import velopack

def update_app():
    manager = velopack.UpdateManager("https://github.com/Bennedi/velo-flask-app")

    update_info = manager.check_for_updates()
    if not update_info:
        return # no updates available

    # Download the updates, optionally providing progress callbacks
    manager.download_updates(update_info)

    # Apply the update and restart the app
    manager.apply_updates_and_restart(update_info)

if __name__ == "__main__":
    # Velopack builder needs to be the first thing to run in the main process.
    # In some cases, it might quit/restart the process to perform tasks.
    velopack.App().run()
