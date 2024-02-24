# -*- coding: utf-8 -*-
"""Task4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12L-2jUx0iufW0QOpYy0uMTNwU9XEExWg
"""

#task4
input_file = open("/content/drive/MyDrive/bracU/5th semester/CSE221/LAB/Lab02/input4.txt","r")
output_file =open("/content/drive/MyDrive/bracU/5th semester/CSE221/LAB/Lab02/output4.txt","w")
T = input_file.readline().split()
N= int(T[0])
p= int(T[1])
person = [0]*p

start =[]
end = []

count=0

for line in input_file:
  temp = line.split()
  start.append(int(temp[0]))
  end.append(int(temp[1]))

for i in range(N):
  for j in range(i+1,N):
    if end[i] > end[j] :
      end[i],end[j] =end[j],end[i]
      start[i],start[j]=start[j],start[i]

for i in range(N):
  person.sort(reverse=True)
  for j in range(p):

    if start[i] >= person[j]:
      person[j] = end[i]
      count+=1
      break


output_file.write(f'{count}')
input_file.close()
output_file.close()