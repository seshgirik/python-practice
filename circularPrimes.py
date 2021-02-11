# Enter your code here. Read input from STDIN. Print output to STDOUT
set_primes = set()


def combinations(nums):
    size = len(nums)
    orig_nums = int(nums)
    for i in range(size):
        list1 = [i for i in nums]
        list1.append(list1.pop(0))
        circular_no = ''.join(list1)
        # print(f'{circular_no} is {prime(int(circular_no)) }')
        if int(circular_no) < orig_nums and int(circular_no) not in set_primes:
            print(f'false {orig_nums} {circular_no} ')
            return False

        elif not prime(int(circular_no)):
            return False
        nums = list1
    return True


def prime(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    set_primes.add(n)
    print(set_primes)
    return True

# N= 100
N = input()
# print(N)
even = ['2', '4', '5', '6', '8', '0']

sum = 7
flag = 0
for num in range(2, int(N)):
    flag = 0
    for element in even:
        if str(num).__contains__(element):
            # print(element)
            flag = 1
            break
    if flag:
        continue
    if not prime(num):
        continue
    if combinations(str(num)):
        # print(num)
        sum += num
print(sum)


