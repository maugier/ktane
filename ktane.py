from collections import defaultdict

        
red = 'red'
r = red

blue = 'blue'
b = blue

black = 'black'
k = black

white = 'white'
w = white

yellow = 'yellow'
y = yellow

star = 'star'
led = 'led'

hold = 'hold'
press = 'press'
detonate = 'detonate'
det = detonate
abort = 'abort'

def start():
    global indicators, serial, strikes
    indicators = defaultdict(lambda: None)
    serial = None
    strikes = 0

def strike():
    global strikes
    strikes += 1

def askserial():
    global serial
    if serial is None:
        serial = input("Serial number> ")
    return serial

def odddigit():
    return int(askserial()[-1]) % 2

def evendigit():
    return not odddigit()

def askindicator(i):
    if indicators[i] is None:
        indicators[i] = (input("Indicator {} [y/n]".format(i)) == 'y')
    return indicators[i]

def batteries():
    if indicators['batteries'] is None:
        indicators['batteries'] = int(input("# of batteries: "))
    return indicators['batteries']

def wires(a,b,c,d=None,e=None,f=None):
    def count(color):
        return sum(x == color for x in (a,b,c,d,e,f))


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


def button(color, label):
    if color == blue and label == abort:
        return hold
    if label == detonate and batteries() > 1:
        return press
    if color == white and askindicator('CAR'):
        return hold
    if batteries() > 2 and askindicator('FRK'):
        return press
    if color == yellow:
        return hold
    if color == red and label == hold:
        return press
    return hold


def complicated(*a):
    C = lambda: True
    D = lambda: False
    S = evendigit
    P = lambda: askindicator("Parallel Port")
    B = lambda: batteries() >= 2

    index = (red in a) + 2*(blue in a) + 4*(star in a) + 8*(led in a)

    table = [ C, S, S, S, C, C, D, P, D, B, P, S, B, B, P, D]

    return table[index]()
        

def password():
    words = ["about", "after", "again", "below", "could",
             "every", "first", "found", "great", "house",
             "large", "learn", "never", "other", "place",
             "plant", "point", "right", "small", "sound",
             "spell", "still", "study", "their", "there",
             "these", "thing", "think", "three", "water",
             "where", "which", "world", "would", "write" ]

    columns = []

    def acceptable(word):
        return all(l in c for (l,c) in zip(word, columns))

    while True:
        columns.append(input("Column {}: ".format(len(columns) + 1)))

        ws = list(filter(acceptable, words))
        if len(ws) < 2:
            return ws

        print(ws)



start()
