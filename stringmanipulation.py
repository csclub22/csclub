# Basics (meant for ide)
# By Julian

string = "Hello World"                  # Declaration

print(string)                           # Prints our string in the console

stringval = string[0]                   # stringval accesses 0th index of string
print(stringval)

print(len(string))                      # Prints length of variable string (does not start at 0)

char = "l"
print(string.count(char))               # Prints number of instances of char in string
print(string.find(char))                # Prints the first index of char appearing in string
print(string.index("World"))            # Prints where the letters "World" appear in string

print(string.count("o"))                # Counts number of "o"'s in string

print(string[3:8])                      # Prints the 3rd index to the 8th in string
print(string[-2])                       # If string is very long or unknown, and you want to acess near the end, 
                                        # use negatives

print(string.split("W"))                # Splits string at char "W"

print(string.startswith("H"))           # Returns true
print(string.endswith("d"))             # Returns true
print(string.startswith("z"))           # Returns false

print("\n"*5)                           # Prints newline 5 times

print(string.replace("Hello", "Olleh")) # Replaces letters "Hello" with "Olleh"

print(string.upper())                   # Converts string to upper case
print(string.lower())                   # Converts string to lower case
print(string.title())                   # Converts string to title format
print(string.capitalize())              # Capitalizes first Letter only in string
print(string.swapcase())                # Swaps all cases in string

print(list(reversed(string)))           # Prints a list of reversed chars in string

string2 = "  Hello World   "
print(string2)
print(string2.strip())                  # Removes whitespaces from both ends of string2
print(string2.lstrip())                 # Removes whitespaces from start of string2
print(string2.rstrip())                 # Removes whitespaces from end of string2
print(string.lstrip("H"))               # Removes H from start of string

print(string + string2)                 # "Adds" string2 to string

print(".".join(string))                 # "Adds" a "." between every char in string

print(string.isalnum())                 # Return True if all char are alphanumeric
print(string.isalpha())                 # Return True if all char in the string are alphabetic
print(string.isdigit())                 # Return True if string contains digits
print(string.istitle())                 # Return True if string contains title words
print(string.isupper())                 # Return True if string contains upper case
print(string.islower())                 # Return True if string contains lower case
print(string.isspace())                 # Return True if string contains spaces
