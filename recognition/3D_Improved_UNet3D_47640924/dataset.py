import numpy as np
import nibabel as nib
from tqdm import tqdm


# Function to load 3D medical image data from a list of file paths
def load_data_3D(imageNames, normImage=False, categorical=False, dtype=np.float32, getAffines=False, orient=False,
                 early_stop=False):
    '''
    Load medical image data from file paths into an array.

    This function pre-allocates 5D arrays for conv3d to avoid excessive memory usage.

    Parameters:
    - imageNames: List of file paths to Nifti files.
    - normImage: bool (default=False). Normalize the image to [0, 1] or mean 0, std 1.
    - categorical: bool (default=False). Convert image to categorical form (one-hot encoding).
    - dtype: Data type for the loaded images (default=np.float32). If dtype=np.uint8, data is assumed to be labels.
    - getAffines: bool (default=False). Whether to return affine matrices of images.
    - orient: bool (default=False). Whether to reorient and resample the image for better alignment.
    - early_stop: bool (default=False). Whether to stop loading early, for quick testing.
    '''

    affines = []  # List to store affine matrices for each image

    # Set interpolation method based on data type (labels use nearest interpolation)
    interp = 'linear'
    if dtype == np.uint8:  # Assuming labels, use nearest neighbor interpolation
        interp = 'nearest'

    # Load the first image to determine the fixed size for pre-allocation
    num = len(imageNames)
    niftiImage = nib.load(imageNames[0])

    # Reorient the image if needed
    if orient:
        niftiImage = im.applyOrientation(niftiImage, interpolation=interp, scale=1)

    # Extract image data as a NumPy array
    first_case = niftiImage.get_fdata(caching='unchanged')

    # Remove any extra dimensions if present
    if len(first_case.shape) == 4:
        first_case = first_case[:, :, :, 0]

    # Pre-allocate memory for images based on the determined shape
    if categorical:
        # Convert the data to one-hot encoded form and determine shape for pre-allocation
        first_case = to_channels(first_case, dtype=dtype)
        rows, cols, depth, channels = first_case.shape
        images = np.zeros((num, rows, cols, depth, channels), dtype=dtype)
    else:
        # If not categorical, pre-allocate 4D array
        rows, cols, depth = first_case.shape
        images = np.zeros((num, rows, cols, depth), dtype=dtype)

    # Iterate over each image file to load and process the data
    for i, inName in enumerate(tqdm(imageNames)):
        niftiImage = nib.load(inName)

        # Reorient the image if required
        if orient:
            niftiImage = im.applyOrientation(niftiImage, interpolation=interp, scale=1)

        # Get the image data as a NumPy array
        inImage = niftiImage.get_fdata(caching='unchanged')
        affine = niftiImage.affine  # Extract affine transformation matrix

        # Remove any extra dimensions if present
        if len(inImage.shape) == 4:
            inImage = inImage[:, :, :, 0]

        # Clip slices to match the depth of the initial case
        inImage = inImage[:, :, :depth]

        # Convert data type to specified type
        inImage = inImage.astype(dtype)

        # Normalize the image if required
        if normImage:
            inImage = (inImage - inImage.mean()) / inImage.std()

        # Convert to categorical form (one-hot encoding) if needed
        if categorical:
            inImage = to_channels(inImage, dtype=dtype)
            images[i, :inImage.shape[0], :inImage.shape[1], :inImage.shape[2],
            :] = inImage  # Store in pre-allocated array
        else:
            images[i, :inImage.shape[0], :inImage.shape[1], :inImage.shape[2]] = inImage  # Store in pre-allocated array

        # Append the affine transformation matrix to the list
        affines.append(affine)

        # Early stopping for testing purposes
        if i > 20 and early_stop:
            break

    # Return images along with affines if requested
    if getAffines:
        return images, affines
    else:
        return images

