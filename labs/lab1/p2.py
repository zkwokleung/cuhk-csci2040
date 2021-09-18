ipt = input("Please input a palindrome: ").lower()
while True:
    if ipt == ipt[::-1]:
        if ipt.isnumeric():
            ipt = input("No BRIBING as I am loyal to the King!: ")
        else:
            break
    else:
        ipt = input("I do not understand what you mean! Say again: ")

print("Welcome to the wonderland!")
