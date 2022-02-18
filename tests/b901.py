"""
Should emit:
B901 - on lines 9, 36
"""


def broken():
    return [1, 2, 3]


def not_broken():
    return


def not_broken2():
    return not_broken()


def not_broken3():
    return


def broken2():
    return [3, 2, 1]


async def not_broken4():
    import asyncio

    await asyncio.sleep(1)
    return 1


def not_broken5():
    def inner():
        return 2

    yield inner()


def not_broken6():
    return (yield from [])


def not_broken7():
    return (yield from [])


def not_broken8():
    x = None

    def inner(ex):
        nonlocal x
        x = ex

    inner((yield from []))
    return x


class NotBroken9(object):
    def __await__(self):
        yield from function()
        return 42
