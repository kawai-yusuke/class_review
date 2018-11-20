class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.toshi = age

    def full_name(self):
        print(f"{self.first_name} {self.family_name}")

    def age(self):
        print(self.toshi)

    def entry_fee(self):
        if self.toshi < 20:
            print(1000)
        if 20 <= self.toshi < 65:
            print(1500)
        if self.toshi >= 65:
            print(1200)


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
ken.entry_fee()  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age=57)
tom.entry_fee()  # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
ieyasu.entry_fee()  # 1200 という値を返す
