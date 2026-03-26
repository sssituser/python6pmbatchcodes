amount = 0
while True:
    try:
        amount = int(input("Enter Amoun to Withdraw : "))
        print("Amount Drawn is  : ",amount)
    except Exception as ex:
        print("Error occured : ",ex)
        
    finally:
        # print("Amount in try block before inital value ",amount)
        # amount = 0
        # print("Amount in try block after inital value ",amount)
        print("Thanku visit again")
        