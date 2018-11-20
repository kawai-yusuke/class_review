class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.toshi = age

    def full_name(self):
        return self.first_name + " " + self.family_name

    def age(self):
        return self.toshi

    def entry_fee(self):
        if self.toshi < 20:
            return 1000
        if 20 <= self.toshi < 65:
            return 1500
        if self.toshi >= 65:
            return 1200

    def info_csv(self):
        print(f"{self.full_name()}, {self.age()}, {self.entry_fee()}")


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
ken.info_csv()  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
