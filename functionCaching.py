import time
from functools import lru_cache

print("functionCaching.py")


@lru_cache(maxsize=None)

def fx(n):
    time.sleep(3)
    return n*5


print(fx(2),"print for 2")
print(fx(3),"print for 3")
print(fx(4),"print for 4")
print(fx(5),"print for 5")

# now pick the data into cache
print("pick data into cach")
print(fx(2),"print for 2")
print(fx(3),"print for 3")
print(fx(4),"print for 4")
print(fx(5),"print for 5")

