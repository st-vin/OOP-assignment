class Laptop:
    def __init__(self, brand, model, ram, storage):
        # Attributes
        self.brand = brand
        self.model = model
        self.ram = ram
        self.storage = storage
    
    # Methods
    def power_on(self):
        return(f"{self.brand} {self.model} is now ON.")
    
    def upgrade_ram(self, new_ram):
        self.ram = new_ram
        return(f"RAM upgraded to {self.ram} GB.")
    
    def show_specs(self):
        return(f"Laptop Specs: {self.brand} {self.model}, RAM: {self.ram} GB, Storage: {self.storage} GB")

my_laptop = Laptop("Lenovo", "T 480", 16, 512)
another_laptop = Laptop("Apple", "MacBook Air", 32, 512)

print(my_laptop.show_specs())

print(another_laptop.show_specs())

print(my_laptop.power_on())

print(my_laptop.upgrade_ram(32))
