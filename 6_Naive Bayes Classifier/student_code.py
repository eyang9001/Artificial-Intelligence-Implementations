import math
import re

class Bayes_Classifier:

    def __init__(self):
        self.wordlist = set()
        self.pos_dict = {}
        self.neg_dict = {}
        self.pos_logprob = {}
        self.neg_logprob = {}
        self.pos_prior = None
        self.neg_prior = None
        pass

    def parse(self, lines):
        sentiments = []
        reviews = []
        positives = []
        negatives = []

        for line in lines:
            line = line.replace('\n', '')
            fields = line.split('|')
            sentiments.append(fields[0])
            reviews.append(fields[2])
            if fields[0] == '1':
                negatives.append(fields[2])
            else:
                positives.append(fields[2])

        return sentiments, reviews, negatives, positives

    def clean(self, reviews):
        stop_list = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', 'arent', 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', 'cant', 'cannot', 'could', 'couldnt', 'did', 'didnt', 'do', 'does', 'doesnt', 'doing', 'dont', 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', 'hadnt', 'has', 'hasnt', 'have', 'havent', 'having', 'he', 'hed', 'hell', 'hes', 'her', 'here', 'heres', 'hers', 'herself', 'him', 'himself', 'his', 'how', 'hows', 'i', 'id', 'ill', 'im', 'ive', 'if', 'in', 'into', 'is', 'isnt', 'it', 'its', 'its', 'itself', 'lets', 'me', 'more', 'most', 'mustnt', 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours', 'ourselves', 'out', 'over', 'own', 'same', 'shant', 'she', 'shed', 'shell', 'shes', 'should', 'shouldnt', 'so', 'some', 'such', 'than', 'that', 'thats', 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', 'theres', 'these', 'they', 'theyd', 'theyll', 'theyre', 'theyve', 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', 'wasnt', 'we', 'wed', 'well', 'were', 'weve', 'were', 'werent', 'what', 'whats', 'when', 'whens', 'where', 'wheres', 'which', 'while', 'who', 'whos', 'whom', 'why', 'whys', 'with', 'wont', 'would', 'wouldnt', 'you', 'youd', 'youll', 'youre', 'youve', 'your', 'yours', 'yourself', 'yourselves']
        # stop_list2 = ['a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']
        regex_pattern = r'([^a-zA-Z ]+?)'

        returnreview = []

        for review in reviews:
            words = review.split(' ')
            newReview = ""
            firstword = 1
            for word in words:
                # lower case for everything
                word = word.lower()
                # remove characters
                word = re.sub(regex_pattern, "", word)
                if word not in stop_list:
                    if firstword == 1:
                        newReview = word
                        firstword = 0
                    else:
                        newReview = newReview + ' ' + word
            returnreview.append(newReview)

        return returnreview

    def removestem(self, old):
        new = re.sub('[s][s][e][s]\b', 'ss', old)
        new = re.sub('[i][e][s]\b', 'i', old)
        new = re.sub('[s]\b', '', old)
        new = re.sub('[s][s][e][s]\b', 'ss', old)

        return new

    def train(self, lines):
        (sentiments, reviews, negatives, positives) = self.parse(lines)
        negatives_c = self.clean(negatives)
        positives_c = self.clean(positives)

        pos_wordcount = 0
        neg_wordcount = 0

        for line in negatives_c:
            words = line.split(' ')
            for word in words:
                if word not in self.wordlist:
                    self.wordlist.add(word)
                    self.neg_dict[word] = 1
                    self.pos_dict[word] = 0
                else:
                    self.neg_dict[word] += 1
                neg_wordcount +=1

        for line in positives_c:
            words = line.split(' ')
            for word in words:
                if word not in self.wordlist:
                    self.wordlist.add(word)
                    self.neg_dict[word] = 0
                    self.pos_dict[word] = 1
                else:
                    self.pos_dict[word] += 1
                pos_wordcount += 1

        # find the number of unique words in each class
        neg_words = 0
        pos_words = 0
        for key in self.wordlist:
            if self.neg_dict[key] != 0:
                neg_words += 1
            if self.pos_dict[key] != 0:
                pos_words += 1

        # convert counts into log probabilities
        self.neg_logprob = {x: math.log2((self.neg_dict[x]+1)/(neg_wordcount+neg_words)) for x in self.neg_dict}
        self.pos_logprob = {x: math.log2((self.pos_dict[x]+1)/(pos_wordcount+pos_words)) for x in self.pos_dict}

        # calculate priors
        review_count = len(positives) + len(negatives)
        self.pos_prior = math.log2((len(positives)+1)/(review_count+2))
        self.neg_prior = math.log2((len(negatives)+1)/(review_count+2))

        pass


    def classify(self, lines):
        reviews = []
        for line in lines:
            line = line.replace('\n', '')
            fields = line.split('|')
            reviews.append(fields[2])

        reviews_c = self.clean(reviews)
        results = []

        for review in reviews_c:
            pos_prob = self.pos_prior
            neg_prob = self.neg_prior
            words = review.split(' ')
            for word in words:
                if word in self.wordlist:
                    pos_prob += self.pos_logprob[word]
                    neg_prob += self.neg_logprob[word]
            if pos_prob > neg_prob:
                results.append('5')
            else:
                results.append('1')
        return results
