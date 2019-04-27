from fileWatcher import FileWatcher

if __name__ == '__main__':
    w = FileWatcher("/home/peter/Desktop/pip", print)
    w.run()
    while True:
        pass
