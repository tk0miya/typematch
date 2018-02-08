# -*- coding: utf-8 -*-

__version__ = '1.0.0'


from typing import Any


class UnsupportedType(Exception):
    pass


def typematch(subject: Any, typ: Any, allow_none=False) -> bool:
    try:
        return mapping[typ](subject, typ, allow_none)
    except KeyError:
        raise UnsupportedType(typ)


def typematch_builtins(subject: Any, typ: Any, allow_none=False) -> bool:
    if subject is None and allow_none:
        return True
    elif type(subject) == bool:
        # To avoid bool values matching to int (because bool is a subclass of int)
        return typ is bool
    else:
        return issubclass(type(subject), typ)


def typematch_None(subject: Any, typ: Any, allow_none=False) -> bool:
    return subject is None


mapping = {
    bool: typematch_builtins,
    int: typematch_builtins,
    float: typematch_builtins,
    list: typematch_builtins,
    tuple: typematch_builtins,
    str: typematch_builtins,
    bytes: typematch_builtins,
    set: typematch_builtins,
    dict: typematch_builtins,
    None: typematch_None,
}
