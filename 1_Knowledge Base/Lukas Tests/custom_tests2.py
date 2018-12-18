import unittest
import read
from student_code import KnowledgeBase
from logical_classes import *

class CustomTests2(unittest.TestCase):

    def setUp(self):
        file = 'statements_kb2.txt'
        self.data = read.read_tokenize(file)
        data = read.read_tokenize(file)
        self.KB = KnowledgeBase([], [])
        for item in data:
            if isinstance(item, Fact) or isinstance(item, Rule):
                self.KB.kb_assert(item)

    def test1(self):
        ask1 = read.parse_input("fact: (attacked ?X ?Y)")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1), 1)
        self.assertEqual(str(answer1[0]), "?X : Ai, ?Y : Nosliw")

    def test2(self):
        ask1 = read.parse_input("fact: (inst ?X ?Y)")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1), 3)
        self.assertEqual(str(answer1[0]), "?X : Sarorah, ?Y : Sorceress")
        self.assertEqual(str(answer1[1]), "?X : Nosliw, ?Y : Dragon")
        self.assertEqual(str(answer1[2]), "?X : Sarorah, ?Y : Wizard")

    def test3(self):
        ask1 = read.parse_input("fact: (safe ?X)")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1), 1)
        self.assertEqual(str(answer1[0]), "?X : HappyDale")

    def test4(self):
        ask1 = read.parse_input("fact: (gives ?X ?Y ?IT)")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1), 1)
        self.assertEqual(str(answer1[0]), "?X : Ai, ?Y : Sarorah, ?IT : Loot")

    def test5(self):
        ask1 = read.parse_input("fact: (hero ?X)")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1), 1)
        self.assertEqual(str(answer1[0]), "?X : Ai")

        ask2 = read.parse_input("fact: (wielding ?X Weapon)")
        answer2 = self.KB.kb_ask(ask2)
        self.assertEqual(len(answer2), 1)
        self.assertEqual(str(answer2[0]), "?X : Ai")

        ask3 = read.parse_input("fact: (magicCastUpon ?X)")
        answer3 = self.KB.kb_ask(ask3)
        self.assertEqual(len(answer3), 1)
        self.assertEqual(str(answer3[0]), "?X : Ai")

        ask4 = read.parse_input("fact: (strong ?X)")
        answer4 = self.KB.kb_ask(ask4)
        self.assertEqual(len(answer4), 1)
        self.assertEqual(str(answer4[0]), "?X : Ai")

        ask5 = read.parse_input("fact: (defeatable ?X)")
        answer5= self.KB.kb_ask(ask5)
        self.assertEqual(len(answer5), 1)
        self.assertEqual(str(answer5[0]), "?X : Nosliw")

        ask6 = read.parse_input("fact: (dead ?X)")
        answer6 = self.KB.kb_ask(ask6)
        self.assertEqual(len(answer6), 1)
        self.assertEqual(str(answer6[0]), "?X : Nosliw")

        fact1 = read.parse_input("fact: (hero Ai)")
        self.KB.kb_retract(fact1)

        ask7 = read.parse_input("fact: (dead ?X)")
        answer7 = self.KB.kb_ask(ask7)
        self.assertEqual(len(answer7), 0)