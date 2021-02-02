from __future__ import print_function
from PIT import *
from PS import PS_init
from FIB import FIB_init

def Network_init(route_num): #route_num, content_num
    network = [['r0', ['r1', 'r2']], ['r1', ['r0', 'r2']], ['r2', ['r0', 'r1']]]
    # fib = \
    FIB_init(network)

    # return  fib

if __name__ == '__main__':
    """
        incomingface = route_ID
        interest = {'route_ID': [interest_ID, consumer_ID, route_ID, content_name, start_time, life_time]}
    """
    interest = {'r0': ['i0', 'c0', 'r0', 'r1/0', 10., 100.]}
    pit = {'r0': [['r1/0', ['r1', 'r3'], ['r4', 'r5']], ['r1/1', ['r2', 'r9'], ['r8', 'r7']]]}
    inface = 'r0'
    # Time_out(inface, interest)
    # PIT_search_interest(inface, interest)
    # Creat_fib_entry(inface, 'r1/1')
    fib = FIB_init()
    print(fib)