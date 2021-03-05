#测试单例模式

class MusicPlayer(object):

    instance = None
    instance_info = True


    def __new__(cls, *args, **kwargs):

        #1.创建方法时,new方法会被自动调用
        print("创建对象，分配空间")

        if cls.instance is None:
            #2.为对象分配空间,赋值
            cls.instance =  super().__new__(cls)

        #3.返回内存地址
        return cls.instance

    def __init__(self):

        #1.判断是否调用过new方法
        if self.instance_info == True:
            print("init方法")

            #2.赋值给info，不再调用
            self.instance_info = False



player = MusicPlayer()
player2 = MusicPlayer()

print(player)
print(player2)
