import math


def spread_sheet_encoding(s):
    mp_codes={
        "A":1,"B":2,"C":3,"D":4,
        "E":5,"F":6,"G":7,"H":8,
        "I":9,"J":10,"K":11,
        "L":12,"M":13,"N":14,"O":15,
        "P":16,"Q":17,"R":18,
        "S":19,"T":20,"U":21,
        "V":22,"W":23,"X":24,
        "Y":25,"Z":26,
    }
    idx=0
    encoded_string=0
    for c in s[::-1]:
        if c in mp_codes:
            val = int(math.pow(26,idx))
            encoded_string += mp_codes[c]*val

            idx+=1

    return encoded_string