import read, copy
from util import *
from logical_classes import *

verbose = 0


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules
        self.ie = InferenceEngine()

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def _get_fact(self, fact):
        """INTERNAL USE ONLY
        Get the fact in the KB that is the same as the fact argument

        Args:
            fact (Fact): Fact we're searching for

        Returns:
            Fact: matching fact
        """
        for kbfact in self.facts:
            if fact == kbfact:
                return kbfact

    def _get_rule(self, rule):
        """INTERNAL USE ONLY
        Get the rule in the KB that is the same as the rule argument

        Args:
            rule (Rule): Rule we're searching for

        Returns:
            Rule: matching rule
        """
        for kbrule in self.rules:
            if rule == kbrule:
                return kbrule

    def kb_add(self, fact_rule):
        """Add a fact or rule to the KB
        Args:
            fact_rule (Fact|Rule) - the fact or rule to be added
        Returns:
            None
        """
        printv("Adding {!r}", 1, verbose, [fact_rule])
        if isinstance(fact_rule, Fact):
            if fact_rule not in self.facts:
                self.facts.append(fact_rule)
                for rule in self.rules:
                    self.ie.fc_infer(fact_rule, rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.facts.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.facts[ind].supported_by.append(f)
                else:
                    ind = self.facts.index(fact_rule)
                    self.facts[ind].asserted = True
        elif isinstance(fact_rule, Rule):
            if fact_rule not in self.rules:
                self.rules.append(fact_rule)
                for fact in self.facts:
                    self.ie.fc_infer(fact, fact_rule, self)
            else:
                if fact_rule.supported_by:
                    ind = self.rules.index(fact_rule)
                    for f in fact_rule.supported_by:
                        self.rules[ind].supported_by.append(f)
                else:
                    ind = self.rules.index(fact_rule)
                    self.rules[ind].asserted = True

    def kb_assert(self, fact_rule):
        """Assert a fact or rule into the KB

        Args:
            fact_rule (Fact or Rule): Fact or Rule we're asserting
        """
        printv("Asserting {!r}", 0, verbose, [fact_rule])
        self.kb_add(fact_rule)

    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Statement to be asked (will be converted into a Fact)

        Returns:
            listof Bindings|False - list of Bindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        if factq(fact):
            f = Fact(fact.statement)
            bindings_lst = ListOfBindings()
            # ask matched facts
            for fact in self.facts:
                binding = match(f.statement, fact.statement)
                if binding:
                    bindings_lst.add_bindings(binding, [fact])

            return bindings_lst if bindings_lst.list_of_bindings else []

        else:
            print("Invalid ask:", fact.statement)
            return []

    def kb_retract(self, fact_or_rule):
        """Retract a fact from the KB

        Args:
            fact (Fact) - Fact to be retracted

        Returns:
            None
        """
        printv("Retracting {!r}", 0, verbose, [fact_or_rule])
        ####################################################
        # Student code goes here

        if isinstance(fact_or_rule, Fact):
            isRule = 0
        else:
            isRule = 1

        if fact_or_rule.asserted:  # If the fact or rule was passed in (not recursively), find pointer within kb
            if isRule:
                for i in self.rules:
                    if str(i) == str(fact_or_rule):
                        fact_or_rule = i
            else:
                for i in self.facts:
                    if str(i.statement) == str(fact_or_rule.statement):
                        fact_or_rule = i
        if len(fact_or_rule.supported_by) == 0:  # if the fact or rule is able to be removed because it is not supported by anything
            # Check the rules and facts that are supported by currently removed one. Remove from list of supported by, and then remove those if last in list
            sFacts = fact_or_rule.supports_facts
            for i in sFacts:
                pairs = i.supported_by
                for pair in pairs:
                    if pair[isRule] == fact_or_rule:
                        i.supported_by.remove(pair)
                        if len(i.supported_by) == 0 and not i.asserted:
                            self.kb_retract(i)

            sRules = fact_or_rule.supports_rules
            for ii in sRules:
                pairs = ii.supported_by
                for pair in pairs:
                    if pair[isRule] == fact_or_rule:
                        ii.supported_by.remove(pair)
                        if len(ii.supported_by) == 0 and not ii.asserted:
                            self.kb_retract(ii)

            # Remove current fact/rule from the supported_by in other rules/facts
            pairs = fact_or_rule.supported_by
            for i in pairs:
                if isRule:
                    i[0].supports_rules.remove(fact_or_rule)
                    i[1].supports_rules.remove(fact_or_rule)
                else:
                    i[0].supports_facts.remove(fact_or_rule)
                    i[1].supports_facts.remove(fact_or_rule)

            if isRule:
                self.rules.remove(fact_or_rule)
            else:
                self.facts.remove(fact_or_rule)

class InferenceEngine(object):
    def fc_infer(self, fact, rule, kb):
        """Forward-chaining to infer new facts and rules

        Args:
            fact (Fact) - A fact from the KnowledgeBase
            rule (Rule) - A rule from the KnowledgeBase
            kb (KnowledgeBase) - A KnowledgeBase

        Returns:
            Nothing            
        """
        printv('Attempting to infer from {!r} and {!r} => {!r}', 1, verbose,
            [fact.statement, rule.lhs, rule.rhs])
        ####################################################
        # Student code goes here
        result = match(rule.lhs[0], fact.statement)
        if result:  # If the rule's first lhs statement matches the fact statement
            if len(rule.lhs) == 1:  # If this results in a new fact
                newState = instantiate(rule.rhs, result)
                newFact = Fact(newState, [[fact, rule]])
                kb.kb_add(newFact)
                indF = kb.facts.index(fact)
                indR = kb.rules.index(rule)
                newInd = kb.facts.index(newFact)
                kb.facts[indF].supports_facts.append(kb.facts[newInd])
                kb.rules[indR].supports_facts.append(kb.facts[newInd])
            else:  # else this results in a new rule (with one less statement)
                newrhs = instantiate(rule.rhs, result)
                newlhs = []
                for curlhs in rule.lhs[1:]:
                    newlhs.append(instantiate(curlhs, result))
                newRule = Rule([newlhs, newrhs], [[fact, rule]])
                kb.kb_add(newRule)
                ind = kb.rules.index(newRule)
                fact.supports_rules.append(kb.rules[ind])
                rule.supports_rules.append(kb.rules[ind])


