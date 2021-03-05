import time


#封装装饰器
def display_time(func):
    def wrapper(*args):
        t1 = time.time()
        #执行函数  有参数传入使用 *args
        result = func(*args)
        t2 = time.time()
        print("Total time:{:.4}".format(t2-t1))

        #return给wrapper
        return result

    # return给func函数
    return wrapper

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        return True


#使用装饰器
@display_time
def prime_nums(nums):
    count = 0
    for i in range(2,nums):
        if is_prime(i):
            count = count+1

    return count


count = prime_nums(10000)
print(count)
