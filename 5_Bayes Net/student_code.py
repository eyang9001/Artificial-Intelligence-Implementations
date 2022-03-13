def ask(var, value, evidence, bn):
    e_copy_og = evidence.copy()

    evidence[var] = not value
    e_copy_og[var] = value

    # make list of known variables
    known_vars = e_copy_og.keys()

    # calculate P(H|E): P(E|H) * P(H)
    h_given_e = recursive(bn.variable_names.copy(), e_copy_og, known_vars,  bn)
    # calculate P(~H|E): P(E|~H) * P(~H)
    not_h_given_e = recursive(bn.variable_names.copy(), evidence, known_vars, bn)
    # calculate alpha: P(E|H) * P(H) + P(E|~H) * P(~H)
    alpha = h_given_e + not_h_given_e
    # return P(H|E)
    return (h_given_e/alpha)

def recursive(varlist, evidence, known_vars, bn):
    # base case check
    if not len(varlist):
        return 1
    else:
        # get next variable
        var = varlist.pop(0)
        
        # if next variable is known
        if var in known_vars:
            # look up probability in CPT using probability function in Bayes Net
            ind = bn.variable_names.index(var)
            p = bn.variables[ind].probability(evidence[var], evidence)

            # recurse on rest of varlist
            jp = p * recursive(varlist.copy(), evidence, known_vars, bn)
            return jp
        
        # if next variable is unknown
        else:
            # find joint probabilities when unknown is True or False
            e_true = evidence.copy()
            e_true[var] = True
            e_false = evidence.copy()
            e_false[var] = False
            
            ind = bn.variable_names.index(var)
            p_true = bn.variables[ind].probability(True, e_true)
            p_false = bn.variables[ind].probability(False, e_false)
            
            jp_true = p_true * recursive(varlist.copy(), e_true, known_vars, bn)
            jp_false = p_false * recursive(varlist.copy(), e_false, known_vars,bn)

            # compute sum and recurse
            return  (jp_true + jp_false)
           

