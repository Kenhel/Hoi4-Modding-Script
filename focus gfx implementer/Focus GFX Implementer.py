import re

with open(r"C:/Users/User/Documents/GitHub/Hoi4 auto code generator/focus gfx implementer/list.txt") as f:
    lines = f.readlines()
    
out = """# made by https://github.com/Kenhel\n"""
for line in lines:
    txt = re.findall(pattern=r"(?=idea_)(.*)$", string=line)
    for text in txt:
        text_a = str(text).replace("idea_", "GFX_idea_").replace(".dds", "")
        text_b = str(text)#.replace("idea_", "generic_idea")
        out += f'    SpriteType = {{\n		name = "{text_a}_shine"\n		texturefile = "gfx/interface/ideas/RUS/{text_b}.png"\n		effectFile = "gfx/FX/buttonstate.lua"\n		animation = {{\n			animationmaskfile = "gfx/interface/ideas/RUS/{text_b}.png"\n			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"			# <- the animated file\n			animationrotation = -90			# -90 clockwise 90 counterclockwise(by default)\n			animationlooping = no			# yes or no ;)\n			animationtime = 0.75			# in seconds\n			animationdelay = 0			# in seconds\n			animationblendmode = "add"			#add, multiply, overlay\n			animationtype = "scrolling"			#scrolling, rotating, pulsing\n			animationrotationoffset = {{\n				x = 0\n				y = 0\n			}}\n			animationtexturescale = {{\n				x = 1\n				y = 1\n			}}\n		}}\n		animation = {{\n			animationmaskfile = "gfx/interface/ideas/RUS/{text_b}.png"\n			animationtexturefile = "gfx/interface/goals/shine_overlay.dds"			# <- the animated file\n			animationrotation = 90			# -90 clockwise 90 counterclockwise(by default)\n			animationlooping = no			# yes or no ;)\n			animationtime = 0.75			# in seconds\n			animationdelay = 0			# in seconds\n			animationblendmode = "add"			#add, multiply, overlay\n			animationtype = "scrolling"			#scrolling, rotating, pulsing\n			animationrotationoffset = {{\n				x = 0\n				y = 0\n			}}\n			animationtexturescale = {{\n				x = 1\n				y = 1\n			}}\n		}}\n		legacy_lazy_load = no\n	}}\n'

with open('C:/Users/User/Documents/GitHub/Hoi4 auto code generator/focus gfx implementer/goals_shine.gfx', 'w') as f:
    f.write(out)



out = """# made by https://github.com/Kenhel\n"""
for line in lines:
        txt = re.findall(pattern=r"(?=idea_)(.*)$", string=line)
        for text in txt:
            text_a = str(text).replace("idea_", "GFX_idea_").replace(".dds", "")
            text_b = str(text)#.replace("idea_", "SER_idea")
            out += f'	SpriteType = {{\n		name = "{text_a}"\n		texturefile = "gfx/interface/ideas/RUS/{text_b}.png"\n	}}\n'

with open('C:/Users/User/Documents/GitHub/Hoi4 auto code generator/focus gfx implementer/goals.gfx', 'w') as f:
    f.write(out)
