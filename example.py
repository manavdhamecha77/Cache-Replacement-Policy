from policies import LRU_policy, FIFO_policy
from cache import Cache

cache1 = Cache(3, LRU_policy())
cache2 = Cache(3, FIFO_policy())

list = [1,2,4,3,2,5,2,5,3,4,3,1,3,2,4,1,2,3,5,4,3,2,1,2,3,2]

hit = 0
miss = 0

for i in list:
    if cache1.access(i) == "Hit":
        hit += 1
    else:
        miss += 1

LRU_hit_ratio = (hit/(miss + hit)) * 100
print("LRU hit ratio : ", LRU_hit_ratio)

hit = 0
miss = 0

for i in list:
    if cache2.access(i) == "Hit":
        hit += 1
    else:
        miss += 1


FIFO_hit_ratio = (hit/(miss + hit)) * 100
print("FIFO hit ratio : ", FIFO_hit_ratio)

if(LRU_hit_ratio > FIFO_hit_ratio):
    print("LRU performed better")
else:
    print("FIFO performed better")