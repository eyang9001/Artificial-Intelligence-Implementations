
class BayesNet:
    def __init__(self):
        self.variables = []
        self.variable_names = []

    def add(self, node):
        """
        Adds Bayes Node to Bayes Net

        Parameters:
        node (BayesNode): node to be added to the Bayes Net

        Returns:
        None
        """
        if node.parents is None:
            self.variables.append(node)
            self.variable_names.append(node.name)
        else:
            for p in node.parents:
                if p not in self.variable_names:
                    print('Parent must be added to Net first')
                    return
            self.variables.append(node)
            self.variable_names.append(node.name)

    def get_var(self, name):
        """
        Gets a Bayes Net variable

        Parameters:
        name (String): name of the variable

        Returns:
        Object
        """
        print("getting", name)
        for v in self.variables:
            if v.name == v:
                return v
        print("None found")

class BayesNode:
    def __init__(self, name, parents, values):
        self.name = name
        self.parents = parents
        self.values = values

    def __str__(self):
        return("({}, {}, {})".format(self.name, self.parents, self.values))

    def repr(self):
        return("({}, {}, {})".format(self.name, self.parents, self.values))

    def probability(self, hypothesis, evidence):
        """
        Calculates the associated joint probability

        Parameters:
        hypothesis (Boolean): is the hypothesis True or False?
        evidence (Array): facts about the world state

        Returns:
        Float
        """
        if self.parents is None:
            v = self.values['']
        elif len(self.parents) == 1:
            v = self.values[evidence[self.parents[0]]]
        else:
            key = []
            for p in self.parents:
                if p in evidence:
                    key.append(evidence[p])
            v = self.values[tuple(key)]
        if hypothesis:
            return v
        else:
            return 1-v

