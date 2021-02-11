

nums = [7,1,5,3,6,4]


def combinations(nums):

    size= len(nums)
    for i in range(size):
        list1 = [i for i in nums]
        list1.append(list1.pop(0))
        circular_no= ''.join(list1)
        print(f'{circular_no} is {prime(int(circular_no)) }')

        if prime(int(circular_no)) == "No":
            return "No"
        nums=list1
    return "Yes"


def prime(n):
    flag = 1
    for i in range(2, n - 1):
        if n % i == 0:
            return "No"
    return "Yes"


nums = '67'

combinations(nums)

# N = input()
# print(N)
#
# sum=0
# for num in range(2,int(N)):
#     str1=str(num)
#     if combinations(str1):
#         print(num)

even = ['2','4','6','8','0']
num = '124'
for element in even:
    if num.__contains__(element):
        print(element)