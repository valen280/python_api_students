class Student:
    """
    def __init__(self,identification,gender, salary,job,name,edad,zonaRural,city):
        self.idenfication = identification
        self.gender = gender
        self.salary = salary
        self.job = job
        self.name = name
        self.edad = edad
        self.zonaRural = zonaRural
        self.city = city


    @classmethod
    def fromDict(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
  """
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
