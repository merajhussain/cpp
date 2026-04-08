def is_string_permutation(s1,s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")
    if len(s1) != len(s2):
        return False
    mp = dict()
    for c in s1:
        if c not in mp:
            mp[c] = 1
        else:
            mp[c] += 1

    for c in s2:
        if c not in mp:
            return False
        else:
            mp[c] -= 1

    for k,v in mp.items():
        if v != 0:
            return False

    return True