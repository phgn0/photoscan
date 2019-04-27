import sys

from fileWatcher import FileWatcher
from fileHandler import FileHandler


def main():
    if len(sys.argv) != 1 + 1:
        print("Provide the android PhotoScan file folder as argument.")
        return

    directory = sys.argv[1]

    handler = FileHandler()

    w = FileWatcher(directory, handler.processNewFile)
    w.run()

    try:
        while True:
            seriesName = input("Current series name: ")
            seriesYear = input("Series Date: ")

            handler.setSeriesName(seriesName)
            handler.setSeriesDate(int(seriesYear))

            print("Running series...")

            # command loop
            command = ""
            while command != "n":
                command = input("[d]elete last image or [n]ext series? ")
                if command == "d":
                    handler.deleteLastFile()

    except KeyboardInterrupt:
        print("")   # force newline in terminal
        w.stop()
        sys.exit()


if __name__ == '__main__':
    main()
