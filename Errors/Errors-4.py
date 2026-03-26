class InvalidAgeException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
while True:
    try:
        age = int(input('Enter Age : '))
        if age<=0 or age>=120:
            raise InvalidAgeException("Entered age is not valid")
        else:
            print("You have successfully Entered age")
            
    except InvalidAgeException as ex:
        print(f"Enter Age between 0 to 120 : {ex}")
    except Exception as ex:
        print("Error occured",ex)
    
        
        