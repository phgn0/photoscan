import os
import subprocess


class FileHandler:
    def __init__(self):
        self.count = 0
        self.displayProcess = None

    def setSeriesName(self, name):
        self.baseName = name

    def setSeriesDate(self, year):
        self.count = 0
        self.baseDate = str(year) + ":01:01 00:{:02d}:{:02d}"

    def _getRunningDate(self):
        seconds = self.count % 60
        hours = self.count // 60

        return self.baseDate.format(hours, seconds)

    def processNewFile(self, path):
        # end showing old image
        if (self.displayProcess):
            self.displayProcess.terminate()
            self.displayProcess.wait()

        # rename file
        directory = os.path.dirname(path) + "/"
        newName = directory + self.baseName + "_{}.jpg".format(self.count)
        os.rename(path, newName)

        # set date
        subprocess.call(
            ["exiftool", "-q", "-overwrite_original",
                "-DateTimeOriginal='{}'".format(self._getRunningDate()),
                newName])

        # display new image
        self.displayProcess = subprocess.Popen(
            ["feh", "--scale-down", newName])

        # reduce file size
        subprocess.Popen(
            ["jpeg-recompress", "-Q", newName, newName])

        self.count += 1
        self.lastFile = newName

    def deleteLastFile(self):
        self.displayProcess.terminate()
        self.displayProcess.wait()

        os.remove(self.lastFile)
        self.count -= 1
