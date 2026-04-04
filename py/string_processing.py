class string_processing:
    def __init__(self):
        pass

    def find_first_uppercase_character(self, string):
        for c in string:
            if c.isupper():
                return c
        return ""

    def __len_helper(self, string):
        if string == "":
            return 0
        return 1+self.__len_helper(string[1:])

    def strlen(self, string):
        return self.__len_helper(string)

    def count_consonants(self, string):
        count = 0
        for c in string:
            if c not in ["a", "e", "i", "o", "u"]:
                count += 1
        return count

    def recursive_multiply(self,a,b):
        if b==0:
            return 0
        b -=1
        return a+self.recursive_multiply(a,b)
