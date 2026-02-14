class RemovePunc:
    def __init__(self, text):
        self.text = text
        self.punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    def clean(self):
        result = ""
        for ch in self.text:
            if ch not in self.punctuation:
                result += ch
        return result
text = input("Enter a string: ")
cleaned = RemovePunc(text)
print("Without punctuation:", cleaned.clean())