# A number without a decimal point is of the type integer.


# A number with a decimal point is a float.
float1 = 6.3 # Floating point number
float2 = 7.0 # This is also a floating point number.

# Anything wrapped in quotation marks is a string.
string1 = "Hello" # String over here!
string2 = "my name is robot" # Literally, anything wrapped in quotes is a string.
string3 = "369" # Yes this is a string too.

# Naming variables is important! This has a capital "S" in string, so it's different
# than the previous variable of 'string1'.
String1 = "Wonderful!"

# You can even combine variables into one variable. We use the "print()" function to produce
# an output to your terminal.
big_string = string1 + string2 #concatination
print(big_string)

# Let's make the output look a little cleaner. You can add in a string of an empty space
# directly between these variables. Also, variables can have their values changed!
# IMPORTANT: Variable's with changing values is an important concept! More on this topic on line 42.
big_string = string1 + " " + string2
print(big_string)

# Python reads from the top of the file to the bottom. Therefore, when "big_string" is first
# printed on line 40, it's value is "Hellomy name is robot", but since we changed the variable's
# value on line 48, it prints out that new value on line 39, which adds a space.

# You don't have to create a variable to print an output. You can put strings directly into print
# statements!!

introduction = "Hello, my name is"
name = "Mykolas Perevicius"

print(introduction +  name)
# When you see, TODO: Section x of TODO y, you should stop where you are and head over to
# the corresponding assignment for this section of the lesson. The line below instructs
# you to visit section 1 of the 2nd TODO and complete it before moving on to the next section.
