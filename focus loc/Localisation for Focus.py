TAG = "QNG"

import re

def Capitalize(s): 
    return ' '.join([i.capitalize() for i in s.split(' ')])

with open(r"C:/Users/User/Documents/GitHub/Hoi4 auto code generator/focus loc/output.txt") as f:
    lines = f.readlines()
    
out = """#made by https://github.com/Kenhel and https://github.com/Syth-1\n"""
for line in lines:
    txt = re.findall(pattern=r'(?<=	id = QNG_focus_)(.*)$', string=line)
    for text in txt:
        out_text = str(text).capitalize().replace("_", ' ')
        out += f'    {TAG}_{text}: "{Capitalize(out_text)}"\n'
        out += f'    {TAG}_{text}_desc: ""\n'
        out += f'\n'


with open('C:/Users/User/Documents/GitHub/Hoi4 auto code generator/focus loc/output.yml', 'w') as f:
    f.write(out)