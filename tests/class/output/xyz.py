#!/usr/bin/env python2

# xyz
# Copyright (C) 2014  xyz developers  (see AUTHORS)
#
# All rights reserved.

class MyClass(object):

    def __init__(self):
        b = 5

class MyAbstractClass(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class MyChildClass(MyAbstractClass):

    def __init__(self, a, b, c):
        super(MyChildClass, self).__init__(a,b,c)

