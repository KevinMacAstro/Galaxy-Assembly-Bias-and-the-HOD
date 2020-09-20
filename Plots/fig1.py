# Plotting Figure 1 from publication: Redshift-space 2PCFs xi(rp,r_pi) for three luminosity cuts (Mr<-19.0, <-20.0, <-21.0) for HW13 and shuffled galaxy mocks.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['contour.negative_linestyle'] = 'dashed'

rpBin1=50
piBin1=50
piBin2=25
rpBin2=25
rp1_cen,pi1_cen,xi1_19=np.loadtxt('Mr19rppi_avg_1.dat', unpack=True)
xi1_19=xi1_19.reshape(piBin1,rpBin1)
rp1_cen=rp1_cen.reshape(piBin1,rpBin1)
rp1_cen=rp1_cen[0,:]
rp2_cen,pi2_cen,xi2_19=np.loadtxt('Mr19rppi_avg_2.dat', unpack=True)
xi2_19=xi2_19.reshape(piBin2,rpBin2)
rp2_cen=rp2_cen.reshape(piBin2,rpBin2)
rp2_cen=rp2_cen[0,:]

R=31
for i in range(0,rpBin1):
	if i < rpBin1:
		if i < R:
			j=int(np.sqrt(R**2-i**2))
			for k in range(j,rpBin1):
				if k < rpBin1:
					xi1_19[i,k]=0
		else:
			for k in range(0,rpBin1):
				if k < rpBin1:
					xi1_19[i,k]=0

R=15
for i in range(0,rpBin2):
        if i < rpBin2:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(0,j):
                                if k < j:
                                        xi2_19[i,k]=0

xi4_19_1=np.zeros((2*piBin1,rpBin1))
for i in range(0,piBin1):
        if i < piBin1:
                for j in range(0,rpBin1):
                        if j < rpBin1:
                                xi4_19_1[i,j]=xi1_19[::-1][i,j]
                                xi4_19_1[(i+piBin1),j]=xi1_19[i,j]
xi4q_19_1=np.hstack((xi4_19_1[:,::-1],xi4_19_1))
logxi4q_19_1=np.log10(xi4q_19_1)

xi4_19_2=np.zeros((2*piBin2,rpBin2))
for i in range(0,piBin2):
	if i < piBin2:
		for j in range(0,rpBin2):
			if j < rpBin2:
				xi4_19_2[i,j]=xi2_19[::-1][i,j]
				xi4_19_2[(i+piBin2),j]=xi2_19[i,j]	
xi4q_19_2=np.hstack((xi4_19_2[:,::-1],xi4_19_2))
logxi4q_19_2=np.log10(xi4q_19_2)

rp1_cen,pi1_cen,exi1_19=np.loadtxt('eMr19rppi_avg_1.dat', unpack=True)
exi1_19=exi1_19.reshape(piBin1,rpBin1)
rp2_cen,pi2_cen,exi2_19=np.loadtxt('eMr19rppi_avg_2.dat', unpack=True)
exi2_19=exi2_19.reshape(piBin2,rpBin2)

R=31
for i in range(0,rpBin1):
        if i < rpBin1:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(j,rpBin1):
                                if k < rpBin1:
                                        exi1_19[i,k]=0
                else:
                        for k in range(0,rpBin1):
                                if k < rpBin1:
                                        exi1_19[i,k]=0

R=15
for i in range(0,rpBin2):
        if i < rpBin2:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(0,j):
                                if k < j:
                                        exi2_19[i,k]=0

exi4_19_1=np.zeros((2*piBin1,rpBin1))
for i in range(0,piBin1):
        if i < piBin1:
                for j in range(0,rpBin1):
                        if j < rpBin1:
                                exi4_19_1[i,j]=exi1_19[::-1][i,j]
                                exi4_19_1[(i+piBin1),j]=exi1_19[i,j]
exi4q_19_1=np.hstack((exi4_19_1[:,::-1],exi4_19_1))
logexi4q_19_1=np.log10(exi4q_19_1)

exi4_19_2=np.zeros((2*piBin2,rpBin2))
for i in range(0,piBin2):
        if i < piBin2:
                for j in range(0,rpBin2):
                        if j < rpBin2:
                                exi4_19_2[i,j]=exi2_19[::-1][i,j]
                                exi4_19_2[(i+piBin2),j]=exi2_19[i,j]
exi4q_19_2=np.hstack((exi4_19_2[:,::-1],exi4_19_2))
logexi4q_19_2=np.log10(exi4q_19_2)

rp1_cen,pi1_cen,xi1_20=np.loadtxt('Mr20rppi_avg_1.dat', unpack=True)
xi1_20=xi1_20.reshape(piBin1,rpBin1)
rp2_cen,pi2_cen,xi2_20=np.loadtxt('Mr20rppi_avg_2.dat', unpack=True)
xi2_20=xi2_20.reshape(piBin2,rpBin2)

R=31
for i in range(0,rpBin1):
        if i < rpBin1:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(j,rpBin1):
                                if k < rpBin1:
                                        xi1_20[i,k]=0
                else:
                        for k in range(0,rpBin1):
                                if k < rpBin1:
                                        xi1_20[i,k]=0

R=15
for i in range(0,rpBin2):
        if i < rpBin2:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(0,j):
                                if k < j:
                                        xi2_20[i,k]=0

xi4_20_1=np.zeros((2*piBin1,rpBin1))
for i in range(0,piBin1):
        if i < piBin1:
                for j in range(0,rpBin1):
                        if j < rpBin1:
                                xi4_20_1[i,j]=xi1_20[::-1][i,j]
                                xi4_20_1[(i+piBin1),j]=xi1_20[i,j]
xi4q_20_1=np.hstack((xi4_20_1[:,::-1],xi4_20_1))
logxi4q_20_1=np.log10(xi4q_20_1)

xi4_20_2=np.zeros((2*piBin2,rpBin2))
for i in range(0,piBin2):
        if i < piBin2:
                for j in range(0,rpBin2):
                        if j < rpBin2:
                                xi4_20_2[i,j]=xi2_20[::-1][i,j]
                                xi4_20_2[(i+piBin2),j]=xi2_20[i,j]
xi4q_20_2=np.hstack((xi4_20_2[:,::-1],xi4_20_2))
logxi4q_20_2=np.log10(xi4q_20_2)


rp1_cen,pi1_cen,exi1_20=np.loadtxt('eMr20rppi_avg_1.dat', unpack=True)
exi1_20=exi1_20.reshape(piBin1,rpBin1)
rp2_cen,pi2_cen,exi2_20=np.loadtxt('eMr20rppi_avg_2.dat', unpack=True)
exi2_20=exi2_20.reshape(piBin2,rpBin2)

R=31
for i in range(0,rpBin1):
        if i < rpBin1:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(j,rpBin1):
                                if k < rpBin1:
                                        exi1_20[i,k]=0
                else:
                        for k in range(0,rpBin1):
                                if k < rpBin1:
                                        exi1_20[i,k]=0

R=15
for i in range(0,rpBin2):
        if i < rpBin2:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(0,j):
                                if k < j:
                                        exi2_20[i,k]=0

exi4_20_1=np.zeros((2*piBin1,rpBin1))
for i in range(0,piBin1):
        if i < piBin1:
                for j in range(0,rpBin1):
                        if j < rpBin1:
                                exi4_20_1[i,j]=exi1_20[::-1][i,j]
                                exi4_20_1[(i+piBin1),j]=exi1_20[i,j]
exi4q_20_1=np.hstack((exi4_20_1[:,::-1],exi4_20_1))
logexi4q_20_1=np.log10(exi4q_20_1)

exi4_20_2=np.zeros((2*piBin2,rpBin2))
for i in range(0,piBin2):
        if i < piBin2:
                for j in range(0,rpBin2):
                        if j < rpBin2:
                                exi4_20_2[i,j]=exi2_20[::-1][i,j]
                                exi4_20_2[(i+piBin2),j]=exi2_20[i,j]
exi4q_20_2=np.hstack((exi4_20_2[:,::-1],exi4_20_2))
logexi4q_20_2=np.log10(exi4q_20_2)


rp1_cen,pi1_cen,xi1_21=np.loadtxt('Mr21rppi_avg_1.dat', unpack=True)
xi1_21=xi1_21.reshape(piBin1,rpBin1)
rp2_cen,pi2_cen,xi2_21=np.loadtxt('Mr21rppi_avg_2.dat', unpack=True)
xi2_21=xi2_21.reshape(piBin2,rpBin2)

R=20
for i in range(0,rpBin1):
        if i < rpBin1:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(j,rpBin1):
                                if k < rpBin1:
                                        xi1_21[i,k]=0
                else:
                        for k in range(0,rpBin1):
                                if k < rpBin1:
                                        xi1_21[i,k]=0

R=10
for i in range(0,rpBin2):
        if i < rpBin2:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(0,j):
                                if k < j:
                                        xi2_21[i,k]=0

xi4_21_1=np.zeros((2*piBin1,rpBin1))
for i in range(0,piBin1):
        if i < piBin1:
                for j in range(0,rpBin1):
                        if j < rpBin1:
                                xi4_21_1[i,j]=xi1_21[::-1][i,j]
                                xi4_21_1[(i+piBin1),j]=xi1_21[i,j]
xi4q_21_1=np.hstack((xi4_21_1[:,::-1],xi4_21_1))
logxi4q_21_1=np.log10(xi4q_21_1)

xi4_21_2=np.zeros((2*piBin2,rpBin2))
for i in range(0,piBin2):
        if i < piBin2:
                for j in range(0,rpBin2):
                        if j < rpBin2:
                                xi4_21_2[i,j]=xi2_21[::-1][i,j]
                                xi4_21_2[(i+piBin2),j]=xi2_21[i,j]
xi4q_21_2=np.hstack((xi4_21_2[:,::-1],xi4_21_2))
logxi4q_21_2=np.log10(xi4q_21_2)


rp1_cen,pi1_cen,exi1_21=np.loadtxt('eMr21rppi_avg_1.dat', unpack=True)
exi1_21=exi1_21.reshape(piBin1,rpBin1)
rp2_cen,pi2_cen,exi2_21=np.loadtxt('eMr21rppi_avg_2.dat', unpack=True)
exi2_21=exi2_21.reshape(piBin2,rpBin2)

R=20
for i in range(0,rpBin1):
        if i < rpBin1:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(j,rpBin1):
                                if k < rpBin1:
                                        exi1_21[i,k]=0
                else:
                        for k in range(0,rpBin1):
                                if k < rpBin1:
                                        exi1_21[i,k]=0

R=10
for i in range(0,rpBin2):
        if i < rpBin2:
                if i < R:
                        j=int(np.sqrt(R**2-i**2))
                        for k in range(0,j):
                                if k < j:
                                        exi2_21[i,k]=0

exi4_21_1=np.zeros((2*piBin1,rpBin1))
for i in range(0,piBin1):
        if i < piBin1:
                for j in range(0,rpBin1):
                        if j < rpBin1:
                                exi4_21_1[i,j]=exi1_21[::-1][i,j]
                                exi4_21_1[(i+piBin1),j]=exi1_21[i,j]
exi4q_21_1=np.hstack((exi4_21_1[:,::-1],exi4_21_1))
logexi4q_21_1=np.log10(exi4q_21_1)

exi4_21_2=np.zeros((2*piBin2,rpBin2))
for i in range(0,piBin2):
        if i < piBin2:
                for j in range(0,rpBin2):
                        if j < rpBin2:
                                exi4_21_2[i,j]=exi2_21[::-1][i,j]
                                exi4_21_2[(i+piBin2),j]=exi2_21[i,j]
exi4q_21_2=np.hstack((exi4_21_2[:,::-1],exi4_21_2))
logexi4q_21_2=np.log10(exi4q_21_2)


gs=plt.GridSpec(10, 30)
ax1=plt.subplot(gs[0:10,0:10])
ax2=plt.subplot(gs[0:10,10:20])
ax3=plt.subplot(gs[0:10,20:30])

#ax1.plot((-2,-2),(-50,50),c='b')
#ax1.plot((2,2),(-50,50),c='b')
#ax2.plot((-2,-2),(-50,50),c='b')
#ax2.plot((2,2),(-50,50),c='b')
#ax3.plot((-2,-2),(-50,50),c='b')
#ax3.plot((2,2),(-50,50),c='b')
ax1.axvspan(-2, 2, color='b', alpha=0.5, lw=0)
ax2.axvspan(-2, 2, color='b', alpha=0.5, lw=0)
ax3.axvspan(-2, 2, color='b', alpha=0.5, lw=0)

ax1.contour(logxi4q_19_1,np.arange(-3.,2.,.5),origin='lower',extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],colors='k')
ax1.contour(logxi4q_19_2,np.arange(-3.,2.,.5),origin='lower',extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],colors='k')
ax2.contour(logxi4q_20_1,np.arange(-3.,2.,.5),origin='lower',extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],colors='k')
ax2.contour(logxi4q_20_2,np.arange(-3.,2.,.5),origin='lower',extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],colors='k')
ax3.contour(logxi4q_21_1,np.arange(-3.,2.,.5),origin='lower',extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],colors='k')
ax3.contour(logxi4q_21_2,np.arange(-3.,2.,.5),origin='lower',extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],colors='k')
ax1.contour(logexi4q_19_1,np.arange(-3.,2.,.5),origin='lower', extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],linestyles='dashed',colors='k')
ax1.contour(logexi4q_19_2,np.arange(-3.,2.,.5),origin='lower', extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],linestyles='dashed',colors='k')
ax2.contour(logexi4q_20_1,np.arange(-3.,2.,.5),origin='lower', extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],linestyles='dashed',colors='k')
ax2.contour(logexi4q_20_2,np.arange(-3.,2.,.5),origin='lower', extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],linestyles='dashed',colors='k')
ax3.contour(logexi4q_21_1,np.arange(-3.,2.,.5),origin='lower',extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],linestyles='dashed',colors='k')
ax3.contour(logexi4q_21_2,np.arange(-3.,2.,.5),origin='lower',extent=[np.amin(-rp2_cen),np.amax(rp2_cen),np.amin(-pi2_cen),np.amax(pi2_cen)],linestyles='dashed',colors='k')
ax1.set_xlabel('r$_p$ [h$^{-1}$Mpc]', fontsize=25)
ax2.set_xlabel('r$_p$ [h$^{-1}$Mpc]', fontsize=25)
ax3.set_xlabel('r$_p$ [h$^{-1}$Mpc]', fontsize=25)
ax1.set_ylabel('r$_\pi$ [h$^{-1}$Mpc]', fontsize=25)
ax1.tick_params('both', length=10, width=1, which='major',labelsize=25)
ax1.tick_params('both', length=5, width=1, which='minor',labelsize=25)
ax2.tick_params('both', length=10, width=1, which='major',labelsize=25)
ax2.tick_params('both', length=5, width=1, which='minor',labelsize=25)
ax3.tick_params('both', length=10, width=1, which='major',labelsize=25)
ax3.tick_params('both', length=5, width=1, which='minor',labelsize=25)

ax1.text(20,40,'$M_r<-19$',fontsize=25,bbox=dict(facecolor='white'))
ax2.text(20,40,'$M_r<-20$',fontsize=25,bbox=dict(facecolor='white'))
ax3.text(20,40,'$M_r<-21$',fontsize=25,bbox=dict(facecolor='white'))
ax1.text(-40,40,'$LOS\sim AVG$',fontsize=25,bbox=dict(facecolor='white'))
#ax1.tick_params(axis='both', which='major', labelsize=40)
plt.show()

