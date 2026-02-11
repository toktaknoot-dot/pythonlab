import calculator
#ตัวอย่างการใช้งาน:คลาสคำนวณที่นำเข้ามาจากโมดูล calculator และเรียกใช้ฟังก์ชันต่างๆ เพื่อทำการคำนวณและแสดงผลลัพธ์    

if __name__ == "__main__":
    calc = calculator.Calculator()
    print("บวก 2 + 3 =",calc.add(2, 3))
    print("ลบ 5 - 3 =",calc.subtract(5, 3))
    print("คูณ 4 * 5 =",calc.multiply(4, 5))
    print("หาร 10 / 2 =",calc.divide(10, 2))