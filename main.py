import subprocess, os, re
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

print('Monitoring folder mangas for new mangas in .cbz format')
OPTIONS=os.getenv('OPTIONS') + " -o"
pattern = r'^input/(.*?) - (.*?) - (.*?)\.([^\.]+)$'

class MyHandler(PatternMatchingEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print("New manga detected :", event.src_path)
            match = re.search(pattern, event.src_path)
            author = match.group(1)
            series = match.group(2)
            title = match.group(3)
            complete_title=series + " - " + title
            METADATA= "-a " + f'"{author}"' + " -t " + f'"{complete_title}"'
            print(METADATA)
            command="python kcc/kcc-c2e.py" + " " + METADATA + " " + OPTIONS + " output " + f'"{event.src_path}"'
            print(command)
            output = subprocess.run([command], shell=True)
            if not output.returncode:
                print("Conversion successful, manga is now available in output")
            else:
                print("Conversion failed, check logs above")
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