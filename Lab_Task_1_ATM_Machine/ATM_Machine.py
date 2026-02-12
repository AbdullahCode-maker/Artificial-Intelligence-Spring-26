print("=== Welcome to ATM ===")
user_pin = "4321"
admin_pin = "9999"
balance = 7000
atm_cash = 50000
attempts = 3
while attempts > 0:
    entered_pin = input("Enter your 4-digit PIN: ")
    if entered_pin == user_pin:
        print("✔️ User Login Successful!")
        user_type = "user"
        break
    elif entered_pin == admin_pin:
        print("✔️ Admin Login Successful!")
        user_type = "admin"
        break
    else:
        attempts -= 1
        print(f"❌ Incorrect PIN! Attempts left: {attempts}")
if attempts == 0:
    print("🚫 Your card has been blocked. Try again later.")
    exit()
if user_type == "admin":
    while True:
        print("\n=== ADMIN MENU ===")
        print("1. View ATM Total Cash")
        print("2. Add Cash to ATM")
        print("3. Change User PIN")
        print("4. Exit Admin Panel")
        admin_choice = input("Enter choice (1-4): ")
        if admin_choice == '1':
            print(f"🏧 Total Cash in ATM: ${atm_cash}")
        elif admin_choice == '2':
            try:
                amt = float(input("Enter cash amount to add to ATM: $"))
                if amt > 0:
                    atm_cash += amt
                    print(f"✅ Successfully added ${amt} to ATM!")
                    print(f"Updated ATM Cash: ${atm_cash}")
                else:
                    print("❌ Amount must be greater than 0.")
            except:
                print("❌ Invalid input!")

        elif admin_choice == '3':
            new_pin = input("Enter new user PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                user_pin = new_pin
                print("🔐 User PIN changed successfully!")
            else:
                print("❌ PIN must be a 4-digit number.")

        elif admin_choice == '4':
            print("🚪 Exiting Admin Panel...")
            exit()

        else:
            print("❌ Invalid choice! Please select between 1 and 4.")
while True:
    print("\n=== ATM MENU ===")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        print(f"💰 Your current balance is: ${balance}")
    elif choice == '2':
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount > 0:
                balance += amount
                atm_cash += amount
                print(f"✅ ${amount} deposited successfully!")
                print(f"New Balance: ${balance}")
            else:
                print("❌ Amount must be greater than 0.")
        except:
            print("❌ Invalid input! Please enter numbers only.")
    elif choice == '3':
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= 0:
                print("❌ Amount must be greater than 0.")
            elif amount > balance:
                print("❌ Insufficient account balance!")
            elif amount > atm_cash:
                print("❌ ATM does not have enough cash currently!")
            else:
                balance -= amount
                atm_cash -= amount
                print(f"💵 Please collect your cash: ${amount}")
                print(f"Remaining Balance: ${balance}")
        except:
            print("❌ Invalid input! Please enter numbers only.")
    elif choice == '4':
        print("💳 Thank you for using 1234ATM. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please select between 1 and 4.")
