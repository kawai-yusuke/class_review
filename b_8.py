class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.toshi = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def age(self):
        return self.toshi

    def entry_fee(self):
        if self.toshi <= 3:
            return 0
        if self.toshi < 20:
            return 1000
        if 20 <= self.toshi < 65:
            return 1500
        if self.toshi >= 75:
            return 500
        if self.toshi >= 65:
            return 1200

    def info_csv(self, between):
        print(f"{self.full_name()}{between}{self.age()}{between}{self.entry_fee()}")


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.info_csv("|")
