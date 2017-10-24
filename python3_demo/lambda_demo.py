# http://www.cnblogs.com/xumengpiaoyun/archive/2012/12/18/2823058.html 
# 1. 函数格式：
# 　　lambda [parameters]: commands
# 
# 2. 函数功能：
# 　　lambda创建匿名函数，而用def创建的方法是有名称的，它是一个表达式。优点：省去定义函数的过程，不需要考虑命名问题。
# 
# 3. 命令实例：
# 例：直接使用
# 　　print(lambda x:x+1(1)) #输出2，(1)是给x复制
# 例：1个参数
# 　　func1 = lambda x:x*2
# 　　print(func1(3)) #结果为6
# 例：多个参数(可以初始化参数)
# 　　func2 = lambda x,y,z=1: x+y+z
# 　　print(func2(2,3)) #结果为6
# 　　print(func2(2,3,4)) #结果为9
#  

# Main thread
# 可以这样认为,lambda作为一个表达式，定义了一个匿名函数，上例的代码x为入口参数，x+1为函数体。
# 在这里lambda简化了函数定义的书写形式。是代码更为简洁，但是使用函数的定义方式更为直观，易理解。
def main():
    # 例：直接使用
    func0 = lambda x:x + 1
    print(func0(1))  # 输出2，(1)是给x复制
    # 例：1个参数
    func1 = lambda x:x * 2
    print(func1(3))  # 结果为6
    # 例：多个参数(可以初始化参数)
    func2 = lambda x, y, z = 1: x + y + z
    print(func2(2, 3))  # 结果为6
    print(func2(2, 3, 4))  # 结果为9
    func = lambda x:x + 1
    print(func(1))
    # 2
    print(func(2))
    # 3
    
# http://www.cnblogs.com/AlwaysWIN/p/6202320.html
from functools import reduce 
def my_filter():
    foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
    foo2 = [2, 3, 4]
    
    # 取能被3整除的数
    print (list(filter(lambda x: x % 3 == 0, foo)))
    # [18, 9, 24, 12, 27]
    
    # 计算x*2+10
    print (list(map(lambda x: x * 2 + 10, foo)))
    # [14, 46, 28, 54, 44, 58, 26, 34, 64]
    
    # 求和
    print (reduce(lambda x, y: x + y, foo))
    # 139
    
    print (reduce(lambda x, y: x + y, foo2))
    # 9
    # 上面例子中的map的作用，非常简单清晰。但是，Python是否非要使用lambda才能做到这样的简洁程度呢？
    # 在对象遍历处理方面，其实Python的for..in..if语法已经很强大，并且在易读上胜过了lambda。
    # 比如上面map的例子，可以写成:print ([x * 2 + 10 for x in foo]) 非常的简洁，易懂。 　　
    # filter的例子可以写成:print ([x for x in foo if x % 3 == 0]) 同样也是比lambda的方式更容易理解。
    
    # foo3 = ['sh601003', 'sz000816', 'sz000778', 'ss600221']
    foo3 = ['sh601003']
    print(list(filter(lambda s: s[:-6] not in ('sh', 'sz', 's_sh', 's_sz'), foo3)))
    filter_result = list(filter(lambda s: s[:-6] not in ('sh', 'sz', 's_sh', 's_sz'), foo3))
    print(filter_result.__len__())
    for item in filter_result:
        print('item ', item)
    #print('filter_result: ', filter_result.__sizeof__())
    if list(filter(lambda s: s[:-6] not in ('sh', 'sz', 's_sh', 's_sz'), foo3)).__len__() > 0 :
        print('Error')

    s = 'sh601003'
    print(s[:-6])
    
if __name__ == '__main__':
    main()
    my_filter()
