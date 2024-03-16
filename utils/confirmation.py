from colorama import Fore, Style


def yes_no_input(prompt: str = '') -> bool:
    while True:
        user_input = input(prompt + f"{Fore.MAGENTA} (Y/n): {Style.RESET_ALL}").lower().strip()
        if user_input in ['y', 'n']:
            return user_input == 'y'
        else:
            print(f"{Fore.YELLOW}Please enter either 'Y' or 'n'.{Style.RESET_ALL}")
