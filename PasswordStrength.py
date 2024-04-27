def PassStrength():
# Prompt to enter password for the user  
  Password=input("Enter Password: ") 
# Check if the Password lenght is greater than or equal to 8
  if(len(Password)>=8):
     
# Using the predefined function isdigit() to check if digits are present in the Password
# any() is another predefined function or iteratable keyword which returns a boolean value depending on condition  
     Result=(any(i.isdigit() for i in Password))
     if(Result==True):
# Using the predefined function islower() to check if lower case letters are present in the Password
         Result= (any(i.islower() for i in Password))
         if(Result==True):
# Using the predefined function isupper() to check if upper case letters are present in the Password
             Result= (any(i.isupper() for i in Password)) 
             if(Result==True):
# The below result returns a boolean value depending on the password, say if password contains specail chrachter defined in SC true is returned
                  SC = set("@#$%&*")
                  Result= (any(i in SC for i in Password))
                  if(Result==True):
# if all the above conditions are met then the below msg with a boolean value is printed.
                    print(True, "Password is strong")
                  else:
                    print("Password must contain atleast one special charchter @#$%&*") 
             else:
               print("password has missing upper case letters")  
         else:
             print("Password has missing lowercase letters")        
     else:
       print ("Password has missig digits")                 
  else:
    print("Password length is less than 8 characters")

PassStrength()
