# Computer Assistant for KTANE (Keep Talking and Nobody Explodes)

This code is ugly, because it is designed to be used directly from
the python command prompt, but with minimal typing overhead

From a command prompt, do:

    >>> from ktane import *

All solvers are stateful and will reuse previously learned information about the bomb. To reset the bomb state
(for instance starting a new level), do

    >>> reset()

## Wires

Call the function wires() with the colors that you see, in order. For instance:

    >>> wires(red,red,black,blue).

You can also use some shortcuts: (r)ed, (w)hite, (b)lue, blac(k) or (y)ellow

## Buttons

Call the function button(color, label). For instance:

    >>> button(red, abort)

It may prompt you for things like the number of batteries on the bomb, or 
the serial number. Eventually, it will answer with 'press' (for press and
release immediately) or 'hold' (for hold the button, then apply the simple
color logic from the manual)

## Complicated wires

Call the cwire function with any of blue, red, led, or star as the arguments.
For instance:

    >>> cwire(red, blue, star)

## Passwords

Call the password() function. Enter the letters available on the first column.
Possible passwords will be displayed, and you will be prompted to enter each
column until there is only one possibility left

Example:

    >>> password
    Column 1: abcd
    ['about', 'after', 'again', 'below', 'could']
    Column 2: owizyk
    ['below']
    >>> 
