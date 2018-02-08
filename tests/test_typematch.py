# -*- coding: utf-8 -*-

from collections import OrderedDict
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from typematch import typematch
from typematch import UnsupportedType


def test_unknown_type():
    try:
        typematch(True, "bool") is True
        assert False
    except UnsupportedType:
        pass


def test_bool():
    assert typematch(True, bool) is True
    assert typematch(False, bool) is True
    assert typematch(1, bool) is False
    assert typematch(1.0, bool) is False
    assert typematch([1, 2, 3], bool) is False
    assert typematch((1, 2, 3), bool) is False
    assert typematch(range(10), bool) is False
    assert typematch('str', bool) is False
    assert typematch(b'str', bool) is False
    assert typematch({1, 2, 3}, bool) is False
    assert typematch({'key': 'value'}, bool) is False
    assert typematch(None, bool) is False
    assert typematch(None, bool, allow_none=True) is True


def test_int():
    assert typematch(True, int) is False
    assert typematch(1, int) is True
    assert typematch(1.0, int) is False
    assert typematch([1, 2, 3], int) is False
    assert typematch((1, 2, 3), int) is False
    assert typematch(range(10), int) is False
    assert typematch('str', int) is False
    assert typematch(b'str', int) is False
    assert typematch({1, 2, 3}, int) is False
    assert typematch({'key': 'value'}, int) is False
    assert typematch(None, int) is False
    assert typematch(None, int, allow_none=True) is True

    # subclass
    class MyInt(int):
        pass

    assert typematch(MyInt(1), int) is True


def test_float():
    assert typematch(True, float) is False
    assert typematch(1, float) is False
    assert typematch(1.0, float) is True
    assert typematch([1, 2, 3], float) is False
    assert typematch((1, 2, 3), float) is False
    assert typematch(range(10), float) is False
    assert typematch('str', float) is False
    assert typematch(b'str', float) is False
    assert typematch({1, 2, 3}, float) is False
    assert typematch({'key': 'value'}, float) is False
    assert typematch(None, float) is False
    assert typematch(None, float, allow_none=True) is True

    # subclass
    class MyFloat(float):
        pass

    assert typematch(MyFloat(1.0), float) is True


def test_list():
    assert typematch(True, list) is False
    assert typematch(1, list) is False
    assert typematch(1.0, list) is False
    assert typematch([], list) is True
    assert typematch([1, 2, 3], list) is True
    assert typematch((1, 2, 3), list) is False
    assert typematch(range(10), list) is False
    assert typematch('str', list) is False
    assert typematch(b'str', list) is False
    assert typematch({1, 2, 3}, list) is False
    assert typematch({'key': 'value'}, list) is False
    assert typematch(None, list) is False
    assert typematch(None, list, allow_none=True) is True

    # subclass
    class MyList(list):
        pass

    assert typematch(MyList(), list) is True


def test_tuple():
    assert typematch(True, tuple) is False
    assert typematch(1, tuple) is False
    assert typematch(1.0, tuple) is False
    assert typematch([1, 2, 3], tuple) is False
    assert typematch(tuple(), tuple) is True
    assert typematch((1, 2, 3), tuple) is True
    assert typematch(range(10), tuple) is False
    assert typematch('str', tuple) is False
    assert typematch(b'str', tuple) is False
    assert typematch({1, 2, 3}, tuple) is False
    assert typematch({'key': 'value'}, tuple) is False
    assert typematch(None, tuple) is False
    assert typematch(None, tuple, allow_none=True) is True

    # subclass
    class MyTuple(tuple):
        pass

    assert typematch(MyTuple(), tuple) is True


def test_str():
    assert typematch(True, str) is False
    assert typematch(1, str) is False
    assert typematch(1.0, str) is False
    assert typematch([1, 2, 3], str) is False
    assert typematch((1, 2, 3), str) is False
    assert typematch(range(10), str) is False
    assert typematch('', str) is True
    assert typematch('str', str) is True
    assert typematch(b'str', str) is False
    assert typematch({1, 2, 3}, str) is False
    assert typematch({'key': 'value'}, str) is False
    assert typematch(None, str) is False
    assert typematch(None, str, allow_none=True) is True

    # subclass
    class MyStr(str):
        pass

    assert typematch(MyStr(), str) is True


def test_bytes():
    assert typematch(True, bytes) is False
    assert typematch(1, bytes) is False
    assert typematch(1.0, bytes) is False
    assert typematch([1, 2, 3], bytes) is False
    assert typematch((1, 2, 3), bytes) is False
    assert typematch(range(10), bytes) is False
    assert typematch('str', bytes) is False
    assert typematch(b'', bytes) is True
    assert typematch(b'str', bytes) is True
    assert typematch({1, 2, 3}, bytes) is False
    assert typematch({'key': 'value'}, bytes) is False
    assert typematch(None, bytes) is False
    assert typematch(None, bytes, allow_none=True) is True

    # subclass
    class MyBytes(bytes):
        pass

    assert typematch(MyBytes(), bytes) is True


def test_set():
    assert typematch(True, set) is False
    assert typematch(1, set) is False
    assert typematch(1.0, set) is False
    assert typematch([1, 2, 3], set) is False
    assert typematch((1, 2, 3), set) is False
    assert typematch(range(10), set) is False
    assert typematch('str', set) is False
    assert typematch(b'str', set) is False
    assert typematch(set(), set) is True
    assert typematch({1, 2, 3}, set) is True
    assert typematch({'key': 'value'}, set) is False
    assert typematch(None, set) is False
    assert typematch(None, set, allow_none=True) is True

    # subclass
    class MySet(set):
        pass

    assert typematch(MySet(), set) is True


def test_dict():
    assert typematch(True, dict) is False
    assert typematch(1, dict) is False
    assert typematch(1.0, dict) is False
    assert typematch([1, 2, 3], dict) is False
    assert typematch((1, 2, 3), dict) is False
    assert typematch(range(10), dict) is False
    assert typematch('str', dict) is False
    assert typematch(b'str', dict) is False
    assert typematch({1, 2, 3}, dict) is False
    assert typematch({}, dict) is True
    assert typematch({'key': 'value'}, dict) is True
    assert typematch(None, dict) is False
    assert typematch(None, dict, allow_none=True) is True

    # subclass
    class MyDict(dict):
        pass

    assert typematch(MyDict(), dict) is True
    assert typematch(OrderedDict(), dict) is True


def test_None():
    assert typematch(True, None) is False
    assert typematch(1, None) is False
    assert typematch(1.0, None) is False
    assert typematch([1, 2, 3], None) is False
    assert typematch((1, 2, 3), None) is False
    assert typematch(range(10), None) is False
    assert typematch('str', None) is False
    assert typematch(b'str', None) is False
    assert typematch({1, 2, 3}, None) is False
    assert typematch({'key': 'value'}, None) is False
    assert typematch(None, None) is True
    assert typematch(None, None, allow_none=True) is True


def test_Any():
    assert typematch(True, Any) is True
    assert typematch(1, Any) is True
    assert typematch(1.0, Any) is True
    assert typematch([1, 2, 3], Any) is True
    assert typematch((1, 2, 3), Any) is True
    assert typematch(range(10), Any) is True
    assert typematch('str', Any) is True
    assert typematch(b'str', Any) is True
    assert typematch({1, 2, 3}, Any) is True
    assert typematch({'key': 'value'}, Any) is True
    assert typematch(None, Any) is True
    assert typematch(None, Any, allow_none=True) is True


def test_Dict():
    assert typematch([], Dict) is False
    assert typematch({}, Dict[int, int]) is True
    assert typematch({1: 2}, Dict[int, int]) is True
    assert typematch({1: 2, 3: 4}, Dict[int, int]) is True
    assert typematch({'1': 2}, Dict[int, int]) is False
    assert typematch({1: '2'}, Dict[int, int]) is False
    assert typematch({1: 2, 3: '4'}, Dict[int, int]) is False


def test_List():
    assert typematch({}, List) is False
    assert typematch([], List[int]) is True
    assert typematch([1], List[int]) is True
    assert typematch([1, 2, 3], List[int]) is True
    assert typematch(['str'], List[int]) is False
    assert typematch([1, 2, '3'], List[int]) is False


def test_Optional():
    assert typematch(1, Optional[int]) is True
    assert typematch(None, Optional[int]) is True
    assert typematch('str', Optional[int]) is False


def test_Set():
    assert typematch([], Set) is False
    assert typematch(set(), Set[int]) is True
    assert typematch({1}, Set[int]) is True
    assert typematch({1, 2, 3}, Set[int]) is True
    assert typematch({'str'}, Set[int]) is False
    assert typematch({1, 2, '3'}, Set[int]) is False


def test_Tuple():
    assert typematch([], Tuple) is False
    assert typematch(tuple(), Tuple) is True
    assert typematch(tuple(), Tuple[int]) is False
    assert typematch((1,), Tuple[int]) is True
    assert typematch((1, 2, 3), Tuple[int]) is False
    assert typematch(('str',), Tuple[int]) is False
    assert typematch((1), Tuple[int, int]) is False
    assert typematch((1, 2), Tuple[int, int]) is True
    assert typematch((1, '2'), Tuple[int, int]) is False
    assert typematch((1, 2, 3), Tuple[int, ...]) is True


def test_Union():
    assert typematch(1, Union[int, str]) is True
    assert typematch('str', Union[int, str]) is True
    assert typematch(1.0, Union[int, str]) is False
    assert typematch(None, Union[int, str]) is False
