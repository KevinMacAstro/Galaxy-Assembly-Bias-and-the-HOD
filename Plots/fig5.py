# Plots Figure 5 from publication: chi2 and number density from modeling fits (HOD, 3 SCAMS).

import numpy as np
import matplotlib.pyplot as plt


hod_chi=np.array([19.73,30.21,49.48])
hod_ng=np.array([0.01605,0.004775,0.000866])
macc_chi=np.array([109.14,195.85,72.84])
macc_ng=np.array([0.003392,0.002059,0.001011])
vacc_chi=np.array([29.55,74.42,38.62])
vacc_ng=np.array([.01538,0.003948,0.0009731])
vpeak_chi=np.array([1.69,7.86,38.65])
vpeak_ng=np.array([0.01577,0.005177,0.0009959])
ls_ng=np.array([0.006193,0.003552,0.0007672])
mags=np.array([-19,-20,-21])

mr19=244784.
mr20=96646.
mr21=17268.
V=15625000.
data_ng=np.array([mr21/V,mr20/V,mr19/V])

hod_chi=hod_chi[::-1]/42.
vacc_chi=vacc_chi[::-1]/43.
macc_chi=macc_chi[::-1]/43.
vpeak_chi=vpeak_chi[::-1]/43.
hod_ng=hod_ng[::-1]
macc_ng=macc_ng[::-1]
vacc_ng=vacc_ng[::-1]
vpeak_ng=vpeak_ng[::-1]
ls_ng=ls_ng[::-1]
mags=mags[::-1]

gs=plt.GridSpec(10, 20)
ax1=plt.subplot(gs[0:10,0:10])
ax2=plt.subplot(gs[0:10,10:20])


ax1.errorbar(mags,hod_chi,fmt='o-',color='k',markerfacecolor='k',markeredgecolor='k',lw=2,ms=10,label='HOD')
ax1.errorbar(mags,vpeak_chi,fmt='o-',color='y',markerfacecolor='y',markeredgecolor='k',lw=2,ms=10,label='V$peak$')
ax1.errorbar(mags,macc_chi,fmt='o-',color='purple',markerfacecolor='purple',markeredgecolor='k',ms=10,lw=2,label='M$acc$')
ax1.errorbar(mags,vacc_chi,fmt='o-',color='red',markerfacecolor='red',markeredgecolor='k',ms=10,lw=2,label='V$acc$')
ax2.errorbar(mags,hod_ng,fmt='o-',color='k',markerfacecolor='k',markeredgecolor='k',lw=2,ms=10)
ax2.errorbar(mags,ls_ng,fmt='o--',color='k',markerfacecolor='k',markeredgecolor='k',lw=2,ms=10,label='HOD$ls-match$')
ax2.errorbar(mags,vpeak_ng,fmt='o-',color='y',markerfacecolor='y',markeredgecolor='k',lw=2,ms=10)
ax2.errorbar(mags,macc_ng,fmt='o-',color='purple',markerfacecolor='purple',markeredgecolor='k',ms=10,lw=2)
ax2.errorbar(mags,vacc_ng,fmt='o-',color='red',markerfacecolor='red',markeredgecolor='k',ms=10,lw=2)
ax2.errorbar(mags,data_ng,fmt='s',color='cyan',markerfacecolor='None',mew=4,markeredgecolor='cyan',lw=2,ms=10,label='HW13')
ax1.set_yscale('log')
ax2.set_yscale('log')
ax1.set_xlim(-18.5,-21.5)
ax2.set_xlim(-18.5,-21.5)
ax1.set_xticks([-19,-20,-21])
ax2.set_xticks([-19,-20,-21])
ax1.set_yticks([0.1,1])
ax2.set_yticks([0.001,0.01])
ax1.set_ylabel('$\chi^2/dof$', fontsize=24)
ax1.set_xlabel('M$_r$', fontsize=24)
ax2.set_ylabel('n$_g$ [h$^3$Mpc$^{-3}$]', fontsize=24)
ax2.set_xlabel('M$_r$', fontsize=24)
ax1.grid(b=True, which='minor',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.tick_params('both', length=15, width=1, which='major',labelsize=24)
ax1.tick_params('both', length=10, width=1, which='minor')
ax2.tick_params('both', length=15, width=1, which='major',labelsize=24)
ax2.tick_params('both', length=10, width=1, which='minor')
ax1.plot((-18,-22),(42,42),ls='--',c='k',lw=2)
ax1.text(-21.2,30,'$dof$',fontsize=20)
ax2.legend(loc='upper right', fontsize=24)
ax1.legend(loc='lower right', fontsize=24)

plt.show()
