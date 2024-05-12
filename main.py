import random

# width = int(input('Enter width: '))
# height = int(input('Enter hight: '))
width=60
height=30
specialChar = '*'
emptyChar = ' '
# ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
# ________________
def isLines(h, w, height, width):
    lineTop = (h>=0.1*height and h<0.2*height)
    lineBottom = (h>=0.8*height and h<0.9*height)
    return lineTop or lineBottom
    
# ✡
def isMagenDavid(h, w, height, width):
    triangleUp = False
    triangleDown = False
    if 0.3*width <= w <= 0.7*width:
        # △
        triangleUp = 0.23*height <= h < 0.65*height and (
            (h>=0.62*height) or # _
            -round(0.38*width) in (h-(width-w), h-w) # /\
        )
        # ▽
        triangleDown = 0.33*height <= h < 0.75*height and (
            (h<0.36*height) or # ‾
            -round(0.13*width) in (h-(width-w), h-w) # \/
        )
    return triangleUp or triangleDown
    
for h in range(height):
    for w in range(width):
        bit = isLines(h,w,height,width) or isMagenDavid(h,w,height,width)
        print(specialChar if bit else emptyChar, end =" ")
    print()
