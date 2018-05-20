u = '中文' #显示指定unicode类型对象u
str_ = u.encode('gb2312') #以gb2312编码对unicode对像进行编码
str1 = u.encode('gbk') #以gbk编码对unicode对像进行编码
str2 = u.encode('utf-8') #以utf-8编码对unicode对像进行编码
u1 = str_.decode('gb2312')#以gb2312编码对字符串str进行解码，以获取unicode
u2 = str1.decode('gbk')
u3 = str2.decode('utf-8')
print(u)
print(type(u))
print('')
print(str_)
print(type(str_))
print('')
print(str1)
print(type(str1))
print('')
print(str2)
print(type(str2))
print('')
print(u1)
print(u2)
print(u3)