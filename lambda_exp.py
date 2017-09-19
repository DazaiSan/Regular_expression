def make_inc(n):
    return lambda x:x+n
make_one = make_inc(1)
print(make_one(5))
