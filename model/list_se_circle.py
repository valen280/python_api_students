from model.student import Student
from .node import Node

class ListSECircle:
    def __init__(self):
        self.head = None

    def add_circle(self,data:Student):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head

        else:
            if self.validete_exist(data.identification):
                raise Exception ("ya existe estudiante con esa identificación")
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                # posicionados en el ultimo
            temp.next = Node(data)
            temp.next.next = self.head
            self.head = temp.next

    def add_to_start_circle(self, data: Student):
        if self.head == None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            if self.validete_exist(data.identification):
                raise Exception("ya existe estudiante con esa identificación")
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
                # posicionados en el ultimo
            temp.next = Node(data)
            temp.next.next = self.head
            self.head = temp.next

    def count_listSECircle(self):
        list_students_circle : []
        temp = self.head
        count = 0
        if self.head != None:
            temp = self.head
            while temp.next != self.head:
                list_students_circle.append(temp.data)
                temp = temp.next
                count = count + 1
                list_students_circle.append(temp.data)
        return count
