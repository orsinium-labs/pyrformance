from true_north import Group


def identity(x):
    return x


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
        text.removeprefix(prefix)  # type: ignore[attr-defined]


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


re_compile = Group('re-compile')


@re_compile.add(name='bad')
def _(r):
    import re
    text = str(list(range(1000)))
    for _ in r:
        re.match('[0-9]+', text)


@re_compile.add(name='good')
def _(r):
    import re
    text = str(list(range(1000)))
    rex = re.compile('[0-9]+')
    for _ in r:
        rex.match(text)


elif_ = Group('elif')


@elif_.add(name='bad')
def _(r):
    v = '123' * 5
    c1 = '123' * 9
    c2 = '123' * 10
    for _ in r:
        if v in c1:
            pass
        if v in c2:
            pass


@elif_.add(name='good')
def _(r):
    v = '123' * 5
    c1 = '123' * 9
    c2 = '123' * 10
    for _ in r:
        if v in c1:
            pass
        elif v in c2:
            pass


map_ = Group('map')


@map_.add(name='bad gen expr')
def _(r):
    items = range(10_000)
    for _ in r:
        for _ in (identity(x) for x in items):
            pass


@map_.add(name='bad list comp')
def _(r):
    items = range(10_000)
    for _ in r:
        for _ in [identity(x) for x in items]:
            pass


@map_.add(name='good')
def _(r):
    items = range(10_000)
    for _ in r:
        for _ in map(identity, items):
            pass


filter_ = Group('filter')


@filter_.add(name='bad gen expr')
def _(r):
    items = range(10_000)
    for _ in r:
        for _ in (x for x in items if bool(x)):
            pass


@filter_.add(name='bad list comp')
def _(r):
    items = range(10_000)
    for _ in r:
        for _ in [x for x in items if bool(x)]:
            pass


@filter_.add(name='good')
def _(r):
    items = range(10_000)
    for _ in r:
        for _ in filter(bool, items):
            pass


double_startswith = Group('double-startswith')


@double_startswith.add(name='bad')
def _(r):
    text = 'ab' * 100
    prefix1 = 'abcd'
    prefix2 = 'ab' * 80
    for _ in r:
        text.startswith(prefix1) or text.startswith(prefix2)


@double_startswith.add(name='good')
def _(r):
    text = 'ab' * 100
    prefix1 = 'abcd'
    prefix2 = 'ab' * 80
    for _ in r:
        text.startswith((prefix1, prefix2))


any_to_or = Group('any-to-or')


@any_to_or.add(name='bad')
def _(r):
    for _ in r:
        if any([0, False, '', 1]):
            pass


@any_to_or.add(name='good')
def _(r):
    for _ in r:
        if 0 or False or '' or 1:
            pass


min_to_if = Group('min-to-if')


@min_to_if.add(name='bad')
def _(r):
    b = 100
    for _ in r:
        a = 1000
        a = min(a, b)


@min_to_if.add(name='good')
def _(r):
    b = 100
    for _ in r:
        a = 1000
        if b < a:
            a = b


for_compr = Group('for-compr')


@for_compr.add(name='bad gen expr')
def _(r):
    items = range(10_000)
    for _ in r:
        for i in (identity(i) for i in items):
            identity(i)


@for_compr.add(name='bad list comp')
def _(r):
    items = range(10_000)
    for _ in r:
        for i in [identity(i) for i in items]:
            identity(i)


@for_compr.add(name='good')
def _(r):
    items = range(10_000)
    for _ in r:
        for i in items:
            i = identity(i)
            identity(i)


dict_update = Group('dict-update')


@dict_update.add(name='bad')
def _(r):
    for _ in r:
        d = {}
        d.update({'a': 1})


@dict_update.add(name='good')
def _(r):
    for _ in r:
        d = {}
        d['a'] = 1


if_len = Group('if-len')


@if_len.add(name='bad')
def _(r):
    items = list(range(10_000))
    for _ in r:
        if len(items) > 0:
            pass


@if_len.add(name='good')
def _(r):
    items = list(range(10_000))
    for _ in r:
        if items:
            pass


GROUPS = (
    any_to_or,
    dict_update,
    double_startswith,
    elif_,
    filter_,
    for_compr,
    map_,
    min_to_if,
    re_compile,
    set_contains,
    str_concat,
    str_removeprefix,
    str_split_maxsplit,
)


if __name__ == '__main__':
    for group in GROUPS:
        group.print()
