import random
import os

class InvoiceNumberGenerator:
    def __init__(self, file_name="generated_numbers.txt"):
        self.file_name = file_name
        self.generated_numbers = self._load_numbers()

    def _load_numbers(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                return set(file.read().splitlines())
        return set()

    def _save_numbers(self, new_number):
        with open(self.file_name, "a") as file:
            file.write(f"{new_number}\n")

    def generate_invoice_number(self):
        while True:
            number = f"{random.randint(0, 99999):05d}"
            if number not in self.generated_numbers:
                self.generated_numbers.add(number)
                self._save_numbers(number)
                return number

generator = InvoiceNumberGenerator()
invoice_number = generator.generate_invoice_number()
print(f"Generated Invoice Number: {invoice_number}")
