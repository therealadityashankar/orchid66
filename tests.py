from orchid66 import printc, printn, color_escape, COLORS

for i in range(0, 256, 20):
    # printc uses colored soooooo
    if i%80:
        end=False
    else:
        end=True
    color = ((i, 100, 100), (100, 100, i))
    printc("hello", color, end)

red =  (255, 0, 0)
blue = (50, 50, 255)
green = (50, 255, 50)
printn('this word is in *red*, and this is in *blue*', (red, blue))
printn('*9&*9 is 81*', ((red, green),))


printn('this is *red*', ('red',))
printn('*9&*9 is 81*', (("red", "green"),))

printn("escaping &*'s", ())
string = "dua@$^**im**csck**"
print(f"normal print (using the builtin print fn): {string}")
escaped = color_escape(string)
blue_in_white = ("blue", "white")
printn(f"escaped printn: *{escaped}*", blue_in_white)

printn("*this is coloured* and this is not", (blue_in_white,))

print()
print('X11 colors')
for color in COLORS.keys():
    printc(' ', ('white', color), end=False)
print()
