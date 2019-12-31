import csv
from definations import *


def readData(fileName):
    """
    read poi data from a csv file
    :param fileName:
    :return: a list contained all poi objects
    """
    csvFile = open(fileName, "r")
    reader = csv.reader(csvFile)

    data = []

    for item in reader:
        if reader.line_num == 1:
            continue
        loc = Point(float(item[0]), float(item[1]))
        data.append(POI(loc, reader.line_num - 1))

    csvFile.close()
    return data

