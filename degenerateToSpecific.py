def degenerateToSpecific(primer):
    """
    Given a primer sequence with degenerative bases, returns a list of all
    possible completely specified sequences.
    """
    bases = {'W': ['A','T'],
             'S': ['C','G'],
             'M': ['A','C'],
             'K': ['G','T'],
             'R': ['A','G'],
             'Y': ['C','T'],
             'B': ['C','G','T'],
             'D': ['A','G','T'],
             'H': ['A','C','T'],
             'V': ['A','C','G'],
             'N': ['A','C','G','T']}

    primer = primer.upper()
            
    seqs = ['']

    for i in range(len(primer)):
        updated = []
        if primer[i] in ['A','C','G','T']: ## Standard base
            for j in range(len(seqs)):
                updated.append(seqs[j] + primer[i])
        else: ## Degenerate base
            for j in range(len(seqs)):
                if primer[i] == 'I': ## Inosine equivalent to N but don't want to double-list
                    for k in bases['N']:
                       updated.append(seqs[j] + k) 
                else:
                    for k in bases[primer[i]]:
                        updated.append(seqs[j] + k)
        seqs = updated[:]

    return seqs
    
