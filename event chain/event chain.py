from __future__ import annotations
from dataclasses import dataclass
import re

@dataclass
class Events(): 
    id : str
    title : str 
    desc : str 
    picture : str 
    options : list[Options]

@dataclass 
class Options(): 
    name : str
    id : str = None
    days : int = None

with open(r"C:/Users/User/Documents/GitHub/Hoi4 auto code generator/event chain/list.txt") as f:
    input = f.read()

tag = "SER_cukur_fountain_incident"

matches = [tuple(i for i in m if i) for m in re.findall("(i=.+)\n(o=.*)\n(p=.+)\n(d=.+)|(i=.+)\n(o=.+)\n(p=.+)", input)]

#first pass -- create struture
data : list[Events] = []
for match in matches:
    i = match[0].split('=')[-1]
    o = int(match[1].split('=')[-1])

    name = f"{tag}.{i}"

    data.append(
        Events(
            id=name,
            title=f"{name}.t",
            desc=f"{name}.d",
            picture="lorem_ipsum",
            options = [Options(name=f"{name}.{chr(iter + ord('a'))}") for iter in range(o)]
        )
    )

#second pass -- add events
for i, match in enumerate(matches):
    if len(match) < 4: 
        continue #if our capture doesnt find days, will only capture 3, no need to add events

    p = match[2].split('=')[-1]

    if p == "0": 
        continue #if there happened to be 4 captures, but p = 0, we can skip

    splitVal = re.findall("(\d+)([a-z])", p) #1 = event index, 2 = option index

    if len(splitVal) == 0: 
        continue #no val found!

    splitVal = list(splitVal[0])

    if not isinstance(splitVal, list) and len(splitVal) != 2: 
        continue #something gone wrong, couldnt find index of event and option index to add to!

    splitVal[0] = int(splitVal[0]) - 1
    splitVal[1] = ord(splitVal[1]) - ord('a')
    
    if len(data)-1 < splitVal[0] or len(data[splitVal[0]].options)-1 < splitVal[1]:
        continue 
        #either values are bigger the number of items in array 

    d = int(match[3].split('=')[-1])

    data[splitVal[0]].options[splitVal[1]].id = data[i].id
    data[splitVal[0]].options[splitVal[1]].days = d

#generate code:
output = "#made by https://github.com/Kenhel and https://github.com/Syth-1\n"
for d in data: 
    output += "country_event = {" + \
        f"\n\tid = {d.id}\n\ttitle = {d.title}\n\tdesc = {d.desc}\n\tpicture = {d.picture}" + \
        "\n\n\t\tfire_only_once = yes\n\n\t\tis_triggered_only = yes\n"

    for o in d.options:
        output += "\n\toption = {" + \
            f"\n\t\tname = {o.name}" + \
            "\n\t\tai_chance = {\n\t\t\tfactor = 0\n\t\t}"

        if o.id is not None: 
            output += "\n\t\tcountry_event = {" + \
                f"\n\t\t\tid = {o.id}\n\t\t\tdays = {o.days}" + \
                "\n\t\t}"

        output += "\n\t}"
    output += "\n}\n"


with open('C:/Users/User/Documents/GitHub/Hoi4 auto code generator/event chain/output.txt', 'w') as f:
    f.write(output)