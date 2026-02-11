# create class calculator with methods add, subtract, multiply, divide
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("บวก 2 + 3 =",calc.add(2, 3))
    print("ลบ 5 - 3 =",calc.subtract(5, 3))
    print("คูณ 4 * 5 =",calc.multiply(4, 5))
    print("หาร 10 / 2 =",calc.divide(10, 2))
    #print(calc.divide(10, 0))
