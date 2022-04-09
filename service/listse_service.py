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

       # self.students.add(student)
