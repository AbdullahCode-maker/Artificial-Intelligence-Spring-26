class fizzbuzz:
    def __init__(self,limit):
        self.limit = limit
    def play(self):
        for i in range(1,self.limit+1):
            if i %3 == 0:
                print("Fizz")
            elif i %5 == 0:
                print("Buzz")
            elif i %3 == 0 and i %5 == 0:
                print("FizzBuzz")
            else:
                print(i)
Project = fizzbuzz(100)
Project.play()