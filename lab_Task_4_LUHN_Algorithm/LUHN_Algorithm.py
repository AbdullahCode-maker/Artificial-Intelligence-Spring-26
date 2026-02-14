class Luhn:
    def __init__(self, number):
        self.number = number
    def check(self):
        digits = [int(d) for d in self.number][::-1]
        total = 0
        for i, d in enumerate(digits):
            if i % 2 == 1:
                d *= 2
                if d > 9:
                    d -= 9
            total += d
        return total % 10 == 0
num = input("Enter card number: ")
card = Luhn(num)
if card.check():
    print("✅ Valid Card")
else:
    print("❌ Invalid Card")