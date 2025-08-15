# constructor
    # เป็น Method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
    # โครงสร้าง constructor
        # def __init__(self):
        #   pass

# destructor
# เป็น method พิเศษที่ตรงข้างกับ constructor จะถูกใช้งานเมื่อ
# สิ้นสุดการทำงานของ class หรือถูกทำก่อนจะสลาย object
# ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่ทำหน้าที่คืนหน่วยความจำให้ระบบ (ไม่ระบุก็ได้)
# โครงสร้าง
# def __init__(self):
#   pass

# การสร้าง constructor

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน  = {}'.format(self.salary))
        print('แผนก  = {}'.format(self.department))

    def __del__(self):
        print('call constructor')

emp1 = Employee('วิบูลย์', 50000, 'ธุระกิจ')
emp1.showData()

emp2 = Employee('โกโก้', 10000, 'นอน')
emp2.showData()

emp3 = Employee('รพี', 1000000, 'คนรวย')
emp3.showData()

emp4 = Employee('plim', 20000, 'HR')
emp4.salary =21000
emp4.showData()