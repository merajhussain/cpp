from collections import defaultdict

d=defaultdict(list)

print(d['a'])

d = defaultdict(int)
print(d['a'])
d = defaultdict(tuple)
print(d['a'])
d = defaultdict(str)
print(d['a'])

names = ["Alice", "Arjun", "Bob", "Basha", "Charlie"]

grouped = {}

for name in names:
    key = name[0]   # first letter

    if key not in grouped:
        grouped[key] = []

    grouped[key].append(name)

print(grouped)


names = ["Alice", "Arjun", "Bob", "Basha", "Charlie"]

grouped = defaultdict(list)

for name in names:
    key = name[0]
    grouped[key].append(name)

print(grouped)

