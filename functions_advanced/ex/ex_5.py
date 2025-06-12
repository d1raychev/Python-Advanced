def concatenate(*args, **kwargs):
    result = ''
    for name in args:
        result += name
    for key, value in kwargs.items():
        if key in result:
            result = result.replace(key, value)

    return result

