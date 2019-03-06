from orchid66 import printc, printn

for i in range(0, 256, 20):
    # printc uses colored soooooo
    printc("hello", (i, 100, 100), (100, 100, i), end=True)

red =  (255, 0, 0)
blue = (50, 50, 255)
printn('this word is in *red*, and this is in *blue*', (red, blue))
printn('*9&*9 is 81*', (red,))
