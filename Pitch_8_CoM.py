import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import signal

############# Pitch 8 ##############
###################################################
# Step 1: Plot the amplitude versus time 
###################################################

# Return: Take the amplitudes of 4 signals and the time from excel file Pitch_1

data = pd.read_excel("Pitch_8.xlsx", skiprows = 74)
time =  pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]


###################################################
# Using subplot to plot 4 signals in 1 figure as a matrix 1x4
# Return: PLot the amplitudes of 4 signals versus time
###################################################

fig, (ampA, ampB, ampC, ampD) = plt.subplots(1, 4, sharex = True, sharey = True)
fig.suptitle("Amplitude versus time (Pitch 8)")

# Plot the amplitude of EMG signal A
ampA.plot(time, amp_A)
ampA.set_title ("EMG A")
ampA.grid(True)

# Plot the amplitude of EMG signal B
ampB.plot(time, amp_B, "tab:green")
ampB.set_title ("EMG B")
ampB.grid(True)

# Plot the amplitude of EMG signal C
ampC.plot(time, amp_C, "tab:red")
ampC.set_title ("EMG C")
ampC.grid(True)

# Plot the amplitude of EMG signal D
ampD.plot(time, amp_D, "tab:orange")
ampD.set_title ("EMG D")
ampD.grid(True)


###################################################
# Step 2: Plot the power spectral density(PSD) of signals
###################################################

# Using subplot to display 4 signals in 1 figure as a matrix 1x4
# Return: The graph of power of each signal per frequency band

fig, (ampA, ampB, ampC, ampD) = plt.subplots(1, 4, sharey = True)
fig.suptitle("Power Spectral Density (Pitch 8)")

# Plot the PSD of EMG signal A
freqs_A, psd_A = signal.welch(amp_A)
ampA.plot(freqs_A, psd_A)
ampA.set_title('EMG A')
ampA.grid(True)

# Plot the PSD of EMG signal B
freqs_B, psd_B = signal.welch(amp_B)
ampB.plot(freqs_B, psd_B, "tab:green")
ampB.set_title('EMG B')
ampB.grid(True)

# Plot the PSD of EMG signal C
freqs_C, psd_C = signal.welch(amp_C)
ampC.plot(freqs_C, psd_C, "tab:red")
ampC.set_title('EMG C')
ampC.grid(True)

# Plot the PSD of EMG signal D
freqs_D, psd_D = signal.welch(amp_D)
ampD.plot(freqs_D, psd_D, "tab:orange")
ampD.set_title('EMG D')
ampD.grid(True)


##########################################################
# Return: Find the coordinates and Plot a line through
# a "center of mass" of PSD
##########################################################
# Solution: Define a function "centroid (X, Y)" 
# with X is frequency, Y is PSD value
# Apply the function to each EMG signal
##########################################################

def centroid_poly(X, Y):
    N = len(X)
    # minimal sanity check
    if not (N == len(Y)): raise ValueError('X and Y must be same length.')
    elif N < 3: raise ValueError('At least 3 vertices must be passed.')
    sum_A, sum_Cx, sum_Cy = 0, 0, 0
    last_iteration = N-1
    # from 0 to N-1
    for i in range(N):
        if i != last_iteration:
            shoelace = X[i]*Y[i+1] - X[i+1]*Y[i]
            sum_A  += shoelace
            sum_Cx += (X[i] + X[i+1]) * shoelace
            sum_Cy += (Y[i] + Y[i+1]) * shoelace
        else:
            # N-1 case (last iteration): substitute i+1 -> 0
            shoelace = X[i]*Y[0] - X[0]*Y[i]
            sum_A  += shoelace
            sum_Cx += (X[i] + X[0]) * shoelace
            sum_Cy += (Y[i] + Y[0]) * shoelace
    A  = 0.5 * sum_A
    factor = 1 / (6*A)
    Cx = factor * sum_Cx
    Cy = factor * sum_Cy
    # returning abs of A is the only difference to
    # the algo from above link
    return Cx, Cy, abs(A)

#########################################################

#Apply function to signal EMG A
Ax_coor, Ay_coor, A = centroid_poly(freqs_A, psd_A)
ampA.scatter(Ax_coor, Ay_coor, color = 'black')
ampA.axvline(Ax_coor, color ='black', ls='--')
print("The coordinates of center of mass of EMG signal A are: " + str(Ax_coor) + " and " +  str(Ay_coor))

#Apply function to signal EMG B
Bx_coor, By_coor, A = centroid_poly(freqs_B, psd_B)
ampB.scatter(Bx_coor, By_coor, color = 'black')
ampB.axvline(Bx_coor, color ='black', ls='--')
print("The coordinates of center of mass of EMG signal B are: " + str(Bx_coor) + " and " +  str(By_coor))

#Apply function to signal EMG C
Cx_coor, Cy_coor, A = centroid_poly(freqs_C, psd_C)
ampC.scatter(Cx_coor, Cy_coor, color = 'black')
ampC.axvline(Cx_coor, color ='black', ls='--')
print("The coordinates of center of mass of EMG signal C are: " + str(Cx_coor) + " and " +  str(Cy_coor))

#Apply function to signal EMG D
Dx_coor, Dy_coor, A = centroid_poly(freqs_D, psd_D)
ampD.scatter(Dx_coor, Dy_coor, color = 'black')
ampD.axvline(Dx_coor, color ='black', ls='--')
print("The coordinates of center of mass of EMG signal D are: " + str(Dx_coor) + " and " +  str(Dy_coor))



