
    def test7(self):
        remove1 = read.parse_input("fact: (goodman a")
        self.KB.kb_retract(remove1)
        ask1 = read.parse_input("fact: (goodman ?X")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),1)
        self.assertEqual(str(answer1[0]), "?X : a")

        remove1 = read.parse_input("fact: (person a")
        self.KB.kb_retract(remove1)
        ask1 = read.parse_input("fact: (goodman ?X")
        answer1 = self.KB.kb_ask(ask1)
        self.assertEqual(len(answer1),0)