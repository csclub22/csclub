# For CS club - result by Julian
for n in range(101):                                         # Iterate through set (0,100)
    string = ""                                              # Declare variable to store value
    if n % 3 == 0: string += "fizz"                          # If remainder of n/3=0, add fizz to string
    if n% 5 == 0: string += "buzz"                           # If remainder of n/5=0, add buzz to string
    if n % 3 != 0 and n % 5 != 0 or n == 0: string = str(n)  # If neither, add n to string
    print(string.title())                                    # Convert string to title case and print it
