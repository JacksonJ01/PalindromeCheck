def palindrome_check(check):
    length = int(len(check))
    print(length)

    if length == 0 or length == 1:
        print("True")
        return True

    elif check[0] != check[-1]:
        print("False")
        return False

    else:
        check = check[1:]
        check = check[:-1]
        check.strip()
        palindrome_check(check)


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
