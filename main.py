import os
import sys
import requests
import time
import json
import keyboard
from colorama import init, Fore
from urllib.parse import quote
from halo import Halo

url = "https://shuriken.pm/api.php"
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.WHITE + "                                                   .:^!7?7!^.                            :~?PB&&@@#?")
    print("                                                .~JPB&&@@@&#GJ~.                      .!YB&@@@@@@@@&")
    print("                                               7G&@@@@@@@@@@@@&G7.                  :?G&@@@@@@@@@@@B")
    print("                                              ~&@@@@@@@@@@@@@@@@@G7.        ......:?B@@@@@@@@@@@@@B~")
    print("                                              ~&@@@@@@@@@@@@@@@@@@&P~.^!?Y5PGGGBBGB@@@@@@@@@@@@@@G^")
    print("                                               ~JG#&@@@@@@@@@@@@@@@@#B&@@@@@@@@@@@@@@@@@@@@@@@@@P:")
    print("                                                 .:~7YPB#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&Y.")
    print("                                                   ...:^~5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B!")
    print("                                          .:^~!7JYPGBB###&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&5^")
    print("                                  .:^~7J5PB#&&@@@@@@@@@@@@@@@@@@@@@@&@@@@@@@@@@@@@@@@@@@@@B!.")
    print("                           .:~!?YPB#&&@@@@@@@&#BGGP5YYJJYY5PG#@@@@@GB@@@@@@@@@@@@@@@@@@@#J:")
    print("                     .:~7JPB#&@@@@@@@@&#G5J7!^:..           .^#@@&YP@@@@@@@@@@@@@@@@@@&Y^")
    print("                  :!JG#&@@@@@@@@&#G5?!^:.    " + Fore.RED + "  ..::^^::. " + Fore.WHITE + "    .G@B75@@@@@@@@@@@@@@@@@&5^")
    print("               .!P#@@@@@@@@&#G5?~:.  .::    " + Fore.RED + ".^~!!777777!:" + Fore.WHITE + "    .PY~5@@@@@@@@@@@@@@@@#Y^")
    print("              .P&@@@@@@&BPJ!:.     ^77:   " + Fore.RED + ":~!77777777777~" + Fore.WHITE + "     :~G@@@@@@@@@@@@@@@BJ^")
    print("              ^#@@@&B5?~:       :!55~   " + Fore.RED + ":~7777777777777!." + Fore.WHITE + "    :J#@@@@@@@@@@@@@&P7:")
    print("               ^7J7^.        .^YB#?.   " + Fore.RED + "^!7777777777777~." + Fore.WHITE + "   .!G@@@@@@@@@@@@&BJ~.")
    print("                           :7P&@G~    " + Fore.RED + ":777777777777!~:" + Fore.WHITE + "   .!G&@@@@@@@@@@&BY!.")
    print("                         ^JB@@@5:     " + Fore.RED + ".!7777777!!~^." + Fore.WHITE + "   ^?G&@@@@@@@@@&BY!:")
    print("                      .!5#@@@&Y.       " + Fore.RED + ".::^^^::." + Fore.WHITE + "   .^7P#@@@@@@@@@#GJ~.")
    print("                    :7G&@@@@@Y.~Y^             .:!JG#@@@@@@@@&BY7^.")
    print("                  :?B@@@@@@@P.:B@G~      .:^!?5G#&@@@@@@&#GY7^.")
    print("                ^J#@@@@@@@@#^ 7@@@&PJJY5PG#&&@@@@@@&#B5?~:.")
    print("              ^Y#@@@@@@@@@@5  Y@@@@@@@@@@@@@@&#BPY7~:.")
    print("            :J#@@@@@@@@@@@@7 .G@@@@@@@@@@@@@57~:..      ....::^~~!77???J??77~^.")
    print("          :J#@@@@@@@@@@@@@@7 .B@@@@@@@@@@@@@&#BGGGPPPPPGGGGBB#&&&@@@@@@@@@@@&&BY!.")
    print("        .7B@@@@@@@@@@@@@@@@Y .G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&G^")
    print("       ~P&@@@@@@@@@@@@@@@@@G. J@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G:")
    print("     .J#@@@@@@@@@@@@@@@@@@@Y  :B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&~")
    print("    ~G@@@@@@@@@@@@@@@@@@@@P:   ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&^")
    print("   7#@@@@@@@@@@@@@@@@@@@#J:     ^P&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P.")
    print(".?&@@@@@@@@@@@@@@@@@@BJ^        .7B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G^")
    print("J&@@@@@@@@@@@@@@@@#P7:            :7G&@@@@@@@@@@@@@@@[ " + Fore.RED + "shuriken.pm" + Fore.WHITE + " ]@@@@@@@@@@&P:")
    print("7&@@@@@@@@@@@@@&B57:                 .^JG#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B7.")
    print("B@@@@@@@@@@&B5?~.                       .^7YG#&@@@@@@@@@@@@@@@@@@@@@@@@@@@@&B?:")
    print("~YPGBGGPY?!^.                               .:~7YPB#&&@@@@@@@@@@@@@@@@@@&B5!.")
    print("   ....                                           .:~!?J5PBB#&&@@@@&#G5?~:);\n" + Fore.RESET)
    print("=" + Fore.RED + "[ Search ]" + Fore.RESET + "============" + Fore.BLUE + "[ Settings ]" + Fore.RESET + "=================================================")
    print(" [1] Search Sites    " + Fore.BLACK + "|" + Fore.RESET + " [0] Exit")
    print(" [2] Search Photos   " + Fore.BLACK + "|" + Fore.RESET)
    print(" [3] Search Videos   " + Fore.BLACK + "|" + Fore.RESET)
    print(" [4] Search Torrents " + Fore.BLACK + "|" + Fore.RESET)
    print(" [5] Search Tor      " + Fore.BLACK + "|" + Fore.RESET)
    cmd = input(Fore.RESET + "=" + Fore.GREEN + "[ Your Choice ]" + Fore.RESET + "====" + Fore.GREEN + " > " + Fore.RESET)
    if cmd == "0":
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    elif cmd == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Fore.RED + "[ Search Sites ] " + Fore.BLACK + "type in ~ to go back")
        query = input(Fore.RESET + " > ")
        if query != "~":
            page = 0;
            def sitesPage():
                global url
                global page
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Fore.RED + "[ Search Sites ] " + Fore.BLACK)
                spinnerText = "Searching for " + Fore.LIGHTMAGENTA_EX + query + Fore.RESET + "..."
                spinner = Halo(spinner='line', text=spinnerText)
                spinner.start()
                queryEncoded = quote(query)
                # checkpoint 1
                params = {
                    "q": queryEncoded,
                    "t": "0",
                    "p": page
                }
                # checkpoint 2
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    spinner.stop()
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(Fore.RED + "[ Search Sites ] " + Fore.BLACK + "Page 1 | " + query)
                    # Request was successful
                    data = response.json()
                    # Process the data as needed
                    if 'special_response' in data:
                        del data['special_response']
                    for obj in data:
                        title = obj.get('title', '')
                        url = obj.get('url', 'Invalid result')
                        description = obj.get('description', '')
                        print(Fore.RED + title + " " + Fore.BLACK + url + "\n" + Fore.WHITE + description + "\n")
                    print(Fore.BLACK + '[<-] Previous ' + Fore.WHITE + "|" + Fore.BLACK + ' [->] Next Page' + Fore.WHITE + " | " + Fore.BLACK + '[Esc] Exit' + Fore.RESET)
                    def on_left_arrow_press(event):
                        global page
                        if page != 0:
                            page = (page - 1)
                            sitesPage()
                    def on_right_arrow_press(event):
                        global page
                        page = (page + 1)
                        sitesPage()
                    keyboard.on_press_key("left", on_left_arrow_press)
                    keyboard.on_press_key("right", on_right_arrow_press)

                    keyboard.wait('esc')
                else:
                    # Request failed
                    print(Fore.RED + " [X] API request failed with status code: " + response.status_code + Fore.RESET)
                    print("Press ESC to go back...")
                    keyboard.wait('esc')
            sitesPage()