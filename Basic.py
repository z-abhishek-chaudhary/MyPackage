class Detector:
    def __init__(self, name, list, dict):
        self.name = name
        self.list = list
        self.dict = dict
    

def __iter__(self):
    self.n = 0
    return self

def __next__(self):
    if self.n < len(self.list):
        num = self.list[n]
        n += 1
        return num
    else:
        raise StopIteration


    def insert(self, value):
        pass
    
    def remove(self, value):
        pass
    
    def search(self, value):
        pass

# To get the length of the list and dictionary
    def __len__(self) -> int:
        length = len(self.list) + len(self.dict)
        return f"Sum of length of list and dict is: {length}"


# To get the sum of the values of the list and dictionary
    def __sum__(self) -> int:
        sum_ = sum(self.list) + sum(self.dict.values())
        return f"Sum of values of list and dict is: {sum_}"


list1 = [1,2,3]
dict1 = {
    'a':1, 'b':2, 'c':3, 'd':4, 'e':5
}

dect = Detector("Abhishek", list1, dict1)
m = iter(list1)
# print(next(m))

dect.n = 0

for i in dect:
    print(next(m))
