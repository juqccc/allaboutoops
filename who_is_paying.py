def who_is_paying(name):
    two_init = name[:2]

    if len(name) <= 2:
        return [name]
    return [name, two_init]



print(who_is_paying("houbenov"))
