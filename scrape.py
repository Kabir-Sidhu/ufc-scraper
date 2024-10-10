import json, requests, uuid
from bs4 import BeautifulSoup

def get_elements(link: str, tag: str, _class: str):
    r = requests.get(link)

    soup = BeautifulSoup(r.content, 'html.parser')

    elements = soup.findAll(tag, attrs = { "class": _class })

    return elements

def get_fights():
    fights = {}
    fighters = []

    elements = get_elements("http://ufcstats.com/statistics/events/completed", "a", "b-link b-link_style_white")
    
    link = elements[0].get("href")

    elements = get_elements(link, "a", "b-link b-link_style_black")

    for i in elements:
        try:
            if "matchup" in str(i).lower():
                continue
            
            fighters.append(i.contents[0].strip())
        except:
            continue

    for i in fighters:
        index = fighters.index(i)

        if index % 2 == 0:
            fights[str(uuid.uuid4())] = {
                "fight": f"{i} vs {fighters[index+1]}",
                "fighter1": i,
                "fighter2": fighters[index+1]
            }
    
    return fights


if __name__ == "__main__":
    fights = get_fights()

    print(fights)