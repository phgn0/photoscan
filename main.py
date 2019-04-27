import sys

from fileWatcher import FileWatcher
from fileHandler import FileHandler


def main():
    if len(sys.argv) != 1 + 1:
        print("Provide the android PhotoScan file folder as argument.")
        return

    directory = sys.argv[1]

    handler = FileHandler()
    handler.setSeriesName("test")
    handler.setSeriesDate(1990)

    w = FileWatcher(directory, handler.processNewFile)
    w.run()

    while True:
        pass


if __name__ == '__main__':
    main()
