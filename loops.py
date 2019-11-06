# Basics (meant for ide)
# By Julian

# FOR LOOPS
for i in range(10):    # Iterates and prints 0 through 9
    print(i)

print("\n")


for i in range(5,10):  # Iterates and prints 5 through 9
    print(i)           # Variables declared with a for loop only exist within that for loop

print("\n")


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", ]
for i in months:
    print(i)           # Print each item of the list

print("\n")


for i in "Hello World":
    print(i)

print("\n")


# WHILE LOOPS
def loop ():
    live = True
    a = 0
    while live:
        numbers = [1,2,3,4,5]
        for i in numbers:
            a = i
            print(i)
            if a == 5:
                live = False
            print("Hello World")


loop()

# EXAMPLE OF A FUNCTIONING LOOP


for i in range(1, 20):
    string = ""
    if i % 3 == 0:
        string += "fizz"
    if i % 5 == 0:
        string += "buzz"
    elif i % 3 != 0:
        string = i
    print(string)