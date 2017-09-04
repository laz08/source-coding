#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Huffman, Shannon, Shannon_fano
import sys, unicodedata, math, collections, random, time, collections
from sets import Set

#reload(sys)
#sys.setdefaultencoding('utf8')

##------------------------------------------------------------------------------
##-------------------------- READING FROM FILE SOURCE --------------------------
##------------------------------------------------------------------------------

#Extracts the text from a file.
def readFromFile(filein):

    file = open(filein, 'r')
    contents = file.read()
    file.close()
    return contents

##------------------------------------------------------------------------------
##---------------------------COMPUTATION OF ENTROPIES---------------------------
##------------------------------------------------------------------------------
#Given a text, returns its alphabet of symbols.
def getTextAlphabet(text):

    return list(Set(text))

#Returns a single letter probability probability computed from given text.
def getSingleLetterProbability(letter, text):

    count = text.count(letter)
    return float(count)/len(text)

#Returns the symbols probabilities.
def getSymbolsProbabilities(text):

    probs = [] #Probabilities array
    alphabet = getTextAlphabet(text)

    for letter in alphabet:
        letterProb = getSingleLetterProbability(letter, text)
        probs.append(letterProb)

    return probs


#Computes the information given in a single probability
def computeInformation(probability):
    if probability == 0:
        return 0

    prob = math.log(probability, 2)
    return -prob


#Returns the symbols probabilities in a dictionary to relate them to its letter.
def getSourceOfText(str):

    source = []
    alphabet = getTextAlphabet(str)
    for letter in alphabet:
        letterProb = getSingleLetterProbability(letter, str)
        source.append((letter, letterProb))

    return source

#Computes the entropy of a source
def getEntropySource(src):

    #print src
    ent = 0
    for tup in src:
        p = tup[1]
        ent = ent + p * computeInformation(p)

    return ent

#Outputs de k-th extensions of a given source src
def extendKTimesSource(src, k):

    if(k == 1):
        return src

    else:
        ext = source_extension(src,  k - 1)
        extendedSrc = []
        for firstKey in ext:
            for secondKey in ext:
                #print(firstKey + " " + secondKey + " " + str(ext[firstKey]) + " " + str(ext[secondKey]))
                extendedSrc.append((firstKey[0] + secondKey[0], firstKey[1] * secondKey[1]))

        return extendedSrc

def computeMeanLength(src):

    meanLen = 0
    for tupl in src:
        meanLen = meanLen + tupl[1] * len(tupl[2])
    return float('{:.2f}'.format(meanLen))

def getOnlyCodes(code):

    onlyCodes = []
    for tupl in code:
        onlyCodes.append(tupl[2])
    return onlyCodes


def getShannonCode(src):

    prefixCode = Shannon.bruteForcePrefixCode(src)
    meanLen = computeMeanLength(prefixCode)
    onlyCodes = getOnlyCodes(prefixCode)
    return (onlyCodes, meanLen)


def getShannonFanoCode(src):

    code = Shannon_fano.createCode(src)
    meanLen = computeMeanLength(code)
    onlyCodes = getOnlyCodes(code)
    return (onlyCodes, meanLen)


def getHuffmanCode(src):

    rootNode = Huffman.createTree(src)
    code = Huffman.getRelatedCodes(rootNode, src)
    code.sort(key=lambda t: len(t[2]))
    meanLen = computeMeanLength(code)
    onlyCodes = getOnlyCodes(code)
    return (onlyCodes, meanLen)
