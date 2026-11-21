balance = 1000
def deposit(amount):
    global balance
    balance += amount
def show_balance():
    balance = 500
    print("Local Balance:", balance)
deposit(500)
print("Account Balance:", balance)
show_balance()
print("Final Account Balance:", balance)