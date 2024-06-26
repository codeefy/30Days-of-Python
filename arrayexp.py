"""# reverse the array and convert it into float array using numpy 

import numpy

def arrays(arr):  #arr is a list of integers separated by space  
    # complete this function
    # use numpy.array
    arr = list(map(float, arr)) #convert the list of integers to a list of floats  
    arr.reverse() #reverse the list of floats 
    
    return numpy.array(arr, float) #return the reversed list of floats as a numpy array of floats 

arr = input().strip().split(' ') #input is a list of integers separated by space    
result = arrays(arr)
print(result)"""

import numpy

my_array = numpy.array([[2, 5], 
                        [3, 7],
                        [1, 3],
                        [4, 0]])

print(numpy.min(my_array, axis = 0)) # it will print the minimum value of each column in the array 
# axis = 0 means column wise operation 
#axis = 1 means row wise operation
#print(my_array)
print(numpy.min(my_array, axis = 1))    # it will print the minimum value of each row in the array     
print(numpy.min(my_array, axis = None)) # it will print the minimum value of the entire array 
print(numpy.min(my_array)) # it will print the minimum value of the entire array 