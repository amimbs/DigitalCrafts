# exception handling and unit testing

# exceptions are errors that are thrown by our applicaiton when something unexpected happens

# result = 1 / 0 
#     result = 1 / 0
# ZeroDivisionError: division by zero - this is the class of error   <------------this occurs whenever you divide by zero

# def divide():
#     result = 1/0

while True:
    try:
        # database_connection.open
        result = 1 / 2                          # your code can try something, and if something unexpected happens, catch it using an except block
        number =  int(input("Enter number: "))  # If the user inputs a char here, then is goes to the second except block
        # break
        # divide()
        
    except ZeroDivisionError:                   # This narrows down our error wont even proceed past this
        print("Please don't divide by zero")
    # except:                                   # catches generic errors. It would be better practice to narrow our errors down
    #     print("Ooops something went wrong")
    except ValueError:
        print("Please don't input characters")
    else:                                       # else will only be execute if there are no errors
        print('Else')
        break
    finally:                                    # Finally blocks are always fired despite an errpr. we use database_connection.(open/close) as and example. Resource clean up absically
        # database_connection.close   
        print("finally")       
