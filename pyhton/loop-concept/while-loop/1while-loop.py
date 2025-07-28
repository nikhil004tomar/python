# Question.no.1: print all 1 to 100 number using while loop 
i=1
while i<=100:
    print("1 to 100 number are priint using while loop:", i)
    i+=1
    print("the first questio us end here")

# question.no2: print all 100 to 1 number using while loop
i=100
while i>=1:
    print("the all number are in reverse formate using while loop:" ,i)
    i-=1
    print("th second question is end here")

# question.no3: print hte multiplecation of table of number n

n=int (input("enter the number:"))
i=1
while i<=10:
    mul=n*i
    print("tne multiplication of number:",mul)
    i+=1
print("the questin 3 is end here ")

# question.no4: print the elemet of the following list using while loop[1,4,9,16,225,36,49,64,81,100]
nums=[1,4,9,16,225,36,49,64,81,100]
idx=0
while idx<len(nums):
    print("the length of array: " ,nums[idx])
    idx+=1
print("the end of question:4 here.")    

# question.no.4: search for a number x in this tuple (1,4,9,16,225,36,49,64,81,100)
nums=(1,4,9,16,225,36,49,64,81,100)
x=16
idx=0
while idx<len(nums):
     if (nums[idx]==x):
      print("the length of array: " ,idx)
     idx+=1
print("the end of question:5 here.")         