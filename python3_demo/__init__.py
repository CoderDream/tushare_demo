# http://www.cnblogs.com/xumengpiaoyun/archive/2012/12/18/2823058.html 
# 1.      函数格式：
# 　　lambda [parameters]: commands
# 
# 2.      函数功能：
# 　　lambda创建匿名函数，而用def创建的方法是有名称的，它是一个表达式。优点：省去定义函数的过程，不需要考虑命名问题。
# 
# 3.      命令实例：
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
def main():
    # 例：直接使用
    print(lambda x:x + 1(1))  # 输出2，(1)是给x复制
    # 例：1个参数
    func1 = lambda x:x * 2
    print(func1(3))  # 结果为6
    # 例：多个参数(可以初始化参数)
    func2 = lambda x, y, z = 1: x + y + z
    print(func2(2, 3))  # 结果为6
    print(func2(2, 3, 4))  # 结果为9

if __name__ == '__main__':
    main()
