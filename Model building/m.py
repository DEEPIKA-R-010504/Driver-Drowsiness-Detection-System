def is_isogram(S):
    char_freq = {}
    for c in S:
        if c in char_freq:
            return 0
        else:
            char_freq[c] = 1
    return 1


is_isogram("MM")