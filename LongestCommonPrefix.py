# 最长公共前缀
# enumerate函数，用于将一个可遍历的数据对象（如列表、元组或字符串）组合为
# 一个索引序列，同时列出数据和数据下标，一般用在for循环当中

a_list = ["flower", "folw", "flight"]
print(enumerate(a_list))
print(list(enumerate(a_list)))
for (i,j) in list(enumerate(a_list)):
    print(i,j)
print(list(enumerate(a_list, 1)))
print("----")
print(min(a_list))
print(max(a_list))
