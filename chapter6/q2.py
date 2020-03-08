import sys

def day_name(day_num):
    week = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    if (-1 < day_num) and (day_num < 7):
        day_name = week[day_num]
        return day_name

    else:
        return

    
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
    test(day_name(3) == 'Wednesday')
    test(day_name(6) == 'Saturday')
    test(day_name(42) == None)
            
test_suite()


