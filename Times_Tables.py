print("Welcome to MAKE THAT TIMES TABLE!. We do the work so you don't have to. Step right up and ask us a number to make a times tables for!")

while True:
#"try" will try the code block. If there is an error, it will go to the except code block. Allows you to catch user errors.
    try: 
        targetNum = int(input("Enter the number for which you want to print the times tables (0 to exit): "))
        #this will print a message once the user enters 0
        if targetNum == 0:
            print("Thank you for trying the 'MAKE THAT TIMES TABLE!' program. See you later!")
            break
#this while loop allows you to use a "try" code block to catch if the user doesnt put in an int. 
        while True:
            try: 
                min_range = int(input("Enter the minimum calculated range of times tables you want to print: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
#this while loop allows you to use another "try" block to catch the possible errors of making the range to big or making the min bigger than the max
        while True:
            try:
                max_range = int(input("Enter the maximum calculated range of times tables you want to print: "))
                if min_range > max_range:
                    print("Minimum range should be smaller than maximum range.")
                    continue
                elif max_range - min_range > 10:
                    print("The range should not be more than 10 numbers apart.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")
#for loop will loop through the numbers in range and print each times table
        for i in range(min_range, max_range+1):
            result = targetNum * i
            print(f"{targetNum} x {i} = {result}")
    except ValueError:
        print("Invalid input. Please enter an integer.")


