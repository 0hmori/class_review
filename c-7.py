# c-7
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def info_csv(self):
        if self.age < 20:
            print(self.first_name + " " + self.family_name, self.age, str(1000), sep="\t")
        elif 20 <= self.age < 65:
            print(self.first_name + " " + self.family_name, self.age, str(1500), sep="\t")
        else:
            print(self.first_name + " " + self.family_name, self.age, str(1200), sep="\t")
