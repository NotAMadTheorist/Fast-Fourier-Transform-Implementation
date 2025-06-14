from fast_fourier_transform import *
from numpy import linspace
import matplotlib.pyplot as plt
from cmath import sin

# if the inputs of the FFT are y-coordinates then the x-coordinates are simply equally spaced numbers on the
# interval [0, s], where s is an arbitrary scaling factor

# then the output of the FFT are frequency values (in Hertz if x-coordinates are seconds) that are equally spaced
# on the interval [0, (2**n - 1)/s].

# In this case, we have s = 1, so the FFT translates from y-values on an x-interval [0, 1] to complex fourier
# values on a frequency interval [0, 2**n - 1]. The IFFT does the reverse process.

# parameters
k = 8
n = 2**k

# function to evaluate
Y = lambda x: sin(2*pi*x*13) + sin(2*pi*x*25)
xVals = linspace(0, 1, n)
yVals = [Y(x) for x in xVals]

# show graph of original function
fig, axis = plt.subplots(1)
axis.plot(xVals, yVals)
axis.set(xlabel="x", ylabel="Y(x)")
axis.set_title("Original Function\nY(x) = sin(2π*13x) + sin(2π*25x)")
plt.show()

# take the fourier transform of f(x)
fVals = [f for f in range(n)]
uVals = FFT(yVals)
uMagnitudes = [abs(u) for u in uVals]   # what we are plotting here is also called a Power Spectrum

# show the magnitudes of the fourier transform
fig, axis = plt.subplots(1)
axis.plot(fVals[:], uMagnitudes[:])
axis.plot([128, 128], [0, max(uMagnitudes)], linestyle = 'dashed')
axis.set(xlabel = "f", ylabel = "|U(f)|")
axis.set_title("Discrete Fourier Transform U(f)")
plt.show()

# if the inputs of the IFFT are frequency values (in Hertz if x-coordinates are seconds) that are equally spaced
# on the interval [0, (2**n - 1)/s],
#
# then the output of the IFFT are y-coordinates whose x-coordinates are simply equally spaced numbers on the
# interval [0, s], where s is an arbitrary scaling factor

# take the inverse fourier transform to get back the original function
yValsComplex = IFFT(uVals)
newYVals = [y.real for y in yValsComplex]

# show the reconstructed original function
fig, axis = plt.subplots(1)
axis.plot(xVals, newYVals)
axis.set(xlabel="x", ylabel="Y(x)")
axis.set_title("Inverse FFT Yields the Original Function\nY(x) = sin(2π*13x) + sin(2π*25x)")
plt.show()