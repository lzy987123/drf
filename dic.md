lis = [1,2]
lis.append(3)
lis.remove(1)  # 可以删除列表中的指定元素
lis.insert(0,1)  # 将元素添加到列表中的指定索引处
lis.reverse()  # 用于将列表中的对象反转位置
lis.sort()  # 列表进行升序排序.两个参数可选。reverse=True 将对列表进行降序排序。默认是 reverse=False。指定排序标准的函数
lis.clear()  # 删除列表中的所有元素
lis.pop()  # 默认删除最后一条数据，或根据制定索引删除
lis = [1,2,3,4,5,6,7]
lis.index(2)  # 获取值为2的索引
lis.count(1)  # 元素1在列表中出现的次数
l = lis.copy()  #

dic = {"a":"hello","b":"world","c":"sunwukong","d":"zhubajie"}
dic.get("a")  # 根据key查询
dic.keys()  # 获取到所有key
Out[5]: dict_keys(['a', 'b', 'c', 'd'])
dic.items()  # 列表返回可遍历的(键, 值) 元组数组
Out[7]: dict_items([('a', 'hello'), ('b', 'world'), ('c', 'sunwukong'), ('d', 'zhubajie')])
di.values()
Out[5]: dict_values(['hello', 'world', 'sunwukong'])
di.clear() # 删除字典中的全部值
di.pop()  # 删除pop指定值并返回

元祖是有序的
tul = (1,2,3,4,5,6,7)
tul.count(1)  # 元素在元祖中出现的次数

集合是无序的
ss = set("hello")
ss.add("hello")
ss.pop()  # 随机删除一个元素并返回
ss.clear()  # 删除集合中的全部元素
