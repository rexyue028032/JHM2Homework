answer = input("Do you want some snack?(yes/no)")
if answer == "no":
    print("Good! Let's play games instead.")
elif answer == "yes":
    snacks = input("enter your choice(ice-cream / cookies / candies):")
    if snacks == "ice-cream":
        print("Remember to wash your hands.")
    elif snacks == "cookies":
        print("Can you share with your friends?")
    else:
        print("Don't eat too much.")