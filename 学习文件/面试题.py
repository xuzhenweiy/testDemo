'''
输入：JSON {"a":"aa","b":"bb","c":{"d":"dd","e":"ee"}}
输出：字典 {'a': 'aa', 'b': 'bb', 'd': 'dd', 'e': 'ee'}
'''


def Json():

    dict_data = {"a":"aa","b":"bb","c":{"d":"dd","e":"ee"}}

    dict_data2 = {}

    for k,v in dict_data.items():
        if k == 'c':
            for k,v in v.items():
                dict_data2[k] = v

        dict_data2[k] = v

    return dict_data2



'''
    4、有一个列表，每个元素存放学生姓名、成绩，按学生成绩从优到差排序。
    ['张三:20','李四:70','王五:88','李六:40','王吉:55.5',]
'''

def sort():

    stu = ['张三:20','李四:70','王五:88','李六:40','王吉:55.5',]
    list_stu = []
    dict_stu = {}

    for i in stu:
        s = i.split(':')
        for k in s:
            list_stu.append(k)

    for j in range(0,len(list_stu),2):
        dict_stu[list_stu[j]] = list_stu[j+1]

        dict2 = sorted(dict_stu.items(), key=lambda item:item[1],reverse=True)

    return dict2


'''
将102张卡片打乱并且打乱后保证不在原位置
'''


def random_num():

    import random

    nums = [1,2,3]
    a = nums[:]
    random.shuffle(nums)
    for i in range(len(nums)-1):
        if a[i]==nums[i]:

            nums[i],nums[i+1] =nums[i+1],nums[i]

        elif a[len(nums)-1]==nums[len(nums)-1]:
            nums[len(nums)-1],nums[0] = nums[0],nums[len(nums)-1]


        else:
            pass

    print(a)
    return nums



if __name__ == '__main__':
    result = random_num()
    print(result)