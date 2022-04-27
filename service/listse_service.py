from model.student import Student
from model.list_se import ListSE

class ListSE_Service:
    cities = ['Manizales', 'Pereira', 'Chinchina', 'Armenia']

    def __init__(self):
        self.students = ListSE()
        """
        #carloaiza = Student("363763763", 1, 5000000,True, "Carlos Loaiza",self.cities[2])
        carloaiza = Student({"identification":"75147236","name":"Carlos Loaiza",
                             "gender":1,"salary":2000000,"job":True,"city":self.cities[2]})
        self.students.add(carloaiza)
        self.students.add(Student({"identification": "1060456789",
                                   "name": "Valentina Hurtado",
                                   "gender":2, "salary":0,"job":False,
                                   "city":self.cities[0]}))
          """
    def get_all_students(self):
        if self.students.head == None:
            return {"message":"la lista esta vacia"}
        return self.students.head

    def add_student(self,data):
        encontro = 0
        ciudadestudiante = data['city' ]
        for ciudad in self.cities:
            if ciudadestudiante == ciudad:
                encontro = encontro + 1
            else:
                encontro = encontro + 0
        if encontro > 0 :
            student = Student(data)
            self.students.add(student)
        else:
            raise Exception('La ciudad no es valida')

    def add_student_to_start(self,data):
        encontro = 0
        ciudadestudiante = data['city' ]
        for ciudad in self.cities:
            if ciudadestudiante == ciudad:
                encontro = encontro + 1
            else:
                encontro = encontro + 0
        if encontro > 0 :
            student = Student(data)
            self.students.add_to_start(student)
        else:
            raise Exception('La ciudad no es valida')


    def invert(self):
        if self.students.head == None:
            return {"message":"la lista esta vacia"}
        else:
            self.students.invert()
            return {"message" : "Se ha invertido la lista"}
       # self.students.add(student)

    def changeXtremes (self):
        if self.student.head == None:
            return {"message": "la lista esta vacia"}
        elif self.students.head.next == None:
            return (self.students)
        else:
            self.students.exchange_extrem()
            return {"message":"Ya se invertio la lista"}


    def deletedata (self, id ):
        if self.students.head == None:
            return {"message":"No hay datos por eliminar"}
        else:
            self.students.deletedata(id)
            return {"message":"Datos eliminados"}