"""Decode a string.

A valid code is a sequence of numbers and letter, always starting with a number
and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string "hey" could be encoded by "0h1ae2bcy". This means
"skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

A single letter should work::

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'
"""


def decode(s):
    """Decode a string."""

    pointer = 0

    final_s = []

    while pointer < len(s):         #"0h1ae2bcy"    #pointer = 5
        if (s[pointer]).isdigit():        #s[pointer] = 2
            moves = int(s[pointer])      #moves = 2
            pointer += 1
            pointer += moves            #pointer = 8

            final_s.append(s[pointer])     #final_s = [h,e,y]
            pointer += 1

    return ''.join(final_s)






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; 0G1ar0e1ba0t2ab! ***\n")
