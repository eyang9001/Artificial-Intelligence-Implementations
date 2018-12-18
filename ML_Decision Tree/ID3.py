from node import Node
import math
import node

def ID3(examples, default):
    '''
    Takes in an array of examples, and returns a tree (an instance of Node)
    trained on the examples.  Each example is a dictionary of attribute:value pairs,
    and the target class variable is a special attribute with the name "Class".
    Any missing attributes are denoted with a value of "?"
    '''
    if not examples:    # The condition that examples is empty, return the default
        return default
    pVal = examples[0].get("Class")
    for i in examples:
        if i.get("Class") != pVal and i.get("Class") is not None:
            break   # There are unique values in the example set
        pVal = i.get("Class")
    else:
        t = Node()
        t.addExamples(examples)
        t.label = mode(examples, "Class")
        t.setLeaf()
        return t

    bestatt = chooseAttribute(examples)
    t = Node()
    t.label = bestatt
    t.addExamples(examples)
    values = {}
    for i in examples:
        val = i[bestatt]
        if values.get(val) is None:
            values[val] = []
            values[val].append(i)
        else:
            values[val].append(i)
    if len(list(values.keys())) == 1:  # This is a trivial split
        t = Node()
        t.addExamples(examples)
        t.label = mode(examples, "Class")
        t.setLeaf()
        return t

  # recursively go through all of the values and create subnodes
    for vals in list(values.keys()):
        test = values[vals]
        child = ID3(test, mode(examples, "Class"))
        t.addChild(child, vals)

    return t


def prune(node, examples):
    '''
    Takes in a trained tree and a validation set of examples.  Prunes nodes in order
    to improve accuracy on the validation data; the precise pruning strategy is up to you.
    '''

    if node.isLeaf == 1:
        return

    for i in list(node.children.keys()):
        pruneRecursive(node.children[i], examples, node, node, i)


def pruneRecursive(node, examples, fullTree, parentNode, childKey):
    if node.isLeaf == 1:
        return  # Quits if leaf

    keys = list(node.children.keys())

    for child in keys:
        if node.children[child].isLeaf == 0:
            pruneRecursive(node.children[child], examples, fullTree, node, child)    # recursive call to get to leaves

    # Check if prunable after potentially pruning children
    keys = node.children.keys()
    for child in keys:
        if node.children[child].isLeaf == 0:
            return  # quits out if not all children are leaves

    # Checks current accuracy
    curAcc = test(fullTree, examples)

    # Creates pruned version
    testNode = Node()
    testNode.setLeaf()
    testNode.examples.append(node.examples)
    testNode.label = mode(node.examples, "Class")
    parentNode.children[childKey] = testNode

    # Checks pruned accuracy
    pruneAcc = test(fullTree, examples)

    # If pruneACC < currAcc, put original node BACK
    if pruneAcc < curAcc:
        parentNode.children[childKey] = node
    return

def test(node, examples):
    '''
    Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
    of examples the tree classifies correctly).
    '''
    tot = len(examples)
    correct = 0
    for i in examples:
        if evaluate(node, i) == i["Class"]:
            correct += 1
    return correct/tot

def evaluate(node, example):
    '''
    Takes in a tree and one example.  Returns the Class value that the tree
    assigns to the example.
    '''

    if node.isLeaf == 1:
        return node.label

    att = node.label
    val = example[att]
    try:
        newNode = node.children[val]
    except KeyError:  # When the example value of the attribute doesn't exist in the tree
        modeval = mode(node.examples, att)  # use the mode value of the tree at that node
        newNode = node.children[modeval]
    return evaluate(newNode, example)


def chooseAttribute(examples):
    keys = list(examples[0].keys())
    maxGain = None
    maxKey = None
    tot = len(examples)
    for curKey in keys:
        if curKey != "Class":
            keyvals= {}
            # get the values of the current key into the dictionary[current key][class output] = count
            for ii in examples:
                attVal = ii[curKey]
                out = ii["Class"]
                if keyvals.get(attVal) is None:
                    keyvals[attVal]= {}
                    keyvals[attVal][out] = 1
                elif keyvals[attVal].get(out) is None:
                    keyvals[attVal][out] = 1
                else:
                    keyvals[attVal][out] += 1
            # calculate entropy of curKey
            curGain = 0
            for vals in list(keyvals.keys()):
                valdenom = sum(keyvals[vals].values())
                logsum = 0
                for outs in list(keyvals[vals].keys()):
                    fraction = keyvals[vals][outs]/valdenom
                    logsum += fraction * math.log(fraction, 2)
                curGain += (valdenom/tot)*logsum
            if maxGain is None or curGain > maxGain:  # not making the gain calculation positive, so checking for max gain for attribute
                maxGain = curGain
                maxKey = curKey
    return maxKey

def mode(examples, attr):
    dict = {}
    modeNum = 0
    modeVal = None
    for i in examples:
        val = i.get(attr)
        if dict.get(val) is None:
            dict[val] = 1
        else:
            dict[val] += 1
    for ii in list(dict.keys()):
        if dict[ii] > modeNum:
            modeNum = dict[ii]
            modeVal = ii
    return modeVal



