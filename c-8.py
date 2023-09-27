# c-8
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.family_name

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        else:
            return 1200

    def pipe_delimited(self):
        print(f"{self.full_name()}|{self.age}|{self.entry_fee()}")


ken = Customer(first_name="Ken", family_name="Tanaka", age=75)
ken.pipe_delimited()
