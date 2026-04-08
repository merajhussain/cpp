def is_anagram(s1,s2):
    s1=s1.lower().replace(' ','')
    s2=s2.lower().replace(' ','')
    if len(s1)!=len(s2):
        return False
    mp_chars = dict()
    for c in s1:
        if c in mp_chars:
            mp_chars[c]+=1
        else:
            mp_chars[c]=1
    for c in s2:
        if c in mp_chars:
            mp_chars[c]-=1
        else:
            mp_chars[c]=0

    for k,v in mp_chars.items():
        if v!=0:
            return False
    return True
