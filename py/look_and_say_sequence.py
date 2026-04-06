def look_and_say_sequence(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        j =i
        while j + 1 < len(s) and s[j] == s[j+1]:
            j += 1
            count += 1
        result.append(str(count) + s[i])
        i = j+1
    return ''.join(result)




def generate_next_num(start):
    return look_and_say_sequence(start)




