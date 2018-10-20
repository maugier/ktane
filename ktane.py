from collections import defaultdict

        
red = 'red'
r = red

blue = 'blue'
b = blue

black = 'black'
bl = black

white = 'white'
w = white

yellow = 'yellow'
y = yellow

star = 'star'
led = 'led'

def start():
    global indicators, serial
    indicators = defaultdict(lambda: None)
    serial = None

def askserial():
    global serial
    if serial is None:
        serial = input("Serial number> ")
    return serial

def askindicator(i):
    if indicators[i] is None:
        indicators[i] = (input("Indicator {} [y/n]".format(i)) == 'y')
    return indicators[i]

def wires(a,b,c,d=None,e=None,f=None):
    def count(color):
        return sum(x == color for x in (a,b,c,d,e,f))
    def odddigit():
        return int(askserial()[-1]) % 2


    if d is None: # 3 wires
        if count(red) == 0:
            return 2
        if c == white:
            return "last wire"
        if count(blue) > 1:
            return "last blue wire"
        return "last wire"

    elif e is None: # 4 wires
        if count(red) > 1 and odddigit():
            return "last red wire"
        if d == yellow and count(red) == 0:
            return 1
        if count(blue) == 1:
            return 1
        if count(yellow) > 1:
            return 4
        return 2

    elif f is None: # 5 wires
        if e == black and odddigit():
            return 4
        if count(red) == 1 and count(yellow) > 1:
            return 1
        if count(black) == 0:
            return 2
        return 1

    else: # 6 wires
        if count(yellow) == 0 and odddigit():
            return 3
        if count(yellow) == 1 and count(white) > 1:
            return 4
        if count(red) == 0:
            return 6
        return 4





start()
