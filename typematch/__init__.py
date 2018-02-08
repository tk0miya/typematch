# -*- coding: utf-8 -*-

__version__ = '1.0.0'


from typing import Any


NoneType = type(None)


class UnsupportedType(Exception):
    pass


def typematch(subject: Any, typ: Any, allow_none=False) -> bool:
    try:
        if getattr(typ, '__module__', None) == 'typing':
            return mapping[str(typ.__class__)](subject, typ, allow_none)
        else:
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


def typematch_Any(subject: Any, typ: Any, allow_none=False) -> bool:
    return True


def typematch_Union(subject: Any, typ: Any, allow_none=False) -> bool:
    return any(typematch(subject, arg) for arg in typ.__args__)


def typematch_Union_py35(subject: Any, typ: Any, allow_none=False) -> bool:
    return any(typematch(subject, arg) for arg in typ.__union_params__)


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
    NoneType: typematch_None,
    "typing.Any": typematch_Any,
    "<class 'typing.AnyMeta'>": typematch_Any,
    "typing.Union": typematch_Union,
    "<class 'typing.UnionMeta'>": typematch_Union_py35,
}
