# -*- coding: UTF-8 -*-
import math

def orderSource(src):
    return sorted(src, key=lambda letterTuple: letterTuple[1], reverse=True)


def existsPrefix(code, existingCodes):

    for extCode in existingCodes:
        if code.startswith(extCode):
            return True

    return False


def incrementOneUnit(code, length):

    return '{0:b}'.format(1 + int(code, 2)).zfill(length)


def generateCode(existingCodes, length):

    newCode = "0" * length
    isCodeValid = False

    while not isCodeValid:

        if (newCode in existingCodes) or existsPrefix(newCode, existingCodes):
            newCode = incrementOneUnit(newCode, length)

        else:
            isCodeValid = True

    return newCode

def bruteForcePrefixCode(src):

    ordSrc = orderSource(src)
    codes = []
    result = []
    for tupl in ordSrc:

        letter = tupl[0]
        prob = tupl[1]

        codeLength = int(math.ceil(-math.log(prob, 2)))

        resultCode = generateCode(codes, codeLength)
        codes.append(resultCode)
        result.append((letter, prob, resultCode))
    return result
