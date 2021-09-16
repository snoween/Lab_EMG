import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from scipy import signal

############# Pitch 1 ##############
###################################################
# Plot the amplitude versus time 
###################################################

#Take the amplitudes of 4 signals and the time from excel file Pitch_1

data = pd.read_excel("Pitch_1.xlsx", skiprows = 74)
time =  pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]

###################################################
#PLot the amplitudes of 4 signals versus time
###################################################

fig, (ampA, ampB, ampC, ampD) = plt.subplots(1, 4, sharex = True, sharey = True)
fig.suptitle("Amplitude versus time (Pitch 1)")

#EMG_A
ampA.plot(time, amp_A)
ampA.set_title ("EMG A")
ampA.grid(True)

#EMG_B
ampB.plot(time, amp_B, "tab:green")
ampB.set_title ("EMG B")
ampB.grid(True)

#EMG_C
ampC.plot(time, amp_C, "tab:red")
ampC.set_title ("EMG C")
ampC.grid(True)

#EMG_D
ampD.plot(time, amp_D, "tab:orange")
ampD.set_title ("EMG D")
ampD.grid(True)


###################################################
# Plot the power spectral density(PSD) of signals
###################################################

# The power of the signal per frequency band
fig, (ampA, ampB, ampC, ampD) = plt.subplots(1, 4, sharey = True)
fig.suptitle("Power Spectral Density (Pitch 1)")

#EMG_A
freqs_A, psd_A = signal.welch(amp_A)
ampA.plot(freqs_A, psd_A)
ampA.set_title('EMG A')
ampA.grid(True)

#EMG_B
freqs_B, psd_B = signal.welch(amp_B)
ampB.plot(freqs_B, psd_B, "tab:green")
ampB.set_title('EMG B')
ampB.grid(True)

#EMG_C
freqs_C, psd_C = signal.welch(amp_C)
ampC.plot(freqs_C, psd_C, "tab:red")
ampC.set_title('EMG C')
ampC.grid(True)

#EMG_D
freqs_D, psd_D = signal.welch(amp_D)
ampD.plot(freqs_D, psd_D, "tab:orange")
ampD.set_title('EMG D')
ampD.grid(True)









