import requests
import json
import os
import time

COMMANDS = ["help", "h", "download", "d", "\n", "", "clear", "cls", "q", "quit", "commands"]

def find_seasons (page : str) -> int:
    print (page)

def find_page (name : str) -> str:
    page = requests.get("https://mobomoviez.fun/post/" + name)
    
    if "اوپس" in page.text:
        return False
    
    else:
        return page.text

def corrected_name (name : str) -> str:
    name = name.lower()
    
    corrected_name = ""
    for char in name:
        
        if char != " ":
            corrected_name += char
            
        else:
            corrected_name += "-"
    
    return corrected_name
        

def main () -> None:
    print("\033[1;32m Welcome to Tv-Show-Downloader CLI Version  \n")
    
    while True:
        command = input("\033[1;30m~ ")
        
        if command not in COMMANDS:
            print (f"\033[1;31m Tv-Show-Download: command not found: {command}")
            
        if command in ["clear", "cls"]:
            os.system("clear")
            
        if command in ["q", "quit"]:
            quit()
            
        if command in ["help", "h", "commands"]:
            print ("Commands List\ndownload (d): Start downloading TV-Show\nhelp (h): Show this list\nclear (cls): Clear the screan\nquit (q): Exit from this program")
            
        if command in ["download", "d"]:
            show_name = input("Enter The TV-Show name: ")
            show_name = corrected_name(show_name)
            
            print ("Finding TV-Show ...")
            
            page = find_page(show_name)
            if not page:
                print ("\033[1;31m Can't find that TV-Show") 

            else:
                print ("Find that TV-Show")
                
                find_seasons(page)
                
            
                
            
            
        
    show_name = input()

if __name__ == "__main__":
    main ()