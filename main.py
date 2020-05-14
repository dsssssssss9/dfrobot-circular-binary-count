from microbit import *
import neopixel

RED = (63, 0, 0)

BLACK = (0, 0, 0)

Num_Bits = 7

Max_Num = 2 ** Num_Bits





pixels = neopixel.NeoPixel(Neo_Pin, Num_Bits)

pixels.clear()

def fillz(s, width):
    if len(s) < width:
        return ("0" * (width - len(s))) + s
    else:
        return s

for c in range(Max_Num):
    Bin_Val = fillz(bin(c)[2:], Num_Bits)
    for i in range(Num_Bits):
        if Bin_Val[i] == "1":
            pixels[i] = RED
        else:   
            pixels[i] = BLACK
    pixels.show()
    sleep(250)