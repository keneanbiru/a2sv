class NumberContainers(object):

    def __init__(self):
        self.mapp={}
        self.valIdx=defaultdict(SortedSet)

    def change(self, index, number):
   
        if index in self.mapp:
            if self.mapp[index]==number: 
                return 
            preVal=self.mapp[index]
            self.valIdx.get(preVal).remove(index)
        
        self.valIdx[number].add(index)
        self.mapp[index]=number


    def find(self, number):
      
        if number not in self.valIdx or not self.valIdx[number]:
            return -1
        return self.valIdx[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)