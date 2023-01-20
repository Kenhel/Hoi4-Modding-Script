TAG = "SER"

import re

def Capitalize(s): 
    return ' '.join([i.capitalize() for i in s.split(' ')])

with open(r"C:/Users/User/Documents/GitHub/Hoi4 auto code generator/event chain loc/input.txt") as f:
    lines = f.readlines()
    
out = """#made by https://github.com/Kenhel and https://github.com/Syth-1\n"""
for line in lines:
    txt = re.findall(pattern=r"(?<=id =)(.*)$", string=line)
    txt1 = re.findall(pattern=r"(?<=title = )(.*)$", string=line)
    txt2 = re.findall(pattern=r"(?<=desc =)(.*)$", string=line)
    txt3 = re.findall(pattern=r"(?<=name =)(.*)$", string=line)
    for text in txt:
        text_a = str(text).replace("", "")

    for text1 in txt1:
        text_b = str(text1).replace("", "")

    for text2 in txt2:
        text_c = str(text2)

    for text3 in txt3:
        text_d = str(text3)
        out += f'    #{text} ""\n'
        out += f'    {text1}:0 ""\n'
        out += f'    {text2}:0 ""\n'
        out += f'    {text3} ""\n'
        out += f'\n'

with open('C:/Users/User/Documents/GitHub/Hoi4 auto code generator/event chain loc/output.yml', 'w') as f:
    f.write(out)