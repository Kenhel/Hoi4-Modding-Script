
import re

with open(r"C:/Users/User/Documents/GitHub/Hoi4 auto code generator/event chain/output.txt") as f:
    lines = f.readlines()

out_line = []
for line in lines: 
    for f in re.findall(r"((?:\t| )*?(?:title|desc|name) = .+)( #.*?)$", line):
        f : tuple[str]
        print(f)
        if ("." not in f[1]):
            line = f[0]
        else: 
            line = f"{f[0]}.{f[1].split('.')[-1]}\n"
    out_line.append(line)


with open('C:/Users/User/Documents/GitHub/Hoi4 auto code generator/event chain/output_finale.txt', 'w') as f:
    f.write("".join(out_line))