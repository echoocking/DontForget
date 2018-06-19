def generator_num():
    num_list = [1, 2, 3, 4, 5, 6, 7]
    for num in num_list:
        yield num


for num in generator_num():
    print 'pussy: {}'.format(num)
