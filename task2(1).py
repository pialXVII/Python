# -*- coding: utf-8 -*-
"""Task2(1)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12L-2jUx0iufW0QOpYy0uMTNwU9XEExWg
"""

#Task2(1)

def merge(a, b):
  i,j=0,0
  sort=[]
  while i< len(a) and j < len(b):
    if a[i]> b[j]:
      sort.append(b[j])
      j+=1

    else:
      sort.append(a[i])
      i+=1

  if i< len(a):
    sort.extend(a[i::])
  elif j < len(b):
    sort.extend(b[j::])

  return sort


def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  else:
    mid = len(arr)//2
    a1 = mergeSort(arr[0:mid]) # write the parameter
    a2 = mergeSort(arr[mid:len(arr)]) # write the parameter
    return merge(a1, a2)


input_file = open("/content/drive/MyDrive/bracU/5th semester/CSE221/LAB/Lab02/input2(1).txt","r")
output_file =open("/content/drive/MyDrive/bracU/5th semester/CSE221/LAB/Lab02/output2(1).txt","w")
N = int(input_file.readline())
Nlst = list(map(int,input_file.readline().split()))
M = int(input_file.readline())
Mlst = list(map(int,input_file.readline().split()))
lst = Nlst + Mlst
x= mergeSort(lst)
lst = list(map(str,x))
output_file.write(f"{' '.join(lst)}")
input_file.close()
output_file.close()