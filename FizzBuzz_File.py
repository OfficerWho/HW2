
import numpy as np

def FizzBuzz(start,finish):
    num = np.arange(start,finish+1)
    obj = np.array(num,dtype=object)

    fizz = num % 3 == 0
    buzz = num % 5 == 0
    fizzbuzz = num % 15 == 0

    obj[fizz] = 'fizz'
    obj[buzz] = 'buzz'
    obj[fizzbuzz] = 'fizzbuzz'

    return(obj)

