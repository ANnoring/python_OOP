# เขียนโปรแกรมสร้าง class ชื่อ Human โดยมี attribute และ Method ดังนี้
# attribute
# name เป็นชื่อของบุคคล
# age เป็นอายุของบุคคล
# method
# aging(year) รับ parameter 1 ตัว คือ year
# - แสดงอายุปัจจุบัน
# - เพิ่มอายุขึ้นเท่ากับ year
# - แสดงอายุหลังเพิ่มแล้ว

class Human():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def aging(self, year):
        print("ชื่อ {}, ปัจจุบันอายุ {} ปี".format(self.name, self.age))
        self.age += year
        print("อายุเพิ่มขึ้น {} ปี, จะอายุ {} ปี".format(year, self.age))

p1 = Human("nom", 25)
p1.aging(5)


