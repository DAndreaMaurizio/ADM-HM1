#Say "Hello, World!" With Python
print("Hello, World!")



#Python If-Else
n=input("Write an integer number 1<=n<=100: ")
n=int(n)
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n > 1 and n < 6:
    print("Not Weird")
elif n % 2 == 0 and n > 5 and n < 21:
    print("Weird")
else:
    print("Not Weird")



#Arithmetic Operators
a = int(input())
b = int(input())
print(a+b)
print(a-b)
print(a*b)



#Python: Division
a = int(input())
b = int(input())
print(a//b)
print(a/b)



#Loops
N=int(input())
for i in range(N):
    print(i*i)
    
 
    
#Write a function
#Control if a year is a leap year
def is_leap(year):
    leap = False
    if year % 4 == 0 and year % 100 != 0:
       leap = True
    elif year % 4 == 0 and year % 400 == 0:
       leap = True
   
    return leap

year = int(input())
print(is_leap(year))



#Print Function
n = int(input())
for i in range(1,n+1):
    print(i, end='') #don't change line after print



#List Comprehensions
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([ [i,j,k] for i in range(x+1) for j in range (y+1) for k in range(z+1) if( (i+j+k)!=n)] )    



#Find the Runner-Up Score!
n = int(input())
A=list(map(int, input().split())) 
A=list(set(A)) #remove multiple occurrences
A.remove(max(A)) #remove max
print(max(A)) #print the new max that is the initial  runner up score



#Nested Lists
N=int(input())
A=[]
s=[]
for i in range(N):
    name = input()
    score = float(input())
    s.append(score) # list of scores
    A.append([name, score]) # list of the pair name-score
s=list(set(s)) #remove duplicates
s.remove(min(s)) #remove min score
n=[]
for i in A:
    if i[1]==min(s):
        n.append(i[0]) # list of name with second lowest grade
n.sort() #put in alphabetic order the list 
for i in n:
    print(i)



#Finding the percentage
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split() # give first input to name and split other in line
    scores = list(map(float, line)) #build a list with scores that are in the list line
    student_marks[name] = scores # build a dictionary where at the name we associate the list with his marks
query_name = input()
print('%.2f' % float(sum(student_marks[query_name])/3))



#Lists
N = int(input())
lst=[]
for i in range(N):
    command, *line = input().split()
    num=list(map(int, line))
    if command == 'insert':
        lst.insert(num[0], num[1])
    elif command == 'print':
        print(lst)
    elif command == 'remove':
        lst.remove(num[0])
    elif command == 'append':
        lst.append(num[0])
    elif command == 'sort':
        lst.sort()
    elif command == 'pop':
        lst.pop()
    elif command == 'reverse':
        lst.reverse()



#Tuples
n = int(input())
integer_list =tuple(map(int, input().split()))
print(hash(t))



#sWAP cASE
def swap_case(s):
    r=''
    for i in range(len(s)):
        if s[i].islower():
            r=r+s[i].upper()
        elif s[i].isupper():
            r=r+s[i].lower()
        else:
            r=r+s[i]
    return r

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    
    
    
#String Split and Join
def split_and_join(line):
    line=line.split(" ")
    line = "-".join(line)
    return line

line = input()
result = split_and_join(line)
print(result)
    

    
#What's Your Name?    
def print_full_name(a, b):
    print("Hello", first_name, last_name+'!',"! you just delved into python.")

first_name = input()
last_name = input()
print_full_name(first_name, last_name)
    
  
  
#Mutations  
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)
    
    

#String Validators 
s = input()
l=len(s)
result=[False, False, False, False, False]
for i in range(l):
    if s[i].isalnum():
        result[0]=True
    if s[i].isalpha():
        result[1]=True
    if s[i].isdigit():
        result[2]=True
    if s[i].islower():
        result[3]=True
    if s[i].isupper():
        result[4]=True
for i in range(5):
    print(result[i])
    


 #Text Alignment
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    
#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    
#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))



#Text Wrap
import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))#create a list splitting the string in a substring of length  max_width

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)



#Designer Door Mat
N, M=input().split()
N=int(N)
M=int(M)
l1=int((N-1)/2)
x=-1
c='.|.'
# Top 
for i in range(l1):
    x=x+2
    l2=int((M-3*x)/2)
    print(('-'*l2) + c*x + ('-'*l2))
#Middle
l2=int((M-7)/2)
print(('-'*l2) + 'WELCOME' + ('-'*l2))
#Bottom
for i in range(l1):
    l2=int((M-3*x)/2)
    print(('-'*l2) + c*x + ('-'*l2))
    x=x-2
   
fptr=open()
s=input()
a=s.split()
result=''
b=[]
for i in range(len(a)):
    b.append(a[i].capitalize())
    result=result+b[i]+' '
print(result)



#Introduction to Sets
def average(array):
    s=set(array)
    result=sum(s)/len(s)
    return result

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)



#No Idea!
n, m = input().split()
N=list(map(int, input().split()))
A=set(map(int, input().split()))
B=set(map(int, input().split()))
happiness=0
for i in N:
    if i in A:
        happiness=happiness+1
    if i in B:
        happiness=happiness-1
print(happiness)


#Set .add()
n=int(input())
s=set()
for i in range(n):
    s.add(input())
print(len(s))



#Set .discard(), .remove() & .pop()

n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command, *line = input().split()
    num=list(map(int, line))
    if command == 'discard':
        s.discard(num[0])
    elif command == 'remove':
        s.remove(num[0])
    elif command == 'pop':
        s.pop()
print(sum(s))



#Set .union() Operation
n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))

print(len(A.union(B)))



#Set .intersection() Operation
n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))
print(len(A.intersection(B)))



#Set .difference() Operation
n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))
print(len(A.difference(B)))



#Set .symmetric_difference() Operation
n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = set(map(int, input().split()))
print(len(A.symmetric_difference(B)))



#Set Mutations
n = int(input())
A = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command, *line = input().split()
    B= set(map(int, input().split()))
    if command == 'update':
        A.update(B)
    elif command == 'intersection_update':
        A.intersection_update(B)
    elif command == 'difference_update':
        A.difference_update(B)
    elif command == 'symmetric_difference_update':
        A.symmetric_difference_update(B)
print(sum(A))



#Symmetric Difference
n = int(input())
A = set(map(int, input().split(' ',n)))
m = int (input())
B = set(map(int, input().split(' ',m)))
A.symmetric_difference_update(B)
lst=list(A)
lst.sort()
for i in lst:
    print(i)



#Check Subset
T = int(input())
for i in range(T):
    n = int(input())
    A = set(map(int, input().split(' ', n)))
    m = int(input())
    B = set(map(int, input().split(' ', m)))
    if B.intersection(A) == A:
        print(True)
    else:
        print(False)



#Check Strict Superset
        A = set(map(int, input().split()))
n = int(input())
x = True
for i in range(n):
    B = set(map(int, input().split()))
    if A.intersection(B) != B or A.difference(B) == set():
        x = False
        break #breack because I found a set the is not a strict subset
print(x)



#The Captain's Room
K=int(input())
A=list(map(int,input().split())) 
B=set(A) #set of rooms
C=set()
#I scroll the list if the element is at its first occurence i put it in set C 
#if it is not the first occurrence then it is not the captain's room and I remove it from the set of rooms 
for i in A:
    if i in C:
        B.difference_update(set([i])) 
    else:
        C.add(i)
print(list(B)[0])



#Capitalize!
s=input().strip()
s=s.capitalize()
result=s[0] #the final string
for i in range(1,len(s)):
    if s[i].isalnum() and s[i-1] == ' ':
        result=result+s[i].capitalize()
    else:
        result=result+s[i]

print(result)



#Find a string
def count_substring(string, sub_string):
    count=0
    #I control all the substring with lenght = lenght of input substring and I count  how many are equal
    for i in range(len(string)-len(sub_string)+1):
        if string[i:i+len(sub_string)] == sub_string:
            count=count+1
    return count

string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)



#String Formatting
def print_formatted(n):
    w = len(str(bin(n)).replace('0b','')) #it is the longest binary number
    for i in range(1,n+1):
        a=oct(i)
        b=hex(i).upper() #default lower case
        c=bin(i)
        
        print(str(i).rjust(w, ' '), a[2:].rjust(w, ' '), b[2:].rjust(w, ' '), c[2:].rjust(w, ' '))

n = int(input())
print_formatted(n)



#Alphabet Rangoli
def print_rangoli(size):
    a='abcdefghijklmnopqrstuvwxyz'
    l=4*size-3 #widht of rectangle
    s=''
    A=[]#A[i] i-th line of rectangle
    j=0
    #Top
    for i in range (size-1,0,-1):
        s=s+'-'+a[i]
        r=s+s[len(s)-2::-1]
        A.append('-'*int((l-len(r))/2)+r+'-'*int((l-len(r))/2))#I add - to the ends
        print(A[j])
        j=j+1
    #Middle
    s=s+'-'+a[0]
    r=s+s[len(s)-2::-1]
    print(r[1:(len(r)-1)])
    #Bottom print in reverse the top 
    for i in range(len(A)-1,-1,-1):
        print(A[i])

n = int(input())
print_rangoli(n)


#Merge the Tools!
def merge_the_tools(string, k):
    m = int(len(string)/k)
    for i in range(m):
        s=''
        for j in range(i*k,(i+1)*k):
            if not(string[j] in s):
                s=s+string[j]
        print(s)
        
string, k = input(), int(input())
merge_the_tools(string, k)



#collections.Counter()
from collections import Counter
X = int(input())
A = Counter(list(map(int, input().split(' ', X-1))))
N = int(input())
earn=0
for i in range(N):
    x, y = input().split(' ', 1)
    x=int(x)
    y=int(y)
    if A[x]>0:
        earn=earn+y
        A[x]=A[x]-1
print(earn)




#DefaultDict Tutorial
#I create a default dictionary where the values of each key is a vector with the position of the occurence
from collections import defaultdict
n, m = map(int, input().split(' ', 1))
d=defaultdict(list)
B=[]
for i in range(n):
    d[input()].append(i+1)
for i in range(m):
    B.append(input())
for i in B:
    if d[i] == []:
        print(-1)
    else:
        s=' '.join(d[i])
        print(s)


#Collections.namedtuple()
from collections import namedtuple
N=int(input())
student=namedtuple('student', input())
sm=0
for i in range(N):
    x=input().split()
    s=student(x[0],x[1],x[2],x[3])
    sm=sm+int(s.MARKS)
print('%.2f' % float(sm/N))



#Collections.OrderedDict()
from collections import OrderedDict
N = int(input())
ordinary_dictionary = OrderedDict()
for _ in range(N):
    item, price = input().rsplit(' ', 1)
    if item in ordinary_dictionary:
        ordinary_dictionary[item] +=  int(price) 
    else:
        ordinary_dictionary[item] =  int(price)
for i in ordinary_dictionary:
    print(i, ordinary_dictionary[i])


#Word Order
from collections import OrderedDict
N = int(input())
ordinary_dictionary = OrderedDict()
for _ in range(N):
    word = input()
    if word in ordinary_dictionary:
        ordinary_dictionary[word] += 1 
    else:
        ordinary_dictionary[word] =  1
print(len(ordinary_dictionary))
for i in ordinary_dictionary:
    print(ordinary_dictionary[i],end=' ') 



#Collections.deque()
from collections import deque
N = int(input())
d=deque()
for i in range(N):
    command, *line = input().split()
    value=list(line)
    if command == 'append':
        d.append(value[0])
    if command == 'appendleft':
        d.appendleft(value[0])
    if command == 'pop':
        d.pop()
    if command == 'popleft':
        d.popleft()
print(' '.join(d))



#Piling Up!
from collections import deque
T = int(input())
for i in range(T):
    n = int(input())
    List=list(map(int, input().split(' ', n-1)))
    d=deque(List)
    a=max(d)
    for j in range(len(List)):
        if d[0]>=d[len(d)-1] and d[0]<=a:
            a=d.popleft()
        elif d[0]<d[len(d)-1] and d[len(d)-1]<=a:
            a=d.pop()
        else:
            print('No')
            break
    if j == len(List)-1: #enter only if i complete the previous loop
        print('Yes')


#Company Logo
from collections import *
s = list(deque(input().strip()))
s.sort() #sort the list because in case of the same number of occurences i print in alphabetic order
d=Counter(s).most_common(3)
for i in d:
    print(i[0], i[1])       


#Calendar Module
import calendar
day=list(map(int, input().split(' ', 2)))
x=calendar.weekday(day[2], day[0], day[1])
if x==0:
    print('MONDAY')
elif x==1:
    print('TUESDAY')
elif x==2:
    print('WEDNESDAY')
elif x==3:
    print('THURSDAY')
elif x==4:
    print('FRIDAY')
elif x==5:
    print('SATURDAY')
else:
    print('SUNDAY')




#The Minion Game
#Consider string s and i=0,1.. the position on the string. len(s)-i is the number of word that i can write strating from s[i] so its also the score of the player    
def minion_game(string):
    vowel='AEIOU'
    Stuart=0
    Kevin=0
    for i in range(len(string)):
        if string[i] in vowel:
            Kevin = Kevin + (len(string) - i)
        else:
            Stuart = Stuart + (len(string) - i)
    if Kevin > Stuart:
        print('Kevin', Kevin)
    elif Stuart > Kevin:
        print('Stuart', Stuart)
    else:
        print('Draw')
    return 
s = input()
minion_game(s)

#Time Delta
import math
import os
import random
import re
import sys
from datetime import datetime 

def time_delta(t1, t2):
    x=datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
    y=datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
    t=abs(x-y)
    return t
t = int(input())
for t_itr in range(t):
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)
    print(int(delta.total_seconds())) #covert the difference in second   
    
    

#Exceptions
T = int(input())
for i in range(T):
   a, b = input().split(' ', 1)

   try:
    print(int(a)//int(b))
   except ZeroDivisionError as e:
    print("Error Code:",e)
   except ValueError as e:
    print("Error Code:",e)
    

#Athlete Sort  
import math
import os
import random
import re
import sys


n, m = input().split(' ', 1)
n = int(n)
m = int(m)
L = []
for _ in range(n):
    L.append(list(map(int, input().rstrip().split())))
k = int(input())
L.sort(key=lambda x: x[k])
for i in range(len(L)):
    for j in range(len(L[i])): #trasform in string to use join
        L[i][j]=str(L[i][j])
    print(' '.join(L[i]))
    

#ginortS  
S=input().strip()
l=''
L=''
nodd=''
neven=''
lst=[]
#split string S in string l, L , n where l contains only lower case, L contains only upper case and n contains only numbers
for i in range(len(S)):
    if S[i].islower():
        l+=S[i]
    elif S[i].isupper():
        L+=S[i]
    elif S[i].isdigit() and int(S[i])%2==1:
        nodd+=S[i]
    else:
        neven+=S[i]

lst.extend(l) #list of characters of l
lst.sort() 
l=''.join(lst)
lst.clear()

lst.extend(L)
lst.sort()
l=l+''.join(lst)
lst.clear()

lst.extend(nodd)
lst.sort()
l=l+''.join(lst)
lst.clear()

lst.extend(neven)
lst.sort()
l=l+''.join(lst)

print(l)  



#Zipped!
N, X = input().split()
N=int(N)
X=int(X)
score=[]
for i in range(X):
    L=list(map(float, input().split(' ',N-1))) # List of students' scores in a particular subject
    score.append(L)
T=tuple(zip(*score))
for i in range(len(T)):
    print(sum(T[i])/X) 
    
    

#Map and Lambda Function 
cube = lambda x: x*x*x  

def fibonacci(n):
    if n==0:
        return []
    elif n==1:
        return [0]
    else:
        L=[0,1]
        for i in range(2,n):
            L.append(L[i-2]+L[i-1])
        return L
n = int(input())
print(list(map(cube, fibonacci(n))))
    
    


#Detect Floating Point Number
def Fun(N):
    if len(N)==1:#Control if ther is at least one decimal number
        return False
    if not(N[0].isnumeric()) and N[0]!='+' and N[0]!='-' and N[0]!='.':#Control if the string starts with valid Character
        return False
    cont=0 #Number of . in the string
    if N[0]=='.':
        cont=1
    for i in range(1,len(N)):
        if not(N[i].isnumeric()) and N[i]!='.':
            return False
        elif N[i]=='.' and cont==1:#there are more than 1 .
            return False
        elif N[i]=='.' and cont==0:
            cont=1
            if i==len(N)-1:# there is not decimal numbers
                return False
    return True


T=int(input())
for i in range(T):
    N=input()
    print(Fun(N)) 
    

#Re.split()    
regex_pattern = r"\D"  
print("\n".join(re.split(regex_pattern, input())))  
    


#Group(), Groups() & Groupdict()
def Fun(S):
    for i in range(len(S)-1):
        if S[i]==S[i+1] and S[i].isalnum():
            return S[i]
    return -1

print(Fun(input()))



#Arrays
import numpy
def arrays(arr):
    arr.reverse()
    return numpy.array(arr,float)

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


#Shape and Reshape
import numpy
print(numpy.reshape(list(map(int, input().split(' ', 8))),(3,3)))



#Transpose and Flatten
import numpy
N, M = input().split(' ', 1)
N=int(N)
M=int(M)
lst=[]
for i in range(N):
    lst.append(list(map(int, input().split(' ', M-1))))
arr=numpy.array(lst)
print(numpy.transpose(arr))
print(arr.flatten())


#Concatenate
import numpy
N, M, P = input().split(' ', 2)
N=int(N)
M=int(M)
P=int(P)
lst=[]
for i in range(N):
    lst.append(list(map(int, input().split(' ', P-1))))

A=numpy.array(lst)
lst.clear()

for i in range(M):
    lst.append(list(map(int, input().split(' ', P-1))))
B=numpy.array(lst)

print(numpy.concatenate((A,B), axis=0))



#Zeros and Ones
import numpy
x=tuple(map(int, input().split()))
print(numpy.zeros(x, dtype=numpy.int))
print(numpy.ones(x, dtype=numpy.int))


#Eye and Identity
import numpy
N, M = input().split(' ', 1)
N=int(N)
M=int(M)
numpy.set_printoptions(sign=' ')  # I see this in discussion but it is only a problem of test case format
print(numpy.eye(N, M, k=0))


#Array Mathematics
import numpy
N, M = input().split(' ', 1)
N=int(N)
M=int(M)
lst=[]
for i in range(N):
    lst.append(list(map(int, input().split(' ',M-1))))
arr1=numpy.array(lst)
lst.clear()
for i in range(N):
    lst.append(list(map(int, input().split(' ',M-1))))
arr2=numpy.array(lst)
print(arr1+arr2)
print(arr1-arr2)
print(arr1*arr2)
print(arr1//arr2)
print(arr1%arr2)
print(arr1**arr2)



#Floor, Ceil and Rint
import numpy
numpy.set_printoptions(sign=' ')
arr=numpy.array(list(map(float, input().split())))
print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))



#Sum and Prod
import numpy

N, M = input().split(' ', 1)
N=int(N)
M=int(M)
lst=[]
for i in range(N):
    lst.append(list(map(int, input().split(' ',M-1))))
arr=numpy.array(lst)
print(numpy.prod(numpy.sum(arr, axis=0)))



#Min and Max
import numpy
N, M = input().split(' ', 1)
N=int(N)
M=int(M)
lst=[]
for i in range(N):
    lst.append(list(map(int, input().split(' ',M-1))))
arr=numpy.array(lst)
print(numpy.max(numpy.min(arr, axis=1)))


#Mean, Var, and Std
import numpy
N, M = input().split(' ', 1)
N=int(N)
M=int(M)
lst=[]
numpy.set_printoptions(legacy='1.13')
for i in range(N):
    lst.append(list(map(int, input().split(' ',M-1))))
arr=numpy.array(lst)
print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.std(arr))


#Dot and Cross
import numpy
N= int(input())
lst=[]
for i in range(N):
    lst.append(list(map(int, input().split(' ',N-1))))
arr1=numpy.array(lst)
lst.clear()
for i in range(N):
    lst.append(list(map(int, input().split(' ',N-1))))
arr2=numpy.array(lst)
print(numpy.dot(arr1,arr2))



#Inner and Outer
import numpy

arr1=numpy.array(list(map(int, input().split())))
arr2=numpy.array(list(map(int, input().split())))
print(numpy.inner(arr1,arr2))
print(numpy.outer(arr1,arr2))


#Polynomials
import numpy
P=list(map(float, input().split()))
x=float(input())
print(numpy.polyval(P, x))


#Linear Algebra
import numpy
N= int(input())
lst=[]
numpy.set_printoptions(legacy='1.13')
for i in range(N):
    lst.append(list(map(float, input().split(' ',N-1))))
arr=numpy.array(lst)
print(numpy.linalg.det(lst))



#Re.findall() & Re.finditer()
# I create a list with findall such that each component is a substring as described in the exercise. After I print each element of the list. If the list is empty print -1
import re
vowels='AEIOUaeiou'
consonant='QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
S=input()
x=True
A=re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})+[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]', S)
#print(A)
for i in A:
    print(i)
    x=False
if x:
    print(-1)
 


#Re.start() & Re.end()
import re
s=input()
k=input()
x=True
for i in range(len(s)):
    if re.match(k, s[i:])!=None:
        m=re.match(k, s[i:])
        print(tuple([i,i+m.end()-1]))
        x=False
if x:
    print(tuple([-1,-1]))
    

#Regex Substitution
import re
#I create a list where each component is a line of the input text. I use '\n'.join to create a string with the imput text. Finally use re.sub for the replacement
N=int(input())
lst=[]
for i in range(N):
    lst.append(input())
s='\n'.join(lst)
s=re.sub(r"(?<=\s)(&&)(?=\s)", lambda x: 'and', s)
print(re.sub(r"(?<=\s)(\|\|)(?=\s)", lambda x: 'or', s))
    



#Validating phone numbers
N=int(input())
valid='987'
for i in range(N):
    s=input().strip().split() #this line of code and the following remove spaces because 987 51 07 655 is a tel number
    s=''.join(s) 
    if s.isnumeric() and (s[0] in valid) and len(s)==10:
        print('YES')
    else:
        print('NO') 
        
#Validating and Parsing Email Addresses
import re
import email.utils
n=int(input())
for i in range(n):
    s=email.utils.parseaddr(input())
    if re.search(r'[\w\.\_]+@[a-zA-Z]+\.[a-zA-Z]+', s[1])!= None:
        v=re.split(r'[\.]', s[1])
        if len(v[len(v)-1])<=3 and s[1][0].isalpha() and ('@' in v[len(v)-2]) and (v[len(v)-1].isalnum()):
            print(email.utils.formataddr(s))
            
            
#Birthday Cake Candles
import math
import os
import random
import re
import sys
def birthdayCakeCandles(ar):
    m=max(ar)
    x=Counter(ar)
    return x[m]

from collections import Counter
ar_count = int(input())
ar = list(map(int, input().rstrip().split()))
print(birthdayCakeCandles(ar))




#Kangaroo
import math
import os
import random
import re
import sys


def kangaroo(x1, v1, x2, v2):
    if x1-x2==0: #kangaroos start at the same point (jump 0 they meet)
        return 'Yes'
    elif x2-x1>0 and v2-v1>=0: #kangaroo 2 is in vantage and jump more
        return 'NO'
    elif x2-x1>0 and v2-v1<0: #kangaroo 2 is in vantage but jump les
        if (x2-x1)%(v1-v2)==0: #difference of jumps is proportional to the distance between the two kangaroos at the beginning so they meet
            return 'YES'
        else:
            return 'NO'
    elif x2-x1<0 and v2-v1<=0:
            return 'NO'
    else:
        if (x1-x2)%(v2-v1)==0:
            return 'YES'
        else:
            return 'NO'
    
    return
x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
print(kangaroo(x1, v1, x2, v2))





#Viral Advertising
import math
import os
import random
import re
import sys

def viralAdvertising(n):
    shared=5
    tot=0
    for i in range(n):
        like=math.floor(shared/2)
        tot+= like
        shared= like * 3
    return tot

n = int(input())
print(viralAdvertising(n))


#Recursive Digit Sum
import math
import os
import random
import re
import sys

# I use a recursive function.
def superDigit(n, k):
    if len(n)==1:
        return int(n)*k
    else:
        s=0
        for i in range(len(n)): #sum the number of the string
            s+=int(n[i])
        return superDigit(str(s),1)*k
    
nk = input().split()
n = nk[0]
k = int(nk[1])
print(superDigit(str(superDigit(n,k)), 1))



#Insertion Sort - Part 1
import math
import os
import random
import re
import sys

def insertionSort1(n, arr):
    i=n-1
    x=arr[i]
    while i>0 and arr[i-1]>x:
        arr[i]=arr[i-1]
        print(' '.join(map(str,arr)))
        i=i-1
    arr[i]=x
    print(' '.join(map(str,arr)))
    return

n = int(input())
arr = list(map(int, input().rstrip().split()))
insertionSort1(n, arr)


#Insertion Sort - Part 2
import math
import os
import random
import re
import sys

# I use the InsertionSort1 created in the previous exercise iteratively for the first k element with k=2,...,n
def insertionSort1(n, arr):
    i=n-1
    x=arr[i]
    while i>0 and arr[i-1]>x:
        arr[i]=arr[i-1]
        i=i-1
    arr[i]=x
    print(' '.join(map(str,arr)))
    return

def insertionSort2(n, arr):
    for i in range(1,n):
        insertionSort1(i+1, arr)
    return

n = int(input())
arr = list(map(int, input().rstrip().split()))
insertionSort2(n, arr)




#Hex Color Code

import re
n=int(input())
x=False # need to know if the line is a selector (False=selector)
for i in range(n):
    s=input()
    if '{'in s:
        x=True
    elif '}'in s:
        x=False
    elif x:
        lst=re.findall(r'[\#][a-fA-F0-9]+',s) #I use findall to create a list where each componente is a valid CSS colors
        for y in lst:
            if len(y)<8 and len(y)>3:
                print(y)
                


#HTML Parser - Part 1
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):# I create a class as describet in the exercise
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for x in attrs:
            print('->',x[0],'>',x[1])
    def handle_endtag(self, tag):
        print("End   :",tag)
    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for x in attrs:
            print('->',x[0],'>',x[1])

n=int(input())
s=''
for i in range(n): #join in a single string the HTML input code
    s+= input().strip()

parser = MyHTMLParser()
parser.feed(s)             
                


#HTML Parser - Part 2
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        LineNumber=len(data.split('\n',))
        if LineNumber==1:
            print('>>> Single-line Comment')
        else:
            print('>>> Multi-line Comment')
        if data.strip():
            print(data)
    def handle_data(self, data):
        if data.strip():
            print('>>> Data')
            print(data)

  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()



#Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser
class MyHTMLParser(HTMLParser):# I create a class as describet in the exercise
    def handle_starttag(self, tag, attrs):
        print(tag)
        for x in attrs:
            print('->',x[0],'>',x[1])
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for x in attrs:
            print('->',x[0],'>',x[1])

n=int(input())
s=''
for i in range(n): #join in a single string the HTML input code
    s+= input().strip()
parser = MyHTMLParser()
parser.feed(s)



#Validating UID
def UpChar(s):
    cont=0
    for i in range(10):
        if s[i].isupper():
            cont+=1
    if cont<2:
        return False
    else:
        return True
# This function return True if the number of digits in s is at least 3. False otherwise
def dig(s):
    cont=0
    for i in range(10):
        if s[i].isnumeric():
            cont+=1
    if cont<3:
        return False
    else:
        return True
#This function return False if there are repeated characters. True otherwise.
def rep(s):
    lst=[]
    lst.extend(s)
    cont=Counter(lst).values()
    if max(cont)>1:
        return False
    else:
        return True


from collections import Counter
T=int(input())
for i in range(T):
    UID=input().strip()
    if(len(UID)==10 and UID.isalnum()and UpChar(UID) and dig(UID) and rep(UID)):
        print('Valid')
    else:
        print('Invalid')
        
        

#Validating Credit Card Numbers
def dig(s):
    #control if the credit card number has only 16 digits
    if len(s)==16 and s.isnumeric():
        return True
    # control if credit card number has digits in groups of , separated by one hyphen "-"
    elif len(s)==19 and s[4]=='-' and s[9]=='-' and s[14]=='-': 
        s=''.join(s.split('-',))
        if s.isnumeric():
            return True
        else:
            return False
    else:
        return False    
#control if credit card number has 4 or more consecutive repeated digits
def rep(s):
    cont=1
    s=''.join(s.split('-',))
    for i in range(1,16):
        if s[i]==s[i-1]:
            cont+=1
        else:
            cont=1
        if cont == 4:
            return False
    return True


n=int(input())
for i in range(n):
    num=input().strip() #Credit Card Number
    if (num[0] in '456') and dig(num) and rep(num):
        print('Valid')
    else:
        print('Invalid')
        
        
        
#Validating Postal Codes
regex_integer_in_range = r"[1-9][\d]{5}$"	
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	
import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)



#Matrix Script
import math
import os
import random
import re
import sys
import re
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
lst=[]
matrix = []
#I create the matrix as described in the exercise 
for _ in range(n):
    lst.extend(input())
    matrix.append(lst)
    lst=[]
T=tuple(zip(*matrix))

s=''
for i in range(m):#find the decoded script
    s+=''.join(list(T[i]))

#I use re.sub to replace symbols or spaces between two alphanumeric characters of the decoded script with a single space.
print(re.sub(r'(?<=[A-Za-z0-9])([^A-Za-z0-9]+)(?=[A-Za-z0-9])', lambda x: ' ', s))



#Validating Roman Numerals
#(M{0,3})= M can appear from 0 to 3 times, (C[MD]|D?C{0,3}) C can appear one time before M,D or after D from 0 to 3 times, the same for the other part of code
regex_pattern = r"(M{0,3})(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$"
import re
print(str(bool(re.match(regex_pattern, input()))))



#XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree
def get_attr_number(node):
    cont=0
    for x in node.iter():
        cont+=len(x.attrib)
    return cont

sys.stdin.readline()
xml = sys.stdin.read()
tree = etree.ElementTree(etree.fromstring(xml))
root = tree.getroot()
print(get_attr_number(root))



#XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree
maxdepth = 0
def depth(elem, level):
    global maxdepth
    level += 1
    if level >= maxdepth:
        maxdepth = level
    for child in elem:
        depth(child, level)
n = int(input())
xml = ""
for i in range(n):
    xml =  xml + input() + "\n"
tree = etree.ElementTree(etree.fromstring(xml))
depth(tree.getroot(), -1)
print(maxdepth)

