def deep_getattr(obj, attr: str):
    for key in attr.split('.'):
        obj = getattr(obj, key)
    return obj
