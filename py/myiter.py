class my_iter:
    def __init__(self):
        self.lst=[]
        self.i=0

    def __iter__(self):
        for item in self.lst:
            yield item

    def append(self,item):
        self.lst.append(item)

    def __next__(self):
        if self.i<len(self.lst):
            yield self.lst[self.i]
            self.i=(self.i+1)%len(self.lst)




it = my_iter()
for i in range(0,10):
    it.append(i)

for item in it:
    print(item)