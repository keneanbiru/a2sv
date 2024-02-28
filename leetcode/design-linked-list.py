class node:
        def __init__(self,value=0):
            self.value=value
            self.next=None
        def __str__(self):
            arr=[self.value]

            temp=self.next
            while temp:
                arr.append(temp.value)
                temp=temp.next
            return "->".join(map(str,arr))

class MyLinkedList:
    
    def __init__(self):
        self.head= node()
    
   
    def get(self, index: int) -> int:
        temp=self.head
        for i in range(index+1):
            temp=temp.next
            if temp==None :
                return -1
        print(self.head)
        return(temp.value)


    def addAtHead(self, val: int) -> None:
        newnode=node(val)
        newnode.next=self.head.next
        self.head.next=newnode

    
    def addAtTail(self, val: int) -> None:
        newnode=node(val)
        temp=self.head
        while temp.next!=None:
            temp=temp.next
        temp.next=newnode
        newnode.next=None


    def addAtIndex(self, index: int, val: int) -> None:
        newnode=node(val)
        temp=self.head
        for i in range (index):
            temp=temp.next
            if temp==None:
                # temp.next=newnode
                return
        newnode.next=temp.next
        temp.next=newnode
        

    def deleteAtIndex(self, index: int) -> None:
        temp=self.head
        for i in range(index):
        
            temp=temp.next
            if temp==None:
                return
        if temp.next:
            temp.next=temp.next.next
        
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)