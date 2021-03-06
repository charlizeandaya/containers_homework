def range(a, b=None, c=None):
    '''
    This function should behave exactly like the built-in range function.
    For example:

    >>> list(range(5))
    [0, 1, 2, 3, 4]
    >>> list(range(1, 5))
    [1, 2, 3, 4]
    >>> list(range(1, 5, 2))
    [1, 3]

    HINT:
    If you can figure out how to use the built-in range function
    (without modifying the test cases!),
    then feel free to do so.
    That's fairly difficult to do, however, and it's much easier
    to just implement this function normally using the yield syntax.

    NOTE:
    For efficiency reasons, Python's built-in range object is written in the C
    programming language rather than natively in python.
    You can find the source code online at
    https://hg.python.org/cpython/file/ee7b713fec71/Objects/rangeobject.c
    The link takes you to a file that is 1445 lines long,
    and all it does is implement this simple functionality.
    My easy to read Python implementation of this function is just 15 lines
    long.
    (And with some code golf I also wrote a less readable version that is only
    4 lines.)
    It is very common for C programs to be 100x longer than their corresponding
    python programs.
    C code must manage lots of details about the computer manually that python
    code automates for you.
    Carefully written C code can be faster than the corresponding python code
    because it can remove some of the overhead of this automation process,
    but the resulting code is much longer and harder to read/write.
    '''
    if b is None:
        start_val = 0
        end_val = a
        increment = 1
    else:
        start_val = a
        end_val = b
        increment = 1
    if c:
        increment = c

    if end_val > start_val and increment > 0:
        while start_val < end_val:
            yield start_val
            start_val += increment

    elif end_val < start_val and increment < 0:
        while start_val > end_val:
            yield start_val
            start_val += increment
