# c-6
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def entry_fee(self):
        if self.age <= 3:
            print(0)
        elif 3 < self.age < 20:
            print(1000)
        elif 20 <= self.age < 65:
            print(1500)
        elif 65 <= self.age < 75:
            print(1200)
        else:
            print(500)


# 確認用
ken = Customer(first_name="Ken", family_name="Tanaka", age=75)
ken.entry_fee()
