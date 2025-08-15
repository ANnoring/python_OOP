# ชื่อพนักงาน ,เงินเดือน
class Employee: # การสร้าง class
    # สร้าง method
    def detail(self, name, salary, department):
        # สร้าง Attribute
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน  = {}'.format(self.salary))
        print('แผนก  = {}'.format(self.department))

# Attribute เป็นกลไกที่กำหนดคุณสมบัติให้กับ class
# การสร้าง Attribute
    # self.name = ชื่อพนักงาน
    # self.salary = เงินเดือน
    # self.age = อายุของพนักงาน

# Method เป็นกลไกทีี่กำหนดพฤติกรรมให้กับ class
# การสร้าง Method
#   def gedName(self):
#       return self.name
# การเรียกใช่งาน
#   ชื่อวัตถุ.getName()

# คีย์เวิร์ด self
#  การใช้คืย์เวิร์ด self จะเป็นตัวชี้หรือบ่งบอกว่าตอนนี้เราทำงานกับวัตถุใด
#  ให้บอกตัวตนของวัตถุนั้นๆ เช่น การกำหนดคุณสมบัติต่างๆ ในวัตถุ

# constructor
# เป็น method พิเศษที่จะถูกใช่งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ต้องระบุก็ได้)
# โครงสร้างของ constructor
#  def __init__(self):


# การสร้างวัตถุ

emp1 = Employee()
emp1.detail('วิบูลย์', 50000, 'ธุระกิจ')
emp1.showData()

emp2 = Employee()
emp2.detail('โกโก้', 10000, 'นอน')
emp2.showData()

emp3 = Employee()
emp3.detail('รพี', 1000000, 'คนรวย')
emp3.showData()
