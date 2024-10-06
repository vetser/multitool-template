import os

try :
    import pystyle
    import requests
    import colorama
    import dhooks
except ModuleNotFoundError:
    os.system('pip install pystyle')
    os.system('pip install requests')
    os.system('pip install colorama')
    os.system('pip install dhooks')

    from dhooks import Webhook
    from pystyle import Write, Colors, Colorate, System
    from colorama import Fore

# ---Design Related---

class Colors:
    c: str = Fore.BLUE
    s: str = Fore.RED
    k: str = Fore.GREEN
    a: str = Fore.LIGHTBLUE_EX
    l: str = Fore.LIGHTRED_EX
    o: str = Fore.LIGHTGREEN_EX

icon == f"""
▄▄▄█████▓ ▒█████   ▒█████   ██▓   [+] All rights deserved to vetser 
▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
 ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
░ ░      ░ ░      ░  ░
                                       """

def clear():
    System.Clear() # ---This will clear the command prompt, this function named "System" in pystyle does it just like "os.system('cls')" But its more easier for me to type "System.Clear()"---

def size():
    System.Size(126, 36) #---Adjusts the size of the terminal as needed---
           

def ip_pinger():
    clear()
    print(Colorate.Horizontal(Colors.blue_to_white, icon))
    ip = input(Colorate.Horizontal(Colors.blue_to_white, f"multitool@ip $: ")) # ---Prompts the user for the ip---
    clear() # ---Calls the function clear as it will clear the terminal---
    size() # ---Calls the function size as it will adjust the terminal size
    os.system("ping" + ip)

def hook_delete():
    clear()
    print(Colorate.Horizontal(Colors.blue_to_white, icon))
    webhook = input(Colorate.Horizontal(Colors.blue_to_white, f"multitool@webhook $: "))
    requests.delete(webhook) # ---Sends a http request that will delete the specified hook---
    print(Colorate.Horizontal(Colors.blue_to_white, f"Succesfully deleted {webhook[:16]}"))

def hook_spammer():
    clear()
    print(Colorate.Horizontal(Colors.blue_to_white, icon))
    webhook = input(Colorate.Horizontal(Colors.blue_to_white, f"multitool@webhook $: "))

    hook = webhook(webhook) # ---Defines the webhook---

    message = input(Colorate.Horizontal(Colors.blue_to_white, f"multitool@message $: "))

    while True:  # ---Creates a loop that will send the webhook messages infinitely---
        hook.send("{message}")

choices = {
    "01": "example", # ---Using dictionary instead of " Elif choice statements " Since kek said to!!!! :sob:
    "02": "ip_pinger",
    "03": "Webhook spammer",
    "04": "Webhook deletor",
    "05": "example",
    "06": "example",
    "07": "example",
    "08": "example",
    "09": "example",
    "10": "example",
}


def wrong_option():
    input = input(f"{Colors.c}[#] Wrong option | Press ENTER to get back to menu")

def main():
    clear()
    print(Colorate.Horizontal(Colors.blue_to_white, icon))
    options = f"""
    [01] > Example          [06] > Example
    [02] > Ip pinger        [07] > Example
    [03] > Webhook spammer  [08] > Example
    [04] > Webhook deleter  [09] > Example
    [05] > Example          [10] > Example
    """
    print(Colorate.Horizontal(Colors.blue_to_cyan, options))

    choice = input(f"{Colors.c}[#] Choice > ")
    
    choices.get(choice, wrong_option)()

main() # ---Calls the main function---
