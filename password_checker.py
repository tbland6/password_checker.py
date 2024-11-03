# 
# password_checker.py  
# 'File Header' password_checker.py is the file name. This is a comment that is commonly used at
# the begining of the file that helps identify and gives a basic description of the file.



CORRECT_PASSWORD = "correct"   
# Hardcoded correct password  This is a comment for readers that says CORRECT_PASSWORD is a variable 
# containing a fixed hardcoded password the program uses to check users input.)


def password_checker():
# This line is a def command, that means to define a function in Python. password_checker is the name of the function,
# the name can be almost anything you want but is best to describe the funtion. The'()' parenthese follow the function
#  name, they are used to add arguments to the function. The colons ":" indicates the start of the functions body.
    attempts = 0  
# This line is the counter for the incorrect attempts.
    
    while attempts < 3:
# This line is a while loop, that gives users a limited number of incorrect attemptes, in this case 3 attempts.
# At the 3rd attempt the loop will stop. The colon '3:' indicates the start of the loop's block code
        password = input("Enter your password: ")
# This line prompts the user to enter a password.

        if password == CORRECT_PASSWORD:
# This line is the conditional "if" statement, this will compare the uesers password entry to the password
# stored in "CORRECT PASSWORD".
            print("Success")
# This line will print "Sucsess" when the correct password is entered.
            return
# Exits the program if successful.

        else:
# This line is an else statement and is part of an if-else statement. It specifies the block of code to run if the "if" condition is not met.
            print("Incorrect Password.")
# This line will display the message "Incorrect Password" if the user enters the wrong password.
            attempts += 1
# This line will increment each time the incorrect password is entered up to 3 times.

    print("Account Locked.")
# This line will notifiy the user, if the incorrect password was entered 3 times, that the account has been locked.
if __name__ == "__main__":
    password_checker()
#   
