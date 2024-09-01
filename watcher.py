from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import subprocess

class FileChangeHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.restart()

    def on_modified(self, event):
        if event.src_path.endswith(self.script):
            print(f"{self.script} has been modified, restarting...")
            self.restart()

    def restart(self):
        if self.process:
            self.process.terminate()
        self.process = subprocess.Popen(['python', self.script])

if __name__ == "__main__":
    script = 'newFact.py'  # replace with the name of your script
    event_handler = FileChangeHandler(script)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
