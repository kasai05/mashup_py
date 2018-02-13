import time, random

sum = 0  # ブランクを空ける
before = time.clock()

# インデントの数を調整する
for i in range( 1000000 ) :
    sum = sum + random.randint(1 , 100)

# geptimeの単語の間に'_'をいれる
gap_time = time.clock() - before

print "dummy:", sum
print "gaptime:", gaptime
