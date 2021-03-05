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
    dict_stu = {}

    for i in stu:
        s = i.split(':')
        print(s)

    return dict_stu

if __name__ == '__main__':
    result = sort()
    print(result)