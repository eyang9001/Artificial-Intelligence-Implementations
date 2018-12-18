import math
import sys
import student_code as nbc
import unittest

def check_imports(source_name):

    imports = []

    with open('student_code.py',"r") as f:
        tokens = f.read().replace("\n", " ").split()

    for i in range(len(tokens)-1):
        if tokens[i] == 'import':
            imports.append(tokens[i+1])

    print('Imported Packages:')
    for i in range(len(imports)):
        print('  %s' % imports[i])
    print(' ')

def f_score(data,predict):

    actual = []

    for line in data:
        line = line.replace('\n','')
        fields = line.split('|')
        wID = int(fields[1])
        sentiment = fields[0]
        actual.append(sentiment)

    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for i in range(len(actual)):
        if predict[i] == '5' and actual[i] == '5':
            tp = tp + 1
        if predict[i] == '5' and actual[i] == '1':
            fp = fp + 1
        if predict[i] == '1' and actual[i] == '1':
            tn = tn + 1
        if predict[i] == '1' and actual[i] == '5':
            fn = fn + 1

    precision = float(tp)/float(tp+fp)
    recall = float(tp)/float(tp+fn)
    f_score_p = float(2.0)*precision*recall/(precision+recall)

    precision = float(tn)/float(tn+fn)
    recall = float(tn)/(fp+tn)
    f_score_n = float(2.0)*precision*recall/(precision+recall)    

    return(f_score_p, f_score_n)

data = []

def load_data():
    global data
    f = open('alldata.txt', "r")
    data = f.readlines()
    f.close()

class NaiveBayesTest(unittest.TestCase):

    def test1(self):
        classifier = nbc.Bayes_Classifier()
        classifier.train(data[:12478])
        predictions = classifier.classify(data[12478:])
        fp, fn = f_score(data[12478:],predictions)
        print(fp,fn)
        self.assertGreater(fp,0.90)
        self.assertGreater(fn,0.60)

if __name__ == "__main__":
    load_data()
    unittest.main()


