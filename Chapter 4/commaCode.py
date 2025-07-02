# delimits list of items using comma and 'and'
def comma_code(items):
    if len(items) == 0:
        return ''
    if len(items) == 1:
        return str(items[0])
    return ', '.join(str(item) for item in items[:-1]) + ', and ' + str(items[-1])


if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats', '1']
    print(comma_code(spam))
