import logging

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class _MyHandler(FileSystemEventHandler):
    def __init__(self, logger):
        self.logger = logger

    def on_created(self, event):
        super().on_created(event)
        if not event.is_directory:
            self.logger.info("%s", event.src_path)


class WatchFiles:
    observer = None

    def __init__(self, ):
        self.started = False

    def run(self, path):
        if self.started:
            return
        try:
            logging.basicConfig(filename='changes.log', level=logging.INFO)
            logger = logging.getLogger('FILE')

            self.observer = Observer()
            self.observer.schedule(_MyHandler(logger), path=path, recursive=True)
            self.observer.start()
            self.started = True
        except Exception as e:
            raise ValueError(e)

    def stop(self):
        if self.started:
            self.observer.unschedule_all()
            self.observer.stop()
            self.observer.join(1000)
            self.started = False


"""
a = Watch("C:\\Users\\glaucio\\Pictures")
a.run()
import time
while 1:
    time.sleep(6000)
"""
