'''
This implementation of the radon transform is By Romberg and Birkfellner.
It is a very simple implementation and do not use the trick with subpixels
as Matlab does. But however, the reconstruction will be our main task.

Matlab still gets better results. The goal should be to be as good as matlab
'''

# import cv2
import matplotlib.pyplot as plt
# import scipy.ndimage
# from PIL import Image
import numpy as np
import scipy.misc  # install pil before
# Read File (later it will be a txt File)
# img = cv2.imread('phantom.png', 0)

# Here for now
img = np.loadtxt('TestI.txt')

# Define needed parameter
Theta = np.arange(180.)
iLength, iWidth = np.shape(img)
iDiag = np.sqrt(iLength*iLength + iWidth*iWidth)
LengthPad = np.ceil(iDiag-iLength) + 2
WidthPad = np.ceil(iDiag-iWidth) + 2

# Define zeros padIMG big enough to rotate and fill with image data
allLength = int(iLength + LengthPad)
allWidth = int(iWidth + WidthPad)
padIMG = np.zeros((allLength, allWidth))
xStart = int(np.ceil(LengthPad/2) - 1)
xEnd = int(np.ceil(LengthPad/2) + iLength - 1)
yStart = int(np.ceil(WidthPad/2) - 1)
yEnd = int(np.ceil(WidthPad/2) + iWidth - 1)
padIMG[xStart:xEnd][:, yStart:yEnd] = img

# Start the radon transform by rotating the image. This is very slow. Need a new algorithm
n = np.size(Theta)
parallelRadon = np.zeros((padIMG.shape[1], n))
for i in range(0, n-1):
    tempimg = scipy.misc.imrotate(padIMG, -Theta[i], interp='bilinear')
    tempSum = np.sum(tempimg, axis=0)
    parallelRadon[:, i] = tempSum.T

# np.savetxt('Test.txt', parallelRadon)
plt.imshow(parallelRadon, extent=[0, 1, 0, 1])
plt.show()

'''
cv2.imshow('ImageWindow', parallelRadon)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
