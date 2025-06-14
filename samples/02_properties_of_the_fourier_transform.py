from fast_fourier_transform import *
from numpy import linspace
import matplotlib.pyplot as plt
from cmath import cos, exp, phase
from math import degrees

# References: https://www.tutorialspoint.com/signals_and_systems/fourier_transforms_properties.htm

# For this file I'll designate the function Y(x) to be in the physical space, while U(f) = FT(Y)(f) is the Fourier
# Transform of Y(x) in the frequency space.
# I will also abbreviate the fourier transform as FT.

# ------------------------------------------------------------------------------------------------------------
# Parameters and Intro
k = 8
n = 2**k

print("Properties of the Fourier Transform \n")
input("---press enter to continue---")
print("\n \n")


# ------------------------------------------------------------------------------------------------------------
# 1. Linearity Property
#   If Y3(x) = a*Y1(x) + b*Y2(x), where a and b are scalars, then U3(f) = a*U1(f) + b*U2(f).
#
#   This also means that the Fourier Transform is a linear transformation on the set of functions F[m, n].

print('')
print("1. Linearity Property:"
      "    If Y3(x) = a*Y1(x) + b*Y2(x), where a and b are scalars, then U3(f) = a*U1(f) + b*U2(f)")
input("")

a, b = 3, 5
Y1 = lambda x: 2*exp(-3*x)
Y2 = lambda x: cos(8*pi*x)*exp(-2*x)
Y3 = lambda x: a*Y1(x) + b*Y2(x)

xRange = list(linspace(0, 1, n))
fRange = [f for f in range(n)]

y1Range = [Y1(x) for x in xRange]
y2Range = [Y2(x) for x in xRange]
y3Range = [Y3(x) for x in xRange]

u1Range = FFT(y1Range)
u1Abs = [abs(u1) for u1 in u1Range]
u2Range = FFT(y2Range)
u2Abs = [abs(u2) for u2 in u2Range]
u3Range = FFT(y3Range)
u3Abs = [abs(u3) for u3 in u3Range]

uLinearRange = [a*u1 + b*u2 for u1, u2 in zip(u1Range, u2Range)]
uLinearAbs = [abs(uL) for uL in uLinearRange]

# plot the two component physical functions Y1(x) and Y2(x) and the combined function Y(x)
fig, axis = plt.subplots(1)
fig.suptitle('Linearity Property of FT\n'
             'Components Y1(x) and Y2(x) and Their Combined Function Y(x)')
axis.plot(xRange, y1Range, label = 'Y1(x)')
axis.plot(xRange, y2Range, label = 'Y2(x)')
axis.plot(xRange, y3Range, label = 'Y(x) = 3*Y1(x) + 5*Y2(x)')
axis.set(xlabel = 'x', ylabel = 'Y1(x), Y2(x), and Combined Y(x)')
axis.legend()
plt.show()

# limit the frequency range
fMax = 20

# plot the fourier transforms U1(f) and U2(f) of the two component physical functions
fig, axis = plt.subplots(1)
fig.suptitle('Linearity Property of FT\n'
             'DFT Components U1(f) and U2(f) and their combined function U(f)')
axis.plot(fRange[:fMax], u1Abs[:fMax], label = 'U1(f)')
axis.plot(fRange[:fMax], u2Abs[:fMax], label = 'U2(f)')
axis.plot(fRange[:fMax], u3Abs[:fMax], label = 'U(f) = 3*U1(f) + 5*U2(f)')
axis.set(xlabel = 'f', ylabel = 'U1(f), U2(f), and combined U(f)')
axis.legend()
plt.show()


# ------------------------------------------------------------------------------------------------------------
# 2. Time Scaling Property
#   If Y(x) has an FT called U(f), then Y(ax) has the FT   1/|a| * U(f/a) for any scalar a.

print('')
print('2. Time Scaling Property:'
      '  If Y(x) has an FT called U(f), then Y(ax) has the FT   1/|a| * U(f/a) for any scalar a.')
input("")

a = 3
Y = lambda x: cos(20*pi*x)*exp(-2*x)
Yscaled = lambda x: Y(a*x)

xRange = list(linspace(0, 1, n))
fRange = [f for f in range(n)]

yRange = [Y(x) for x in xRange]
yScaledRange = [Yscaled(x) for x in xRange]

uRange = FFT(yRange)
uAbs = [abs(u) for u in uRange]
uScaledRange = FFT(yScaledRange)
uScaledAbs = [abs(u) for u in uScaledRange]


# plot the original function and the scaled function
fig, axis = plt.subplots(1)
axis.plot(xRange, yRange, label = 'Y1(x) = cos(20πx)*exp(-2x)')
axis.plot(xRange, yScaledRange, label = 'Y2(x) = Y1(3x) = cos(60πx)*exp(-6x)')
fig.suptitle('Scaling Property of FT\n'
             'Function Y1(x) and Scaled Function Y2(x) = Y1(3x)')
axis.set_xlabel('x')
axis.set_ylabel('Y1(x), Y2(x)')
axis.legend()
plt.show()

# limit the frequency range
fMax = 80

# plot the fourier transforms of the original function and of the scaled function
fig, axis = plt.subplots(1)
axis.plot(fRange[:fMax], uAbs[:fMax],   label = 'U1(f)')
axis.plot(fRange[:fMax], uScaledAbs[:fMax],  label = 'U2(f) = U1(f/3)/3')
fig.suptitle('Scaling Property of FT\n'
             'DFT U1(f) of Y1(x) and the DFT U2(f) of the Scaled Function Y2 = Y1(3x)')
axis.set_xlabel('f')
axis.set_ylabel('U1(f),  U2(f)')
axis.legend()
print(f"Actual Ratio Between Heights of the Peaks U1/U2 = {uAbs[10] / uScaledAbs[30]:.2f}")
print(f"Expected Ratio Between Heights of the Peaks U1/U2 = 3.00")
plt.show()

# You can see that the peak of the orange graph (which is the FT of Y(a*x)) has a lower peak that is roughly
# one-third of that of the blue peak, but is three times farther to the right of the graph since dividing f
# by a = 3 stretches the graph thrice in the horizontal direction.
#
# Note here that f is the same variable in U(f) and 1/|a| * U(f/a)



# ------------------------------------------------------------------------------------------------------------
# 3. Differentiation Property
#   If Y(x) has an FT called U(f), then dY(x)/dx has an FT which is i*f*U(f).
#
#   This makes sense since the derivative or velocity of a vector moving around a circle is 90 degrees to it
#   and hence we multiply by the imaginary number i to add 90 degrees to the FT values.
#
#   Since we cannot visualize the complex numbers on a graph, we will just show that their phase angles are
#   changed by 90 degrees and that the FT of the derivative increases with frequency.

print('3. Differentiation Property'
      ' If Y(x) has an FT called U(f), then dY(x)/dx has an FT which is i*f*U(f).\n\n'
      ''
      'SIDE NOTE: For some reason, FFT and IFFT do not follow this property as well as the other two properties.')
input("")

Y = lambda x: exp(-6*x)
Yderivative = lambda x: -6*exp(-6*x)

xRange = list(linspace(0, 1, n))
fRange = [f for f in range(n)]

yRange = [Y(x) for x in xRange]
yDerivativeRange = [Yderivative(x) for x in xRange]

uRange = FFT(yRange)
uAbs = [abs(u) for u in uRange]
uPhase = [degrees(phase(u)) for u in uRange]

uDerivativeRange = FFT(yDerivativeRange)
uDerivativeAbs = [abs(u) for u in uDerivativeRange]
uDerivativePhase = [degrees(phase(u)) for u in uDerivativeRange]

uPhaseDifference = [u2 - u1 for u1, u2 in zip(uPhase, uDerivativePhase)]

uComparisonRange = [f*(1j)*u for f, u in zip(fRange, uRange)]
uComparisonAbs = [abs(u) for u in uComparisonRange]
uComparisonPhase = [degrees(phase(u)) for u in uComparisonRange]

# setup pyplot
fig, ax = plt.subplots(figsize=(8, 6))

# plot the original function and its derivative
ax.plot(xRange, yRange, label="Y(x) = exp(-6x)")
ax.plot(xRange, yDerivativeRange, label= "dY/dx = -6*exp(-6x)")   # much larger in magnitude than yRange
ax.set_xlabel('Physical Variable [x]')
ax.set_ylabel('Physical Magnitudes [y = Y(x), dY(x)/dx]')
fig.suptitle('Attempt at Showing Differentiation Property of FT\n'
             'Functions Y(x) and Its Derivative dY/dx')
ax.legend()
plt.show()

# limit the frequency range
fMax = 20

# plot the magnitudes of the fourier transforms of the original function and of its derivative
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(fRange[:fMax], uAbs[:fMax], label="DFT of Y(x) = exp(-6x)")
ax.plot(fRange[:fMax], uDerivativeAbs[:fMax], label="DFT of dy/dx = -6*exp(-6x)")
ax.plot(fRange[:fMax], uComparisonAbs[:fMax], label="Expected FT of exp(-6x)")
ax.set_xlabel('frequency [f]')
ax.set_ylabel('frequency magnitudes [u = U(f), i*f*U(f)]')
fig.suptitle('Attempt at Showing Differentiation Property of FT\n'
             'Comparison Between Magnitudes of DFT of Y(x) and Expected FT of Y(x)')
ax.legend()
plt.show()

# plot the phase difference between the fourier transforms of the original function and of its derivative
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(fRange[:fMax], uPhaseDifference[:fMax])
ax.set_xlabel('frequency [f]')
ax.set_ylabel('frequency phases in degrees [u = U(f), i*f*U(f)]')
fig.suptitle('Attempt at Showing Differentiation Property of FT\n'
             'Phase Difference between DFT of Y(x) and Expected FT of Y(x)')
plt.show()
