#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Utils
import sys, getopt

def usage():

    print ('Usage: main.py -i <inputfile> | -s <inputfileASSource>')
    sys.exit(2)

def main(argv):

    if len(argv) < 2:
         usage()
    try:
        opts, args = getopt.getopt(argv,"hi:s:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        usage()

    isSource = False
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-i", "--ifile"):
            filein = arg
        elif opt in ("-s", "--source"):
            filein = arg
            isSource = True

    print ("Reading from file " + filein)
    result = Utils.readFromFile(filein)
    result = result.replace('\n','').replace('\r', '')

    if not isSource:

        print Utils.getTextAlphabet(result)

        print ('')
        print("Source from string")
        src = Utils.getSourceOfText(result)
        print (src)

    else:
        src = eval(result)
        print src

    k = 1
    print "Source extension: " + str(k)
    extSrc2 = Utils.extendKTimesSource(src, k)

    print ('')
    print ("Entropy: ")
    print (Utils.getEntropySource(src))

    print ('')
    print ("Huffman code: ")
    print (Utils.getHuffmanCode(src))

    print ('')
    print ("Shannon code: ")
    print (Utils.getShannonCode(extSrc2))

    print ('')
    print ("Shannon fano code: ")
    print (Utils.getShannonFanoCode(src))





if __name__ == "__main__":
   main(sys.argv[1:])
