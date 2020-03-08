import sys

def turn_clockwise(str_now):
    """ takes ('N','E','S','W') these four compass points as its parameter, 
    and returns the next compass point in the clockwise direction.
    """
    compass = ['N','E','S','W']
    j = 0
    for i in range(len(compass)):

        if compass[i] == str_now:
            j = i + 1     
            while j > 3:
                j = j - 4
                        
        str_next = compass[j]

        return str_next


def test(did_pass):
    '''Print the result of the test.'''
    linenum = sys._getframe(1).f_lineno #Get the caller's line number
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))

    print(msg)

def test_suite():
    """Run the suite of tests for code in this module(this file)
    """
    test(turn_clockwise('N') == 'E')
    test(turn_clockwise('W') == 'N')        
            
            
test_suite()


