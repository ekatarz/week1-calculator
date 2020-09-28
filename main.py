number_1 = input("Enter the first number: ")
number_2 = input("Enter the second number: ")
print()
print()


def menu():
    print("*CALCULATOR*")
    print()

    choice = input("""
       A:  “A“ if you want to ADD
       B:  “B“ if you want to subsctract
       C:  “C“ for division
       D:  “D“ for multiplication
       E:  “E“ for square
       F:  “F“ for power

    Please enter your choice: """)

    if choice == "A" or choice =="a":
        
        sum=float(number_1) + float(number_2)
        print(sum)

    elif choice == "B" or choice =="b":
        sum=float(number_1) - float(number_2)
        print(sum)

    elif choice == "C" or choice =="c":
      sum=float(number_1) / float(number_2)
      print(sum)

    elif choice=="D" or choice=="d":
      sum=float(number_1) * float(number_2)
      print(sum)
    
    elif choice=="E" or choice=="e":
      sum=float(number_1) * float(number_1)
      print("Square of the first number: ",sum)

      sum=float(number_2) * float(number_2)
      print("Square of the second number: ",sum)

    elif choice=="F" or choice=="f":
      sum=float(number_1) ** float(number_1)
      print("Power of the first number: ", sum)
      sum=float(number_2) ** float(number_2)
      print("Power of the second number: ", sum)

    else:
        print("You must only select either A,B,C,D,E, or F.")
        print("Please try again")
        
        
menu()