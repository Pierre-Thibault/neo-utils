# -*- coding: utf-8 -*-
'''
Network utilities.

@author: Pierre Thibault (pierre.thibault1 -at- gmail.com)
@since: 2010-11-09
'''

__docformat__ = "epytext en"

def Base64Length(byte_length):
    """
    Calculate the maximum length needed to stock a base64 encoded stream of
    bytes.
    @param byte_length: Length of byte stream.
    @return: The length needed in byte. 
    """
    return ((byte_length + 3 - (byte_length % 3)) /3) * 4
