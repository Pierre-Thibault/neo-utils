# -*- coding: utf-8 -*-
'''
Tests neo_utils.core.

@author: Pierre Thibault (pierre.thibault1 -at- gmail.com)
@license: MIT
@since: 2010-11-10
'''

__docformat__ = "epytext en"

import unittest

from neo_utils.core import count
from neo_utils.core import every 
from neo_utils.core import inverse_linked_list
from neo_utils.core import Prototype
from neo_utils.core import negate
from neo_utils.core import some
from neo_utils.core import transform

class TestNeoUtils(unittest.TestCase):
    """TestNeoUtils the methods of the module """

    EMPTY_LIST = []
    ALL_FALSE = [False, 0, []]
    ALL_TRUE = [True, 1, -45, (1)]
    SOME_TRUE = (0, False, [1], [])
    
    @staticmethod
    def indentity(p):
        return p
    
    def assert_linked_list_order(self, linked_list, sequence_order):
        current_node = linked_list
        index = 0
        while current_node:
            self.assertEqual(current_node, sequence_order[index])
            current_node = current_node.next
            index += 1
        self.assertEqual(index, len(sequence_order))
    
    def test_every(self):
        self.assertTrue(every(TestNeoUtils.indentity, 
                              TestNeoUtils.EMPTY_LIST))
        self.assertFalse(every(TestNeoUtils.indentity, 
                               TestNeoUtils.ALL_FALSE))
        self.assertTrue(every(TestNeoUtils.indentity, 
                              TestNeoUtils.ALL_TRUE))
        self.assertFalse(every(TestNeoUtils.indentity, 
                               TestNeoUtils.SOME_TRUE))

    def test_count(self):
        self.assertEqual(0, count(TestNeoUtils.indentity, 
                                       TestNeoUtils.EMPTY_LIST))
        self.assertEqual(0, count(TestNeoUtils.indentity, 
                                  TestNeoUtils.ALL_FALSE))
        self.assertEqual(4, count(TestNeoUtils.indentity, 
                                  TestNeoUtils.ALL_TRUE))
        self.assertEqual(1, count(TestNeoUtils.indentity, 
                                  TestNeoUtils.SOME_TRUE))

    def test_inverse_linked_list(self):
        o1 = Prototype()
        o2 = Prototype()
        o3 = Prototype()
        o1.next = o2
        o2.next = o3
        o3.next = None
        self.assert_linked_list_order(inverse_linked_list(o1), (o3, o2, o1))
        self.assert_linked_list_order(inverse_linked_list(None), tuple())
        o1 = Prototype()
        o2 = Prototype()
        o1.next = o2
        o2.next = None
        self.assert_linked_list_order(inverse_linked_list(o1), (o2, o1))

    def test_negate(self):
        negation = negate(TestNeoUtils.indentity)
        result = []
        for i in TestNeoUtils.SOME_TRUE:
            result.append(negation(i))
        self.assertEqual(result, [True, True, False, True])

    def test_some(self):
        self.assertFalse(some(TestNeoUtils.indentity, 
                              TestNeoUtils.EMPTY_LIST))
        self.assertFalse(some(TestNeoUtils.indentity, TestNeoUtils.ALL_FALSE))
        self.assertTrue(some(TestNeoUtils.indentity, TestNeoUtils.ALL_TRUE))
        self.assertTrue(some(TestNeoUtils.indentity, TestNeoUtils.SOME_TRUE))
        
    def test_transform(self):
        l = [4, 5, 7]
        transform(lambda x: x + 1, l)
        self.assertEqual(l, [5, 6, 8])
        l = []
        transform(lambda x: x * x, l)
        self.assertEqual(l, [])
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'TestNeoUtils.testName']
    unittest.main()