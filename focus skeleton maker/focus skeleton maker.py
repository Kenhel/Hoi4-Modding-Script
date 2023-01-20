import re

from flask import g

def Capitalize(s): 
    return ' '.join([i.capitalize() for i in s.split(' ')])

with open(r"C:/Users/User/Documents/GitHub/Hoi4 auto code generator/focus skeleton maker/list.txt") as f:
    lines = f.readlines()
    
out = """# Made by Kenhel
"""
for line in lines:
    txt = re.findall(pattern=r"(?=i= )(.*)$", string=line)
    txt1 = re.findall(pattern=r"(?=p= )(.*)$", string=line)
    txt2 = re.findall(pattern=r"(?=g= )(.*)$", string=line)
    
    for text in txt:
        text_a = str(text).replace("i= ", "QNG_focus_")

    for text1 in txt1:
        text_b = str(text1).replace("p= ", "QNG_focus_")
        text_d = str(text1).replace("p= ", "")

    for text2 in txt2:
        text_c = str(text2).replace("g= ", "")

        if text_d == str(0):
            out += f'	focus = {{\n        id = {text_a}\n		icon = {text_c}\n		x = 0\n		y = 0\n		cost = 70\n\n		ai_will_do = {{\n			factor = 0\n			modifier = {{\n				factor = 0\n				is_historical_focus_on = yes\n			}}\n		}}\n		completion_reward = {{\n\n		}}\n	}}\n\n' 
        else:
            out += f'	focus = {{\n        id = {text_a}\n		icon = {text_c}\n		relative_position_id = {text_b}\n		x = 0\n		y = 1\n		cost = 70\n\n		ai_will_do = {{\n			factor = 0\n			modifier = {{\n				factor = 0\n				is_historical_focus_on = yes\n			}}\n		}}\n		prerequisite = {{\n			focus = {text_b}\n		}}\n		completion_reward = {{\n\n		}}\n	}}\n\n'
with open('C:/Users/User/Documents/GitHub/Hoi4 auto code generator/focus skeleton maker/output.txt', 'w') as f:
    f.write(out)
