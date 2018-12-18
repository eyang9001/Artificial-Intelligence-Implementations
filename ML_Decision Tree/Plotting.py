import ID3, parse, random
import matplotlib.pyplot as plt

def testPruningOnHouseData(inFile, trainSize):
    withPruning = []
    withoutPruning = []
    data = parse.parse(inFile)
    for i in range(100):
        random.shuffle(data)
        train = data[:trainSize]
        valid = data[trainSize:(trainSize + ((len(data)-trainSize) // 2))]
        test = data[(trainSize + ((len(data)-trainSize) // 2)):]
        tree = ID3.ID3(train, 'democrat')
        ID3.prune(tree, valid)
        acc = ID3.test(tree, test)
        withPruning.append(acc)
        tree = ID3.ID3(train + valid, 'democrat')
        acc = ID3.test(tree, test)
        withoutPruning.append(acc)
    return [sum(withPruning) / len(withPruning), sum(withoutPruning) / len(withoutPruning)]

def main():
    testsize = []
    pruning = []
    noprune = []
    for i in range(10, 300, 5):
        result = testPruningOnHouseData("house_votes_84.data", i)
        testsize.append(i)
        pruning.append(result[0])
        noprune.append(result[1])
    pplot, = plt.plot(testsize, pruning, 'r', label='Pruned')
    npplot, = plt.plot(testsize, noprune, 'b', label='No Prune')
    plt.legend(handles=[pplot, npplot])
    plt.ylabel('Accuracy %')
    plt.xlabel('Training Set Size')

    plt.show()

main()

