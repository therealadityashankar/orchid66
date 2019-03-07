# Orchid66: print colorful stuff nicely
![version tag](https://img.shields.io/static/v1.svg?label=version&message=1.0.3&color=3596e4)
![pypi tag](https://img.shields.io/static/v1.svg?label=pypi&message=1.0.3&color=87b031&link=https://pypi.org/project/orchid66/1.0.3/)

**yeah just, print colorful stuff nicely**

*Note: currently only supports linux*

## example:
```
from orchid66 import printn

printn("this is in *red*, and this is in *blue*", ('red', 'blue'))
printn("I like *green* && *blue*", ('green', 'blue'))

green_in_blue = ('green', 'blue')

# notice tuple in tuple in second parameter
printn("I like *green in blue*", (green_in_blue,))
```
![example output](exampleoutput.png)

## example gif:
![usage gif](usage_gif.gif)

## installation

### through pypi

`pip install orchid66`

### by cloning the repository
1. clone this repository
2. change the current directory into this repository
3. execute `pip install .`

## orchid66s' mini language
text between `*` is rendered as colored, except when preceded by a `&`

`&*` refers to a single `*` that is rendered

`&&` refers to a single `&` that is rendered


## docs:
```python
def color_escape:
    color escape text
    that is, color escaped text will be rendered normally
    when print c is used

    :param text: text to escape
    :type text: str
    

def colored_bash:
    return a string that will return
    a string that will appear curr_color when printed

    :param text: text to show
    :type text: string

    :param color: a tuple (red, green, blue)
                  to represent the fgcolor
                  to be used

                  or 2 tuples ((r, g, b), (r, g, b))
                  to represent the fgcolor, bgcolor

                  or a color string such as 'blue' or 'red'
    :type color: tuple
    :returns: string
    

def getcolor:
    retrieves fgcolor and bgcolor

    :param color: value corresponding to a color
                  if a tuple such as (r, g, b) or ((r, g, b))
                      return that as fgcolor and bgcolor as None

                  if a tuple such as ((r, g, b), (r, g, b))
                      fgcolor is 1st tuple
                      bgcolor is 2nd tuple
                
                  if  None returns None, None
                  if string returns appropriate color for string
                      or raises exception
    :type color: tuple

    :returns: fgcolor, bgcolor
    :return type: tuple
    

def getcolorstr:
    get color from string
    raises an exception if
    the color is not present
    :param colorstr: a color in string
                     like 'white' or 'blue'
    :type str:
    

def printc:
    prints the text using the "curr_color" function
    of this module

    :param text: text to show
    :type text: string

    :param color: a tuple (red, green, blue)
                  to represent the color
                  to be used
    :type color: tuple

    :param end: boolean to indicate if 
                text should end with 
                newline
    :type end: bool
    

def printn:
    print nicely

    see the nicely printing mini language with
    print(thepycolor.__minilang__)

    :param text: the text between '*' (astriks) is curr_color with the
                 color in colors at the appropriate index
                 (an "&*" is rendered as a single "*")
                 (an "&&" is rendered as a single "&")
    :type text: color

    :param colors: iterable of one or two colors
                   eg: [(133, 100, 90), 
                        (90, 60, 89),
                        [(45, 78, 240), (0, 0, 50)]]

                   color is a iterable corrosponding 
                   to (r ,g ,b)
                   
                   if 1 iterable of numbers, eg: (56, 78, 90)
                        numbers corrospond to foreground color
                   
                   if 1 iterable of 2 colors, eg: [(45, 56, 89),
                                                   (77, 8, 56)]
                        numbers corrospond to foreground and
                        background color
    :type colors: indexable iterable

    :Example:
        red = (255, 0, 0)
        blue = (50, 50, 255)
        printn('this word is in *red*, and this is in *blue*', (red, blue))
        printn('9&*9 is 81')
```
