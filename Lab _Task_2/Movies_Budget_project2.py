class moviesbudget:
    def __init__(self):
        self.movies = [
 ("Eternal Sunshine of the Spotless Mind", 20000000),
 ("Memento", 9000000),
 ("Requiem for a Dream", 4500000),
 ("Pirates of the Caribbean: On Stranger Tides", 379000000),
 ("Avengers: Age of Ultron", 365000000),
 ("Avengers: Endgame", 356000000),
 ("Incredibles 2", 200000000)
]
    def add(self):
        choice = input("Add movies(Yes,No) : ")
        if choice == "yes":
            name = input("Enter the Name : ")
            budget = int(input("Enetr the Budget : "))
            self.movies.append((name,budget))
            print(self.movies)
    def calculate(self):
        total = 0
        for movie in self.movies:
            total += movie[1]
        self.average = total / len(self.movies)
        print("\n Average is : ", self.average)
    def highbudget(self):
        print("\n High-Budget Movies (above average)")
        self.count = 0
        for name, budget in self.movies:
            if budget > self.average:
                diff = budget - self.average
                print(f"{name} → Budget: {budget} (Above average by {diff:.2f})")
                self.count += 1
    def Count_high_budget(self):
        print("\n Count of High-Budget Movies : ",self.count)
mov = moviesbudget()
mov.add()
mov.calculate()
mov.highbudget()
mov.Count_high_budget()