# c-1
class Customer:
    def __init__(self, first_name, family_name):
        self.first_name = first_name
        self.family_name = family_name

    def full_name(self):
        print(self.first_name + " " + self.family_name)


ken = Customer(first_name="Ken", family_name="Tanaka")
ken.full_name()  # "Ken Tanaka" という値を返す

tom = Customer(first_name="Tom", family_name="Ford")
tom.full_name()  # "Tom Ford" という値を返す


# c-2
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.age  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.age  # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.age  # 73 という値を返す


# c-3
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def entry_fee(self):
        if self.age < 20:
            print(1000)
        elif 20 <= self.age < 65:
            print(1500)
        else:
            print(1200)


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.entry_fee()  # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee()  # 1200 という値を返す


# c-4
# info_csvメソッドで、金額を直接printしていますが、年齢から金額を求めるメソッドを作成し、そのメソッドを使用して金額を算出するように修正お願いします
# また、カンマ区切りになっていないので、修正お願いします
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        print(self.first_name + " " + self.family_name)

    def entry_fee(self):
        if self.age < 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        else:
            return 1200

    def info_csv(self):
        fee = self.entry_fee
        print(f"{self.full_name()}, {self.age}, {fee}")


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す


# c-5
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
        else:
            print(1200)


# 確認用
ken = Customer(first_name="Ken", family_name="Tanaka", age=3)
ken.entry_fee()


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


# c-8は未完成
