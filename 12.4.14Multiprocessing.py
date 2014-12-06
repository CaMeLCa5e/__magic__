#12.4.14Multiprocessing.py

import multiprocessing as mp 
import random 
import string 

#define an output queue
output = mp.Queue()

def rand_string(length, output):
    """ Generates a random string of numbers, lower- and uppercase chars. """
    rand_str = ''.join(random.choice(
                    string.ascii_lowercase
                    + string.ascii_uppercase
                    + string.digits)
               for i in range(length))
    output.put(rand_str)

#setup a list of processes to run
processes = [mp.Process(target=rand_string, args=(5, output)) for x in range(4)]

#run processes
for p in processes:
	p.start()

#Exit the completed processes
for p in processes:
	p.join()

#Get process results from the output queue
results = [output.get() for p in processes]

print(results)
