from matplotlib import pyplot as plt
import pandas as pd
from scipy import signal

##################################################
#Step 1
#Return: Take datum from 9 excel files
#Data: time (different fomr 9 files), Amplitude of 4 EMG signals
#Using pandas to do
##################################################

#Data from Pitch_1        
data = pd.read_excel("Pitch_1.xlsx", skiprows = 74)
time_1 = pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A1 = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B1 = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C1 = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D1 = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]

#Data from Pitch_2
data = pd.read_excel("Pitch_2.xlsx", skiprows = 74)
time_2 = pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A2 = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B2 = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C2 = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D2 = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]

#Data from Pitch_3
data = pd.read_excel("Pitch_3.xlsx", skiprows = 74)
time_3 = pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A3 = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B3 = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C3 = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D3 = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]

#Data from Pitch_4
data = pd.read_excel("Pitch_4.xlsx", skiprows = 74)
time_4 = pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A4 = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B4 = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C4 = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D4 = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]

#Data from Pitch_5
data = pd.read_excel("Pitch_5.xlsx", skiprows = 74)
time_5 = pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A5 = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B5 = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C5 = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D5 = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]

#Data from Pitch_6
data = pd.read_excel("Pitch_6.xlsx", skiprows = 74)
time_6 = pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A6 = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B6 = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C6 = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D6 = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]

#Data from Pitch_7
data = pd.read_excel("Pitch_7.xlsx", skiprows = 74)
time_7 = pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A7 = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B7 = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C7 = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D7 = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]

#Data from Pitch_8
data = pd.read_excel("Pitch_8.xlsx", skiprows = 74)
time_8 = pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A8 = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B8 = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C8 = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D8 = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]

#Data from Pitch_9
data = pd.read_excel("Pitch_9.xlsx", skiprows = 74)
time_9 = pd.DataFrame(data, columns= ['Time']).to_numpy()[:,0]
amp_A9 = pd.DataFrame(data, columns= ['Amp A']).to_numpy()[:,0]
amp_B9 = pd.DataFrame(data, columns= ['Amp B']).to_numpy()[:,0]
amp_C9 = pd.DataFrame(data, columns= ['Amp C']).to_numpy()[:,0]
amp_D9 = pd.DataFrame(data, columns= ['Amp D']).to_numpy()[:,0]


##################################################
#Step 2
#Return: 1 figure will show 3 groups of 4-EMG-signals 
#Plot: amplitude versus time 
#Using matplotlib with approriate variables
##################################################


#Group 1: Including files: Pitch_1, Pitch_2, Pitch_3
#The results will be shown as matrix (3x4)


#Create the form of matrix (3x4)
fig, amp = plt.subplots (3,4, sharex = True, sharey= True)
fig.suptitle("Amplitude versus time for 4-EMG signals (pitch 1-3)")

###################
#Pitch_1

#EMG A, position (0,0)
amp[0,0].plot(time_1, amp_A1)
amp[0,0].set_title("EMG A_1")
amp[0,0].grid(True)

#EMG B, position (0,1)
amp[0,1].plot(time_1, amp_B1, "tab:green")
amp[0,1].set_title("EMG B_1")
amp[0,1].grid(True)

#EMG C, position (0,2)
amp[0,2].plot(time_1, amp_C1, "tab:orange")
amp[0,2].set_title("EMG C_1")
amp[0,2].grid(True)

#EMG D, position (0,3)
amp[0,3].plot(time_1, amp_D1, "tab:red")
amp[0,3].set_title("EMG D_1")
amp[0,3].grid(True)

###################
#Pitch_2

#EMG A, position (1,0)
amp[1,0].plot(time_2, amp_A2)
amp[1,0].set_title("EMG A_2")
amp[1,0].grid(True)

#EMG B, position (1,1)
amp[1,1].plot(time_2, amp_B2, "tab:green")
amp[1,1].set_title("EMG B_2")
amp[1,1].grid(True)

#EMG C, position (1,2)
amp[1,2].plot(time_2, amp_C2, "tab:orange")
amp[1,2].set_title("EMG C_2")
amp[1,2].grid(True)

#EMG D, position (1,3)
amp[1,3].plot(time_2, amp_D2, "tab:red")
amp[1,3].set_title("EMG D_2")
amp[1,3].grid(True)

###################
#Pitch_3

#EMG A, position (2,0)
amp[2,0].plot(time_3, amp_A3)
amp[2,0].set_title("EMG A_3")
amp[2,0].grid(True)

#EMG B, position (2,1)
amp[2,1].plot(time_3, amp_B3, "tab:green")
amp[2,1].set_title("EMG B_3")
amp[2,1].grid(True)

#EMG C, position (2,2)
amp[2,2].plot(time_3, amp_C3, "tab:orange")
amp[2,2].set_title("EMG C_3")
amp[2,2].grid(True)

#EMG D, position (2,3)
amp[2,3].plot(time_3, amp_D3, "tab:red")
amp[2,3].set_title("EMG D_3")
amp[2,3].grid(True)


##################################################


#Group 2: Including files: Pitch_4, Pitch_5, Pitch_6
#The results will be shown as matrix (3x4)


#Create the form of matrix (3x4)
fig, amp = plt.subplots (3,4, sharex = True, sharey= True)
fig.suptitle("Amplitude versus time for 4-EMG signals (pitch 4-6)")

###################
#Pitch_4

#EMG A, position (0,0)
amp[0,0].plot(time_4, amp_A4)
amp[0,0].set_title("EMG A_4")
amp[0,0].grid(True)

#EMG B, position (0,1)
amp[0,1].plot(time_4, amp_B4, "tab:green")
amp[0,1].set_title("EMG B_4")
amp[0,1].grid(True)

#EMG C, position (0,2)
amp[0,2].plot(time_4, amp_C4, "tab:orange")
amp[0,2].set_title("EMG C_4")
amp[0,2].grid(True)

#EMG D, position (0,3)
amp[0,3].plot(time_4, amp_D4, "tab:red")
amp[0,3].set_title("EMG D_4")
amp[0,3].grid(True)

###################
#Pitch_5

#EMG A, position (1,0)
amp[1,0].plot(time_5, amp_A5)
amp[1,0].set_title("EMG A_5")
amp[1,0].grid(True)

#EMG B, position (1,1)
amp[1,1].plot(time_5, amp_B5, "tab:green")
amp[1,1].set_title("EMG B_5")
amp[1,1].grid(True)

#EMG C, position (1,2)
amp[1,2].plot(time_5, amp_C5, "tab:orange")
amp[1,2].set_title("EMG C_5")
amp[1,2].grid(True)

#EMG D, position (1,3)
amp[1,3].plot(time_5, amp_D5, "tab:red")
amp[1,3].set_title("EMG D_5")
amp[1,3].grid(True)

###################
#Pitch_6

#EMG A, position (2,0)
amp[2,0].plot(time_6, amp_A6)
amp[2,0].set_title("EMG A_6")
amp[2,0].grid(True)

#EMG B, position (2,1)
amp[2,1].plot(time_6, amp_B6, "tab:green")
amp[2,1].set_title("EMG B_6")
amp[2,1].grid(True)

#EMG C, position (2,2)
amp[2,2].plot(time_6, amp_C6, "tab:orange")
amp[2,2].set_title("EMG C_6")
amp[2,2].grid(True)

#EMG D, position (2,3)
amp[2,3].plot(time_6, amp_D6, "tab:red")
amp[2,3].set_title("EMG D_6")
amp[2,3].grid(True)

##################################################


#Group 3: Including files: Pitch_7, Pitch_8, Pitch_9
#The results will be shown as matrix (3x4)


#Create the form of matrix (3x4)
fig, amp = plt.subplots (3,4, sharex = True, sharey= True)
fig.suptitle("Amplitude versus time for 4-EMG signals (pitch 7-9)")

###################
#Pitch_7

#EMG A, position (0,0)
amp[0,0].plot(time_7, amp_A7)
amp[0,0].set_title("EMG A_7")
amp[0,0].grid(True)

#EMG B, position (0,1)
amp[0,1].plot(time_7, amp_B7, "tab:green")
amp[0,1].set_title("EMG B_7")
amp[0,1].grid(True)

#EMG C, position (0,2)
amp[0,2].plot(time_7, amp_C7, "tab:orange")
amp[0,2].set_title("EMG C_7")
amp[0,2].grid(True)

#EMG D, position (0,3)
amp[0,3].plot(time_7, amp_D7, "tab:red")
amp[0,3].set_title("EMG D_7")
amp[0,3].grid(True)

###################
#Pitch_8

#EMG A, position (1,0)
amp[1,0].plot(time_8, amp_A8)
amp[1,0].set_title("EMG A_8")
amp[1,0].grid(True)

#EMG B, position (1,1)
amp[1,1].plot(time_8, amp_B8, "tab:green")
amp[1,1].set_title("EMG B_8")
amp[1,1].grid(True)

#EMG C, position (1,2)
amp[1,2].plot(time_8, amp_C8, "tab:orange")
amp[1,2].set_title("EMG C_8")
amp[1,2].grid(True)

#EMG D, position (1,3)
amp[1,3].plot(time_8, amp_D8, "tab:red")
amp[1,3].set_title("EMG D_8")
amp[1,3].grid(True)

###################
#Pitch_9

#EMG A, position (2,0)
amp[2,0].plot(time_9, amp_A9)
amp[2,0].set_title("EMG A_9")
amp[2,0].grid(True)

#EMG B, position (2,1)
amp[2,1].plot(time_9, amp_B9, "tab:green")
amp[2,1].set_title("EMG B_9")
amp[2,1].grid(True)

#EMG C, position (2,2)
amp[2,2].plot(time_9, amp_C9, "tab:orange")
amp[2,2].set_title("EMG C_9")
amp[2,2].grid(True)

#EMG D, position (2,3)
amp[2,3].plot(time_9, amp_D9, "tab:red")
amp[2,3].set_title("EMG D_9")
amp[2,3].grid(True)


##################################################
#Step 3: Plot the PSD and detect the center of mass (CoM) 
#Return: 1 figure will show 3 groups of 4-EMG-signals 
#Plot: PSD versus frequency, point out center of mass
#Solution:
#1. Write a function to calculate the coordinates of CoM
#2.Calculate PSD, freq by using scipy library
#3.Plot the figure and CoM in same graph by using matplotlib

##########################################################

#Step 1:
#Function to calculate the coordinates of center of mass

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
#step 2: calculate the PSD, freq by using scipy library
#Apply the function "def centroid_poly(Cx, Cy) to each signal
#########################################################

#Group 1: Including files: Pitch_1, Pitch_2, Pitch_3
#The results will be shown as matrix (3x4)

#Create the form of matrix (3x4)
fig, amp = plt.subplots (3,4, sharex = True, sharey= True)
fig.suptitle("PSD versus frequency for 4-EMG signals (pitch 1-3)")

###################

#Pitch_1
print("The coordinates of center of mass for 4 EMG signals in Pitch 1 are:")


#EMG A, position (0,0)
freqs_A1, psd_A1 = signal.welch(amp_A1)
amp[0,0].plot(freqs_A1, psd_A1)
amp[0,0].set_title("EMG A_1")
amp[0,0].grid(True)
#Apply function to signal EMG A
Ax_coor1, Ay_coor1, A = centroid_poly(freqs_A1, psd_A1)
amp[0,0].scatter(Ax_coor1, Ay_coor1, color = 'black')
amp[0,0].axvline(Ax_coor1, color ='black', ls='--')
print("Ax and Ay are: " + str(Ax_coor1) + " and " +  str(Ay_coor1))


#EMG B, position (0,1)
freqs_B1, psd_B1 = signal.welch(amp_B1)
amp[0,1].plot(freqs_B1, psd_B1, "tab:green")
amp[0,1].set_title("EMG B_1")
amp[0,1].grid(True)
#Apply function to signal EMG B
Bx_coor1, By_coor1, A = centroid_poly(freqs_B1, psd_B1)
amp[0,1].scatter(Bx_coor1, By_coor1, color = 'black')
amp[0,1].axvline(Bx_coor1, color ='black', ls='--')
print("Bx and By are: " + str(Bx_coor1) + " and " +  str(By_coor1))


#EMG C, position (0,2)
freqs_C1, psd_C1 = signal.welch(amp_C1)
amp[0,2].plot(freqs_C1, psd_C1, "tab:orange")
amp[0,2].set_title("EMG C_1")
amp[0,2].grid(True)
#Apply function to signal EMG C
Cx_coor1, Cy_coor1, A = centroid_poly(freqs_C1, psd_C1)
amp[0,2].scatter(Cx_coor1, Cy_coor1, color = 'black')
amp[0,2].axvline(Cx_coor1, color ='black', ls='--')
print("Cx and Cy are: " + str(Cx_coor1) + " and " +  str(Cy_coor1))

#EMG D, position (0,3)
freqs_D1, psd_D1 = signal.welch(amp_D1)
amp[0,3].plot(freqs_D1, psd_D1, "tab:red")
amp[0,3].set_title("EMG D_1")
amp[0,3].grid(True)
#Apply function to signal EMG D
Dx_coor1, Dy_coor1, A = centroid_poly(freqs_D1, psd_D1)
amp[0,3].scatter(Dx_coor1, Dy_coor1, color = 'black')
amp[0,3].axvline(Dx_coor1, color ='black', ls='--')
print("Dx and Dy are: " + str(Dx_coor1) + " and " +  str(Dy_coor1))

###################
#Pitch_2
print("\nThe coordinates of center of mass for 4 EMG signals in Pitch 2 are:")

#EMG A, position (0,0)
freqs_A2, psd_A2 = signal.welch(amp_A2)
amp[1,0].plot(freqs_A2, psd_A2)
amp[1,0].set_title("EMG A_2")
amp[1,0].grid(True)
#Apply function to signal EMG A
Ax_coor2, Ay_coor2, A = centroid_poly(freqs_A2, psd_A2)
amp[1,0].scatter(Ax_coor2, Ay_coor2, color = 'black')
amp[1,0].axvline(Ax_coor2, color ='black', ls='--')
print("Ax and Ay are: " + str(Ax_coor2) + " and " +  str(Ay_coor2))

#EMG B, position (0,1)
freqs_B2, psd_B2 = signal.welch(amp_B2)
amp[1,1].plot(freqs_B2, psd_B2, "tab:green")
amp[1,1].set_title("EMG B_2")
amp[1,1].grid(True)
#Apply function to signal EMG B
Bx_coor2, By_coor2, A = centroid_poly(freqs_B2, psd_B2)
amp[1,1].scatter(Bx_coor2, By_coor2, color = 'black')
amp[1,1].axvline(Bx_coor2, color ='black', ls='--')
print("Bx and By are: " + str(Bx_coor2) + " and " +  str(By_coor2))

#EMG C, position (0,2)
freqs_C2, psd_C2 = signal.welch(amp_C2)
amp[1,2].plot(freqs_C2, psd_C2, "tab:orange")
amp[1,2].set_title("EMG C_2")
amp[1,2].grid(True)
#Apply function to signal EMG C
Cx_coor2, Cy_coor2, A = centroid_poly(freqs_C2, psd_C2)
amp[1,2].scatter(Cx_coor2, Cy_coor2, color = 'black')
amp[1,2].axvline(Cx_coor2, color ='black', ls='--')
print("Cx and Cy are: " + str(Cx_coor2) + " and " +  str(Cy_coor2))

#EMG D, position (0,3)
freqs_D2, psd_D2 = signal.welch(amp_D2)
amp[1,3].plot(freqs_D2, psd_D2, "tab:red")
amp[1,3].set_title("EMG D_2")
amp[1,3].grid(True)
#Apply function to signal EMG D
Dx_coor2, Dy_coor2, A = centroid_poly(freqs_D2, psd_D2)
amp[1,3].scatter(Dx_coor2, Dy_coor2, color = 'black')
amp[1,3].axvline(Dx_coor2, color ='black', ls='--')
print("Dx and Dy are: " + str(Dx_coor2) + " and " +  str(Dy_coor2))

###################
#Pitch_3
print("\n The coordinates of center of mass for 4 EMG signals in Pitch 3 are:")

#EMG A, position (0,0)
freqs_A3, psd_A3 = signal.welch(amp_A3)
amp[2,0].plot(freqs_A3, psd_A3)
amp[2,0].set_title("EMG A_3")
amp[2,0].grid(True)
#Apply function to signal EMG A
Ax_coor3, Ay_coor3, A = centroid_poly(freqs_A3, psd_A3)
amp[2,0].scatter(Ax_coor3, Ay_coor3, color = 'black')
amp[2,0].axvline(Ax_coor3, color ='black', ls='--')
print("Ax and Ay are: " + str(Ax_coor3) + " and " +  str(Ay_coor3))

#EMG B, position (0,1)
freqs_B3, psd_B3 = signal.welch(amp_B3)
amp[2,1].plot(freqs_B3, psd_B3, "tab:green")
amp[2,1].set_title("EMG B_3")
amp[2,1].grid(True)
#Apply function to signal EMG B
Bx_coor3, By_coor3, A = centroid_poly(freqs_B3, psd_B3)
amp[2,1].scatter(Bx_coor3, By_coor3, color = 'black')
amp[2,1].axvline(Bx_coor3, color ='black', ls='--')
print("Bx and By are: " + str(Bx_coor3) + " and " +  str(By_coor3))

#EMG C, position (0,2)
freqs_C3, psd_C3 = signal.welch(amp_C3)
amp[2,2].plot(freqs_C3, psd_C3, "tab:orange")
amp[2,2].set_title("EMG C_3")
amp[2,2].grid(True)
#Apply function to signal EMG C
Cx_coor3, Cy_coor3, A = centroid_poly(freqs_C3, psd_C3)
amp[2,2].scatter(Cx_coor3, Cy_coor3, color = 'black')
amp[2,2].axvline(Cx_coor3, color ='black', ls='--')
print("Cx and Cy are: " + str(Cx_coor3) + " and " +  str(Cy_coor3))

#EMG D, position (0,3)
freqs_D3, psd_D3 = signal.welch(amp_D3)
amp[2,3].plot(freqs_D3, psd_D3, "tab:red")
amp[2,3].set_title("EMG D_3")
amp[2,3].grid(True)
#Apply function to signal EMG D
Dx_coor3, Dy_coor3, A = centroid_poly(freqs_D3, psd_D3)
amp[2,3].scatter(Dx_coor3, Dy_coor3, color = 'black')
amp[2,3].axvline(Dx_coor3, color ='black', ls='--')
print("Dx and Dy are: " + str(Dx_coor3) + " and " +  str(Dy_coor3))


##################################################

#Group 2: Including files: Pitch_4, Pitch_5, Pitch_6
#The results will be shown as matrix (3x4)


#Create the form of matrix (3x4)
fig, amp = plt.subplots (3,4, sharex = True, sharey= True)
fig.suptitle("PSD versus frequency for 4-EMG signals (pitch 4-6)")

###################

#Pitch_4
print("\nThe coordinates of center of mass for 4 EMG signals in Pitch 4 are:")

#EMG A, position (0,0)
freqs_A4, psd_A4 = signal.welch(amp_A4)
amp[0,0].plot(freqs_A4, psd_A4)
amp[0,0].set_title("EMG A_4")
amp[0,0].grid(True)
#Apply function to signal EMG A
Ax_coor4, Ay_coor4, A = centroid_poly(freqs_A4, psd_A4)
amp[0,0].scatter(Ax_coor4, Ay_coor4, color = 'black')
amp[0,0].axvline(Ax_coor4, color ='black', ls='--')
print("Ax and Ay are: " + str(Ax_coor4) + " and " +  str(Ay_coor4))

#EMG B, position (0,1)
freqs_B4, psd_B4 = signal.welch(amp_B4)
amp[0,1].plot(freqs_B4, psd_B4, "tab:green")
amp[0,1].set_title("EMG B_4")
amp[0,1].grid(True)
#Apply function to signal EMG B
Bx_coor4, By_coor4, A = centroid_poly(freqs_B4, psd_B4)
amp[0,1].scatter(Bx_coor4, By_coor4, color = 'black')
amp[0,1].axvline(Bx_coor4, color ='black', ls='--')
print("Bx and By are: " + str(Bx_coor4) + " and " +  str(By_coor4))

#EMG C, position (0,2)
freqs_C4, psd_C4 = signal.welch(amp_C4)
amp[0,2].plot(freqs_C4, psd_C4, "tab:orange")
amp[0,2].set_title("EMG C_4")
amp[0,2].grid(True)
#Apply function to signal EMG C
Cx_coor4, Cy_coor4, A = centroid_poly(freqs_C4, psd_C4)
amp[0,2].scatter(Cx_coor4, Cy_coor4, color = 'black')
amp[0,2].axvline(Cx_coor4, color ='black', ls='--')
print("Cx and Cy are: " + str(Cx_coor4) + " and " +  str(Cy_coor4))

#EMG D, position (0,3)
freqs_D4, psd_D4 = signal.welch(amp_D4)
amp[0,3].plot(freqs_D4, psd_D4, "tab:red")
amp[0,3].set_title("EMG D_4")
amp[0,3].grid(True)
#Apply function to signal EMG D
Dx_coor4, Dy_coor4, A = centroid_poly(freqs_D4, psd_D4)
amp[0,3].scatter(Dx_coor4, Dy_coor4, color = 'black')
amp[0,3].axvline(Dx_coor4, color ='black', ls='--')
print("Dx and Dy are: " + str(Dx_coor4) + " and " +  str(Dy_coor4))

###################
#Pitch_5
print("\nThe coordinates of center of mass for 4 EMG signals in Pitch 5 are:")

#EMG A, position (0,0)
freqs_A5, psd_A5 = signal.welch(amp_A5)
amp[1,0].plot(freqs_A5, psd_A5)
amp[1,0].set_title("EMG A_5")
amp[1,0].grid(True)
#Apply function to signal EMG A
Ax_coor5, Ay_coor5, A = centroid_poly(freqs_A5, psd_A5)
amp[1,0].scatter(Ax_coor5, Ay_coor5, color = 'black')
amp[1,0].axvline(Ax_coor5, color ='black', ls='--')
print("Ax and Ay are: " + str(Ax_coor5) + " and " +  str(Ay_coor5))

#EMG B, position (0,1)
freqs_B5, psd_B5 = signal.welch(amp_B5)
amp[1,1].plot(freqs_B5, psd_B5, "tab:green")
amp[1,1].set_title("EMG B_5")
amp[1,1].grid(True)
#Apply function to signal EMG B
Bx_coor5, By_coor5, A = centroid_poly(freqs_B5, psd_B5)
amp[1,1].scatter(Bx_coor5, By_coor5, color = 'black')
amp[1,1].axvline(Bx_coor5, color ='black', ls='--')
print("Bx and By are: " + str(Bx_coor5) + " and " +  str(By_coor5))

#EMG C, position (0,2)
freqs_C5, psd_C5 = signal.welch(amp_C5)
amp[1,2].plot(freqs_C5, psd_C5, "tab:orange")
amp[1,2].set_title("EMG C_5")
amp[1,2].grid(True)
#Apply function to signal EMG C
Cx_coor5, Cy_coor5, A = centroid_poly(freqs_C5, psd_C5)
amp[1,2].scatter(Cx_coor5, Cy_coor5, color = 'black')
amp[1,2].axvline(Cx_coor5, color ='black', ls='--')
print("Cx and Cy are: " + str(Cx_coor5) + " and " +  str(Cy_coor5))

#EMG D, position (0,3)
freqs_D5, psd_D5 = signal.welch(amp_D5)
amp[1,3].plot(freqs_D5, psd_D5, "tab:red")
amp[1,3].set_title("EMG D_5")
amp[1,3].grid(True)
#Apply function to signal EMG D
Dx_coor5, Dy_coor5, A = centroid_poly(freqs_D5, psd_D5)
amp[1,3].scatter(Dx_coor5, Dy_coor5, color = 'black')
amp[1,3].axvline(Dx_coor5, color ='black', ls='--')
print("Dx and Dy are: " + str(Dx_coor5) + " and " +  str(Dy_coor5))

###################
#Pitch_6
print("\nThe coordinates of center of mass for 4 EMG signals in Pitch 6 are:")

#EMG A, position (0,0)
freqs_A6, psd_A6 = signal.welch(amp_A6)
amp[2,0].plot(freqs_A6, psd_A6)
amp[2,0].set_title("EMG A_6")
amp[2,0].grid(True)
#Apply function to signal EMG A
Ax_coor6, Ay_coor6, A = centroid_poly(freqs_A6, psd_A6)
amp[2,0].scatter(Ax_coor6, Ay_coor6, color = 'black')
amp[2,0].axvline(Ax_coor6, color ='black', ls='--')
print("Ax and Ay are: " + str(Ax_coor6) + " and " +  str(Ay_coor6))

#EMG B, position (0,1)
freqs_B6, psd_B6 = signal.welch(amp_B6)
amp[2,1].plot(freqs_B6, psd_B6, "tab:green")
amp[2,1].set_title("EMG B_6")
amp[2,1].grid(True)
#Apply function to signal EMG B
Bx_coor6, By_coor6, A = centroid_poly(freqs_B6, psd_B6)
amp[2,1].scatter(Bx_coor6, By_coor6, color = 'black')
amp[2,1].axvline(Bx_coor6, color ='black', ls='--')
print("Bx and By are: " + str(Bx_coor6) + " and " +  str(By_coor6))

#EMG C, position (0,2)
freqs_C6, psd_C6 = signal.welch(amp_C6)
amp[2,2].plot(freqs_C3, psd_C6, "tab:orange")
amp[2,2].set_title("EMG C_6")
amp[2,2].grid(True)
#Apply function to signal EMG C
Cx_coor6, Cy_coor6, A = centroid_poly(freqs_C6, psd_C6)
amp[2,2].scatter(Cx_coor6, Cy_coor6, color = 'black')
amp[2,2].axvline(Cx_coor6, color ='black', ls='--')
print("Cx and Cy are: " + str(Cx_coor6) + " and " +  str(Cy_coor6))

#EMG D, position (0,3)
freqs_D6, psd_D6 = signal.welch(amp_D6)
amp[2,3].plot(freqs_D6, psd_D6, "tab:red")
amp[2,3].set_title("EMG D_6")
amp[2,3].grid(True)
#Apply function to signal EMG D
Dx_coor6, Dy_coor6, A = centroid_poly(freqs_D6, psd_D6)
amp[2,3].scatter(Dx_coor6, Dy_coor6, color = 'black')
amp[2,3].axvline(Dx_coor6, color ='black', ls='--')
print("Dx and Dy are: " + str(Dx_coor6) + " and " +  str(Dy_coor6))


##################################################

#Group 3: Including files: Pitch_7, Pitch_8, Pitch_9
#The results will be shown as matrix (3x4)


#Create the form of matrix (3x4)
fig, amp = plt.subplots (3,4, sharex = True, sharey= True)
fig.suptitle("PSD versus frequency for 4-EMG signals (pitch 7-9)")

###################

#Pitch_7
print("\nThe coordinates of center of mass for 4 EMG signals in Pitch 7 are:")

#EMG A, position (0,0)
freqs_A7, psd_A7 = signal.welch(amp_A7)
amp[0,0].plot(freqs_A7, psd_A7)
amp[0,0].set_title("EMG A_7")
amp[0,0].grid(True)
#Apply function to signal EMG A
Ax_coor7, Ay_coor7, A = centroid_poly(freqs_A7, psd_A7)
amp[0,0].scatter(Ax_coor7, Ay_coor7, color = 'black')
amp[0,0].axvline(Ax_coor7, color ='black', ls='--')
print("Ax and Ay are: " + str(Ax_coor7) + " and " +  str(Ay_coor7))

#EMG B, position (0,1)
freqs_B7, psd_B7 = signal.welch(amp_B7)
amp[0,1].plot(freqs_B7, psd_B7, "tab:green")
amp[0,1].set_title("EMG B_7")
amp[0,1].grid(True)
#Apply function to signal EMG B
Bx_coor7, By_coor7, A = centroid_poly(freqs_B7, psd_B7)
amp[0,1].scatter(Bx_coor7, By_coor7, color = 'black')
amp[0,1].axvline(Bx_coor7, color ='black', ls='--')
print("Bx and By are: " + str(Bx_coor7) + " and " +  str(By_coor7))

#EMG C, position (0,2)
freqs_C7, psd_C7 = signal.welch(amp_C7)
amp[0,2].plot(freqs_C7, psd_C7, "tab:orange")
amp[0,2].set_title("EMG C_7")
amp[0,2].grid(True)
#Apply function to signal EMG C
Cx_coor7, Cy_coor7, A = centroid_poly(freqs_C7, psd_C7)
amp[0,2].scatter(Cx_coor7, Cy_coor7, color = 'black')
amp[0,2].axvline(Cx_coor7, color ='black', ls='--')
print("Cx and Cy are: " + str(Cx_coor7) + " and " +  str(Cy_coor7))

#EMG D, position (0,3)
freqs_D7, psd_D7 = signal.welch(amp_D7)
amp[0,3].plot(freqs_D7, psd_D7, "tab:red")
amp[0,3].set_title("EMG D_7")
amp[0,3].grid(True)
#Apply function to signal EMG D
Dx_coor7, Dy_coor7, A = centroid_poly(freqs_D7, psd_D7)
amp[0,3].scatter(Dx_coor7, Dy_coor7, color = 'black')
amp[0,3].axvline(Dx_coor7, color ='black', ls='--')
print("Dx and Dy are: " + str(Dx_coor7) + " and " +  str(Dy_coor7))

###################
#Pitch_8
print("\nThe coordinates of center of mass for 4 EMG signals in Pitch 8 are:")

#EMG A, position (0,0)
freqs_A8, psd_A8 = signal.welch(amp_A8)
amp[1,0].plot(freqs_A8, psd_A8)
amp[1,0].set_title("EMG A_8")
amp[1,0].grid(True)
#Apply function to signal EMG A
Ax_coor8, Ay_coor8, A = centroid_poly(freqs_A8, psd_A8)
amp[1,0].scatter(Ax_coor8, Ay_coor8, color = 'black')
amp[1,0].axvline(Ax_coor8, color ='black', ls='--')
print("Ax and Ay are: " + str(Ax_coor8) + " and " +  str(Ay_coor8))

#EMG B, position (0,1)
freqs_B8, psd_B8 = signal.welch(amp_B8)
amp[1,1].plot(freqs_B8, psd_B8, "tab:green")
amp[1,1].set_title("EMG B_8")
amp[1,1].grid(True)
#Apply function to signal EMG B
Bx_coor8, By_coor8, A = centroid_poly(freqs_B8, psd_B8)
amp[1,1].scatter(Bx_coor8, By_coor8, color = 'black')
amp[1,1].axvline(Bx_coor8, color ='black', ls='--')
print("Bx and By are: " + str(Bx_coor8) + " and " +  str(By_coor8))

#EMG C, position (0,2)
freqs_C8, psd_C8 = signal.welch(amp_C8)
amp[1,2].plot(freqs_C8, psd_C8, "tab:orange")
amp[1,2].set_title("EMG C_8")
amp[1,2].grid(True)
#Apply function to signal EMG C
Cx_coor8, Cy_coor8, A = centroid_poly(freqs_C8, psd_C8)
amp[1,2].scatter(Cx_coor8, Cy_coor8, color = 'black')
amp[1,2].axvline(Cx_coor8, color ='black', ls='--')
print("Cx and Cy are: " + str(Cx_coor8) + " and " +  str(Cy_coor8))

#EMG D, position (0,3)
freqs_D8, psd_D8 = signal.welch(amp_D8)
amp[1,3].plot(freqs_D8, psd_D8, "tab:red")
amp[1,3].set_title("EMG D_8")
amp[1,3].grid(True)
#Apply function to signal EMG D
Dx_coor8, Dy_coor8, A = centroid_poly(freqs_D8, psd_D8)
amp[1,3].scatter(Dx_coor8, Dy_coor8, color = 'black')
amp[1,3].axvline(Dx_coor8, color ='black', ls='--')
print("Dx and Dy are: " + str(Dx_coor8) + " and " +  str(Dy_coor8))

###################
#Pitch_9
print("\nThe coordinates of center of mass for 4 EMG signals in Pitch 9 are:")

#EMG A, position (0,0)
freqs_A9, psd_A9 = signal.welch(amp_A9)
amp[2,0].plot(freqs_A9, psd_A9)
amp[2,0].set_title("EMG A_9")
amp[2,0].grid(True)
#Apply function to signal EMG A
Ax_coor9, Ay_coor9, A = centroid_poly(freqs_A9, psd_A9)
amp[2,0].scatter(Ax_coor9, Ay_coor9, color = 'black')
amp[2,0].axvline(Ax_coor9, color ='black', ls='--')
print("Ax and Ay are: " + str(Ax_coor9) + " and " +  str(Ay_coor9))

#EMG B, position (0,1)
freqs_B9, psd_B9 = signal.welch(amp_B9)
amp[2,1].plot(freqs_B9, psd_B9, "tab:green")
amp[2,1].set_title("EMG B_9")
amp[2,1].grid(True)
#Apply function to signal EMG B
Bx_coor9, By_coor9, A = centroid_poly(freqs_B9, psd_B9)
amp[2,1].scatter(Bx_coor9, By_coor9, color = 'black')
amp[2,1].axvline(Bx_coor9, color ='black', ls='--')
print("Bx and By are: " + str(Bx_coor9) + " and " +  str(By_coor9))

#EMG C, position (0,2)
freqs_C9, psd_C9 = signal.welch(amp_C9)
amp[2,2].plot(freqs_C9, psd_C9, "tab:orange")
amp[2,2].set_title("EMG C_9")
amp[2,2].grid(True)
#Apply function to signal EMG C
Cx_coor9, Cy_coor9, A = centroid_poly(freqs_C9, psd_C9)
amp[2,2].scatter(Cx_coor9, Cy_coor9, color = 'black')
amp[2,2].axvline(Cx_coor9, color ='black', ls='--')
print("Cx and Cy are: " + str(Cx_coor9) + " and " +  str(Cy_coor9))

#EMG D, position (0,3)
freqs_D9, psd_D9 = signal.welch(amp_D9)
amp[2,3].plot(freqs_D9, psd_D9, "tab:red")
amp[2,3].set_title("EMG D_9")
amp[2,3].grid(True)
#Apply function to signal EMG D
Dx_coor9, Dy_coor9, A = centroid_poly(freqs_D9, psd_D9)
amp[2,3].scatter(Dx_coor9, Dy_coor9, color = 'black')
amp[2,3].axvline(Dx_coor9, color ='black', ls='--')
print("Dx and Dy are: " + str(Dx_coor9) + " and " +  str(Dy_coor9))

