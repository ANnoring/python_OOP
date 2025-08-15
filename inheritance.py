# การสืบทอดคุณสมบัติ inheritance
# หลักการของ imheritance คือ ทำการสร้างสิ่งใหม่ขี้นด้วยสืบทอดหรือรับเอา (inheritance)
# ข้อดีของการ inheritance ตือ จากการที่สามารถนำสิ่งที่เคยสร้างขี้นแล้วนำกลับมาใช่ใหม่ (re-use) ได้
# ทำให้ช่วยประหยัดเวลาการทำงานลง เนื่องจากไม่ต้องเสียเวลาพัฒนาใหม่หมด
# Class -> ยกเว้น Priveate Attribute & Private Mehod
# การสืบทอดคุณสมบัติ
# คลาสแม่
# class Employee:

# คลาสลูก
# class Programmer(Employee)

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
        print('ชื่อพนักงาน = {}'+self.__name())
        print('เงินเดือน  = {}'+self.__salary())
        print('แผนก  = {}'+self.__department())

class Accounting(Employee):
    __departmentName = 'แผนกบัญชี'
    def __init__(self):
        pass

class Programmer(Employee):
    __departmentName = 'แผนกพัฒนาระบบ'
    def __init__(self):
        pass

class Sale(Employee):
    __departmentName = 'แผนกขาย'
    def __init__(self):
        pass

account = Accounting()
print(account._companyName)
programmer = Programmer()
print(programmer._minSalary)
sale = Sale()
print(sale._maxSalary)