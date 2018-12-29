#l = list(filter(lambda x: x for i in range(2,j),range(2,100)))

#print(l)

# def is_prime(x):
#     if x<2:
#         return False
#     for i in range(2,x):
#         if x %i ==0:
#             return False
#     else:
#         return True
#
# #l = filter(is_prime,range(100))
# #print(list(l))
# l = [is_prime(i) for i in range(100)]

# def mysum(n):
#     if n<1:
#         return 0
#     return n+mysum(n-1)
#
# print(mysum(100))


# def get_age(n):
#     if n ==1:
#         return 10
#     return 2+get_age(n-1)
#
# print(get_age(3))

# def make_counter():
#     count = 0
#
#     def counter():
#         #nonlocal count
#         return count
#
#     return counter
#
#
# def make_counter_test():
#     mc = make_counter()
#     print(mc())
#     print(mc())
#     print(mc())
#
# make_counter_test()

# def fn(n):
#     if n<=2:
#         return n
#     return fn(n-1)+fn(n-2)
# print(fn(3))
import time
print(time.strftime("%Y-%m-%d %H:%I:%S", time.localtime( time.time() ) ) )
l = [1,2,3,[4,5,[4,5],[4,5]],[4,5],[3,4,5,[4,3]]]
# L = []
#
# def sum_l(l):
#     for i in l:
#         print(i)
#         if type(i) is int:
#             L.append(i)
#         else:
#              sum_l(i)
# sum_l(l)
# print(L)
# s=0
# def sum_l(l):
#     for i in l:
#         if type(i) is int:
#            s=s+i
#         else:
#             sum_l(i)
# sum_l(l)

# 将一个数逆序放入列表中 如：1234----【4,3,2,1】
# l = '1234'
# length = len(l)
# def revert(x):
#     if x == -1:
#         return []
#     return [l[x]] + revert(x - 1)  # 每次生成新的列表
# print((revert(len(l) - 1)))

# 1!  + 2 !  ++++  20 !


# def fn(x):
#     s = 1
#     for i in range(1,x+1):
#         s = s*i
#     return s
# print(list((map(fn,range(1,21)))))

# def app(**kwargs):
#     for i,j in kwargs.items():
#         print(i,j)
#
#
# app(a = 1,b=2)
# import re
# dic = {
#     'email':"\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?",
#     'name':'^[a-zA-Z0-9_]{4,12}$',
#     'password':'^[a-zA-Z0-9_\+-=]{6,18}$',
#     'age':'(^[1-9][0-9]$)|(^[0-9]$)',
#     'img':'^(\w){4}$'
# }
# if 'email' in dic:
#     s = re.findall("^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$",'1223324@asd.com')
#     print(s)

# import time
# print(time.gmtime())

import itertools
l = ['a','b','c','d']

print (list(itertools.permutations(l)))

#  a b c d  的 排列组合  等于  a 在第一位时 b c d 的排列组合    a 在第二位时 b c d 的排列组合    a 在第三位时 b c d 的排列组合  a 在第四位时 b c d 的排列组合

def group(s,i):
	'''
	列表所有元素的排列组合
	'''
	if i ==len(s):   #
		print(s)
	else:
		for j in range(i,len(s)):
			s[j] ,s[i] = s[i],s[j]  #  交换位置
			group(s,i+1)                   #  i 是子列表    group(s,i+1)   子列表的全排序
			s[j],s[i] = s[i],s[j]   #  换回来
			print('次数')
group(l,0)

'''
递归思想：
取出数组中第一个元素放到最后，即a[1]与a[n]交换，然后递归求a[n-1]的全排列

1）如果数组只有一个元素n=1，a={1} 则全排列就是{1}
2）如果数组有两个元素n=2，a={1,2} 则全排列是：
{2,1}--a[1]与a[2]交换。交换后求a[2-1]={2}的全排列，归结到1)
{1,2}--a[2]与a[2]交换。交换后求a[2-1]={1}的全排列，归结到1)
3）如果数组有三个元素n=3，a={1,2,3} 则全排列是
{{2,3},1}--a[1]与a[3]交换。后求a[3-1]={2,3}的全排列，归结到2）
{{1,3},2)--a[2]与a[3]交换。后求a[3-1]={1,3}的全排列，归结到2）
{{1,2},3)--a[3]与a[3]交换。后求a[3-1]={1,2}的全排列，归结到2）
'''

'''
举个例子，比如你要对a,b,c三个字符进行全排列，那么它的全排列有abc,acb,bac,bca,cba,cab这六种可能，
你们想想你们是如何得出这六种可能的。
没错！就是当指针指向第一个元素a时，
它可以是其本身a(即和自己进行交换)，
还可以和b，c进行交换，故有3种可能，当第一个元素a确定以后
，指针移向第二位置，第二个位置可以和其本身b及其后的元素c进行交换，
又可以形成两种排列，当指针指向第三个元素c的时候，这个时候其后没有元素了，
此时，则确定了一组排列，输出。但是每次输出后要把数组恢复为原来的样子。

简单来说，它的思想即为，确定第1位，对n-1位进行全排列，确定第二位，对n-2位进行全排列。。。显然，这是一种递归的思想。
'''



'''
 a b c 
 
3 2 1

 a b c d 
 
 4 3 2 1

     


'''