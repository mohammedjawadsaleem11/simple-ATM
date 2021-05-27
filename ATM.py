import time

print("Welcome to Mcode programmers  ATM")
restart = "Y"
chances = 3
balance = 1010.2
while chances >= 0:
	pin = int(input('Please Enter Your Personal Identification Number(PIN): '))
	if pin == 1234:
		time.sleep(5)
		print("Authenticated")
		time.sleep(3)
		while restart not in ('n','NO','no','N'):  #I didnt understand
			print("-------------------------------------------------------")
			print("Press 1 For Balance Info\n")
			print("Press 2 To Make a Withdrawl\n")
			print("Press 3 To Pay in\n")
			print("Press 4 To Return Card\n")
			print("-------------------------------------------------------")
			option = int(input("Enter Option: "))
			if option == 1:
				print(f"Your Account balance is {balance}.\n")
				restart = str(input("Would You Like To Go Back?"))
				if restart in ('n','NO','no','N'):
					print("Thank You For Using Our Service ")
					break
			elif option == 2:
				option == 'y'
				print("\nEnter Amount in 100,500,2000")
				withdrawl = float(input("How much would you like to withdraw? "))
				if withdrawl in [100,200,300,400,500,600,700,800,900,1000,list(range(0,10000,100))]:#might encounter a bug
					balance = balance - withdrawl
					print(f"Avalible Balance is {balance}")
					restart = input("Would You Like To Go Back? ")
					if restart in ('n','NO','no','N'):
						print("Thanks For Using Mcode ATM\n")
						break
				elif withdrawl != [100,200,300,400,500,600,700,800,900,1000,list(range(0,10000,100))]:
					print("Invalid Amount, Please Re-try\n")
					restart = 'y'
				elif withdrawl ==1:
					withdrawl = float(input("Enter The Amount"))
			elif option == 3:
				pay_in = float(input("How Much Would You Like To Pay in? "))
				balance = balance + pay_in
				print(f"Your Avalible Balance is {balance}.")
				restart = input("Would You Like to Go Back? ")
				if restart in ('n','NO','no','N'):
					print("Thanks For Using Mcode ATM\n")
					break
			elif option == 4:
				print("Please wait whilst your card us Returned ")
				time.sleep(10)
				print("Thank you For Using our Service")
				break
			else:
				print("Please Enter a Correct Number")
				restart = 'y'
	elif pin != 1234:
		time.sleep(3)
		print("Incorrect Password")
		chances = chances - 1
		print(f"You Have {chances} Chances Left!")
		if chances == 0:
			time.sleep(5)
			print("Account Blocked")
			break


