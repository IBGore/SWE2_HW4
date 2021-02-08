def vol(x, y, z):
    #check is int or float
    assert(isinstance(x, int) or isinstance(x, float)), "X value Must be an int or Float"
    assert(isinstance(y, int) or isinstance(y, float)), "Y value Must be an int or Float"
    assert(isinstance(z, int) or isinstance(z, float)), "Z value Must be an int or Float"
    #check is positive
    assert(x >= 0 and y >= 0 and z >= 0), "All Inputs Must be Positive"
    return x * y * z