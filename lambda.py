Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> (lambda x: x*3)(4)
12
>>> (lambda x: x*3)([4])
[4, 4, 4]
>>> li=[1,2,3,4]
>>> l=filter(lambda x: x%2==0,li)
>>> l
<filter object at 0x0000022904249310>
>>> print(list(l))
[2, 4]
>>> l=map(lambda x: x*x,li)
>>> list(l)
[1, 4, 9, 16]
>>> l=list(map(lambda x: x+2,li))
>>> print(l)
[3, 4, 5, 6]
>>> name=["amit","sumit","ram","syam"]
>>> last_name=["patel","mukati","patel","mandloi"]
>>> l=list(map(lambda x,y:x+" "+y,name,last_name))
>>> print(l)
['amit patel', 'sumit mukati', 'ram patel', 'syam mandloi']
>>> 