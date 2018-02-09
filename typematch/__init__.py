# -*- coding: utf-8 -*-

__version__ = '1.0.0'


import collections.abc
import itertools
from typing import Any, Callable, Union


NoneType = type(None)


class UnsupportedType(Exception):
    pass


def typematch(subject: Any, typ: Any, allow_none=False) -> bool:
    try:
        modname = getattr(typ, '__module__', None)
        if modname == 'typing':
            qualname = getattr(typ, '__qualname__', None)
            name = getattr(typ, '__name__', None)
            if qualname and qualname in mapping:
                return mapping[qualname](subject, typ, allow_none)
            elif name and name in mapping:
                return mapping[name](subject, typ, allow_none)
            else:
                return mapping[str(typ.__class__)](subject, typ, allow_none)
        elif modname == 'collections.abc':
            matcher = typematch_Generic(typ)
            return matcher(subject, typ, allow_none)
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


def typematch_AnyStr(subject: Any, typ: Any, allow_none=False) -> bool:
    return typematch(subject, Union[bytes, str], allow_none)


def typematch_Generic(generic_type: Any) -> Callable[[Any, Any, bool], bool]:
    def matcher(subject: Any, typ: Any, allow_none=False) -> bool:
        if subject is None and allow_none:
            return True
        else:
            return isinstance(subject, generic_type)

    return matcher


def typematch_Dict(subject: Any, typ: Any, allow_none=False) -> bool:
    if not issubclass(type(subject), dict):
        return False
    elif typ.__args__:
        if (all(typematch(key, typ.__args__[0]) for key in subject.keys()) and
                all(typematch(value, typ.__args__[1]) for value in subject.values())):
            return True
        else:
            return False
    else:
        # Dict not having any argument
        return True


def typematch_List(subject: Any, typ: Any, allow_none=False) -> bool:
    if not issubclass(type(subject), list):
        return False
    elif getattr(typ, '__args__', None):
        subtype = typ.__args__[0]
        return all(typematch(elem, subtype) for elem in subject)
    else:
        # List not having any argument
        return True


def typematch_Set(subject: Any, typ: Any, allow_none=False) -> bool:
    if not issubclass(type(subject), set):
        return False
    elif getattr(typ, '__args__', None):
        subtype = typ.__args__[0]
        return all(typematch(elem, subtype) for elem in subject)
    else:
        # List not having any argument
        return True


def typematch_Tuple(subject: Any, typ: Any, allow_none=False) -> bool:
    if not issubclass(type(subject), tuple):
        return False
    elif getattr(typ, '__args__', None):
        for elem, subtype in itertools.zip_longest(subject, typ.__args__):
            if subtype is ...:
                return True
            elif not typematch(elem, subtype):
                return False
        else:
            return True
    elif getattr(typ, '__tuple_params__', None):  # for py35
        if len(subject) < len(typ.__tuple_params__):
            return False
        elif len(subject) > len(typ.__tuple_params__) and not typ.__tuple_use_ellipsis__:
            return False

        for elem, subtype in zip(subject, typ.__tuple_params__):
            if not typematch(elem, subtype):
                return False
        else:
            return True
    else:
        # Tuple not having any argument
        return True


def typematch_Union(subject: Any, typ: Any, allow_none=False) -> bool:
    return any(typematch(subject, arg) for arg in typ.__args__)


def typematch_Union_py35(subject: Any, typ: Any, allow_none=False) -> bool:
    return any(typematch(subject, arg) for arg in typ.__union_params__)


mapping = {
    # builtin types
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

    # typing
    "typing.Any": typematch_Any,
    "AnyStr": typematch_AnyStr,
    "<class 'typing.AnyMeta'>": typematch_Any,
    "Dict": typematch_Dict,
    "List": typematch_List,
    "Set": typematch_Set,
    "Tuple": typematch_Tuple,
    "typing.Union": typematch_Union,
    "<class 'typing.UnionMeta'>": typematch_Union_py35,

    # generics
    "AbstractSet": typematch_Generic(collections.abc.Set),
    "ByteString": typematch_Generic(collections.abc.ByteString),
    "Container": typematch_Generic(collections.abc.Container),
    "Hashable": typematch_Generic(collections.abc.Hashable),
    "ItemsView": typematch_Generic(collections.abc.ItemsView),
    "Iterable": typematch_Generic(collections.abc.Iterable),
    "Iterator": typematch_Generic(collections.abc.Iterator),
    "KeysView": typematch_Generic(collections.abc.KeysView),
    "Mapping": typematch_Generic(collections.abc.Mapping),
    "MappingView": typematch_Generic(collections.abc.MappingView),
    "MutableMapping": typematch_Generic(collections.abc.MutableMapping),
    "MutableSequence": typematch_Generic(collections.abc.MutableSequence),
    "MutableSet": typematch_Generic(collections.abc.MutableSet),
    "Sequence": typematch_Generic(collections.abc.Sequence),
    "Sized": typematch_Generic(collections.abc.Sized),
    "ValuesView": typematch_Generic(collections.abc.ValuesView),
}
