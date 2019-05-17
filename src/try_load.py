# import sys
# sys.path.append('/home/madhevan/Documents/py_packages')
from src.batcher import BatchGen
path = '../../dev-v1.1.json'
batch_size = 10
gp = False
tr = False
#f = BatchGen(path,batch_size,gpu = gp,is_train = tr)

import json

with open(path, 'r', encoding='utf-8') as reader:
    # filter
    data = []
    cnt = 0
    print(type(reader))
    c=0
    for line in reader:
        if c < 10:
            sample = json.loads(line)
            print(c)
            c+=1
            print(sample)
            print('\n')
        else:
            break

    print(type(sample))
    print(len(sample))
    print(sample.keys())

