# ClassInstanceVariable

# Class Variable คือ ตัวแปรที่ทำงานภายใน class ส่วนอื่นสามารถเข้าถึงข้อมุูลส่วนนีได้เลย (static attribute)
# โดยไม่จำเป็นต้องสร้าง object ขึ้นมา

# instanแe Veriable คือ ตัวแปรที่อยู่ภายใน object
# สามารถเข้าถึงข้อมูลส่วนนี้โดยต้องสร้าง object ขึ้นมา

class Employee:
    _minSalary = 30000
    _mixSalary = 50000
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

    def getName(self):
        return self.__name


emp1 = Employee('วิบูลย์', 50000, 'ธุระกิจ')
# print('เงินเดือนขั้นต่ำ = '+str(Employee.__minSalary))
print(Employee._companyName)