# Hello World program in Python
    



a=[7,2,4,1,5,3]
#a=[1,2,3,4,5]
#a=[5,4,3,2,1]
print (a)

for i in range(1,len(a)):
    print ("i is ", i)
    #print ("\n")
    for j in reversed(range(0,i+1)): ''' To optimize insertion sort, compare element with previous element, to achieve this use j in reversed range as shown above '''
        print ("j is", j)
        if (j>0 and a[j]<a[j-1]):
            temp=a[j]
            a[j]=a[j-1]
            a[j-1]=temp
            print a
        else:
            #pass
            break
'''
('i is ', 4)
('j is', 4)
[1, 2, 4, 5, 7, 3]
('j is', 3)
here j is 3rd index which is 5 , since 5 >4 (previous element) , previous list already in sorted so breaking the j loop

         why break here ?
          breaking j loop, since no need to compare other elements

          if a[j] is not less than a[j-1]) ie previous element is lesser than current element , no need to compare again with previous to previous why becoz its alredy sorted 

[7, 2, 4, 1, 5, 3]
('i is ', 1)
('j is', 1)
[2, 7, 4, 1, 5, 3]
('j is', 0)
[2, 7, 4, 1, 5, 3]
('i is ', 2)
('j is', 2)
[2, 4, 7, 1, 5, 3]
('j is', 1)
[2, 4, 7, 1, 5, 3]
('i is ', 3)
('j is', 3)
[2, 4, 1, 7, 5, 3]
('j is', 2)
[2, 1, 4, 7, 5, 3]
('j is', 1)
[1, 2, 4, 7, 5, 3]
('j is', 0)
[1, 2, 4, 7, 5, 3]
('i is ', 4)
('j is', 4)
[1, 2, 4, 5, 7, 3]
('j is', 3)

[1, 2, 4, 5, 7, 3]
('i is ', 5)
('j is', 5)
[1, 2, 4, 5, 3, 7]
('j is', 4)
[1, 2, 4, 3, 5, 7]
('j is', 3)
[1, 2, 3, 4, 5, 7]
('j is', 2)
[1, 2, 3, 4, 5, 7]
[1, 2, 3, 4, 5, 7]

'''
    print (a)

            
print (a)
        
