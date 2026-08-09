account = 500
PIN = 1852

enter_pin = int(input("Enter your PIN: "))

if enter_pin != PIN:
    again_pin = int(input("Wrong PIN! Enter PIN again: "))

    if again_pin != PIN:
        print("Incorrect PIN. Access denied.")
    else:
        print("Correct PIN!")

else:
    print("Correct PIN!")


# Banking operations
if enter_pin == PIN or 'again_pin' in locals() and again_pin == PIN:

    deposit = int(input("Enter amount for deposit: ₹"))
    account += deposit

    print(f"Total bank balance: ₹{account}")

    withdraw = int(input("Enter amount for withdrawal: ₹"))

    if withdraw <= account:
        account -= withdraw
        print(f"Bank balance: ₹{account}")
    else:
        print("Insufficient balance!")