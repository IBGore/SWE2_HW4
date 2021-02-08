def fullName(first, last):
    assert(isinstance(first, str) and isinstance(last, str)), "Names Must Be Strings"
    if(len(first) == 0 or len(last) == 0):
        return first + last
    return first + " " + last
