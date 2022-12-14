from bs4 import BeautifulSoup
import requests
import os

URL = "https://mobomovies.fun/post/"

def normalize_name (series_name : str) -> str:
    series_name = series_name.lower()
    
    result = ""
    for i in series_name:
        
        if i != " ":
            result += i

        else:
            result += "-"
    
    return result
            
series_name = input("Enter the TV-show name")
series_name = normalize_name(series_name)

page = requests.get(URL + series_name)

if "اوپس" in page.text:
    print ("Sorry dude we can't find it :(")

else:
    print ("WOW! We find that show!")

    
    