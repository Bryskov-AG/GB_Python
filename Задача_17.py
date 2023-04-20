# Дан список чисел.Определите,сколько в нём встречается различных чисел.

# Input:[1,1,2,0,-1,3,4,4]
# Output:6


#######################################
# list_a = [1, 1 , 2, 0, -1, 3, 4, 4]
# list_b = []
# for i in list_a:
#     if i in list_b:
#         pass
#     else:
#         list_b.append(i)

# print(list_b)
############################################
list_1=[1,1,2,0,-1,3,4,4]
print(list_1)
# c=list(set(list_1))
# print(c)

print(list(set(list_1)))