"""This module allows to scramble an image array and export it with the
same dimensions as the original array.
Also inclues simple convenience methods for 'channels_first()' and
'channels_last()' conversion.

Part of the 'in_blocks()' code was borrowed from scikit-image:
https://github.com/scikit-image/scikit-image/blob/master/skimage/util/shape.py

Copyright (C) 2019, the scikit-image team
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the
    distribution.
 3. Neither the name of skimage nor the names of its contributors may be
    used to endorse or promote products derived from this software without
    specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

import numpy as np
from numpy.lib.stride_tricks import as_strided


def channels_first(image_array):
    """Converts an input image array to channels first representation.
    
    Arguments:
        image_array {numpy.array} -- the array of an image with channels in
        last dim
    
    Returns:
        image_array -- image array with channels in first dim
    """

    return np.moveaxis(image_array, -1, 0)


def channels_last(image_array):
    """Converts an input image array to channels last representation.
    
    Arguments:
        image_array {numpy.array} -- the array of an image with channels in
        first dim
    
    Returns:
        image_array -- image array with channels in last dim
    """

    return np.moveaxis(image_array, 0, -1)


class ScrambleImage():
    """A class that takes in an image array with channels first
    representation and represents it as blocks.
    The blocks dimension is given by 'block_sz'.
    These blocks can be shuffled and rearranged.
    If shuffled, the 'export()' method allows to get a shuffled
    image array back with also the respective change to the
    indices.
    
    Returns:
        numpy array, numpy array -- 'export()' returns possibly
        changed image array and changed indices.
    """
    def __init__(self, image_array, block_sz, channels=3):
        """Initializes the class instance with given arguments.
        
        Arguments:
            image_array {numpy.array} -- image array to be scrambled
            with channels first representation.
            block_sz {int} -- side length of the block
        
        Keyword Arguments:
            channels {int} -- number of colour channels of the image
            array (default: {3})
        """

        self.channels = channels
        self.block_sz = block_sz
        self.block_num = None
        self.blocks = None
        self.indices = None
        self._block_num(image_array)
        self._in_blocks(image_array)
        self._indices()

    def _block_num(self, image_array):
        """Calculates number of blocks generated accross one dim.
        Total block_num would be block_num*block_num.
        
        Arguments:
            image_array {numpy.array} -- array for which the block
            sizes is calculated
        """

        self.block_num = image_array.shape[1] // self.block_sz

    def _in_blocks(self, image_array):
        """Represents an image array as an array of image blocks.
        
        Arguments:
            image_array {numpy.array} -- image array to be represented
            as blocks
        """

        block_shape = np.array((self.channels, self.block_sz, self.block_sz))
        arr_shape = np.array(image_array.shape)

        image_array = np.ascontiguousarray(image_array)

        new_shape = tuple(arr_shape // block_shape) + tuple(block_shape)
        new_strides = tuple(
            image_array.strides * block_shape) + image_array.strides
        # get blocks representation of image
        blocks_arr = as_strided(image_array,
                                shape=new_shape,
                                strides=new_strides).squeeze()
        # reshape to have all blocks in first dim
        self.blocks = blocks_arr.reshape(self.block_num**2, self.channels,
                                         self.block_sz, self.block_sz)

    def _indices(self):
        """The indices of the unchanged array are stored to keep track
        if changes are made.
        """

        self.indices = np.arange(self.blocks.shape[0])

    def _reshape(self):
        """Reshapes the blocks array from e.g. (16,3,56) (4,4,3,56,56)
        to make processing easier.
        
        Returns:
            np.array -- array with the same dimension as original image
            array.
        """
        blocks_arr = self.blocks.reshape(self.block_num, self.block_num,
                                         self.channels, self.block_sz,
                                         self.block_sz)

        return np.block([list(column) for column in blocks_arr])

    def scramble(self):
        """Allows to shuffle the blocks. Also keeps track by storing
        change in the indices.
        """
        # shuffle indices and apply it to blocks
        np.random.shuffle(self.indices)
        self.blocks = self.blocks[self.indices]

    def export(self):
        """Exports the possibly shuffled image array with correct
        dimensions.
        
        Returns:
            np.array -- possibly shuffled image array with same dim
            as original image array
        """
        array = self._reshape()

        return self.indices, array
