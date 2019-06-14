Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?
O(1) - I believe this may scale at a constant because of the constraint of the buffer
2. What is the space complexity of your ring buffer's `append` function?
O(1)
3. What is the runtime complexity of your ring buffer's `get` method?
O(N) - need to iterate through a for loop in buffer to fetch item
4. What is the space complexity of your ring buffer's `get` method?
O(N)

5. What is the runtime complexity of the provided code in `names.py`?
O(N^2) - two for loops to iterate through
6. What is the space complexity of the provided code in `names.py`?
O(N)
7. What is the runtime complexity of your optimized code in `names.py`?
O(N) - more efficient complexity running through a dictionary
8. What is the space complexity of your optimized code in `names.py`?
O(N) - still order N, optimzed code used wouldn't save space complexity