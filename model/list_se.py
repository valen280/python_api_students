from .node import Node
from model.student import Student
class ListSE:
    def __init__(self):
        self.head = None

    def add(self,data:Student):
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

    def add_to_start(self,data:Student):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp

    def invert(self):
        if self.head != None:
            list_cp = ListSE()
            temp = self.head
            while temp != None:
                list_cp.add_to_start(temp.data)
                temp = temp.next
            self.head = list_cp.head


    def validate_exit(self,id):
        temp = self.head
        while temp != None:
            if temp.data.identification == id:
                return True
            temp = temp.next
        return False

    def exchange_extrem(self):
        temp = self.head
        if temp != None:
            if temp.next != None:
                head = self.head
                list_ex = ListSE()
                next = temp.next
                while next.next != None:
                    list_ex.add(temp.data)
                    next = temp.next
                ultimate = next
                list_ex.add(head.data)
                list_ex.add_to_start(ultimate.data)
                self.head=list_ex.head

    def deletedata(self,id):
        if self.head.identification == id:
         self.head = self.head.next
        else:
            temp = self.head
            while temp.next != None:
                if temp.next.data.id == id:
                    temp.next = temp.next.next
                    break
                temp = temp.next

    def woman_first(self):
        list_cp = ListSE()
        temp = self.head
        while temp != None:
            if temp.data.gender == 2:
                list_cp.add_to_start(temp.data)
            else:
                list_cp.add(temp.data)
            temp = temp.next
        self.head = list_cp.head
"""
    def insert_position(self):
        count=0
        position = self.head
        if self.head != None:
            if position > 0 and position <= count +1:
                add_to_star(Student)
            else:
                temp = self.head
                count = 1
                if count == position -1:
                    new_nodo = None(data)
                    new_nodo = new_node.next
                    pass
"""


