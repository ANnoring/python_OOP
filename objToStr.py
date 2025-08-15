# obJotStr
#แปลง Object เป็น String
# def __str__(self):
# return "ชุดข้อความ"

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

        #รายได้ต่อปี
    def _grtIncome(self):
        return self.__salary * 12

    def __str__(self):
        return ("ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {} , รายได้ต่อปี = {}"
                .format(self.__name, self.__department, self.__salary, self._grtIncome()))

class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)

class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)

class Sale(Employee):
    __departmentName = 'แผนกขาย'
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)

account = Accounting("นูน", 30000)
print(account.__str__())

programmer = Programmer("โน๊ต", 60000)
print(programmer.__str__())

sale = Sale("นัด", 25000)
print(sale.__str__())
