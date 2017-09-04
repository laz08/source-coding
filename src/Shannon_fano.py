# -*- coding: UTF-8 -*-

def sumAllProbs(codeList):


    sumProbs = 0
    if(len(codeList) > 0):  #Shpuld always be True
        for tupl in codeList:
            sumProbs = sumProbs + tupl[1]

    return sumProbs

def computeShannonFanoCode(codeList):

    listCodes = []
    codeListLen = len(codeList)
    if(codeListLen == 1):
        return codeList

    elif(codeListLen == 0):
        return []

    elif len(codeList) == 2:
        listCodes.append((codeList[0][0], codeList[0][1], codeList[0][2] + "0"))
        listCodes.append((codeList[1][0], codeList[1][1], codeList[1][2] + "1"))
        return listCodes

    else:

        min = sumAllProbs(codeList)
        appendedCode = []

        #Computation of middle index
        indx = 1
        count = indx
        for code in codeList:

            sumRangeTop = sumAllProbs(codeList[0:indx+1])
            sumRangeBottom = sumAllProbs(codeList[indx:])

            diff = abs(sumRangeTop - sumRangeBottom)

            if(diff <=  min):

                min = diff
                indx = count

            count = count + 1


        #Appending code
        for code in codeList[0:indx]:
            appendedCode.append((code[0], code[1], code[2] + "0"))

        for code in codeList[indx:codeListLen]:
            appendedCode.append((code[0], code[1], code[2] + "1"))

        #Recursive calls
        topList = computeShannonFanoCode(appendedCode[0:indx])
        for code in topList:
            listCodes.append(code)

        bottomList = computeShannonFanoCode(appendedCode[indx:codeListLen])
        for code in bottomList:
            listCodes.append(code)
            print ("Symb: " + code[0] + " Prob: " + str(code[1]) + " Constructed code: " + code[2])


        return listCodes

def sortSource(src):
    return sorted(src, key=lambda letterTuple: letterTuple[1], reverse=True)

def adaptList(src):

    newList = []
    for tupl in src:
        newList.append((tupl[0], tupl[1], ""))
    return newList


def createCode(src):

    codeList = sortSource(src)
    adaptedList = adaptList(codeList)
    code = computeShannonFanoCode(adaptedList)
    return code
