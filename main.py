import qrcode
import datetime
import colorama
from colorama import Fore, Back, Style


def generate_qrcode(userText):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    fullDateTimeNow = datetime.datetime.today()
    dateTimeNow = fullDateTimeNow.strftime("%Y-%d-%B-%H-%M-%S")
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(f"QrImage{dateTimeNow}.png")


print(f"{Fore.YELLOW}This is a QRCode-generator! (exit() to quit){Fore.RESET}")

isEnteringText = True
while isEnteringText:
    text = input("Give me your text/url: ")
    if text == "":
        print(f"{Fore.RED}Error: You cannot leave it blank!{Fore.RESET}")
        isEnteringText = True
    elif text == "exit()":
        print(f"{Fore.GREEN}Have a good day!{Fore.RESET}")
        print(f"{Fore.YELLOW}Github: https://github.com/toghr0l{Fore.RESET}")
        isEnteringText = False
    else:
        try:
            generate_qrcode(text)
        except:
            print(f"{Fore.RED}Something went wrong!{Fore.RESET}")
        else:
            print(f"{Fore.GREEN}Passed with 0 errors!{Fore.RESET}")
