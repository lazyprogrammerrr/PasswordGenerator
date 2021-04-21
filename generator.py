import string,time
import random
import pyAesCrypt
import os
import pyfiglet
from colorama import Fore,Back,Style
from rich.console import Console
from rich import print

c= Console()

c.print(pyfiglet.figlet_format("\t\tRandom Password Generator\n",font="starwars",justify="center",width=180),style="green") #Rich module console print
print('''[bold magenta]                            Do You Want To Create A New Passwords File & Encrypt It?[/bold magenta] or [bold green]Do You Only Want To Encrypt A File?[/bold green] or [bold red]Do You Only Want To Decrypt A File?[/bold red]\n''')

while True:
    try:
        enc_dec = c.input("\t[bold yellow]Press (N) To New File! or Press (E) To Encrypt! or Press (D) to Decrypt! -> [/bold yellow]")
        if enc_dec.casefold() == 'n'.casefold():
            while True:
                try:
                    user_size = int(c.input("\n[bold blue]Enter The Length For Your Password\n (12 or More Recommended) -> [/bold blue]"))
                    break
                except ValueError:
                    print("[u red3]Please Enter Numeric Value Only![/u red3]")
            
            user_strength = str(c.input("\n[b bright_cyan]Enter The Strength For Your Password\n Poor(p), Medium(m), Strong(s) -> [/b bright_cyan]"))

            while True:
                try:
                    password_limit = int(c.input("\n[b deep_pink4]How Many Passwords You Want -> [/b deep_pink4]"))
                    break
                except ValueError:
                    print("[b underline red3]Please Enter Numeric Value Only![/b underline red3]")

            file_name = c.input("\n[b bright_white]Enter File Name -> [/b bright_white]")
            password_secretKey = c.input("\n[b spring_green3]Enter Your Secret Key(Remember This) To Decrypt Your File -> [/b spring_green3]")

            poor = string.ascii_lowercase + string.ascii_uppercase
            medium = string.ascii_lowercase + string.ascii_uppercase + string.digits
            strong = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

            def pass_gen(size=user_size):
                try:
                    passprint=''
                    if user_strength.casefold() == 'p'.casefold():
                        passprint = ''.join(random.choice(poor) for i in range(size))
                        time.sleep(0.1)
                        print("[b hot_pink2]Password Generated and Encrypted[/b hot_pink2]")
                    elif user_strength.casefold() == 'm'.casefold():
                        passprint = ''.join(random.choice(medium) for i in range(size))
                        time.sleep(0.1)
                        print("[b yellow1]Password Generated and Encrypted[/b yellow1]")
                    elif user_strength.casefold() == 's'.casefold():
                        passprint = ''.join(random.choice(strong) for i in range(size))
                        time.sleep(0.1)
                        print("[b chartreuse3]Password Generated and Encrypted[/b chartreuse3]")
                    else:
                        print("Please Select From Options Only!")
                        time.sleep(1)
                    with open(file_name+".txt",'a') as f:
                        f.write(passprint + "\n")
                except ValueError:
                    print("Please Select From Options Poor(p), Medium(m), Strong(s) Only.")

            _pass = 0
            while _pass!=password_limit:    
                pass_gen()
                _pass = _pass + 1
            
            buffersize = 64*1024
            pyAesCrypt.encryptFile(file_name +".txt",file_name +'.aes',password_secretKey,buffersize)
            os.remove(file_name + ".txt")
            break
        elif enc_dec.casefold() == "d".casefold():
            buffersize = 64*1024
            print("\n\t\t\t\t\t\t\t\t\t\t\t[b bright_green]---DECRYPT FILE---[/b bright_green]")
            file_name = c.input("\n[b bright_cyan]Enter File Name -> [b bright_cyan]")
            password_secretKey = c.input("\n[b yellow2]Enter Your Secret Key -> [/b yellow2]")
            try:
                pyAesCrypt.decryptFile(file_name +".aes",file_name +'.txt',password_secretKey,buffersize)
                os.remove(file_name +".aes")
                print("[bold chartreuse1]File Decrypted![/bold chartreuse1]")
                time.sleep(2)
            except ValueError:
                print("\n[bold red]Wrong Filename or Password![bold red]")
                print("[bold yellow]Exiting......[bold yellow]")
                time.sleep(3)
            break
        elif enc_dec.casefold() == "e".casefold():
            buffersize = 64*1024
            print("\n\t\t\t\t\t\t\t\t\t\t\t[b bright_green]---ENCRYPT FILE---[/b bright_green]")
            file_name = c.input("\n[b purple4]Enter File Name -> [/b purple4]")
            password_secretKey = c.input("\n[b bright_cyan]Enter Your Secret Key(Remember This) To Decrypt Your File -> [b bright_cyan]")
            try:
                pyAesCrypt.encryptFile(file_name +".txt",file_name +'.aes',password_secretKey,buffersize)
                os.remove(file_name +".txt")
                print("[bold chartreuse1]File Encrypted![/bold chartreuse1]")
                time.sleep(2)
            except ValueError:
                print("\n[bold red]Wrong Filename or Password![bold red]")
                print("[bold yellow]Exiting......[bold yellow]")
                time.sleep(3)
            break
        else:
            print("[bold red]\nWrong Selection! Please Select From Given Options Only.[/bold red]\n")
            time.sleep(1)
    
    except Exception as e:
        print(e)