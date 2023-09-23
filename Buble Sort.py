import os



def bubbleSort(array):
    
  for i in range(len(array)):
    swapped = False
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    if not swapped:
      break

data = [123,1,4,1,5,12,1,14,2,5]

bubbleSort(data)

os.system("cls")
print('Sorted Array in Ascending Order:')
print(data)