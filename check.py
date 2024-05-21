# a = [('chill',1), ('five',2)]
# N = 2
# res = list(map(lambda sub: tuple(filter(lambda ele: ele != N, sub)), a))
# print(a)
test_list = [('chill',1), ('five',0)]
for i in test_list:
    if i[1] == 0:
        test_list.remove(i)
print(test_list)
# print("The original list is : " + str(test_list))
# N = 1
# res = list(map(lambda sub: tuple(filter(lambda ele: ele != N, sub)), test_list))
# print("The Tuple List after removal of element : " + str(res))