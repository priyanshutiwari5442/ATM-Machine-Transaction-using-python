# ATM(automated teller machine)

# Import datetime function
from datetime import datetime
from datetime import date
from datetime import timedelta
today_date= datetime.today() + timedelta(hours = 5.5)
transaction_date = datetime.strftime(today_date,'%Y-%m-%d %I:%M:%S %p')



def deposit(balance):
  '''create it for depoiting money in your account'''
  deposit_amount = int(input("Deposit money in your account "))
  balance += deposit_amount
  print(f"Your account is credited INR {balance} on date {transaction_date} in your account")
def withdraw(balance):
  '''create it for withdrawing money from your account'''
  withdraw_amount = int(input("Amount withdraw from your account "))
  if withdraw_amount <= balance :
    balance -= withdraw_amount
    print(f"Rs {balance} debited from your account on date {transaction_date}")
  else:
    print("Insufficient balance, Please enter less amount")
def check_balance(balance):
  '''Check balance in your account'''
  print(f"Your remaining balance is {balance}")
def change_pin(pin):
  '''Here you can change your pin number'''
  new_pin = int(input("enter your new pin "))
  confirmation_pin = int(input("enter your confirmation pin "))
  if new_pin == confirmation_pin:
    print(f"Your pin has been changed on date {transaction_date} of your account")
    return new_pin
  else:
    print("Your new pin mismatch with confirmation pin, please try again")
def transfer_to(balance):
  '''here we transfer money from one account to another'''
  transferable_amount= int(input("enter the transfer amount from your account "))
  payee_account = int(input("enter the account of your payee account number "))
  if transferable_amount<=balance:
    balance -= transferable_amount
    print("Payment is successfully made, your remaining balance is ",balance)
  else:
    print("Insufficient Balance, Please try less amount to pay")

def main():
  """
  The main function that handles the ATM operations.
  """
  pin = 1098
  balance = 50000

  print('INSERT YOUR CARD ')
  confirm_pin = int(input("Enter Your Pin: "))
  if pin == confirm_pin:
      print("Enter 1 for Money Deposit")
      print("Enter 2 for Money Withdrawal")
      print("Enter 3 for Balance Inquiry")
      print("Enter 4 to Change PIN")
      print("Enter 5 to Transfer Funds")

      option = int(input("Select an option (1/2/3/4/5): "))
      if option == 1:
          deposit(balance)
      elif option == 2:
          withdraw(balance)
      elif option == 3:
          check_balance(balance)
      elif option == 4:
          change_pin(pin)
      elif option == 5:
          transfer_to(balance)
      else:
          print("Invalid Option")
  else:
      print("Invalid PIN")
  print("Thank You, Visit Again")
if __name__ == "__main__":
  main()
