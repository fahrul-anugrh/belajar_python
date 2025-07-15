# Episode 1
# How python works

import time
start_time = time.time()

print("Hello")
print("World")
print("Hello World")

for i in range(1,1000):
    print(i)

print(time.time()-start_time)

""" Python bisa dicompile meskipun dia interpreted
    Caranya : python -m py_compile episode1.py
    Compiled : lebih cepat diproses
"""

