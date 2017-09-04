# -*- coding: UTF-8 -*-
import Queue

class HuffmanNode(object):

    def __init__(self, left=None, right=None, root=None):
        self.root = root
        self.left = left
        self.right = right

#Creates a binary tree with the frequencies
def createTree(freqs):

    p = Queue.PriorityQueue()
    for tupl in freqs:
        tuplReversed = (tupl[1], tupl[0])
        p.put(tuplReversed)

    while p.qsize() > 1:
        l = p.get()
        r = p.get()
        node = HuffmanNode(l, r)
        sumProbs = l[0]+r[0]

        p.put((sumProbs, node))

    #Return root node
    return p.get()

#Recorre tot l'arbre
def goOverTree(node, prefix, code):

    if isinstance(node[1].left[1], HuffmanNode):
        goOverTree(node[1].left, prefix + "0", code)

    else:
        code[node[1].left[1]] = prefix + "0"

    if isinstance(node[1].right[1], HuffmanNode):
        goOverTree(node[1].right, prefix + "1", code)

    else:
        code[node[1].right[1]] = prefix + "1"

    return(code)

def getRelatedCodes(rootNode, src):

    code = goOverTree(rootNode, "", {})

    codes = []
    for tupl in src:
        codes.append((tupl[0], tupl[1], code[tupl[0]]))
    return codes
