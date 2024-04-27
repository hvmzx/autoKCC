import subprocess, os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

print('Monitoring folder mangas for new mangas in .cbz format')
OPTIONS=os.getenv('OPTIONS') + " -o"

class MyHandler(PatternMatchingEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print("New manga detected :", event.src_path)
            command="python kcc/kcc-c2e.py " + OPTIONS + " output " + f'"{event.src_path}"'
            print(command)
            subprocess.run([command], shell=True)
            print("Conversion successful, manga is now available in output")
if __name__ == "__main__":
    observer = Observer()
    event_handler = MyHandler(patterns=["*.cbz"])
    observer.schedule(event_handler, path="input", recursive=True)
    observer.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()