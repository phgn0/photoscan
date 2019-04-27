import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class FileWatcher(FileSystemEventHandler):
    def __init__(self, directory, callback):
        self.directory = directory
        self.callback = callback
        self.observer = Observer()

    def run(self):
        event_handler = self
        self.observer.schedule(
            event_handler, self.directory, recursive=True)
        self.observer.start()

    def stop(self):
        self.observer.stop()
        self.observer.join()

    def on_any_event(self, event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            if event.src_path.endswith("_exiftool_tmp"):
                return
            self.callback(event.src_path)

        # elif event.event_type == 'modified':
        #     # Taken any action here when a file is modified.
        #     print("Received modified event - %s." % event.src_path)
