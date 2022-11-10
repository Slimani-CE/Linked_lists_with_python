
class Data:
    def __init__(self, _id, name = "Name", age = 0):
        self.name = name
        self.age = age
        self.id = _id
        self.target = _id
        
    def __str__(self) -> str:
        return self.name

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)

    # Insertion methods
    def insertAtBeg(self, data):
        node = Node(data)
        node.next = self.head.next
        self.head.next = node

    def insertAtEnd(self, data):
        curNode = self.head
        while(curNode.next != None):
            curNode = curNode.next
        curNode.next = Node(data)

    def insertAtIndex(self, data, index):
        curNode = self.head
        curIndex = -1 # The head of the linked list is a sentinel Node that contains no data so the indexing starts with the second node. Therefor
        while(curIndex < index - 1 and curNode.next != None):
            curNode = curNode.next
            curIndex += 1
        node = Node(data)
        node.next = curNode.next
        curNode.next = node

    def insertBeforeNode(self, data, node):
        curNode = self.head
        oldNode = curNode
        while(curNode.next != None):
            oldNode = curNode
            curNode = curNode.next
            if(curNode.data.target == node.target):
                node = Node(data)
                node.next = curNode
                oldNode.next = node
                break

    def insertAfterNode(self, data, node):
        curNode = self.head
        while curNode.next != None :
            curNode = curNode.next
            if (curNode.data.target == node.target) :
                node = Node(data)
                node.next = curNode.next
                curNode.next = node
                break

    def insertArrayAtEnd(self, array):
        curNode = self.head
        while(curNode.next != None):
            curNode = curNode.next
        for i in range(len(array)):
            curNode.next = Node(array[i])
            curNode = curNode.next
        
    def insertArrayAtBeg(self, array):
        curNode = self.head
        nextNode = curNode.next
        for i in range(len(array)):
            node = Node(array[i])
            curNode.next = node
            curNode = curNode.next
        curNode.next = nextNode
            

    # Deletion methods
    def deletAtBeg(self):
        if(self.head.next != None):
            self.head.next = self.head.next.next
        
    def deleteAtEnd(self):
        if(self.head.next != None):
            curNode = self.head
            while(curNode.next.next != None):
                curNode = curNode.next
            curNode.next = None

    def deleteAtIndex(self, index):
        curIndex = -1
        curNode = self.head
        while(curNode.next != None and curIndex < index - 1):
            curNode = curNode.next
            curIndex += 1
        if(curNode.next != None):
            curNode.next = curNode.next.next


    def __str__(self) -> str:
        output = ""
        curHead = self.head
        count = 0
        while( curHead.next != None ):
            curHead = curHead.next
            output += "Node " + str(count) + " -> " + "{" + str(curHead.data) + "}\n"
            count += 1
        return output


def main():
    l1 = LinkedList()

    Ahmed = Data(10, "Ahmed", 31)
    Mustapha = Data(11, "Mustapha", 29)
    Khaled = Data(12, "Khaled", 35)

    Mohamed = Data(13, "Mohamed", 20)

    Salma = Data(14, "Salma", 21)
    hassan = Data(15, "Hassan", 23)
    othman = Data(16, "Othman", 21)

    array_1 = [Ahmed,Mustapha,Khaled] 
    array_2 = [Salma,hassan,othman] 

    # l1.insertAtBeg(Ahmed)
    # l1.insertAtEnd(Mustapha)
    # l1.insertAtBeg(Khaled)
    # l1.insertAtBeg(Mohamed)
    # l1.insertAtIndex(Salma, 1)
    # l1.insertAtIndex(hassan, 2)


    # l1.insertArrayAtEnd(array_2)
    
    # l1.insertArrayAtEnd(array_1)
    # l1.insertAtBeg(Mohamed)
    l1.insertArrayAtBeg(array_2)

    print("Before-------------")
    print(l1)

    # l1.insertAtBeg(Khaled)
    # l1.insertBeforeNode(Mohamed, Khaled)

    print("After-------------")
    print(l1)



if __name__ == "__main__":
    main()

