def revcomp(seq):
    """
    Returns the reverse complement of the input sequence.
    """
    seq = seq.upper()
    complements = {"A":"T",
                   "C":"G",
                   "G":"C",
                   "T":"A"}
    complement = ''
    for i in seq:
        complement += complements[i]

    return complement[::-1]
                   
