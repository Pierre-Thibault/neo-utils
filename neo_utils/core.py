# -*- coding: utf-8 -*-
'''
Fundamental functions and class helpers to support everyday programming. 
@author: Pierre Thibault (pierre.thibault1 -at- gmail.com)
@license: MIT
@since: 2010-11-10
'''

__docformat__ = "epytext en"

import functools

class Prototype:
    """
    An empty class to create objects as prototypes.
    Client are free to add properties to instances of this type. I created
    this class because we cannot do the same with object type. 
    """
    
def count(predicate, iterable):
    """
    Iterate over iterable, pass the value to the predicate predicate and
    return the number of times the predicate returns value considered True.
    @param predicate: Predicate function.
    @param iterable: Iterable containing the elements to count.
    @return: The number of true element.
    """
    result = 0L
    for i in iterable:
        if predicate(i):
            result += 1
    return result

def every(predicate, iterable):
    """
    Iterate over iterable, pass the value to the predicate predicate and
    return True if all the predicate returns True for all the values.
    @param  predicate: Predicate function.
    @param iterable: Iterable containing the elements to test.
    @return: Return True if all the elements are True based on the predicate.
    If iterable is empty, it returns True.
    """
    for i in iterable:
        if not predicate(i):
            return False
    return True

def inverse_linked_list(list_to_inverse, next_node_property_name="next"):
    """
    A linked list inversor. No new nodes are created. 
    @param list_to_inverse: The linked list to inverse.
    @param next_node_property_name: The name of property pointing to the next
    node.
    @return: The head of the inversed list.
    """
    source_current_node = list_to_inverse
    dest_head = None
    while source_current_node:
        old_source_head_next = getattr(source_current_node, 
                                       next_node_property_name)
        setattr(source_current_node, next_node_property_name, dest_head)
        dest_head = source_current_node
        source_current_node = old_source_head_next
    return dest_head

def negate(function):
    """
    Return the opposite function of function.
    @param function: The function to negate.
    @return: The negated function.
    """
    @functools.wraps(function)
    def result(*args, **keywords):
        return not function(*args, **keywords)
    return result

def some(predicate, iterable):
    """
    Iterate over iterable, pass the value to the predicate predicate and
    return True if the predicate returns True at least one time.
    @param  predicate: Predicate function.
    @param iterable: Iterable containing the elements to test.
    @return: Return True if any element is True based on the predicate.
    If iterable is empty, it returns False.
    """
    for i in iterable:
        if predicate(i):
            return True
    return False

def transform(func, sequence):
    """
    Process all the elements in sequence with func and store the result again
    in sequence at the same place. Sequence must be mutable.
    @param func: Transformation function.
    @param sequence: The sequence to process.
    """
    for index, value in enumerate(sequence):
        sequence[index] = func(value)

