from colorama import Fore, Style

print(f'\n{Fore.YELLOW}< Console-Calculator >{Style.RESET_ALL}')

while True:

    number1 = float(input(f'\n{Fore.MAGENTA}Number1 input -> {Style.RESET_ALL}'))
    number2 = float(input(f'\n{Fore.MAGENTA}Number2 input -> {Style.RESET_ALL}'))

    operation = input(f'\n{Fore.GREEN}::: Math operation : {Style.RESET_ALL}')

    match operation:

        case 'add' | '+': 
            print(f'\n{Fore.YELLOW}Addition :: {number1 + number2}{Style.RESET_ALL}')

        case 'sub' | '-':
            print(f'\n{Fore.YELLOW}Subtraction :: {number1 - number2}{Style.RESET_ALL}')
        
        case 'mul' | '*':
            print(f'\n{Fore.YELLOW}Multiplication :: {number1 * number2}{Style.RESET_ALL}')
        
        case 'div' | '/':
            print(f'\n{Fore.YELLOW}Division :: {number1 / number2}{Style.RESET_ALL}')

        case 'mod' | 'divmod' | '.':
            print(f'\n{Fore.YELLOW}Division mod :: {number1 % number2}{Style.RESET_ALL}')