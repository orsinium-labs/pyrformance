from true_north import Group

maxsplit = Group('str-split-maxsplit')


@maxsplit.add(name='bad')
def _(r):
    text = 'ab cd ' * 100
    for _ in r:
        text.split()[0]


@maxsplit.add(name='good')
def _(r):
    text = 'ab cd ' * 100
    for _ in r:
        text.split(maxsplit=1)[0]


removeprefix = Group('str-removeprefix')


@removeprefix.add(name='bad')
def _(r):
    text = 'lorem ipsum dolor sit amet'
    prefix = 'lorem ipsum'
    for _ in r:
        if text.startswith(prefix):
            text[len(prefix):]


@removeprefix.add(name='good')
def _(r):
    text = 'lorem ipsum dolor sit amet'
    prefix = 'lorem ipsum'
    for _ in r:
        text.removeprefix(prefix)


set_contains = Group('set-contains')


@set_contains.add(name='bad')
def _(r):
    items = list(range(1000))
    item = 500
    for _ in r:
        item in set(items)


@set_contains.add(name='good')
def _(r):
    items = list(range(1000))
    item = 500
    for _ in r:
        item in items


str_concat = Group('str-concat')


@str_concat.add(name='bad')
def _(r):
    a = 'a' * 20
    b = 'b' * 20
    for _ in r:
        'hello' + a + b


@str_concat.add(name='good')
def _(r):
    a = 'a' * 20
    b = 'b' * 20
    for _ in r:
        f'hello{a}{b}'


if __name__ == '__main__':
    maxsplit.print()
    removeprefix.print()
    set_contains.print()
    str_concat.print()
