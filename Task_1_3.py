x = int(input("x = "))
y = int(input("y = "))
list_val = [x + y, x - y, x*y, x/y, x//y]
res_list = set(list_val)
res_list.remove(max(res_list))
print(max(res_list))