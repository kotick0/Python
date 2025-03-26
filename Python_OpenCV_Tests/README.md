## MISCELLANEOUS

1. KERNEL SIZE - Kernel as reading the image per matrix bases consists of 2 variables for example.: (3,3) will be an image in a size of 3 rows vertically and 3 rows horizontally.

2. IMAGE VECTORS - Vectors of an image are as follows [0] and [1]. Where [0] variable stands for height and [1] for width.

## BLURRING_METHODS

1. BLURRING AVERAGE MECHANISM - The most common blurring method is taking a center pixel of a kernel and inspecting pixel intensity of all of the pixels surrounding the center pixel. Than averaging the intensity of all surrounding pixels

2. BLURRING GAUSSIAN MECHANISM - Similar to averaging but here it doesn't count the average but rather puts a value(weight) to a specific pixel. This method gives a lighter but more natural blur.

3. BLURRING MEDIAN MECHANISM - Pretty self explanatory, basically you take the surrounding pixels but instead of averaging them you do a median.

4. BLURRING BILATERAL MECHANISM - Most effective method of blurring / used in a lot of projects. It essentially retains the root image edges smudging the rest of an image. IMPORTANT: setting the sigma space higher (last value parsed) indicates influence of pixels across the image.

## BITWISE_OPERATORS

1. BITWISE AND - Joins only the intersections of an image cutting the rest. (So for example.: If we take an image of a circle and rectangle we will get an image of round edged rectangle).

2. BITWISE OR - Joins intersecting and non intersecting parts of an image. (If we get the same objects as in the example before we get rectangle and circle on top of each other without cutting anything.)

3. BITWISE XOR - Shows only the NON intersecting regions.

4. BITWISE NOT - Inverts the colors in an image. (binary colors.)

## MASKING

1. MASKING - Allows to focus on certain parts of an image that we would like to focus on. It's useful when we work for example on a program designed for reading faces visible on an image or video.

2. SIZE - The size of a mask needs to be the same size as the image. Doing otherwise will output an error.

3. In masking we use the knowledge of bitwise operators to essentially draw on an image.

## HISTOGRAMS

1. HISTOGRAMS - Visualise the distribution and intensity of pixels on an image using a histogram (graph). Histograms are built with matplotlib module. On linux you have to also import some gtk specific modules.
2. COMPUTATION - Of histograms can be done with RGB/BGR images and grayscale images.

3. cv.calcHist - Needs following values to run: (['list of images'], [channels (of colors)], mask, [HistSize (Number of bins.)], [range of pixels (ex.: 0,256)])

4. COMBINING - Histograms with masks we can get pixel intensity of only a specific region of an image. [That way we can probably train a computer to look out for the specific histogram values on an image.]

## THRESHHOLDING

1. THRESHHOLDING - Is binarizing the image so it is easier to read for the computer. 

2. SIMPLE TRESHOLDING - Manual binirizing by taking the threshold value and the maximum value. cv.THRESH_BINARY or for inverted cv.THRESH_BINARY_INV.

3. ADAPTIVE THRESHOLDING - Build upon the computer choosing the right threshholding value for an image. Here we need to specify the neighborhood size of the kernel size and a "C" value.

4. ADAPTIVE METHODS - We can use a lot of diffrent adaptive thresholding methods simillar to blurring. One method we can use is for example the gaussian thresholding method.

## GRADIENTS

1. GRADIANTS - In mathematics gradients and edges are 2 completly difftent things. In programming we can get away with thinking as if they are the same thing.

2. ALGHORITMS - There are several alghoritms for computing gradiants. The multi level alghoritm is canny which at one part of computation uses Sobel alghoritm to compute the edges in the image. All alghoritms supported by OpenCV are as follows: Laplacian alghoritm, Sobel algorithm and Canny edge detection alghorithm.

3. SOBEL - Alghoritm takes x,y axis of an image and then it is up to us if we want to combine those two to make an image out of them. It is often used in more complicated computer vision projects.

4. CANNY - Alghoritm combines multiple alghoritms to make the final image. One of the canny algoritm stages initializes the Sobel computation alghotitm.

## FACE_DETECTION

1. OPENCV - Offers the built in face detection alghoritm as well as some additional ones on OpenCV github page under /data.

2. HAAR CASCADE - Face recognition alghoritm. It is a very popular algorithm tho it has a lot of downsides like for example.: It's prone to even the smallest noise in the image often recognizing noise in an image as faces. By tweaking the minNeighbors value we can get a cleaner image but it's important to remember this algotitm is not perfect.

3. ALGHORITMS - Are imported by putting the alghoritm code as a file in the project directory.

## FACE_RECOGNITION
