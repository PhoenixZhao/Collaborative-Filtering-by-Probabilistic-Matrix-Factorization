import numpy
ratings=[]
infile = open('/home/yao/workspace/project/code/ml-100k/u.data', 'r')
for line in infile.readlines():
    f = line.rstrip('\r\n').split("\t")
    f = (float(f[0]),float(f[1]),float(f[2]))
    ratings.append(f)

print ratings
