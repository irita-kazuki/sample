class Cal(object):
    """Add and double
    >>> c = Cal()
    >>> c.add_num_and_double(1, 1)
    5
    """
    def add_num_and_double(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = (x + y)* 2
        return result
