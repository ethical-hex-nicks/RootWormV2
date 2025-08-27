##  _________________________________________
##   |_______  authors: Eks1azy     _______|
##    \_\_\_|______  Oqwe4O  _______|\_\_\_\
##    \_\_\_|______  Tusay1  _______|\_\_\_\
##           \_\_\_\_\_\_\_\_\_\_\_\
##   ___________________________________________
##  |                                          /\
##  |  github:https://github.com/Eks1azy      / /
##  |                                        / /
##  |    if you will find some bugs or      / /
##  |                                      / /
##  |    have ideas for improvements,     / /
##  |                                    / /
##  |       please send it to me        / /
##  |__________________________________/ /
##  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_/

 
 
from PIL import Image

import os
import time
import threading

let = "\033[38;5;196m"
clear = "\033[0m"
ler = "\033[38;5;160m"  
leu = "\033[38;5;124m" 

def wait_for_enter(stop_flag):
    input() 
    stop_flag.append(True)

def get_icon_path(user_input):
    if user_input and os.path.isfile(user_input):
        return user_input
    else:
        return "None"

def RootWorm3():
    stop_flag = []

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_colored_art(art, gradient):
        for i, line in enumerate(art):
            color = gradient[i % len(gradient)]
            print(f"\033[38;5;{color}m{line}\033[0m")

    gradient_colors = [
        [217, 210, 203, 196, 160, 124, 124, 88, 88],
        [217, 203, 196, 160, 160, 124, 124, 88, 88],
        [203, 196, 196, 160, 160, 124, 124, 88, 88],
    ]

    ascii_arts = [ascii_art1, ascii_art2, ascii_art3] = [ 
        [
            "  ██▀███   ▒████▄  ▒████▄     █▒   ██       ██  ▒████▄  ██▀███   ▄▄▄ ▄▄▄     ",
            " ▓██ ▒ ██▒▒██▀▒██▌▒▒██▀ ██▌   ██▒  ▓█▄     ▒▀█ ▒██▀▒██▌▓██ ▒ ██▒█▌▀▀█▌▀▀█    ",
            " ▓██ ░▄█ ▒░██   █▌▒░██  ▒█▌ ▄▄██▄▄░▓▀██░ █░░█▀░░██   █▌▓██ ░▄█ ▒█▌ ░█▌ ░█░   ",
            " ▒██▀▀█▄  ░▓█▄ ▒█▓ ░▓█▄▒▒█▓░▒▒██▒▒▒░░▀█▄█▀█▓█▒░░▓█▄ ▒█▓▒██▀▀█▄▒▒█▌░▒█▌▒▒█▒   ",
            " ░██▓ ▒██▒░▒▓███▓▒▒░▒▓███▓▒▓ ▒▀███▀░▒░▀█▀▒▀█▀▒░░▒▓███▓▒░██▓ ▒██▒██▒▒█▓░▒█▓▒  ",
            " ░ ▒▓ ░▒▓░ ▒▒▓ ▒▒   ▒▒▓ ▒▒   ░ ▓▒░░   ▒ ▒░ ▒░ ░  ▒▒▓ ▒▒ ░ ▒▓ ░▒▓░ ▓▒░▒  ░▓▒░ ",
            "   ░▒ ░ ▒░ ░ ▒  ▒   ░ ▒  ▒     ▒      ░  ░  ░    ░ ▒  ▒   ░▒ ░ ▒░ ▒  ░   ▒░  ",
            "   ░░   ░  ░ ░  ░        ░     ░            ░     ░ ░  ░   ░░   ░         ░  ",
            "                                                                             ",  
           f"{let}________________________________________________________{clear}         ",  
           f"                                                                             ",  
           f"           {let}Press{clear} [Enter] {let}to continue{clear}                 ",  
           f"                                                                             ",  
           f"              {let}______________________________________/{clear}            "   
        ], 

        [
            "  ██▀███   ▒████▄  ▒████▄     █▒   ██       ██  ▒████▄  ██▀███   ▄▄▄ ▄▄▄    ",
            " ▓██ ▒ ██▒▒██▀▒██▌▒▒██▀ ██▌   ██▒  ▓█▄     ▒▀█ ▒██▀▒██▌▓██ ▒ ██▒█▌▀▀█▌▀▀█   ",
            " ▓██░░▄█ ▒░██   █▌▒░██  ▒█▌ ▄▄██▄▄░▓▀██░ █░░█▀░░██   █▌▓██ ░▄█ ▒█▌ ░█▌ ░█░  ",
            " ▒██▀▀█▄  ░▓█▄ ▒█▓ ░▓█▄▒▒█▓░▒▒██▒▒░▒░▀█▄█▀█▓█▒░░▓█▄ ▒█▓▒██▀▀█▄▒▒█▌▒▒█▌▒▒█▒  ",
            " ░██▓ ▒██▒░▒▓███▓▒▒░▒▓███▓▒▓ ▒▀███▀░░▒▀█▀▒▀█▀▒░░▒▓███▓▒░██▓ ▒██▒██▒▒█▓░▓█▓▒ ",
            " ░ ▒▓ ░▒▓░ ▒▒▓ ▒▒   ▒▒▓ ▒▓░  ░ ▓▒░ ░ ▒ ▓▒ ▒▒ ░  ▒▒▓ ▒▒ ░ ▒▓ ░▒▓░ ▓▒░▒  ░▓▒░ ",
            " ░ ░▒   ░ ░ ▒  ▒   ░ ▒  ▒     ▒      ░  ░  ░    ░ ▒  ▒   ▒▒ ░ ▒░ ▒      ▒░  ",
            "   ░░ ░ ░  ░ ░  ░    ░   ░     ░     ░          ░ ░  ░    ░   ░     ░   ░   ",
            "                                                                            ",
           f"{let}________________________________________________________{clear}        ",
           f"                                                                            ",
           f"           {let}Press{clear} [Enter] {let}to continue{clear}                ",
           f"                                                                            ",
           f"              {let}______________________________________/{clear}           " 
        ], 

        [   
           "  ██▀███   ▒████▄  ▒████▄     █▒   ██       ██  ▒████▄  ██▀███   ▄▄▄ ▄▄▄     ",
           " ▓██ ▒ ██▒▒██▀▒██▌▒▒██▀ ██▌   ██▒  ▓█▄     ▒▀█ ▒██▀▒██▌▓██ ▒ ██▒█▌▀▀█▌▀▀█    ",
           " ▓██░░▄█ ▒░██   █▌▒░██  ▒█▌░▄▄██▄▄░▓▀██░ █░░█▀░░██   █▌▓██ ░▄█ ▒█▌ ░█▌ ░█░   ",
           " ▒██▀▀█▄  ░▓█▄ ▓█▓ ░▓█▄▒▒█▓░▒▓██▒░░░▒▀█▄█▀█▓█▒░░▓█▄ ▒█▓▒██▀▀█▄▒▒█▌▒▒█▌ ▒█▒   ",
           " ░██▓ ▒██░░▒▓███▓▒▒░▒▓███▓▒░░▒▀███▀░▒▓▀█▀▒▀█▀▒░░▒▓███░▒░█▓ ▒██▒ ██▒▒█▓░▒█▒   ",
           " ░ ▒▓ ░▒▓░ ▒▒░ ▒▒   ▒▒░ ░░░  ░ ▓▒░░ ░▒ ▓▒ ▒▒ ░  ▒▒░ ▒▒░ ░▓▒░ ▓▒ ░▓▒░▒░ ▓▓▒░  ",
           " ░ ░▒  ░░ ░ ▒  ▒   ░ ▒  ▒     ▒      ░  ░  ░  ░ ░ ▒  ▒   ▒▒ ░ ▒░ ▒   ░  ▒░   ",
           "   ░    ░  ░ ░  ░  ░ ░   ░     ░  ░  ░          ░ ░  ░    ░   ░  ░       ░   ",
           "                                                                             ",
          f"{let}________________________________________________________{clear}         ",
          f"                                                                             ",
          f"           {let}Press{clear} [Enter] {let}to continue{clear}                 ",
          f"                                                                             ",
          f"              {let}______________________________________/{clear}            "                  
        ],  
    ]

    
    input_thread = threading.Thread(target=wait_for_enter, args=(stop_flag,), daemon=True)
    input_thread.start()

    i = 0

    while not stop_flag:
        clear_screen()
        print_colored_art(ascii_arts[i % 3], gradient_colors[i % 3])
        time.sleep(1)
        i += 1

    clear_screen()

    gradient_colors_logo = [217, 203, 196, 160, 160, 124, 124, 88, 88]
    ascii_art_logo = [
        "  ██▀███   ▒████▄  ▒████▄     █▒    ██       ██  ▒████▄  ██▀███   ▄▄▄ ▄▄▄       ",
        " ▓██ ▒ ██▒▒██▀▒██▌▒▒██▀ ██▌   ██▒   ▓█▄     ▒▀█ ▒██▀▒██▌▓██ ▒ ██▒█▌▀▀█▌▀▀█      ",
        " ▓██░░▄█ ▒░██   █▌▒░██  ▒█▌ ▄▄██▄▄ ░▓▀██░ █░░█▀░░██   █▌▓██ ░▄█ ▒█▌ ░█▌ ░█░     ",
        " ▒██▀▀█▄  ░▓█▄ ▒█▓ ░▓█▄▒▒█▓░▒▒██▒░ ▒▒░▀█▄█▀█▓█▒░░▓█▄ ▒█▓▒██▀▀█▄▒▒█▌▒▒█▌▒▒█▒     ",
        " ░██▓ ▒██▒░▒▓███▓▒▒░▒▓███▓▒▓ ▒▀███▀░▒ ▒▀█▀▒▀█▀▒░░▒▓███▓▒░██▓ ▒██▒██▒▒█▓░▓█▓▒    ",
        " ░ ▒▓ ░▒▓░ ▒▒▓ ▒▒   ▒▒▓ ▒▓░  ░ ▓▒░ ░  ▒ ▓▒ ▒▒ ░  ▒▒▓ ▒▒ ░ ▒▓ ░▒▓░ ▓▒░▒  ░▓▒░    ",
        " ░ ░▒   ░ ░ ▒  ▒   ░ ▒  ▒     ▒      ░  ░  ░    ░ ▒  ▒   ▒▒ ░ ▒░ ▒      ▒░      ",
        "   ░░ ░ ░  ░ ░  ░    ░   ░     ░     ░          ░ ░  ░    ░   ░     ░   ░       ",
        "                                                                                ",
       f"{let}________________________________________________________{clear}            ", 
       f"[{let}*{clear}] RootWorm{ler}V2{clear} RAT                                      ", 
       f"[{let}*{clear}] Authors        {let}|{clear} Eks1azy, Oqwe4O, Tusay1            ", 
       f"[{let}*{clear}] Github         {let}|{clear} https://github.com/Eks1azy      ",      
       f"              {let}______________________________________/{clear}               "    
    ]

    print_colored_art(ascii_art_logo, gradient_colors_logo)

    def convert(path):
        try:
            if not os.path.exists(path):
                raise FileNotFoundError(f"ERROR: file is missing {path}")

            img = Image.open(path)
            output_icon = "icon.ico"
            img.save(output_icon, "ICO")
            return output_icon

        except Exception as e:
            print(f"{ler}ERROR: {e}{clear}")
            
            default_icon = os.path.join("lib", "text", "icon.ico")
            
            if os.path.exists(default_icon):
                print("Use default icon.")
                return default_icon
            else:
                print(f"{ler}ERROR: missing icon {default_icon}{clear}")
                return None

    def build():
        paths = convert(icon) 
        if paths is None or not os.path.exists(paths):
            print(f"{ler}FAILED — icon does not exist.")
            return


        if not os.path.exists("Your(EXE)"):
            os.makedirs("Your(EXE)")

        # Nuitka-command
        if choice == "2":
            print(f"{let}Building with Nuitka...{clear}")
            command = (
            f"python -m nuitka "
            f"--standalone "
            f"--onefile "
            f"--windows-console-mode=disable "
            f"--windows-icon-from-ico={paths} "
            f"--output-dir=Your(EXE) "
            f"--output-filename={exe}.exe "
            f"--include-data-file=config.py=config.py "
            f"--nofollow-import-to=tkinter "
            f"--assume-yes-for-downloads "
            f"--remove-output "
            f"bot.py"
            )

        
        # PyInstaller-command
        if choice == "1":
            print(f"{let}Building with PyInstaller...{clear}")
            command = (
                f"py -{version} -m PyInstaller --onefile --noconsole "
                f"--icon={paths} "
                f"--name={exe} "
                f"--add-data config.py;. "
                f"--collect-submodules setuptools._distutils "
                f"--distpath Your(EXE) "
                f"bot.py"
            )
  
        os.system(command)

        print(f"{let}Done.{clear}")
        input()    

    print(f"""
    {let}__________________________________________________________{clear}
                                                       
    {ler}>>{clear} Enter the executable file name (.exe): 
    """)
    
    exe = input(f"{let}root@RootWormV2{clear}:{ler}~{clear}$ ")

    print(f"""
    {ler}>>{clear} Enter the icon file path (.ico): 
    """)   
    
    icon = input(f"{let}root@RootWormV2{clear}:{ler}~{clear}$ ")

    print(f"""
    {ler}>>{clear} Enter your Python version (like 3.11.0): 
    """) 

    version = input(f"{let}root@RootWormV2{clear}:{ler}~{clear}$ ")

    print(f"""
    {ler}>>{clear} Choose the compiler:
    {ler}1.{clear} PyInstaller ( Faster, compatible, antivirus-friendly )
    {ler}2.{clear} Nuitka  ( Slower, less compatible, stealthy )
    """)   
    
    choice = input(f"{let}root@RootWormV2{clear}:{ler}~{clear}$ ")

    build()
    

RootWorm3()

