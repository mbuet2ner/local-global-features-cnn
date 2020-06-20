"""This module renders patches on an image using Pillow.
The patch size is variable.
The image is assumed to have equal side length!
"""

from math import trunc
from copy import deepcopy


class PatchImage:
    """Applies patches of a given size to a given image.
    The colour of the patches is configuarable with the 'colour'
    attribute.
    So is the patch size with the 'patch_sz' attribute.
    
    Yields:
        Pillow image -- first yields the single patched variants,
        then the final all_patched one
    """
    def __init__(self, image, patch_sz, colour=(0, 0, 0)):
        """Creates an 'PatchImage' with given image, patch size
        and colour.
        
        Arguments:
            image {Pillow image} -- the image that the patches are applied
            to
            patch_sz {int} -- the desired side length size of the patch
        
        Keyword Arguments:
            colour {tuple} -- the colour that is going to be applied.
            defaults to black (default: (0, 0, 0))
        """
        self.image = image
        self.colour = colour
        self.patch_sz = patch_sz
        self.patch_dict = {}
        self.image_sz = None
        self.border = None
        self._get_image_sz()
        self._calc_border()

    def _get_image_sz(self):
        """Simple helper method that gets image dimension
        accross one axis.
        """
        self.image_sz = self.image.size[0]

    def _calc_border(self):
        """Calculates the area the area that is not covered
        by the patches has therefore to be excluded.
        """
        patch_num = trunc(self.image_sz / self.patch_sz)
        # we need an uneven amount of patches
        if patch_num % 2 == 0:
            patch_num -= 1
        self.border = int((self.image_sz - (patch_num * self.patch_sz)) / 2)

    def _apply_patch(self, image, x_dim, y_dim):
        """Applies a patch with colour and given dimension and patch
        size.
        
        Arguments:
            image Pillow image -- image that patch is applied to
            x_dim {int} -- starting point of x dimension
            y_dim {int} -- starting point of y dimension
        """
        image.paste(
            self.colour,
            [x_dim, y_dim, x_dim + self.patch_sz, y_dim + self.patch_sz])

    def patch(self):
        """Umbrella method that calls '_apply_patch()' on both single-
        and patched variants and saves both to the dictionary
        'patch_dict'.

        Yields:
            Pillow image -- first yields the single patched variants,
            then the final all_patched one
        """
        # index for x dimension
        i = 0
        # index for y dimension
        j = 0
        all_patched = deepcopy(self.image)

        for y_dim in range(self.border, self.image_sz - self.border,
                           self.patch_sz):
            j += 1
            if j % 2 == 0:
                i += 1
                continue
            for x_dim in range(self.border, self.image_sz - self.border,
                               self.patch_sz):
                i += 1
                if i % 2 == 0:
                    continue
                single_patched = deepcopy(self.image)
                # apply patch to both temp image and patched images
                self._apply_patch(all_patched, x_dim, y_dim)
                self._apply_patch(single_patched, x_dim, y_dim)
                yield single_patched
        yield all_patched
