from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def entropy(signal):
    signal = signal/255.0
    lensig = signal.size
    symset = list(set(signal))
    propab = [np.size(signal[signal == i])/(1.0*lensig) for i in symset]
    ent = np.sum([p*np.log2(1.0/p) for p in propab])*255
    return ent

IMAGE_PATH = "PATH_TO_IMAGE"

greyIm = Image.open(IMAGE_PATH)
greyIm.thumbnail((250, 250))
greyIm = np.array(greyIm)

N = 5
S = greyIm.shape
E = greyIm.copy()

for row in range(S[0]):
    for col in range(S[1]):
        Lx = np.max([0, col - N])
        Ux = np.min([S[1], col + N])

        Ly = np.max([0, row - N])
        Uy = np.min([S[1], row + N])

        region = greyIm[Ly:Uy, Lx:Ux].flatten()
        E[row, col] = entropy(region)


plt.imshow(E)
plt.show()
