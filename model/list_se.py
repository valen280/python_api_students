from .node import Node

class ListSE:
    def __init__(self):
        self.head = None

    def add(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            if self.validate_exit(data.identification):
                raise Exception('ya existe estudiante con la identificacion')
            temp = self.head
            while temp.next != None:
                temp = temp.next
            #posicionados en el ultimo
            temp.next = Node(data)

    def validate_exit(self,id):
        temp = self.head
        while temp != None:
            if temp.data.identification == id:
                return True
            temp = temp.next
        return False