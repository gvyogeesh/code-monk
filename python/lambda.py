# Example 1
def double(x):
   return x*2

#Above function can be replaced with below lambda function

double_lmb = lambda x: x*2

print(double(2))
print(double_lmb(2))
print

# Example 2
def add(x, y):
   return x+y

add_lmb = lambda x,y: x+y

print add(2,3)
print add_lmb(2,3)
print 

# Example 3
def min(x,y):
   if (x<y):
      return x
   else:
      return y

# lambda version is as below
min_lmb = lambda x,y: x if x<y else y
print(min(2,3))
print(min_lmb(2,3))
print

# Example 4 
def make_inc(n):
   def inc(val):
      return n+val
   return inc

inc_2 = make_inc(2)
inc_4 = make_inc(4)

print inc_2(10)
print inc_4(20)
print 

#Lambda version is as below
def make_inc_lmb(n):
   return lambda x: n+x

inc_2_lmb = make_inc_lmb(2)
inc_4_lmb = make_inc_lmb(4)

print inc_2_lmb(10)
print inc_4_lmb(20)

