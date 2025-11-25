# create a 1D and 2D array using list 


import numpy

number = [1,2,3,4,5]
n = numpy.array(number)
print(n)
print(n.shape)


number1 = [[1,2,3,4],[5,6,7,8]]
m = numpy.array(number1)
print(m)
print(m.shape)

# create an array of even numbers from 10 to 50

number3 = numpy.arange(10,51,2)
print(number3)

# create a 1D array of 12 elements then  reshape it into (3,4) matrix

arr = numpy.arange(1,13)
print(arr)
new = arr.reshape(3,4)
print(new)

# find the mean,median,std

print(numpy.mean(arr))
print(numpy.median(arr))
print(numpy.std(arr))

# create two 3*2 matrix and perform addition and multiplication

max1 = numpy.random.randint(1,20,size=(3,2))
max2 = numpy.random.randint(20,40,size=(3,2))
print(max1)
print(max2)

print(f"addition:\n{max1 + max2}")
print(f"multiplication:\n{max1 * max2}")

# create a 3 * 5 matrix and multiply all elements with  2 and extract right corner 2 * 2 submatrix

max1 = numpy.random.randint(1,20,size=(3,5))
result = numpy.array(max1)
print(result)
mul = result * 2
print(mul)
print(mul[0:2,3:])