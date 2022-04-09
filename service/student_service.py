from model.student import Student
import json

class StudentService:
    students = []
    cities = ['Manizales','Pereira','Chinchina','Armenia']
    def __init__(self):
        self.students=[]
        carloaiza = Student({"identification":"75147236","name":"Carlos"})
        self.students.append(carloaiza)
        """
        
        self.students.append(Student("363763763", 1, 22020202,True, "Carlos Loaiza",34,True,self.cities[2]))
        self.students.append(Student("363766667", 2, 2200000, True, "Valentina Hurtado",19,True,self.cities[1]))
        self.students.append(Student("233t6363", 1, 10000000, True, "Kevin Sánchez",45,False,self.cities[3]))
        self.students.append(Student("1006107803",1,2200000,True,"Alejandro Libreros",23,False,self.cities[0]))
        self.students.append(Student("1006107803", 2,2700000, True, "Laura",19,True,self.cities[1]))
        """
    def get_all_students(self):
        return self.students



    def get_percentage_students_by_gender(self,gender):
        count =0
        for student in self.students:
            if student.gender == gender:
                count = count +1
        return count/ len(self.students)

    def get_percentage_students_job_avg_salary(self, gender):
        count = 0
        sum_salary = 0
        for student in self.students:
            if student.job == True and student.gender == gender:
                count = count + 1
                sum_salary = sum_salary + student.salary
        if count > 0:
            return {"salario promedio": sum_salary / count,
                "cantidad": count,
                "% trabajan": count / len(self.students)}
        else:
            return{"error": "la consulta no generó resultados" }
#exercise 1
    def get_salary_students(self, gender, salary):
        list_gender = []
        for student in self.students:
            if student.gender == gender and student.salary > salary:
                list_gender.append(student.__dict__)
        return (list_gender)
#exercise 2
    def get_most_payed(self, gender):
        list_gender = []
        for student in self.students:
            if student.gender == gender:
                list_gender.append(student.salary)

        topSalary = list_gender[0]
        for salary in list_gender:
            if salary > topSalary:
                topSalary = salary

        for student_mayor in self.students:
            if student_mayor.gender == gender and student_mayor.salary == topSalary:
                return (student_mayor)
#exercise 3
    def determinar_salario(self, rangoMin, rangoMax ):
        listStudentDeter=[]

        for student in self.students:
            if student.salary >= rangoMin and student.salary <= rangoMax:
                listStudentDeter.append(student)
        return (listStudentDeter)
#exercise4
    def prom_salarial(self,gender):
        contPersontrab = 0
        acumSala = 0
        for student in self.students:
            if student.gender == gender:
                if student.job == True:
                    contPersontrab = contPersontrab + 1
                    acumSala = acumSala + student.salary
        promedio = acumSala/contPersontrab
        if gender == 1:
            return ("Promedio de los hombres :",promedio)
        if gender == 2:
            return ("promedio de las mujeres :",promedio)
#exercise5
    def edad_promedio(self):
        contadorEdad = 0
        sumEdad = 0
        for  student in self.students:
            contadorEdad = contadorEdad + 1
            sumEdad = sumEdad + student.edad
        return sumEdad/contadorEdad

    def get_zona_rural_encima_prom(self):
        personas = 0
        prom = self.edad_promedio()
        listapersorural = []
        for student in self.students:
            if student.zonaRural == True:
                if student.edad > prom:
                    listapersorural.append(student)
        return listapersorural
####################################################
    def get_dict_cities(self):
        dict_cities = {}
        for city in self.cities:
            dict_cities[city] = [0,0]
        return dict_cities

    def get_students_by_city(self):
        dict_cities = self.get_dict_cities()
        for student in self.students:
            if student.job:
                dict_cities[student.city][0] = dict_cities[student.city][0] + 1
            else:
                dict_cities[student.city][1] = dict_cities[student.city][1] + 1
        return dict_cities
