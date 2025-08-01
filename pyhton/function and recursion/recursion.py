# this is the example of recursion in pyhton

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)

# Question.no.1 Factorial
def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)
print(fact(4))


# question.no.2 calculate the sum of n natural number
def calc_sum(n):
    if(n ==0):
        return 0
    return calc_sum(n-1)+n
print(calc_sum(6))
print(calc_sum(7))
print(calc_sum(8))
print(calc_sum(9))