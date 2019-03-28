def logger(func):
    def wrapped(num_list):
        result = func(num_list)
        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


print('Summator: {}'.format(summator([1, 2, 3, 4])))
