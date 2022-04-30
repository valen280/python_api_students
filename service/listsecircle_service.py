from model.student import Student
from model.ListSECircle import ListSECircle
class ListSECircle:

    cities = ['Manizales', 'Pereira', 'Chinchina', 'Armenia']

    def __init__(self):
        self.students = ListSECircle()

    def get_all_students(self):
        if self.students.head == None:
            return {"message":"la lista esta vacia"}
        return self.students.head

    def add_circle(self,data):
        encontro = 0
        ciudadestudiante = data['city' ]
        for ciudad in self.cities:
            if ciudadestudiante == ciudad:
                encontro = encontro + 1
            else:
                encontro = encontro + 0
        if encontro > 0 :
            student = Student(data)
            self.students.add_circle(student)
        else:
            raise Exception('La ciudad no es valida')

    def add_to_start_circle(self,data):
        encontro = 0
        ciudadestudiante = data['city' ]
        for ciudad in self.cities:
            if ciudadestudiante == ciudad:
                encontro = encontro + 1
            else:
                encontro = encontro + 0
        if encontro > 0 :
            student = Student(data)
            self.students.add_to_start_circle(student)
        else:
            raise Exception('La ciudad no es valida')

