# Main menu
print('Menu:')
print('1. Draw a Triangle')
print('2. Draw a Rectangle')
print('3. Draw a Pyramid')
print('4. Quit')

while True:
    print('')
    choice = input('Enter your choice (1/2/3/4): ')
    print('')

# Exit
    if choice == '4':
        print('Goodbye!')
        break

# Draw triangle pattern
    elif choice == "1":
        n = int(input('Enter the number or rows for the triangle: '))
        up_down = input('Enter "u" for upward or "d" for downward: ')
        print('')

        if up_down == "u":
            count = 0
            for i in range(n):
                count += 1
                print("*" * count)
            continue
        elif up_down == "d":
            count = n + 1
            for i in range(n, 0, -1):
                count -= 1
                print("*" * count)
            continue

# Draw rectangle pattern
    elif choice == "2":
        row = int(input('Enter the number of rows for the rectangle: '))
        col = int(input('Enter the number of columns for the rectangle: '))
        print('')

        for req in range(row):
            print("*" * col)

        continue

# Draw pyramid pattern
    elif choice == '3':
        rows = int(input('Enter the number of rows for the pyramid: '))
        print('')
        space = rows - 1

        for i in range(0, rows * 2):
            if i % 2 == 0:
                continue
            print(" " * space + "*" * i + " " * space)
            space = space - 1
        continue
    else:
        continue
