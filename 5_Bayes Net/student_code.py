
def ask(var, value, evidence, bn):
    #finds all of the unknown and known variables
    evidence2 = evidence.copy()
    evidence2[var] = value

    evidence3 = evidence.copy()
    evidence3[var] = not value

    unknown = list(set(bn.variable_names) - set(evidence2.keys()))

    numerator = askRecursive(evidence2, bn, unknown, bn.variable_names.copy())
    denom = numerator + askRecursive(evidence3, bn, unknown, bn.variable_names.copy())
    quotient = numerator/denom

    return quotient

def askRecursive(evidence, bn, unknown, varlist):
    curvar = varlist.pop(0)

    if curvar in unknown:
        #  if the current variable is unknown will have to sum the values
        if len(varlist) > 0:
            trueevidence = evidence.copy()
            trueevidence[curvar] = True
            falseevidence = evidence.copy()
            falseevidence[curvar] = False

            varindex = bn.variable_names.index(curvar)
            trueprob = bn.variables[varindex].probability(True, trueevidence)
            falseprob = bn.variables[varindex].probability(False, falseevidence)

            return (trueprob * askRecursive(trueevidence, bn, unknown, varlist.copy())) + (falseprob * askRecursive(falseevidence, bn, unknown, varlist.copy()))
        else:
            return 1
    else:
        varindex = bn.variable_names.index(curvar)
        prob = bn.variables[varindex].probability(evidence[curvar], evidence)

    if len(varlist) > 0:
        return prob * askRecursive(evidence, bn, unknown, varlist.copy())
    else:
        return prob


