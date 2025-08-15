# AccessModifier
# คือระดับในการเข้าถึง class attribute method และอื่นๆ ในภาษาเชิงวัตถุ
# โดยมีประโยชน์อย่างมากในเรื่องของการกำหนดระดับการเข้าถึง
# สิทธิในการเข้าใช้งาน การซ้อนข้อมูล และอื่นๆ

# Public คือการประกาศระดับการเข้าถึงที่เข้มงวดน้อยทีสุด หรือกล่าวได้ว่าใครๆ ก็สามารถเข้าถึงการใช้งานได้

# Protected(_) เป็นการประกาศระดับการเข้าถึงเฉพาะคลาสขอตัวเองและคลาสลูกที่สืบทอดคุณสมบัติ

# Prive(_) เป็นการประกาศระดับการเข้าถึงที่เข้มงวดที่สุด กล่าวคือ จะมีแต่คลาสของ
# ตัวมันเองเท่านั้นที่มสิทธิ์ใช้งานได้

class Employee:
    def __init__(self, name, salary, department):
        # Protected attribute
        self._name = name
        self._salary = salary
        self._department = department
        self._salary = salary

    # Protected
    def _showData(self):
        print('ชื่อพนักงาน = {}'.format(self._name))
        print('เงินเดือน  = {}'.format(self._salary))
        print('แผนก  = {}'.format(self._department))


emp1 = Employee('วิบูลย์', 50000, 'ธุระกิจ')
emp1.salary = 51000