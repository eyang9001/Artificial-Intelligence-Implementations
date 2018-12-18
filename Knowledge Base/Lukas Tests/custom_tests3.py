import unittest
import read
from student_code import KnowledgeBase
from logical_classes import *

class CustomTests3(unittest.TestCase):

    def setUp(self):
        file = 'statements_kb3.txt'
        self.data = read.read_tokenize(file)
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.KB.kb_assert(item)

    def test1(self):
        ask1 = read.parse_input("fact: (goodman ?X)")
        answer1 = self.KB.kb_ask(ask1)

        self.assertEqual(len(answer1), 1)
        self.assertEqual(str(answer1[0]), "?X : a")

    def test2(self):
        fact1 = read.parse_input("fact: (goodman a)")
        self.KB.kb_retract(fact1)

        ask1 = read.parse_input("fact: (goodman ?X)")
        answer1 = self.KB.kb_ask(ask1)

        self.assertEqual(len(answer1), 1)
        self.assertEqual(str(answer1[0]), "?X : a")

    def test3(self):
        fact1 = read.parse_input("fact: (hero a)")
        fact2 = read.parse_input("fact: (person a)")
        self.KB.kb_retract(fact1)
        self.KB.kb_retract(fact2)

        ask1 = read.parse_input("fact: (hero ?X)")
        ask2 = read.parse_input("fact: (person ?X)")
        answer1 = self.KB.kb_ask(ask1)
        answer2 = self.KB.kb_ask(ask2)
        self.assertEqual(len(answer1), 0)
        self.assertEqual(len(answer2), 0)

    def test4(self):
        fact1 = read.parse_input("fact: (hero a)")
        fact2 = read.parse_input("fact: (person a)")
        fact3 = read.parse_input("fact: (goodman a)")
        self.KB.kb_retract(fact1)
        self.KB.kb_retract(fact2)
        self.KB.kb_retract(fact3)

        ask1 = read.parse_input("fact: (goodman ?X")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),0)

    def test5(self):
        fact1 = read.parse_input("fact: (hero a)")
        fact2 = read.parse_input("fact: (person a)")
        self.KB.kb_retract(fact1)
        self.KB.kb_retract(fact2)

        ask1 = read.parse_input("fact: (goodman ?X")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),1)
        self.assertEqual(str(answer1[0]), "?X : a")

        fact3 = read.parse_input("fact: (goodman a)")
        self.KB.kb_retract(fact3)
        ask1 = read.parse_input("fact: (goodman ?X")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),0)

    def test6(self):
        fact1 = read.parse_input("fact: (human a)")
        rule1 = read.parse_input("rule: ((human ?y)) -> (person ?y)")
        self.KB.kb_assert(fact1)
        self.KB.kb_assert(rule1)

        remove1 = read.parse_input("fact: (person a")
        self.KB.kb_retract(remove1)
        ask1 = read.parse_input("fact: (goodman ?X")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),1)
        self.assertEqual(str(answer1[0]), "?X : a")

        remove1 = read.parse_input("fact: (human a")
        self.KB.kb_retract(remove1)
        ask1 = read.parse_input("fact: (goodman ?X")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),1)
        self.assertEqual(str(answer1[0]), "?X : a")

        remove1 = read.parse_input("fact: (person a")
        self.KB.kb_retract(remove1)
        ask1 = read.parse_input("fact: (goodman ?X")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),1)
        self.assertEqual(str(answer1[0]), "?X : a")

        remove1 = read.parse_input("fact: (goodman a")
        self.KB.kb_retract(remove1)
        ask1 = read.parse_input("fact: (goodman ?X")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),0)