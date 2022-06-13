import numpy as np
import skfuzzy as sk
from matplotlib import pyplot as plt

#Defining current angle
theta = np.arange(-180, 180, 1)

tmi = sk.sigmf(theta, -150, -0.2)
ti = sk.gaussmf(theta, -90, 22)
tc = sk.gaussmf(theta, 0, 20)
td = sk.gaussmf(theta, 90, 22)
tmd = sk.sigmf(theta, 150, 0.2)


plt.subplot(181)
plt.title("Theta")
plt.plot(theta,tmi)
plt.plot(theta,ti)
plt.plot(theta,tc)
plt.plot(theta,td)
plt.plot(theta,tmd)


#Defining distance to goal
dist = np.arange(0, 16, 0.1)

dmb = sk.sigmf(dist, 2, -2.5)
db = sk.gaussmf(dist, 4, 0.8)
dm = sk.gaussmf(dist, 8, 0.8)
da = sk.gaussmf(dist, 12, 0.8)
dma = sk.sigmf(dist, 14, 2.5)


plt.subplot(182)
plt.title("Distancia")
plt.plot(dist,dmb)
plt.plot(dist,db)
plt.plot(dist,dm)
plt.plot(dist,da)
plt.plot(dist,dma)


#Defining desired velocity 
velocidad = np.arange(0, 10, 0.1)

vmb = sk.sigmf(velocidad, 2, -4)
vb = sk.gaussmf(velocidad, 3, 0.4)
vm = sk.gaussmf(velocidad, 5, 0.4)
va = sk.gaussmf(velocidad, 7, 0.4)
vma = sk.sigmf(velocidad, 8, 4)


plt.subplot(183)
plt.title("Velocidad")
plt.plot(velocidad,vmb)
plt.plot(velocidad,vb)
plt.plot(velocidad,vm)
plt.plot(velocidad,va)
plt.plot(velocidad,vma)


#Defining angular speed
omega = np.arange(-2, 2, 0.01)

omi = sk.sigmf(omega, -1.5, -10)
oi = sk.gaussmf(omega, -0.9, 0.23)
oc = sk.gaussmf(omega, 0, 0.2)
od = sk.gaussmf(omega, 0.9, 0.23)
omd = sk.sigmf(omega, 1.5, 10)


plt.subplot(184)
plt.title("Omega")
plt.plot(omega,omi)
plt.plot(omega,oi)
plt.plot(omega,oc)
plt.plot(omega,od)
plt.plot(omega,omd)
#plt.show()


len_theta = len(theta)
len_dist = len(dist)

#Fuzzy logic to get the desired angle (omega)
res_omega = [[0]*500]*500
res_vel = [[0]*500]*500
c=0
for j in range(len_theta):
    
    for k in range (len_dist):
        c+=1
        #print("Loading...", ((((k+1)*(j+1)))/(len_dist*len_theta)), "%")
        print("Loading", ((c*100)/(57600)))

        #Normalize theta array to have it as an int and use it as an index
        t = theta[j]+180
        d = round(dist[k]*10)

        #Declaring rules
        R1 = min(tmi[t], dmb[d])
        R2 = min(tmi[t], db[d])
        R3 = min(tmi[t], dm[d])
        R4 = min(tmi[t], da[d])
        R5 = min(tmi[t], dma[d])
        R6 = min(ti[t], dmb[d])
        R7 = min(ti[t], db[d])
        R8 = min(ti[t], dm[d])
        R9 = min(ti[t], da[d])
        R10 = min(ti[t], dma[d])
        R11 = min(tc[t], dmb[d])
        R12 = min(tc[t], db[d])
        R13 = min(tc[t], dm[d])
        R14 = min(tc[t], da[d])
        R15 = min(tc[t], dma[d])
        R16 = min(td[t], dmb[d])
        R17 = min(td[t], db[d])
        R18 = min(td[t], dm[d])
        R19 = min(td[t], da[d])
        R20 = min(td[t], dma[d])
        R21 = min(tmd[t], dmb[d])
        R22 = min(tmd[t], db[d])
        R23 = min(tmd[t], dm[d])
        R24 = min(tmd[t], da[d])
        R25 = min(tmd[t], dma[d])
        R26 = min(tmi[t], dmb[d])
        R27 = min(tmi[t], db[d])
        R28 = min(tmi[t], dm[d])
        R29 = min(tmi[t], da[d])
        R30 = min(tmi[t], dma[d])
        R31 = min(ti[t], dmb[d])
        R32 = min(ti[t], db[d])
        R33 = min(ti[t], dm[d])
        R34 = min(ti[t], da[d])
        R35 = min(ti[t], dma[d])
        R36 = min(tc[t], dmb[d])
        R37 = min(tc[t], db[d])
        R38 = min(tc[t], dm[d])
        R39 = min(tc[t], da[d])
        R40 = min(tc[t], dma[d])
        R41 = min(td[t], dmb[d])
        R42 = min(td[t], db[d])
        R43 = min(td[t], dm[d])
        R44 = min(td[t], da[d])
        R45 = min(td[t], dma[d])
        R46 = min(tmd[t], dmb[d])
        R47 = min(tmd[t], db[d])
        R48 = min(tmd[t], dm[d])
        R49 = min(tmd[t], da[d])
        R50 = min(tmd[t], dma[d])


        #Rules fro omega
        omega_actual = []
        max_omi = max(R16, R21, R22)
        max_oi = max(R17, R18, R23, R24)
        max_oc = max(R5, R9, R10, R11, R12, R13, R14, R15, R19, R20, R25)
        max_od = max(R3, R4, R7, R8)
        max_omd = max(R1, R2, R6)

        vel_actual = []
        max_vmb = max(R26, R31, R41, R46)
        max_vb = max(R27, R36, R47)
        max_vm = max(R28, R29, R30, R32, R33, R37, R42, R43, R48, R49, R50)
        max_va = max(R34, R35, R38, R44, R45)
        max_tvma = max(R39, R40)
        
        omi2 = np.copy(omi)
        oi2 = np.copy(oi)
        oc2 = np.copy(oc)
        od2 = np.copy(od)
        omd2 = np.copy(omd)

        for i in range(len(omi)):
            if omi[i] > max_omi:
                omi2[i] = max_omi
            if oi[i] > max_oi:
                oi2[i] = max_oi
            if oc[i] > max_oc:
                oc2[i] = max_oc
            if od[i] > max_od:
                od2[i] = max_od
            if omd[i] > max_omd:
                omd[i] = max_omd

            omega_actual.append(max(omi2[i], oi2[i], oc2[i], od2[i] ,omd2[i]))
            sum1 = 0
            sum2 = 0
            x = 0.0
            for i in range(len(omega_actual)):
                x = x+0.1
                sum1 += omega_actual[i]*x
                sum2 += omega_actual[i]
        res_omega[j][k] = sum1/sum2


        #Rules for velocity
        vel_actual = []
        max_vmb = max(R26, R31, R41, R46)
        max_vb = max(R27, R36, R47)
        max_vm = max(R28, R29, R30, R32, R33, R37, R42, R43, R48, R49, R50)
        max_va = max(R34, R35, R38, R44, R45)
        max_vma = max(R39, R40)
        
        vmb2 = np.copy(vmb)
        vb2 = np.copy(vb)
        vm2 = np.copy(vm)
        va2 = np.copy(va)
        vma2 = np.copy(vma)

        for i in range(len(vmb)):
            if vmb[i] > max_vmb:
                vmb2[i] = max_vmb
            if vb[i] > max_vb:
                vb2[i] = max_vb
            if vm[i] > max_vm:
                vm2[i] = max_vm
            if va[i] > max_va:
                va2[i] = max_va
            if vma[i] > max_vma:
                vma[i] = max_vma
            
            vel_actual.append(max(vmb2[i], vb2[i], vm2[i], va2[i] ,vma2[i]))
            sum1 = 0
            sum2 = 0
            x = 0.0
            for i in range(len(vel_actual)):
                x = x+0.1
                sum1 += vel_actual[i]*x
                sum2 += vel_actual[i]
        res_vel[j][k] = sum1/sum2


np.savetxt('theta.csv', theta, delimiter=',')
np.savetxt('dist.csv', dist, delimiter=',')
np.savetxt('velocidad.csv', velocidad, delimiter=',')
np.savetxt('omega.csv', omega, delimiter=',')
np.savetxt('vel_actual.csv', vel_actual, delimiter=',')
np.savetxt('omega_actual.csv', omega_actual, delimiter=',')

plt.subplot(185)
plt.plot(omega,omi)
plt.plot(omega,oi)
plt.plot(omega,oc)
plt.plot(omega,od)
plt.plot(omega,omd)
plt.title("Angulo deseado")
plt.subplot(186)
plt.plot(omega, omega_actual)
plt.title("omega_actual")


plt.subplot(187)
plt.plot(velocidad,vmb)
plt.plot(velocidad,vb)
plt.plot(velocidad,vm)
plt.plot(velocidad,va)
plt.plot(velocidad,vma)
plt.title("velocidad deseada")
plt.subplot(188)
plt.plot(velocidad, vel_actual)
plt.title("velocidad_actual")
plt.show()