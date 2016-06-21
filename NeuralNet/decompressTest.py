import random
import csv
import json
from lzstring import LZString
from StringIO import StringIO

def decompressTest():


    with open('SessionStreamTest.csv', 'rb') as f:
        reader = csv.reader(f)
        StreamList = list(reader)

    lzstringer = LZString()

    eventDataBlob = StreamList[1][6]
    print eventDataBlob
    eventDataBlob = lzstringer.decompress(eventDataBlob)
    print eventDataBlob

    decompressedString = StringIO(eventDataBlob)

    print decompressedString

    return

if  __name__ =='__main__':
    decompressTest()