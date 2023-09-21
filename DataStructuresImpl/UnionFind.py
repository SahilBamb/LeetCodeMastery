class UnionFind:
    def __init__(self):
        self.rank = {} #size of each set
        self.parent = {} #parent of each node

    def __str__(self):
        rList = {}
        for num in self.parent:
            par = self.find(num)
            if par not in rList:
                rList[par] = []
            rList[par].append(num)

        return str(list(rList.values()))

    def createSet(self, value):
        self.rank[value] = 1
        self.parent[value] = value

    def find(self, value):
        if value not in self.parent:
            return None
        while (value!=self.parent[value]):
            value = self.parent[self.parent[value]]
        return value

    def union(self, valueOne, valueTwo):
        set1 = self.find(valueOne)
        set2 = self.find(valueTwo)
        if set1 == None or set2 == None or set1==set2:
            return
        if self.rank[set1] > self.rank[set2]:
            self.rank[set1] += self.rank[set2]
            self.rank[set2] = 0
            self.parent[set2] = set1
        else:
            self.rank[set2] += self.rank[set1]
            self.rank[set1] = 0
            self.parent[set1] = set2


# Initially: (5) (10) -> After Union: (5, 10) -> After 9: (5, 10) (9) -> After Union w/ 5 or 10: (5,10,9)


obj = UnionFind()
obj.createSet(5)

assert obj.find(5) == 5, "Incorrect Set: answer is 5"
obj.createSet(10)
assert obj.find(10) == 10, "Incorrect Set: answer is 10"

obj.union(5,10)
assert obj.find(5) == 10, "Incorrect Set: answer is 10"
assert obj.find(10) == 10, "Incorrect Set: answer is 10"

obj.createSet(9)
assert obj.find(9) == 9, "Incorrect Set: answer is 9"

print(obj) #[[5, 10], [9]]

obj.union(5,9)
assert obj.find(9) == 10, "Incorrect Set: answer is 10"

obj.union(5,30)
assert obj.find(30) == None, "Incorrect Set: answer is None"

print(obj) #[[5, 10, 9]]

obj.createSet(13)
assert obj.find(13) == 13, "Incorrect Set: answer is 13"

obj.createSet(15)
assert obj.find(15) == 15, "Incorrect Set: answer is 15"

obj.union(13,15)
assert obj.find(15) == 15, "Incorrect Set: answer is 15"
assert obj.find(13) == 15, "Incorrect Set: answer is 13"

print(obj) #[[5, 10, 9],[13,15]]

