bob = {'name': 'Bob Smith', 'age': 42, 'pay': 3000, 'job': 'dev'}
sue = {'name': 'Sue Smith', 'age': 45, 'pay': 4000, 'job': 'hdw'}
tom = {'name': 'Tom Smith', 'age': 50, 'pay': 0, 'job': None}

db = {'bob': bob, 'sue': sue, 'tom': tom}

if __name__=='__main__':
    for key in db:
        print(key, '=>', db[key])

