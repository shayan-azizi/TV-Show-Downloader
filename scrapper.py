import requests

URL = "https://mobomoviez.fun/post/"


find = True
is_paused = False

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
    link = "https://mobomoviez.fun/"
    append = False
    
    for i in link_tag:
        if append:
            link += i
        
        if i == "/":
            append = True
            
        if i == '"':
            append = False
    
    return link[:-1]

def find_link (page, season_number, resolution_number, episode):
    print ("WOW! We find that show!")
    
    page_list = page.text.split ("\n")
    
    seasons = []
    
    for i in range (len(page_list)):
        element = page_list[i]
        if "<h3>" in element and "</h3>" in element and "فصل" in element:
            seasons.append (i)
            
    print (f"That show has {len(seasons)} seasons")
    season_number = int(season_number)
    

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

    return [final_link, file_name]

def find_page (show_name : str):
    
    
    show_name = normalize_name(show_name)

    page = requests.get(URL + show_name)


    if "اوپس" in page.text:
        return False
    
    else:
        return page

def terminate_download ():
    OBJ.stop()
    
def pause_download ():
    global is_paused
    
    if is_paused:
        OBJ.resume()
        is_paused = not is_paused
        
    else:
        OBJ.pause()
        is_paused = not is_paused
