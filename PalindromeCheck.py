def palindrome_check(check):
    #You should strip when you come in to make sure there are no blank spaces at the start or end
    check = check.strip
    
    length = int(len(check))
    print(length)

    if length == 0 or length == 1:
        print("True")
        return True

    elif check[0] != check[-1]:
        print("False")
        return False

    else:
        #check = check[1:]
        #check = check[:-1]
        #check.strip()
        #palindrome_check(check)
        
        #You needed to return the call to the method
        return palindrome_check(check[1:-1])


test = 'aam n nmaa'.lower().replace(' ', '')
print(palindrome_check(test))
# input("PRESS ENTER")
# print("Hello there user")#

string = "Enter String"
while string != 0:
    cont = input("Do you want to test another string?"
                 "\n>>>").title()
    if cont == 'Y' or cont == "Yes":
        string = input("\nEnter a string please"
                       "\nNo punctuation needed"
                       "\n>>>").lower().replace(' ', '')

        print(palindrome_check(string))

    elif cont == 'N' or cont == 'No':
        print("Have a good day")
        string = 0
