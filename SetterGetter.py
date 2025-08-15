#Getter / Setter method

# Setter การกำหนดค่าให้ object
# Getter การดึงค่าจาก object

# Ex_Setter
    # def setName(self, newname):
    #   self.__name = newname
    # Getter
    #   def getName(self):
    #   return self.__name

class Employee:
    def __init__(self, name, salary, department):
        # Prive attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

    # Prive method
    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.getName())
        print('เงินเดือน  = {}'+self.getSalary())
        print('แผนก  = {}'+self.getDepartment())

# setter mathod
    def setName(self, newname):
        self.__name = newname
    def setSalary(self, newsalary):
        self.__salary = newsalary
    def setDepartment(self, newdeparment):
        self.__department = newdeparment

    # Getter mathod
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department

emp1 = Employee('วิบูลย์', 50000, 'ธุระกิจ')
print('พนังงานดีเด่นประจำปี = {}'.format(emp1.getName()))
print('เงินเดือน = {}'.format(emp1.getSalary()))
print('แผนก = {}'.format(emp1.getDepartment()))
