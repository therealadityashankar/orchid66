# orchid66
print stuff with colors

Note: currently only supports linux

# installation

1. clone this repository
2. change the current directory into this repository
3. execute `pip install .`

# example:
```
from orchid66 import printn

red = (255, 0, 0)
blue = (50, 50 , 255)
gree = (50, 255, 50)
printn("this is in *red*, and this is in *blue*, red, blue)
printn("I like *green* && *blue*", green, blue)
```

# orchid66' mini language

`&*` refers to a single `*` that is rendered
`&&` refers to a single `&` that is rendered
