class InstallmentPlan:
    def __init__(self, price):
        self.price = price

    def calculate_total_cost(self):
        return self.price


class FixedInstallment(InstallmentPlan):
    def __init__(self, price, months):
        super().__init__(price)
        self.months = months

    def calculate_total_cost(self):
        return self.price * self.months


class VariableInstallment(InstallmentPlan):
    def __init__(self, price, months, interest_rate):
        super().__init__(price)
        self.months = months
        self.interest_rate = interest_rate

    def calculate_total_cost(self):
        return self.price * self.months * round((1 + self.interest_rate), 2)


fixed_plan = FixedInstallment(100, 12)

variable_plan = VariableInstallment(100, 12, 15)


print(fixed_plan.calculate_total_cost())
print(variable_plan.calculate_total_cost())
