def fullName(first, last):
    assert(isinstance(first, str) and isinstance(last, str)), "Names Must Be Strings"
    assert(len(first) > 0 and len(last) > 0), "Names Must Not Be Empty"
    return first + " " + last
