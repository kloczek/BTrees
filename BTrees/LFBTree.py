##############################################################################
#
# Copyright (c) 2001-2012 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

__all__ = ('Bucket', 'Set', 'BTree', 'TreeSet',
           'LFBucket', 'LFSet', 'LFBTree', 'LFTreeSet',
           'union', 'intersection', 'difference',  
           'weightedUnion', 'weightedIntersection', 'multiunion',
          )

from zope.interface import moduleProvides

from .Interfaces import IIntegerFloatBTreeModule
from ._base import Bucket
from ._base import MERGE
from ._base import MERGE_WEIGHT_numeric
from ._base import MERGE_DEFAULT_float
from ._base import Set
from ._base import Tree as BTree
from ._base import TreeSet
from ._base import difference as _difference
from ._base import intersection as _intersection
from ._base import multiunion as _multiunion
from ._base import setop as _setop
from ._base import to_long as _to_key
from ._base import to_float as _to_value
from ._base import union as _union
from ._base import weightedIntersection as _weightedIntersection
from ._base import weightedUnion as _weightedUnion

_BUCKET_SIZE = 120
_TREE_SIZE = 500
using64bits = True


class LFBucketPy(Bucket):
    MAX_SIZE = _BUCKET_SIZE
    _to_key = _to_key
    _to_value = _to_value
    MERGE = MERGE
    MERGE_WEIGHT = MERGE_WEIGHT_numeric
    MERGE_DEFAULT = MERGE_DEFAULT_float


class LFSetPy(Set):
    MAX_SIZE = _BUCKET_SIZE
    _to_key = _to_key
    MERGE = MERGE
    MERGE_WEIGHT = MERGE_WEIGHT_numeric
    MERGE_DEFAULT = MERGE_DEFAULT_float


class LFBTreePy(BTree):
    MAX_SIZE = _TREE_SIZE
    _to_key = _to_key
    _to_value = _to_value
    MERGE = MERGE
    MERGE_WEIGHT = MERGE_WEIGHT_numeric
    MERGE_DEFAULT = MERGE_DEFAULT_float


class LFTreeSetPy(TreeSet):
    MAX_SIZE = _TREE_SIZE
    _to_key = _to_key
    MERGE = MERGE
    MERGE_WEIGHT = MERGE_WEIGHT_numeric
    MERGE_DEFAULT = MERGE_DEFAULT_float


# Can't declare forward refs, so fix up afterwards:

LFBucketPy._mapping_type = LFBucketPy._bucket_type = LFBucketPy
LFBucketPy._set_type = LFSetPy

LFSetPy._mapping_type = LFBucketPy
LFSetPy._set_type = LFSetPy._bucket_type = LFSetPy

LFBTreePy._mapping_type = LFBTreePy._bucket_type = LFBucketPy
LFBTreePy._set_type = LFSetPy

LFTreeSetPy._mapping_type = LFBucketPy
LFTreeSetPy._set_type = LFTreeSetPy._bucket_type = LFSetPy


differencePy = _setop(_difference, LFSetPy)
unionPy = _setop(_union, LFSetPy)
intersectionPy = _setop(_intersection, LFSetPy)
multiunionPy = _setop(_multiunion, LFSetPy)
weightedUnionPy = _setop(_weightedUnion, LFSetPy)
weightedIntersectionPy = _setop(_weightedIntersection, LFSetPy)

try:
    from _LFBTree import LFBucket
    from _LFBTree import LFSet
    from _LFBTree import LFBTree
    from _LFBTree import LFTreeSet
    from _LFBTree import difference
    from _LFBTree import union
    from _LFBTree import intersection
    from _LFBTree import multiunion
    from _OIBTree import weightedUnion
    from _OIBTree import weightedIntersection
except ImportError: #pragma NO COVER
    LFBucket = LFBucketPy
    LFSet = LFSetPy
    LFBTree = LFBTreePy
    LFTreeSet = LFTreeSetPy
    difference = differencePy
    union = unionPy
    intersection = intersectionPy
    multiunion = multiunionPy
    weightedUnion = weightedUnionPy
    weightedIntersection = weightedIntersectionPy

Bucket = LFBucket
Set = LFSet
BTree = LFBTree
TreeSet = LFTreeSet

moduleProvides(IIntegerFloatBTreeModule)
