"""
this module has a curr_color function that
represents text if it were curr_color
"""
from collections import OrderedDict

# base error class
class Error(Exception): pass

class COLORS:
    red = (255, 50, 50)
    blue = (50, 50, 255)
    green = (50, 255, 50)
    pink = (255, 192, 203)
    black = (0, 0, 0)
    white = (255, 255, 255)
    # add colors here


def colored_bash(text, color=None):
    """
    return a string that will return
    a string that will appear curr_color when printed

    Parameters
    ----------
    text : string
        text to show

    color : a tuple (red, green, blue)
           to represent the fgcolor
           to be used
           or 2 tuples ((r, g, b), (r, g, b))
           to represent the fgcolor, bgcolor
           or a color string such as 'blue' or 'red'

    Returns
    -------
    string
           string representing a colored string in bash
    """
    fgcolor, bgcolor = getcolor(color)
    if fgcolor:
        red, green, blue = fgcolor
        fgcolor_thing = f"\033[38;2;{red};{green};{blue}m"
    else:
        fgcolor_thing = ""

    if bgcolor:
        bgred, bggreen, bgblue = bgcolor
        bgcolor_thing = f"\033[48;2;{bgred};{bggreen};{bgblue}m"
    else:
        bgcolor_thing = ""

    reset_thing = "\033[39;49m"
    return_thing = fgcolor_thing + bgcolor_thing + text + reset_thing
    return return_thing


def printc(text, color=None, end=False):
    """
    prints the text using the "curr_color" function
    of this module

    Parameters
    ----------
    text : string
        text to show

    color : tuple
        a tuple (red, green, blue)
        to represent the color
        to be used
        
    end : bool
        boolean to indicate if 
        text should end with 
        newline
    """
    end = "\n" if end else ""
    ctext = colored_bash(text, color)
    print(ctext, end=end)


def getcolorstr(colorstr):
    '''
    get color from string
    raises an exception if
    the color is not present

    Parameters
    ---
    colorstr : string
        a color in string
        like 'white' or 'blue'

    Returns
    ---
    tuple
        tuple indicating appropriate
        color in RGB
    '''
    color = getattr(COLORS, colorstr, None)
    if color is None:
        raise Error(f'unknown color {color}')

    return color
    

def getcolor(color):
    '''
    retrieves fgcolor and bgcolor

    Parameters
    ---
    color: string or tuple
        value corresponding to a color
        if a tuple such as (r, g, b) or ((r, g, b))
            return that as fgcolor and bgcolor as None

        if a tuple such as ((r, g, b), (r, g, b))
            fgcolor is 1st tuple
            bgcolor is 2nd tuple
    
         if  None returns None, None
         if string returns appropriate color for string
             or raises exception

    Returns
    ---
    tuple
        fgcolor, bgcolor
        both of which are
        tuples representing RGB
        colors in (r, g, b)
    '''
    if color is None: return None, None

    # if string
    if type(color) == str:
        color = getcolorstr(color)
        return color, None

    # if first is number
    # assume tuple of numbers
    if type(color[0]) == int or type(color[0]) == float:
        return color, None

    # else list of tuples
    else:
        # if one tuple in the list its fgcolor
        if len(color) == 1:
            color = color[0]
            if type(color) == str:
                color = getcolorstr(color)
            return color, None

        # else fgcolor, bgcolor
        else:
            fgcolor, bgcolor = color

            if type(fgcolor) == str:
                fgcolor = getcolorstr(fgcolor)

            if type(bgcolor) == str:
                bgcolor = getcolorstr(bgcolor)

            return fgcolor, bgcolor

def printn(text, colors):
    '''
    print nicely

    see the nicely printing mini language with
    print(thepycolor.__minilang__)

    Parameters
    ---
    text: string
        the text between '*' (astriks) is curr_color with the
        color in colors at the appropriate index
        (an "&*" is rendered as a single "*")
        (an "&&" is rendered as a single "&")

    colors : indexable iterable
        iterable of one or two colors
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

    Example
    ---
    a simple example
    I can't show the outputs as
    colors cannot be shown (obvio)

    >>> red = (255, 0, 0)
    >>> blue = (50, 50, 255)
    >>> printn('this word is in *red*, and this is in *blue*', (red, blue))
    >>> printn('9&*9 is 81')
    >>>
    '''
    curr_color_index = -1
    sen_colors = OrderedDict()

    text_len = len(text)
    curr_index = 0

    # take in the next character
    # increase the current
    # character index
    def gulp():
        nonlocal curr_index
        char = text[curr_index]
        curr_index += 1
        return char

    # get the next color
    def next_color():
        nonlocal curr_color_index
        curr_color_index += 1

        if curr_color_index < len(colors):
            color = colors[curr_color_index]
        else:
            color = None

        return color

    curr_color = None
    curr_sen   = ''
    while curr_index < text_len:
        char = gulp()
        if char == '&':
            char = gulp()
            if char in '*&':
                curr_sen += char

        elif char == '*':
            # register previous sentence and color
            sen_colors[curr_sen] = curr_color
            curr_sen = ''

            # if first tag switch color
            # to next color, else if
            # tag switch to no color
            # so it alternates right ?
            if curr_color is None:
                curr_color = next_color()
            else:
                curr_color = None
        else:
            curr_sen += char

    for sen in sen_colors:
        color = sen_colors[sen]
        fgcolor, bgcolor = getcolor(color)
        printc(sen, fgcolor, bgcolor)
    
    printc("\n")


def color_escape(text):
    '''
    color escape text
    that is, color escaped text will be rendered normally
    when print c is used

    Parameters
    ---
    text : string
        text to escape

    Returns
    ---
    string
        color escaped text
    '''
    escaped = text.replace("&", "&&")
    escaped = escaped.replace("*", "&*")
    return escaped

__minilang__ =\
'''
the pycolors mini language guide:

text in between astriks ('*') is rendered colored
with the corrosponding color

& behaves as an escape sequence here
'&*' is rendered as an '*' and
'&&' is rendered as an '&'
'''
