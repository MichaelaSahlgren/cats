import scipy.ndimage
import numpy

def

# read in the the drawing and convert to a matrix.
mask_matrisen = scipy.ndimage.imread('/home/michaela/katter/annotations/trimaps/pomeranian_62.png', flatten=False, mode=None)
#konvert outline and inside to 1:s and surrounding to 0
# FIXME: Would be nice to use a more elegant and efficient approach, something like this:
#filtrerad_mask_matrisen = numpy.abs(mask_matrisen - 2)

# Use a slower approach:
def mask_convert(val):
    if val == 2:
        return 0
    else:
        return 1

vfunc_mask_convert = numpy.vectorize(mask_convert)
filtrerad_mask_matrisen =  vfunc_mask_convert(mask_matrisen)

#read in the photo
foto_matrisen = scipy.ndimage.imread('/home/michaela/katter/images/pomeranian_62.jpg', flatten=False, mode=None)

# extract red,green and blur channel matrixes
red_matrix_foto = foto_matrisen[:,:,0]
green_matrix_foto = foto_matrisen[:,:,1]
blue_matrix_foto = foto_matrisen[:,:,2]

#modify the redgrenblue_matrixes so that they match the mask matrix
mod_red_matrix_foto = red_matrix_foto * filtrerad_mask_matrisen
mod_green_matrix_foto = green_matrix_foto * filtrerad_mask_matrisen
mod_blue_matrix_foto = blue_matrix_foto * filtrerad_mask_matrisen

#put it all back together into a matrix that can be viewed as a photo
fardig_matris = numpy.zeros(foto_matrisen.shape, dtype=numpy.uint8)
fardig_matris[:, :, 0] = mod_red_matrix_foto
fardig_matris[:, :, 1] = mod_green_matrix_foto
fardig_matris[:, :, 2] = mod_blue_matrix_foto

scipy.misc.imsave('testkatt4.png', fardig_matris, format='png')

#Save the matrixindexes of the pixels where the outline and the filling is in the drawing

#Load the corresponding image and turn into a matrix, with the same numer of indexes as the drawing.

# make everything that is not the same matrix index as the outline and filling in the corresponfing drawing blank.

