import unittest
import read
from student_code import KnowledgeBase
from logical_classes import *

class CustomTests1(unittest.TestCase):

    def setUp(self):
        file = 'statements_kb.txt'
        self.data = read.read_tokenize(file)
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.KB.kb_assert(item)

    def test1(self):
        ask1 = read.parse_input("fact: (inst bigbox ?X)")
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer), 2)
        self.assertEqual(str(answer[0]), "?X : box")
        self.assertEqual(str(answer[1]), "?X : container")

        ask2 = read.parse_input("fact: (inst ?X box)")
        answer = self.KB.kb_ask(ask2)
        self.assertEqual(len(answer), 2)
        self.assertEqual(str(answer[0]), "?X : bigbox")
        self.assertEqual(str(answer[1]), "?X : littlebox")

    def test2(self):
        ask1 = read.parse_input("fact: (flat ?X)")
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer),4)
        self.assertEqual(str(answer[0]), "?X : cube1")
        self.assertEqual(str(answer[1]), "?X : cube2")
        self.assertEqual(str(answer[2]), "?X : cube3")
        self.assertEqual(str(answer[3]), "?X : cube4")

    def test3(self):
        fact = read.parse_input("fact: (inst cube1 cube)")
        self.KB.kb_retract(fact)
        fact = read.parse_input("fact: (inst cube3 cube)")
        self.KB.kb_retract(fact)
        ask1 = read.parse_input("fact: (flat ?X)")
        answer = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer),2)
        self.assertEqual(str(answer[0]), "?X : cube2")
        self.assertEqual(str(answer[1]), "?X : cube4")

    def test4(self):
        rule = read.parse_input("rule: ((inst ?x cube)) -> (flat ?x)")
        self.KB.kb_retract(rule)
        ask1 = read.parse_input("fact: (flat ?X)")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),4)

    def test5(self):
        ask1 = read.parse_input("fact: (covered ?X)")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),0)
        ask2 = read.parse_input("fact: (married ?X ?Y)")
        answer2 = self.KB.kb_ask(ask2)
        self.assertEqual(len(answer2),0)
        ask3 = read.parse_input("fact: (happy ?X)")
        answer3 = self.KB.kb_ask(ask3)
        self.assertEqual(len(answer3),0)

    def test6(self):
        ask1 = read.parse_input("fact: (inst ?X block")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),9)
        self.assertEqual(str(answer1[0]), "?X : pyramid1")
        self.assertEqual(str(answer1[1]), "?X : pyramid2")
        self.assertEqual(str(answer1[2]), "?X : pyramid3")
        self.assertEqual(str(answer1[3]), "?X : pyramid4")
        self.assertEqual(str(answer1[4]), "?X : cube1")
        self.assertEqual(str(answer1[5]), "?X : cube2")
        self.assertEqual(str(answer1[6]), "?X : cube3")
        self.assertEqual(str(answer1[7]), "?X : cube4")
        self.assertEqual(str(answer1[8]), "?X : sphere1")