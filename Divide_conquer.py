

def div_con(x):
    str_num_list = [num for num in x if isinstance(num, str)]
    int_num_list = [num for num in x if isinstance(num, int)]
    total_str = sum(int(num)for num in str_num_list)
    total_num = sum(int_num_list)
    result = total_num - total_str
    print(result)






print(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]))
