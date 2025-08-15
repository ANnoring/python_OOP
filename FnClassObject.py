# FnClassObject
# ฟังก์ชั่นที่ทำงานร่วมกับ class และ object

# isinstance และ dir คือฟังก์ชั่นที่ทำงานร่วมกับ class และ object
# โดยมีรายระเอียดดังนี้
# isinstance => เช็คว่า object นี้ถูกสร้างจาก class ที่เรานิยามหรือไม่
# dir => แสดง attribute และ mothod
# __class__ => แสดงชื่อ class และ object

class Employee:
    def __init__(self, name, salary, department):

        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน  = {}'.format(self.salary))
        print('แผนก  = {}'.format(self.department))


emp1 = Employee('วิบูลย์', 50000, 'ธุระกิจ')
emp2 = Employee('โกโก้', 10000, 'นอน')
emp3 = Employee('รพี', 1000000, 'คนรวย')
emp4 = Employee('plim', 20000, 'HR')

print(isinstance(emp1, Employee))
print(dir(emp1))
print(emp1.__class__)