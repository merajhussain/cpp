from collections import *

s1="test"
s2="test"
c1 = Counter(s1)
c2 = Counter(s2)
print(c1)
print(c2)
c1.subtract(c2)

print(c1)
s3="test_counter"
c3 = Counter(s3)
print(c3)
print(c3.most_common())
print(c3.most_common(1))
