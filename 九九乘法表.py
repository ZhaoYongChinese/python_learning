"""
print(x,end="") # end="" means that the next print statement will continue on the same line, instead of starting a new line.
print("hello\tworld") # \t is a tab character, which adds a horizontal space between "hello" and "world".
print("hello\nworld") # \n is a newline character, which moves "world" to a new line after "hello".
"""

i = 1
while i <= 9:
    j = 1
    if i < 9:
        while j <= i:
            print(f"{j}*{i}={i*j:2d}", end="\t")
            j += 1
        print()
    else:
        while j <= i:
            print(f"{j}*{i}={i*j:2d}", end="\t")
            j += 1
        # print() # This line is not necessary because after the last line of the multiplication table, we don't need to move to a new line.
    i += 1