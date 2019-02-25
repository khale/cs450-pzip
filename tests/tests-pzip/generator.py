#!/usr/bin/env python
import os
import sys
import string
import struct
import numpy
def fib(n):
  if n <= 0:
     return []
  if n == 1:
     return [0]
  result = [0, 1]
  if n == 2:
     return result
  for i in xrange(2, n):
     result.append(result[i-1] + result[i-2])
  return result

def calculateSum(n) : 
    if (n <= 0) : 
        return 0
   
    fibo =[0] * (n+1) 
    fibo[1] = 1
   
    # Initialize result 
    sm = fibo[0] + fibo[1] 
   
    # Add remaining terms 
    for i in range(2,n+1) : 
        fibo[i] = fibo[i-1] + fibo[i-2] 
        sm = sm + fibo[i] 
          
    return sm 
  
  
# Driver program to test 
# above function 
def type_into_file(filename):
    times = fib(26)
    alphs = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","m","n","b","g","h","k","j","l","z","x","c","v"]
    for i in xrange(1,26):
        for j  in xrange(1,times[i]):
            filename.write(alphs[i]) 


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit('usage: generate.py <file_size in MB> <output_location>\n example: python generator.py 100 1.in')

    output_size = int(sys.argv[1])
    output = sys.argv[2]

filepath  = output
filename  = open(filepath, "a")
if os.path.exists(filepath):
    while os.path.getsize(filepath) < output_size*1024*1024:
        type_into_file(filename)
