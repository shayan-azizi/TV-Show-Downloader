import wget
import json
import requests
import os

URL = "https://mobomovies.fun/post/"
CONFIG = json.load(open("config.json"))


def normalize_name (series_name : str) -> str:
    series_name = series_name.lower()
    
    result = ""
    for i in series_name:
        
        if i != " ":
            result += i

        else:
            result += "-"
    
    return result

def normalize_link (link_tag : str) -> str:
    link = "https://mobomovies.fun/"
    append = False
    
    for i in link_tag:
        if append:
            link += i
        
        if i == "/":
            append = True
            
        if i == '"':
            append = False
    
    return link[:-1]
    
    
            
series_name = input("Enter the TV-show name: ")
series_name = normalize_name(series_name)

page = requests.get(URL + series_name)

if "اوپس" in page.text:
    print ("Sorry dude we can't find it :(")

else:
    print ("WOW! We find that show!")
    
    page_list = page.text.split ("\n")
    
    seasons = []
    
    for i in range (len(page_list)):
        element = page_list[i]
        if "<h3>" in element and "</h3>" in element and "فصل" in element:
            seasons.append (i)
            
    print (f"That show has {len(seasons)} seasons")
    season_number = int(input ("Enter the season number: "))
    
    resolution_number = input ("Enter your resolution: ")

    resolutions = []
    
    try:
        limit = seasons[season_number]
        
    except:
        limit = len (page_list) - 100
        
    for i in range (seasons[season_number - 1], limit):
        element = page_list[i]
        if resolution_number in element:
            resolutions.append (i)
    
    limit = resolutions[-1]    
    if len (resolutions) == 1:
        try:
            limit = seasons[season_number]
        
        except:
            limit = len(page_list) - 100
    
    subtitle = 0
    for i in range (resolutions[0], limit):
        element = page_list[i]
        
        if "زیرنویس چسبیده" in element:
            subtitle = i
            break
        
    
    episode = input ("Enter the episode number: ")
    
    episode_idx = 0
    for i in range (subtitle, limit):
        element = page_list[i]
        
        if "قسمت" + " " + episode in element:
            episode_idx = i
            break
        
    link = ""
    for i in range (episode_idx, subtitle, -1):
        element = page_list[i]
        
        if "href" in element and "<a" in element:
            link = element
            break
    
    
    link = normalize_link(link)
    
    print ("  ===================   ")
    
    download_page = requests.get(link)
    
    download_page_list = download_page.text.split("\n")
    
    final_link_tag = ""
    for i in range (len (download_page_list)):
        element = download_page_list[i]
        
        if "fal fa-download ml-2" in element:
            final_link_tag = download_page_list[i - 1]
            break
    
    final_link = ""
    
    append = False
    
    for i in final_link_tag:
        if append:
            
            final_link += i
        
        if i == "=":
            append = True
            
        if i == " ":
            append = False
            
    
    final_link = final_link[1:-37]
    
    print ("i will get this link: ")
    print (final_link)
    
    file_name = ""
    for i in range (len (final_link) - 1, 0, -1):
        
        if final_link[i] != "/":
            file_name += final_link[i]
        
        else:
            break
            
    file_name = file_name [::-1]
    print (file_name)
    
    if CONFIG["location"][-1] != "/":
        CONFIG["location"] += "/"

    response = wget.download(final_link, CONFIG["location"] + file_name)
    
    
    
    


    
    