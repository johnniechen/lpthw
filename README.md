>*虽然Python是解释性语言，但是它是面向对象的，能够进行对象编程。下面就来了解一下如何在Python中进行对象编程*。

#一、如何定义一个类

在进行python面向对象编程之前，先来了解几个术语：**类，类对象，实例对象，属性，函数和方法**。

类是对现实世界中一些事物的封装，定义一个类可以采用下面的方式来定义：

    class className:
        block

注意类名后面有个冒号，在block块里面就可以定义属性和方法了。当一个类定义完之后，就产生了一个类对象。类对象支持两种操作：**引用和实例化**。*引用操作是通过类对象去调用类中的属性或者方法，而实例化是产生出一个类对象的实例，称作实例对象*。比如定义了一个people类：

    class people:
        name = 'jack'         #定义了一个属性
    
        def printName(self):  #定义了一个方法
            print self.name

people类定义完成之后就产生了一个全局的类对象，可以通过类对象来访问类中的属性和方法了。当通过people.name（至于为什么可以直接这样访问属性后面再解释，这里只要理解类对象这个概念就行了）来访问时，people.name中的people称为类对象，这点和C++中的有所不同。当然还可以进行实例化操作，p=people( )，这样就产生了一个people的实例对象，此时也可以通过实例对象p来访问属性或者方法了(p.name).

理解了类、类对象和实例对象的区别之后，我们来了解一下Python**中属性、方法和函数的区别**。

在上面代码中注释的很清楚了，name是一个属性，printName( )是一个方法，与某个对象进行绑定的函数称作为方法。*一般在类里面定义的函数与类对象或者实例对象绑定了，所以称作为方法；而在类外定义的函数一般没有同对象进行绑定，就称为函数。*

#二、属性

在类中我们可以定义一些属性，比如：

    class people:
        name = 'jack'
        age = 12

    p = people()
    print p.name,p.age

定义了一个people类，里面定义了name和age属性，默认值分别为'jack'和12。在定义了类之后，就可以用来产生实例化对象了，这句p = people( )实例化了一个对象p，然后就可以通过p来读取属性了。这里的name和age都是公有的，可以直接在类外通过对象名访问，如果想定义成私有的，则需在前面加2个下划线 ' __'。

    class people:
        __name = 'jack'
        __age = 12

    p = people()
    print p.__name,p.__age

这段程序运行会报错：

![](http://images.cnitblog.com/blog/288799/201303/28165802-583b4b244e0045b9893d9bf405ccd499.jpg)

提示找不到该属性，因为私有属性是不能够在类外通过对象名来进行访问的。在Python中没有像C++中public和private这些关键字来区别公有属性和私有属性，它是以属性命名方式来区分，如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性（方法也是一样，方法名前面加了2个下划线的话表示该方法是私有的，否则为公有的）。

#三、方法

在类中可以根据需要定义一些方法，定义方法采用def关键字，在类中定义的方法至少会有一个参数，一般以名为'self'的变量作为该参数（用其他名称也可以），而且需要作为第一个参数。下面看个例子：

    class people:
        __name = 'jack'
        __age = 12

        def getName(self):
            return self.__name
        def getAge(self):
            return self.__age

    p = people()
    print p.getName(),p.getAge()

![](http://images.cnitblog.com/blog/288799/201303/28171702-3ca401270bb94bf9afc57fb9b6dd25a5.jpg)

如果对self不好理解的话，可以把它当做C++中类里面的this指针一样理解，就是对象自身的意思，在用某个对象调用该方法时，就将该对象作为第一个参数传递给self。

#四、类中内置的方法

在Python中有一些内置的方法，这些方法命名都有比较特殊的地方（*其方法名以2个下划线开始然后以2个下划线结束*）。**类中最常用的就是构造方法和析构方法**。

构造方法`__init__(self,....)`在生成对象时调用，可以用来进行一些初始化操作，不需要显示去调用，系统会默认去执行。构造方法支持重载，如果用户自己没有重新定义构造方法，系统就自动执行默认的构造方法。

析构方法`__del__(self)`在释放对象时调用，支持重载，可以在里面进行一些释放资源的操作，不需要显示调用。

还有其他的一些内置方法：

比如 `__cmp__( )`, `__len( )__`等，具体的用法可以参考这篇[博文](http://www.cnblogs.com/simayixin/archive/2011/05/04/2036295.html)。


#五、类属性、实例属性、类方法、实例方法以及静态方法

在了解了类基本的东西之后，下面看一下python中这几个概念的区别。

先来谈一下类属性和实例属性

在前面的例子中我们接触到的就是类属性，顾名思义，类属性就是类对象所拥有的属性，它被所有类对象的实例对象所共有，在内存中只存在一个副本，这个和C++中类的静态成员变量有点类似。对于公有的类属性，在类外可以通过类对象和实例对象访问。

    class people:
        name = 'jack'  #公有的类属性
        __age = 12     #私有的类属性

    p = people()

    print p.name             #正确
    print people.name        #正确
    print p.__age            #错误，不能在类外通过实例对象访问私有的类属性
    print people.__age       #错误，不能在类外通过类对象访问私有的类属性
实例属性是不需要在类中显示定义的，比如：

    class people:
        name = 'jack'

    p = people()
    p.age = 12
    print p.name    #正确
    print p.age     #正确

    print people.name    #正确
    print people.age     #错误

在类外对类对象people进行实例化之后，产生了一个实例对象p，然后p.age = 12这句给p添加了一个实例属性age，赋值为12。这个实例属性是实例对象p所特有的，注意，类对象people并不拥有它（所以不能通过类对象来访问这个age属性）。当然还可以在实例化对象的时候给age赋值。

    class people:
        name = 'jack'
    
        #__init__()是内置的构造方法，在实例化对象时自动调用
        def __init__(self,age):
            self.age = age

    p = people(12)
    print p.name    #正确
    print p.age     #正确

    print people.name    #正确
    print people.age     #错误

如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。如果通过实例对象去引用，会产生一个同名的实例属性，这种方式修改的是实例属性，不会影响到类属性，并且之后如果通过实例对象去引用该名称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。

    class people:
        country = 'china'
    
    print people.country
    p = people()
    print p.country
    p.country = 'japan' 
    print p.country      #实例属性会屏蔽掉同名的类属性
    print people.country
    del p.country    #删除实例属性
    print p.country

![](http://images.cnitblog.com/blog/288799/201303/29155046-6415b08470ba4ce696c2bcfd2888a3a9.jpg)

下面来看一下类方法、实例方法和静态方法的区别。

类方法：是类对象所拥有的方法，需要用修饰器`@classmethod`来标识其为类方法，对于类方法，第一个参数必须是类对象，一般以”cls”作为第一个参数（当然可以用其他名称的变量作为其第一个参数，但是大部分人都习惯以’cls’作为第一个参数的名字，就最好用’cls’了），能够通过实例对象和类对象去访问。

    class people:
        country = ‘china’
    
        #类方法，用classmethod来进行修饰
        @classmethod
        def getCountry(cls):
            return cls.country

    p = people()
    print p.getCountry()    #可以用过实例对象引用
    print people.getCountry()    #可以通过类对象引用
类方法还有一个用途就是可以对类属性进行修改：

    class people:
        country = ‘china’
    
        #类方法，用classmethod来进行修饰
        @classmethod
        def getCountry(cls):
            return cls.country
        
        @classmethod
        def setCountry(cls,country):
            cls.country = country
        

    p = people()
    print p.getCountry()    #可以用过实例对象引用
    print people.getCountry()    #可以通过类对象引用

    p.setCountry(‘japan’)   

    print p.getCountry()   
    print people.getCountry()    
运行结果：

![](http://images.cnitblog.com/blog/288799/201303/29161013-894d051b78be49f78cf55a6801879f9a.jpg)

结果显示在用类方法对类属性修改之后，通过类对象和实例对象访问都发生了改变。

实例方法：在类中最常定义的成员方法，它至少有一个参数并且必须以实例对象作为其第一个参数，一般以名为’self’的变量作为第一个参数（当然可以以其他名称的变量作为第一个参数）。**在类外实例方法只能通过实例对象去调用，不能通过其他方式去调用**。

    class people:
        country = ‘china’
    
        #实例方法
        def getCountry(self):
            return self.country
        

    p = people()
    print p.getCountry()         #正确，可以用过实例对象引用
    print people.getCountry()    #错误，不能通过类对象引用实例方法
静态方法：需要通过修饰器”@staticmethod”来进行修饰，静态方法不需要多定义参数。

    class people:
        country = ‘china’
    
        @staticmethod
        #静态方法
        def getCountry():
            return people.country
        

    print people.getCountry()     
对于类属性和实例属性，如果在类方法中引用某个属性，该属性必定是类属性，而如果在实例方法中引用某个属性（不作更改），并且存在同名的类属性，此时若实例对象有该名称的实例属性，则实例属性会屏蔽类属性，即引用的是实例属性，若实例对象没有该名称的实例属性，则引用的是类属性；如果在实例方法更改某个属性，并且存在同名的类属性，此时若实例对象有该名称的实例属性，则修改的是实例属性，若实例对象没有该名称的实例属性，则会创建一个同名称的实例属性。想要修改类属性，如果在类外，可以通过类对象修改，如果在类里面，只有在类方法中进行修改。

从类方法和实例方法以及静态方法的定义形式就可以看出来，类方法的第一个参数是类对象cls，那么通过cls引用的必定是类对象的属性和方法；而实例方法的第一个参数是实例对象self，那么通过self引用的可能是类属性、也有可能是实例属性（这个需要具体分析），不过在存在相同名称的类属性和实例属性的情况下，实例属性优先级更高。静态方法中不需要额外定义参数，因此在静态方法中引用类属性的话，必须通过类对象来引用。

关于面向对象编程暂时就讲这么多了，其他关于类的继承和方法重载这些内容将在后面继续讲解。
