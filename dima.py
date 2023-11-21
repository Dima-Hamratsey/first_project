from datetime import date 
 
class Medicine: 
    def __init__(self, name, price, quantity, prescription_needed, expiration_date): 
        self.name = name 
        self.price = price 
        self.quantity = quantity 
        self.prescription_needed = prescription_needed 
        self.expiration_date = expiration_date 
 
    def __str__(self): 
        return f"{self.name} - Price: {self.price}, Quantity: {self.quantity}, Prescription Needed: {self.prescription_needed}, Expiration Date: {self.expiration_date}" 
 
class Pharmacy: 
    def __init__(self): 
        self.medicines = [] 
 
    def add_medicine(self, medicine): 
        self.medicines.append(medicine) 
 
    def remove_medicine(self, medicine): 
        if medicine in self.medicines: 
            self.medicines.remove(medicine) 
 
    def check_expiration(self): 
        today = date.today() 
        self.medicines = [medicine for medicine in self.medicines if medicine.expiration_date >= today] 
 
    def apply_discount(self): 
        for medicine in self.medicines: 
            medicine.price *= 0.9 
 
    def find_cheapest_medicines(self): 
        return sorted(self.medicines, key=lambda x: x.price) 
 
    def display_medicines(self): 
        for medicine in self.medicines: 
            print(medicine) 
 
if __name__ == "__main__": 
    medicine1 = Medicine("MedicineA", 100, 50, False, date(2024, 12, 31)) 
    medicine2 = Medicine("MedicineB", 50, 30, True, date(2023, 6, 30)) 
    medicine3 = Medicine("MedicineC", 75, 20, False, date(2023, 9, 15)) 
 
    pharmacy = Pharmacy() 
    pharmacy.add_medicine(medicine1) 
    pharmacy.add_medicine(medicine2) 
    pharmacy.add_medicine(medicine3) 
 
    print("Pharmacy Inventory:") 
    pharmacy.display_medicines() 
 
    pharmacy.check_expiration() 
    print("\nAfter checking expiration dates:") 
    pharmacy.display_medicines() 
 
    pharmacy.apply_discount() 
    print("\nAfter applying a 10% discount:") 
    pharmacy.display_medicines() 
 
    cheapest_medicines = pharmacy.find_cheapest_medicines() 
    print("\nCheapest Medicines:") 
    for medicine in cheapest_medicines: 
        print(medicine)