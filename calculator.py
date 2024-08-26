class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Деление на ноль нельзя акмак!!!")
        return Calculator(self.value / other.value)

    def __str__(self):
        return str(self.value)


calc1 = Calculator(10)
calc2 = Calculator(5)

print(f"Сумма {calc1 + calc2}")
print(f"Разность {calc1 - calc2}")
print(f"Произведение {calc1 * calc2}")
print(f"Частное {calc1 / calc2}")
