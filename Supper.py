# Super
# เมื่อต้องการเรียกใช้งานคุณสมบัติต่างๆ ในคลาสแม่
# เช่น Constructor, method, Attridute

# super().__init__(name)

class Employee:
    #class variable
    _minSalary = 30000
    _maxSalary = 50000
    _companyName = 'บริษัท XYZ จำกัด'

    def __init__(self, name, salary, department):
        # Prive attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

    # Prive method
    def _showData(self):
        print('ชื่อพนักงาน = '+self.__name)
        print('เงินเดือน  = ', format(self.__salary))
        print('แผนก  = '+self.__department)

class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showData()

class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showData()

class Sale(Employee):
    __departmentName = 'แผนกขาย'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        super()._showData()

account = Accounting("นูน", 30000)

programmer = Programmer("โน๊ต", 60000)

sale = Sale("นัด", 25000)
