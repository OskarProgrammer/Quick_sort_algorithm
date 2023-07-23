import random

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        index = random.randint(0,len(array)-1)  #pivot in the random place of the array
        # index = len(array)//2  -- pivot in the half of the array
        # both variations has got speed of the algorithm O(n * log(n))

        less = [i for i in array[0:index] if i <= array[index]] + [i for i in array[index+1:] if i <= array[index]]

        greater = [i for i in array[0:index] if i > array[index]] + [i for i in array[index+1:] if i > array[index]]

        return quickSort(less) + [array[index]] + quickSort(greater)

print(quickSort([1,5,1,2,3,4,10,4,100,99]))