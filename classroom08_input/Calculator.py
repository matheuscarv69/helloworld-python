"""

Input Data

Calculator

"""

print('- Calculator -')

firstValue = int(input('Enter a first value: '))
operation = input('Choice an Operation: | + | - | * | / | ** | // | % | : ')
secondValue = int(input('Enter a second value: '))

print()
if '+' in operation:

    print(f'Operator - Addition \n'
          f'Result: {firstValue + secondValue}')

elif '-' in operation:

    print(f'Operator - Subtraction \n'
          f'Result: {firstValue - secondValue}')

elif '*' in operation:

    print(f'Operator - Multiplacation \n'
          f'Result: {firstValue * secondValue}')

elif '/' in operation:

    print(f'Operator - Division')

    if secondValue == 0:
        print(f'Error: The Divisor {secondValue} cannot be zero')
        exit()

    print(f'Result: {firstValue / secondValue}')

elif '**' in operation:

    print(f'Operator - Potentiation \n'
          f'Result: {firstValue ** secondValue}')

elif '//' in operation:

    print(f'Operator - Rounded Division')

    if secondValue == 0:
        print(f'Error: The Divisor {secondValue} cannot be zero')
        exit()

    print(f'Result: {firstValue // secondValue}')

elif '%' in operation:

    print(f'Operator - Module')

    if secondValue == 0:
        print(f'Error: The Divisor {secondValue} cannot be zero')
        exit()

    print(f'Result: {firstValue // secondValue}')
