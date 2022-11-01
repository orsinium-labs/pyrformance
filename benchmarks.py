from true_north import Group

str_split_maxsplit = Group('str-split-maxsplit')


@str_split_maxsplit.add(name='bad')
def _(r):
    text = 'ab cd ' * 100
    for _ in r:
        text.split()[0]


@str_split_maxsplit.add(name='good')
def _(r):
    text = 'ab cd ' * 100
    for _ in r:
        text.split(maxsplit=1)[0]


str_removeprefix = Group('str-removeprefix')


@str_removeprefix.add(name='bad')
def _(r):
    text = 'lorem ipsum dolor sit amet'
    prefix = 'lorem ipsum'
    for _ in r:
        if text.startswith(prefix):
            text[len(prefix):]


@str_removeprefix.add(name='good')
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


dict_merge = Group()


@dict_merge.add(name='bad1')
def _(r):
    d1 = {i: i * 2 for i in range(100)}
    d2 = {i: i * 2 for i in range(100)}
    for _ in r:
        {**d1, **d2}


@dict_merge.add(name='bad2')
def _(r):
    d1 = {i: i * 2 for i in range(100)}
    d2 = {i: i * 2 for i in range(100)}
    for _ in r:
        d = d1.copy()
        d.update(d2)


@dict_merge.add(name='good')
def _(r):
    d1 = {i: i * 2 for i in range(100)}
    d2 = {i: i * 2 for i in range(100)}
    for _ in r:
        d1 | d2


if __name__ == '__main__':
    dict_merge.print()
    set_contains.print()
    str_concat.print()
    str_removeprefix.print()
    str_split_maxsplit.print()
