#Jacob Sexton 7/15/25

def repeat_char(char, times):
    if times <= 0:
        return ""
    else:
        return char + repeat_char(char, times - 1)

# Example usage:
char = input("What character would you like to repeat? ")
times = int(input(f"How many {char}\'s would you like: "))

result = repeat_char(char, times)
print(result)
