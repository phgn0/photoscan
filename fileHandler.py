import os


class FileHandler:
    def __init__(self):
        self.count = 0

    def setSeriesName(self, name):
        self.baseName = name

    def setSeriesDate(self, date):
        self.baseDate = date

    def processNewFile(self, path):
        directory = os.path.dirname(path) + "/"
        newName = directory + self.baseName + "_{}.jpg".format(self.count)
        os.rename(path, newName)

        self.count += 1
