number = int(input("Enter the number of which the user want to print multiplication table:"))
print("The Multiplication table of:", number)
for count in range(1,11):
    print(number, 'x', count, '=', number*count)