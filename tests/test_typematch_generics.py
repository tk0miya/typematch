# -*- coding: utf-8 -*-

from typing import (
    AbstractSet, ByteString, Container, Hashable, ItemsView, Iterable, Iterator,
    KeysView, Mapping, MappingView, MutableMapping, MutableSequence, MutableSet,
    Reversible, Sequence, Sized, ValuesView
)

from typematch import typematch


def test_AbstractSet():
    assert typematch(True, AbstractSet) is False
    assert typematch(1, AbstractSet) is False
    assert typematch(1.0, AbstractSet) is False
    assert typematch([1, 2, 3], AbstractSet) is False
    assert typematch((1, 2, 3), AbstractSet) is False
    assert typematch(range(10), AbstractSet) is False
    assert typematch('str', AbstractSet) is False
    assert typematch(b'str', AbstractSet) is False
    assert typematch({1, 2, 3}, AbstractSet) is True
    assert typematch({'key': 'value'}, AbstractSet) is False
    assert typematch(None, AbstractSet) is False
    assert typematch(None, AbstractSet, allow_none=True) is True


def test_ByteString():
    assert typematch(True, ByteString) is False
    assert typematch(1, ByteString) is False
    assert typematch(1.0, ByteString) is False
    assert typematch([1, 2, 3], ByteString) is False
    assert typematch((1, 2, 3), ByteString) is False
    assert typematch(range(10), ByteString) is False
    assert typematch('str', ByteString) is False
    assert typematch(b'str', ByteString) is True
    assert typematch({1, 2, 3}, ByteString) is False
    assert typematch({'key': 'value'}, ByteString) is False
    assert typematch(None, ByteString) is False
    assert typematch(None, ByteString, allow_none=True) is True


def test_Container():
    assert typematch(True, Container) is False
    assert typematch(1, Container) is False
    assert typematch(1.0, Container) is False
    assert typematch([1, 2, 3], Container) is True
    assert typematch((1, 2, 3), Container) is True
    assert typematch(range(10), Container) is True
    assert typematch('str', Container) is True
    assert typematch(b'str', Container) is True
    assert typematch({1, 2, 3}, Container) is True
    assert typematch({'key': 'value'}, Container) is True
    assert typematch(None, Container) is False
    assert typematch(None, Container, allow_none=True) is True


def test_Hashable():
    assert typematch(True, Hashable) is True
    assert typematch(1, Hashable) is True
    assert typematch(1.0, Hashable) is True
    assert typematch([1, 2, 3], Hashable) is False
    assert typematch((1, 2, 3), Hashable) is True
    assert typematch(range(10), Hashable) is True
    assert typematch('str', Hashable) is True
    assert typematch(b'str', Hashable) is True
    assert typematch({1, 2, 3}, Hashable) is False
    assert typematch({'key': 'value'}, Hashable) is False
    assert typematch(None, Hashable) is True
    assert typematch(None, Hashable, allow_none=True) is True


def test_ItemsView():
    assert typematch(1, ItemsView) is False
    assert typematch({'key': 'value'}, ItemsView) is False
    assert typematch({'key': 'value'}.items(), ItemsView) is True
    assert typematch({'key': 'value'}.keys(), ItemsView) is False
    assert typematch({'key': 'value'}.values(), ItemsView) is False
    assert typematch(None, ItemsView) is False
    assert typematch(None, ItemsView, allow_none=True) is True


def test_Iterable():
    assert typematch(True, Iterable) is False
    assert typematch(1, Iterable) is False
    assert typematch(1.0, Iterable) is False
    assert typematch([1, 2, 3], Iterable) is True
    assert typematch((1, 2, 3), Iterable) is True
    assert typematch(range(10), Iterable) is True
    assert typematch('str', Iterable) is True
    assert typematch(b'str', Iterable) is True
    assert typematch({1, 2, 3}, Iterable) is True
    assert typematch({'key': 'value'}, Iterable) is True
    assert typematch(None, Iterable) is False
    assert typematch(None, Iterable, allow_none=True) is True


def test_Iterator():
    assert typematch(1, Iterator) is False
    assert typematch([1, 2, 3], Iterator) is False
    assert typematch(iter([1, 2, 3]), Iterator) is True
    assert typematch((1, 2, 3), Iterator) is False
    assert typematch(iter((1, 2, 3)), Iterator) is True
    assert typematch('str', Iterator) is False
    assert typematch(iter('str'), Iterator) is True
    assert typematch(None, Iterator) is False
    assert typematch(None, Iterator, allow_none=True) is True


def test_KeysView():
    assert typematch(1, KeysView) is False
    assert typematch({'key': 'value'}, KeysView) is False
    assert typematch({'key': 'value'}.items(), KeysView) is False
    assert typematch({'key': 'value'}.keys(), KeysView) is True
    assert typematch({'key': 'value'}.values(), KeysView) is False
    assert typematch(None, KeysView) is False
    assert typematch(None, KeysView, allow_none=True) is True


def test_Mapping():
    assert typematch(True, Mapping) is False
    assert typematch(1, Mapping) is False
    assert typematch(1.0, Mapping) is False
    assert typematch([1, 2, 3], Mapping) is False
    assert typematch((1, 2, 3), Mapping) is False
    assert typematch(range(10), Mapping) is False
    assert typematch('str', Mapping) is False
    assert typematch(b'str', Mapping) is False
    assert typematch({1, 2, 3}, Mapping) is False
    assert typematch({'key': 'value'}, Mapping) is True
    assert typematch(None, Mapping) is False
    assert typematch(None, Mapping, allow_none=True) is True


def test_MappingView():
    assert typematch(1, MappingView) is False
    assert typematch({'key': 'value'}, MappingView) is False
    assert typematch({'key': 'value'}.items(), MappingView) is True
    assert typematch({'key': 'value'}.keys(), MappingView) is True
    assert typematch({'key': 'value'}.values(), MappingView) is True
    assert typematch(None, MappingView) is False
    assert typematch(None, MappingView, allow_none=True) is True


def test_MutableMapping():
    assert typematch(True, MutableMapping) is False
    assert typematch(1, MutableMapping) is False
    assert typematch(1.0, MutableMapping) is False
    assert typematch([1, 2, 3], MutableMapping) is False
    assert typematch((1, 2, 3), MutableMapping) is False
    assert typematch(range(10), MutableMapping) is False
    assert typematch('str', MutableMapping) is False
    assert typematch(b'str', MutableMapping) is False
    assert typematch({1, 2, 3}, MutableMapping) is False
    assert typematch({'key': 'value'}, MutableMapping) is True
    assert typematch(None, MutableMapping) is False
    assert typematch(None, MutableMapping, allow_none=True) is True


def test_MutableSequence():
    assert typematch(True, MutableSequence) is False
    assert typematch(1, MutableSequence) is False
    assert typematch(1.0, MutableSequence) is False
    assert typematch([1, 2, 3], MutableSequence) is True
    assert typematch((1, 2, 3), MutableSequence) is False
    assert typematch(range(10), MutableSequence) is False
    assert typematch('str', MutableSequence) is False
    assert typematch(b'str', MutableSequence) is False
    assert typematch({1, 2, 3}, MutableSequence) is False
    assert typematch({'key': 'value'}, MutableSequence) is False
    assert typematch(None, MutableSequence) is False
    assert typematch(None, MutableSequence, allow_none=True) is True


def test_MutableSet():
    assert typematch(True, MutableSet) is False
    assert typematch(1, MutableSet) is False
    assert typematch(1.0, MutableSet) is False
    assert typematch([1, 2, 3], MutableSet) is False
    assert typematch((1, 2, 3), MutableSet) is False
    assert typematch(range(10), MutableSet) is False
    assert typematch('str', MutableSet) is False
    assert typematch(b'str', MutableSet) is False
    assert typematch({1, 2, 3}, MutableSet) is True
    assert typematch({'key': 'value'}, MutableSet) is False
    assert typematch(None, MutableSet) is False
    assert typematch(None, MutableSet, allow_none=True) is True


def test_Sequence():
    assert typematch(True, Sequence) is False
    assert typematch(1, Sequence) is False
    assert typematch(1.0, Sequence) is False
    assert typematch([1, 2, 3], Sequence) is True
    assert typematch((1, 2, 3), Sequence) is True
    assert typematch(range(10), Sequence) is True
    assert typematch('str', Sequence) is True
    assert typematch(b'str', Sequence) is True
    assert typematch({1, 2, 3}, Sequence) is False
    assert typematch({'key': 'value'}, Sequence) is False
    assert typematch(None, Sequence) is False
    assert typematch(None, Sequence, allow_none=True) is True


def test_Sized():
    assert typematch(True, Sized) is False
    assert typematch(1, Sized) is False
    assert typematch(1.0, Sized) is False
    assert typematch([1, 2, 3], Sized) is True
    assert typematch((1, 2, 3), Sized) is True
    assert typematch(range(10), Sized) is True
    assert typematch('str', Sized) is True
    assert typematch(b'str', Sized) is True
    assert typematch({1, 2, 3}, Sized) is True
    assert typematch({'key': 'value'}, Sized) is True
    assert typematch(None, Sized) is False
    assert typematch(None, Sized, allow_none=True) is True


def test_ValuesView():
    assert typematch(1, ValuesView) is False
    assert typematch({'key': 'value'}, ValuesView) is False
    assert typematch({'key': 'value'}.items(), ValuesView) is False
    assert typematch({'key': 'value'}.keys(), ValuesView) is False
    assert typematch({'key': 'value'}.values(), ValuesView) is True
    assert typematch(None, ValuesView) is False
    assert typematch(None, ValuesView, allow_none=True) is True
