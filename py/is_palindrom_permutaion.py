def is_palindrome_permutation(s):
    s = s.lower().replace(" ","")
    len_is_odd = len(s)%2!=0
    if len(s)==0:
        return True
    mp_chars=dict()
    for char in s:
        if char in mp_chars:
            mp_chars[char]=mp_chars[char]+1
        else:
            mp_chars[char]=1

    odd_count=0
    for k,v in mp_chars.items():
        if v%2!=0:
            odd_count+=1
    if len_is_odd and odd_count > 1:
        return False
    if len_is_odd is False and odd_count > 0:
        return False
    return True



