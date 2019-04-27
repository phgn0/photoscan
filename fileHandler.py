import os
import subprocess


class FileHandler:
    def __init__(self):
        self.count = 0

    def setSeriesName(self, name):
        self.baseName = name

    def setSeriesDate(self, year):
        self.baseDate = str(year) + ":01:01 00:{:02d}:{:02d}"

    def _getRunningDate(self):
        self.count = 0

        seconds = self.count % 60
        hours = self.count // 60

        return self.baseDate.format(hours, seconds)

    def processNewFile(self, path):
        # rename file
        directory = os.path.dirname(path) + "/"
        newName = directory + self.baseName + "_{}.jpg".format(self.count)
        os.rename(path, newName)

        # set date
        subprocess.call(
            ["exiftool", "-q", "-overwrite_original",
                "-DateTimeOriginal='{}'".format(self._getRunningDate()),
                newName])

        # displays
        # subprocess.call(["feh", "--scale-down", newName])

        self.count += 1
