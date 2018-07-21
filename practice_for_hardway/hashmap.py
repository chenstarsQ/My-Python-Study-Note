#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-07-10 22:25:21
# @Author  : Star (1140330611@qq.com)
# @Link    : ${link}
# @Version : $Id$


def new(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    aMap = []  # 创建一个包含列表的变量aMap
    for i in range(0, num_buckets):  # num_buckets用来存放给hashmap设置的内容
        aMap.append([])  # 将num_buckets放入aMap
    return aMap
# 创建函数生成hashmap的开始，即初始化。


def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to
    an index for the aMap's buckets."""
    return hash(key) % len(aMap)
# 用hash()函数将字符转化为长数字，之后采用 % 将长数字缩小
# 限制大数）来获得一个较小的数字。
# 是dict如何工作的核心


def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]
# 使用hash_key()来找到一个Key所在的位置（bucket_id）


def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found.
    """
    bucket = get_bucket(aMap, key)
    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v
    return -1, key, default
# enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个
# 索引序列，同时列出数据和数据下标，一般用在 for 循环当中
# get_slot() 使用get_bucket() 来获得一个Key的bucket，之后通过遍历bucket
# 中的每一个元素来获得对应的Key，之后返回一个(i, K, v)的元组，
# i 是Key的下标，K 是key本身，v是Key的值。


def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default)
    return v
# 使用get_slot()获得i, k, v 但只返回v


def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)
    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not, append to create it
        bucket.append((key, value))
# 对字典bucket进行set，并实现无此键值新增（append），
# 有此键值则覆盖（bucke[i] = (key, value)）


def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)
    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break
# xrange() 与range() 使用方法类似，不同的是xrange()
# 为一生成器（单个数），而range()则生成一数列（一组数）

def list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print(k, v)
