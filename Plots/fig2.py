# Plots figure 2 from publication: 2PCF (wp,xi_0,xi_2,xi_4) for difference luminosity thresholds.
# Also used for Fig. 6, 8, 11, and C1

import numpy as np
import matplotlib.pyplot as plt


s_center,fabxi19_l0,fabxi19_l2,fabxi19_l4,fnabxi19_l0,fnabxi19_l2,fnabxi19_l4=np.loadtxt('Xipoles19_HW13_avg.dat',unpack=True)
s_center,fabxi20_l0,fabxi20_l2,fabxi20_l4,fnabxi20_l0,fnabxi20_l2,fnabxi20_l4=np.loadtxt('Xipoles20_HW13_avg.dat',unpack=True)
s_center,fabxi21_l0,fabxi21_l2,fabxi21_l4,fnabxi21_l0,fnabxi21_l2,fnabxi21_l4=np.loadtxt('Xipoles21_HW13_avg.dat',unpack=True)
fs_center,fh1xi19_l0,fh1xi19_l2,fh1xi19_l4,fh2xi19_l0,fh2xi19_l2,fh2xi19_l4,fh3xi19_l0,fh3xi19_l2,fh3xi19_l4,fh4xi19_l0,fh4xi19_l2,fh4xi19_l4,fh5xi19_l0,fh5xi19_l2,fh5xi19_l4=np.loadtxt('Xipoles19_models_avg_new.dat',unpack=True)
fs_center,fh1xi20_l0,fh1xi20_l2,fh1xi20_l4,fh2xi20_l0,fh2xi20_l2,fh2xi20_l4,fh3xi20_l0,fh3xi20_l2,fh3xi20_l4,fh4xi20_l0,fh4xi20_l2,fh4xi20_l4,fh5xi20_l0,fh5xi20_l2,fh5xi20_l4=np.loadtxt('Xipoles20_models_avg_new.dat',unpack=True)
fs_center,fh1xi21_l0,fh1xi21_l2,fh1xi21_l4,fh2xi21_l0,fh2xi21_l2,fh2xi21_l4,fh3xi21_l0,fh3xi21_l2,fh3xi21_l4,fh4xi21_l0,fh4xi21_l2,fh4xi21_l4,fh5xi21_l0,fh5xi21_l2,fh5xi21_l4=np.loadtxt('Xipoles21_models_avg_new.dat',unpack=True)



fabxi19_error_l0=np.loadtxt('Mr19mono_covar.dat')
fabxi19_error_l2=np.loadtxt('Mr19quad_covar.dat')
fabxi19_error_l4=np.loadtxt('Mr19hexa_covar.dat')
fabxi20_error_l0=np.loadtxt('Mr20mono_covar.dat')
fabxi20_error_l2=np.loadtxt('Mr20quad_covar.dat')
fabxi20_error_l4=np.loadtxt('Mr20hexa_covar.dat')
fabxi21_error_l0=np.loadtxt('Mr21mono_covar.dat')
fabxi21_error_l2=np.loadtxt('Mr21quad_covar.dat')
fabxi21_error_l4=np.loadtxt('Mr21hexa_covar.dat')
fabxi19_error_l0=np.sqrt(np.diag(fabxi19_error_l0))
fabxi19_error_l2=np.sqrt(np.diag(fabxi19_error_l2))
fabxi19_error_l4=np.sqrt(np.diag(fabxi19_error_l4))
fabxi20_error_l0=np.sqrt(np.diag(fabxi20_error_l0))
fabxi20_error_l2=np.sqrt(np.diag(fabxi20_error_l2))
fabxi20_error_l4=np.sqrt(np.diag(fabxi20_error_l4))
fabxi21_error_l0=np.sqrt(np.diag(fabxi21_error_l0))
fabxi21_error_l2=np.sqrt(np.diag(fabxi21_error_l2))
fabxi21_error_l4=np.sqrt(np.diag(fabxi21_error_l4))


s_center,cabxi19_l0,cabxi19_l2,cabxi19_l4,cnabxi19_l0,cnabxi19_l2,cnabxi19_l4=np.loadtxt('Xipoles19_HW13_centAVG.dat',unpack=True)
s_center,cabxi20_l0,cabxi20_l2,cabxi20_l4,cnabxi20_l0,cnabxi20_l2,cnabxi20_l4=np.loadtxt('Xipoles20_HW13_centAVG.dat',unpack=True)
s_center,cabxi21_l0,cabxi21_l2,cabxi21_l4,cnabxi21_l0,cnabxi21_l2,cnabxi21_l4=np.loadtxt('Xipoles21_HW13_centAVG.dat',unpack=True)


ab_rp_cen,abwp19,abwp20,abwp21,nabwp19,nabwp20,nabwp21=np.loadtxt('HW13wp_avg_p1.dat',unpack=True)

abwp19_err=np.sqrt(np.loadtxt('Mr19wpavg_err.dat', unpack=True))
abwp20_err=np.sqrt(np.loadtxt('Mr20wpavg_err.dat', unpack=True))
abwp21_err=np.sqrt(np.loadtxt('Mr21wpavg_err.dat', unpack=True))
abwp19_err=np.loadtxt('Mr19wp_covar_cent.dat', unpack=True)
abwp20_err=np.loadtxt('Mr20wp_covar_cent.dat', unpack=True)
abwp21_err=np.loadtxt('Mr21wp_covar_cent.dat', unpack=True)
abwp19_err=np.sqrt(np.diag(abwp19_err))
abwp20_err=np.sqrt(np.diag(abwp20_err))
abwp21_err=np.sqrt(np.diag(abwp21_err))
abwp19_err=abwp19_err[0:12]*0
abwp20_err=abwp20_err[0:12]*0
abwp21_err=abwp21_err[0:12]*0
rp,enabwp19,enabwp20,enabwp21=np.loadtxt('hodHW13wp_cent_avg.dat',unpack=True)
rp,maccwp19,maccwp20,maccwp21=np.loadtxt('maccHW13wp_cent_avg.dat',unpack=True)
rp,vaccwp19,vaccwp20,vaccwp21=np.loadtxt('vaccHW13wp_cent_avg.dat',unpack=True)
rp,vpeakwp19,vpeakwp20,vpeakwp21=np.loadtxt('vpeakHW13wp_cent_avg.dat',unpack=True)
ab_rp_cen19,h1wp19,h1wp20,h1wp21,h2wp19,h2wp20,h2wp21,h3wp19,h3wp20,h3wp21,h4wp19,h4wp20,h4wp21,h5wp19,h5wp20,h5wp21=np.loadtxt('Wp_models_avg.dat', unpack=True)


ab_rp_cen19,cabwp19,cabwp19_err=np.loadtxt('Mr19wp_centavg.dat', unpack=True)
ab_rp_cen19,cabwp20,ca=np.loadtxt('Mr20wp_centavg.dat', unpack=True)
ab_rp_cen20,cabwp21,caberror_xi21=np.loadtxt('Mr21wp_centavg.dat', unpack=True)
ab_rp_cen19,cnabwp19,cabwp19_err=np.loadtxt('eMr19wp_centavg.dat', unpack=True)
ab_rp_cen19,cnabwp20,ca=np.loadtxt('eMr20wp_centavg.dat', unpack=True)
ab_rp_cen20,cnabwp21,caberror_xi21=np.loadtxt('eMr21wp_centavg.dat', unpack=True)


#Fig.2 HW13 vs 
ab_s_cen19=fs_center
r=1
a=.25
i=3

gs=plt.GridSpec(20, 20)
ax1=plt.subplot(gs[0:10,0:10])
ax2=plt.subplot(gs[0:10,10:20])
ax3=plt.subplot(gs[10:20,0:10])
ax4=plt.subplot(gs[10:20,10:20])

ax1.errorbar(ab_rp_cen19,0.1*abwp19,yerr=None,lw=r,markerfacecolor='k',color='k',fmt='o-',label='HW13$_{full}$')
ax1.fill_between(ab_rp_cen19,0.1*(abwp19+abwp19_err),0.1*(abwp19-abwp19_err),color='k', alpha=a)
ax1.errorbar(ab_rp_cen19,0.1*nabwp19,yerr=None,color='k',lw=i,fmt='--',label='Shuffled$_{full}$')
ax1.errorbar(ab_rp_cen19,0.1*h1wp19,yerr=None,color='orange',lw=i,fmt='--',label='HOD$_{full}$')
ax1.errorbar(ab_rp_cen19,0.1*h3wp19,yerr=None,color='m',lw=i,fmt=':',label='M$acc_{full}$')
ax1.errorbar(ab_rp_cen19,0.1*h4wp19,yerr=None,color='r',lw=i,fmt='-.',label='V$acc_{full}$')
ax1.errorbar(ab_rp_cen19,0.1*h5wp19,yerr=None,color='y',lw=i,fmt='--',label='V$peak_{full}$')
ax1.errorbar(ab_rp_cen19,0.1*cabwp19,yerr=None,color='k',markerfacecolor='grey',markeredgecolor='k',lw=i,fmt='s-',label='HW13$Centrals$')
ax1.errorbar(ab_rp_cen19,0.1*cnabwp19,yerr=None,color='k',fillstyle='none',markeredgecolor='k',lw=i,fmt='s--',label='Shuffled$Centrals$')
ax1.errorbar(ab_rp_cen19,abwp20,yerr=None,markerfacecolor='k',lw=r,color='k',fmt='o-')
ax1.fill_between(ab_rp_cen19,(abwp20+abwp20_err),(abwp20-abwp20_err),color='k', alpha=a)
ax1.errorbar(ab_rp_cen19,nabwp20,yerr=None,color='k',lw=i,fmt='--')
ax1.errorbar(ab_rp_cen19,h1wp20,yerr=None,color='orange',lw=i,fmt='--')
ax1.errorbar(ab_rp_cen19,h3wp20,yerr=None,color='m',lw=i,fmt=':')
ax1.errorbar(ab_rp_cen19,h4wp20,yerr=None,color='r',lw=i,fmt='-.')
ax1.errorbar(ab_rp_cen19,h5wp20,yerr=None,color='y',lw=i,fmt='--')
ax1.errorbar(ab_rp_cen19,cnabwp20,yerr=None,color='k',fillstyle='none',markeredgecolor='k',lw=i,fmt='s--')
ax1.errorbar(ab_rp_cen19,cabwp20,yerr=None,color='k',markerfacecolor='grey',markeredgecolor='k',lw=i,fmt='s-')
ax1.errorbar(ab_rp_cen19,10*abwp21,yerr=None,markerfacecolor='k',lw=r,color='k',fmt='o-')
ax1.fill_between(ab_rp_cen19,10*(abwp21+abwp21_err),10*(abwp21-abwp21_err),color='k', alpha=a)
ax1.errorbar(ab_rp_cen19,10*nabwp21,yerr=None,color='k',lw=i,fmt='--')
ax1.errorbar(ab_rp_cen19,10*h1wp21,yerr=None,color='orange',lw=i,fmt='--')
ax1.errorbar(ab_rp_cen19,10*h3wp21,yerr=None,color='m',lw=i,fmt=':')
ax1.errorbar(ab_rp_cen19,10*h4wp21,yerr=None,color='r',lw=i,fmt='-.')
ax1.errorbar(ab_rp_cen19,10*h5wp21,yerr=None,color='y',lw=i,fmt='--')
ax1.errorbar(ab_rp_cen21,10*cabwp21,yerr=None,markerfacecolor='grey',markeredgecolor='k',color='k',lw=i,fmt='s-')
ax1.errorbar(ab_rp_cen21,10*cnabwp21,yerr=None,fillstyle='none',markeredgecolor='k',color='k',lw=i,fmt='s--')

ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*cabxi19_l2),yerr=None,lw=i,markerfacecolor='grey',color='k',fmt='s-')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*cnabxi19_l2),yerr=None,lw=i,fillstyle='none',color='k',fmt='s--')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*cabxi19_l0+20),yerr=None,lw=i,markerfacecolor='grey',color='k',fmt='s-',label='Centrals')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*cnabxi19_l0+20),yerr=None,lw=i,fillstyle='none',color='k',fmt='s--',label='Centrals$_{shuff}$')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*cabxi19_l4-120),yerr=None,color='k',markerfacecolor='grey',lw=i,fmt='s-')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*cnabxi19_l4-120),yerr=None,color='k',fillstyle='none',lw=i,fmt='s--')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi19_l2),yerr=None,lw=r,color='k',fmt='o-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(fabxi19_l2+fabxi19_error_l2),(ab_s_cen19**2)*(fabxi19_l2-fabxi19_error_l2),color='k', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi19_l2),yerr=None,lw=i,color='k',fmt='--')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh1xi19_l2),yerr=None,lw=i,color='orange',fmt='--')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh3xi19_l2),yerr=None,lw=i,color='m',fmt=':')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh4xi19_l2),yerr=None,lw=i,color='r',fmt='-.')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh5xi19_l2),yerr=None,lw=i,color='y',fmt='--')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi19_l0+20),yerr=None,lw=r,color='k',fmt='o-',label='Full')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(fabxi19_l0+fabxi19_error_l0)+20,(ab_s_cen19**2)*(fabxi19_l0-fabxi19_error_l0)+20,color='k', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi19_l0+20),yerr=None,lw=i,color='k',fmt='--',label='Full$_{shuff}$')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh1xi19_l0+20),yerr=None,lw=i,color='orange',fmt='--',label='Full$_{shuff}$')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh3xi19_l0+20),yerr=None,lw=i,color='m',fmt=':',label='Full$_{shuff}$')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh4xi19_l0+20),yerr=None,lw=i,color='r',fmt='-.',label='Full$_{shuff}$')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh5xi19_l0+20),yerr=None,lw=i,color='y',fmt='--',label='Full$_{shuff}$')

ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi19_l4-120),yerr=None,lw=r,color='k',fmt='o-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(fabxi19_l4+fabxi19_error_l4)-120,(ab_s_cen19**2)*(fabxi19_l4-fabxi19_error_l4)-120,color='k', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi19_l4-120),yerr=None,color='k',lw=i,fmt='--')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh1xi19_l4-120),yerr=None,color='orange',lw=i,fmt='--')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh3xi19_l4-120),yerr=None,color='m',lw=i,fmt=':')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh4xi19_l4-120),yerr=None,color='r',lw=i,fmt='-.')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh5xi19_l4-120),yerr=None,color='y',lw=i,fmt='--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*cabxi20_l2),yerr=None,markerfacecolor='grey',lw=i,color='k',fmt='s-')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*cnabxi20_l2),yerr=None,fillstyle='none',lw=i,color='k',fmt='s--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*cabxi20_l0+20),yerr=None,lw=i,markerfacecolor='grey',color='k',fmt='s-',label='Centrals')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*cnabxi20_l0+20),yerr=None,lw=i,fillstyle='none',color='k',fmt='s--',label='Centrals$_{shuff}$')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*cabxi20_l4-120),yerr=None,lw=i,color='k',markerfacecolor='grey',fmt='s-')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*cnabxi20_l4-120),yerr=None,lw=i,color='k',fillstyle='none',fmt='s--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi20_l2),yerr=None,lw=r,color='k',fmt='o-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(fabxi20_l2+fabxi20_error_l2),(ab_s_cen19**2)*(fabxi20_l2-fabxi20_error_l2),color='k', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi20_l2),yerr=None,lw=i,color='k',fmt='--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh1xi20_l2),yerr=None,lw=i,color='orange',fmt='--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh3xi20_l2),yerr=None,lw=i,color='m',fmt=':')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh4xi20_l2),yerr=None,lw=i,color='r',fmt='-.')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh5xi20_l2),yerr=None,lw=i,color='y',fmt='--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi20_l0+20),yerr=None,lw=r,color='k',fmt='o-',label='HW13')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(fabxi20_l0+fabxi20_error_l0)+20,(ab_s_cen19**2)*(fabxi20_l0-fabxi20_error_l0)+20,color='k', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi20_l0+20),yerr=None,lw=i,color='k',fmt='--',label='Shuffled')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh1xi20_l0+20),yerr=None,lw=i,color='orange',fmt='--',label='Shuffled')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh3xi20_l0+20),yerr=None,lw=i,color='m',fmt=':',label='Shuffled')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh4xi20_l0+20),yerr=None,lw=i,color='r',fmt='-.',label='Shuffled')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh5xi20_l0+20),yerr=None,lw=i,color='y',fmt='--',label='Shuffled')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi20_l4-120),yerr=None,lw=r,color='k',fmt='o-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(fabxi20_l4+fabxi20_error_l4)-120,(ab_s_cen19**2)*(fabxi20_l4-fabxi20_error_l4)-120,color='k', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi20_l4-120),yerr=None,lw=i,color='k',fmt='--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh1xi20_l4-120),yerr=None,lw=i,color='orange',fmt='--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh3xi20_l4-120),yerr=None,lw=i,color='m',fmt=':')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh4xi20_l4-120),yerr=None,lw=i,color='r',fmt='-.')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh5xi20_l4-120),yerr=None,lw=i,color='y',fmt='--')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*cabxi21_l2),yerr=None,lw=i,color='k',markerfacecolor='grey',fmt='s-')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*cnabxi21_l2),yerr=None,lw=i,color='k',fillstyle='none',fmt='s--')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*cabxi21_l0+20),yerr=None,lw=i,color='k',fmt='s-',markerfacecolor='grey',label='Centrals')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*cnabxi21_l0+20),yerr=None,lw=i,color='k',fmt='s--',fillstyle='none',label='Centrals$_{shuff}$')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*cabxi21_l4-120),yerr=None,lw=i,color='k',markerfacecolor='grey',fmt='s-')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*cnabxi21_l4-120),yerr=None,lw=i,color='k',fillstyle='none',fmt='s--')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi21_l2),yerr=None,lw=r,color='k',fmt='o-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(fabxi21_l2+fabxi21_error_l2),(ab_s_cen19**2)*(fabxi21_l2-fabxi21_error_l2),color='k', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi21_l2),yerr=None,lw=i,color='k',fmt='--')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh1xi21_l2),yerr=None,lw=i,color='orange',fmt='--')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh3xi21_l2),yerr=None,lw=i,color='m',fmt=':')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh4xi21_l2),yerr=None,lw=i,color='r',fmt='-.')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh5xi21_l2),yerr=None,lw=i,color='y',fmt='--')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi21_l0+20),yerr=None,lw=r,color='k',fmt='o-',label='HW13')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(fabxi21_l0+fabxi21_error_l0)+20,(ab_s_cen19**2)*(fabxi21_l0-fabxi21_error_l0)+20,color='k', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi21_l0+20),yerr=None,lw=i,color='k',fmt='--',label='Shuffled')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh1xi21_l0+20),yerr=None,lw=i,color='orange',fmt='--',label='Shuffled')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh3xi21_l0+20),yerr=None,lw=i,color='m',fmt=':',label='Shuffled')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh4xi21_l0+20),yerr=None,lw=i,color='r',fmt='-.',label='Shuffled')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh5xi21_l0+20),yerr=None,lw=i,color='y',fmt='--',label='Shuffled')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi21_l4-120),yerr=None,lw=r,color='k',fmt='o-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(fabxi21_l4+fabxi21_error_l4)-120,(ab_s_cen19**2)*(fabxi21_l4-fabxi21_error_l4)-120,color='k', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi21_l4-120),yerr=None,lw=i,color='k',fmt='--')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh1xi21_l4-120),yerr=None,lw=i,color='orange',fmt='--')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh3xi21_l4-120),yerr=None,lw=i,color='m',fmt=':')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh4xi21_l4-120),yerr=None,lw=i,color='r',fmt='-.')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fh5xi21_l4-120),yerr=None,lw=i,color='y',fmt='--')

ax1.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.tick_params('both', length=15, width=1, which='major',labelsize=20)
ax1.tick_params('both', length=10, width=1, which='minor')
ax2.tick_params('both', length=15, width=1, which='major',labelsize=20)
ax2.tick_params('both', length=10, width=1, which='minor')
ax3.tick_params('both', length=15, width=1, which='major',labelsize=20)
ax3.tick_params('both', length=10, width=1, which='minor')
ax4.tick_params('both', length=15, width=1, which='major',labelsize=20)
ax4.tick_params('both', length=10, width=1, which='minor')
ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')
ax1.set_yscale('log')
ax4.set_xscale('log')
ax1.set_xlim(0.1,50)
ax2.set_xlim(0.1,50)
ax3.set_xlim(0.1,50)
ax4.set_xlim(0.1,50)
ax1.set_ylim(0.007,20000)
ax2.set_ylim(-140,120)
ax3.set_ylim(-140,120)
ax4.set_ylim(-140,120)
ax1.set_xlabel('r$_p$ [h$^{-1}$Mpc]',fontsize=20)
ax2.set_xlabel('s [h$^{-1}$Mpc]',fontsize=20)
ax3.set_xlabel('s [h$^{-1}$Mpc]',fontsize=20)
ax4.set_xlabel('s [h$^{-1}$Mpc]',fontsize=20)
ax1.set_ylabel(r'w$_p$(r$_p$) [h$^{-1}$Mpc]',labelpad=-1,fontsize=20)
ax2.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-1,fontsize=20)
ax3.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-1,fontsize=20)
ax4.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-4,fontsize=20)
ax1.set_yticks([1,100,10000])
ax2.set_yticks(np.arange(-120,120,40))
ax3.set_yticks(np.arange(-120,120,40))
ax4.set_yticks(np.arange(-120,120,40))
ax2.text(0.2,100,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=20)
ax3.text(0.2,100,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=20)
ax4.text(0.2,100,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=20)
ax1.text(4,0.10,'M$_r$ <-19\n-1 dex',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax1.text(2,80,'M$_r$ < -20',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax1.text(5,600,'M$_r$ < -21\n+1 dex',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax2.text(0.15,-109,r's$^2$$\xi_4$-120',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax2.text(0.15,-19,r's$^2$$\xi_2$',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax2.text(0.15,31,r's$^2$$\xi_0$+20',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)

ax1.legend(loc='lower left', fontsize=15)
plt.show()



#Fig. 7 HW13 vs SDSS DR7
rp_dr7,wp19dr7,xi19dr7_l0,xi19dr7_l2,xi19dr7_l4=np.loadtxt('wpxi_dr72_mr19.dat',unpack=True)
rp_dr7,wp20dr7,xi20dr7_l0,xi20dr7_l2,xi20dr7_l4=np.loadtxt('wpxi_dr72_mr20.dat',unpack=True)
rp_dr7,wp21dr7,xi21dr7_l0,xi21dr7_l2,xi21dr7_l4=np.loadtxt('wpxi_dr72_mr21.dat',unpack=True)
wpxicov19=np.loadtxt('wpxicov_dr72_mr19.dat')
wpxicov20=np.loadtxt('wpxicov_dr72_mr20.dat')
wpxicov21=np.loadtxt('wpxicov_dr72_mr21.dat')

wp19dr7_err=np.sqrt(np.diag(wpxicov19)[0:12])
xi19dr7_error_l0=np.sqrt(np.diag(wpxicov19)[12:24])
xi19dr7_error_l2=np.sqrt(np.diag(wpxicov19)[24:36])
xi19dr7_error_l4=np.sqrt(np.diag(wpxicov19)[36:48])
wp20dr7_err=np.sqrt(np.diag(wpxicov20)[0:12])
xi20dr7_error_l0=np.sqrt(np.diag(wpxicov20)[12:24])
xi20dr7_error_l2=np.sqrt(np.diag(wpxicov20)[24:36])
xi20dr7_error_l4=np.sqrt(np.diag(wpxicov20)[36:48])
wp21dr7_err=np.sqrt(np.diag(wpxicov21)[0:12])
xi21dr7_error_l0=np.sqrt(np.diag(wpxicov21)[12:24])
xi21dr7_error_l2=np.sqrt(np.diag(wpxicov21)[24:36])
xi21dr7_error_l4=np.sqrt(np.diag(wpxicov21)[36:48])

fs_center,fabxi19_l0,fabxi19_l2,fabxi19_l4,fnabxi19_l0,fnabxi19_l2,fnabxi19_l4=np.loadtxt('Xipoles19_HW13_avg_12bin.dat',unpack=True)
fs_center,fabxi20_l0,fabxi20_l2,fabxi20_l4,fnabxi20_l0,fnabxi20_l2,fnabxi20_l4=np.loadtxt('Xipoles20_HW13_avg_12bin.dat',unpack=True)
fs_center,fabxi21_l0,fabxi21_l2,fabxi21_l4,fnabxi21_l0,fnabxi21_l2,fnabxi21_l4=np.loadtxt('Xipoles21_HW13_avg_12bin.dat',unpack=True)

ab_rp_cen19,abwp19,abwp20,abwp21,nabwp19,nabwp20,nabwp21=np.loadtxt('HW13wp_avg_12bin.dat', unpack=True)

fs_center,fnabxi19_l0,fnabxi19_l2,fnabxi19_l4=np.loadtxt('Xipoles19_eHW13_avg_12bin.dat',unpack=True)
fs_center,fnabxi20_l0,fnabxi20_l2,fnabxi20_l4=np.loadtxt('Xipoles20_eHW13_avg_12bin.dat',unpack=True)
fs_center,fnabxi21_l0,fnabxi21_l2,fnabxi21_l4=np.loadtxt('Xipoles21_eHW13_avg_12bin.dat',unpack=True)

ab_rp_cen19,nabwp19,nabwp20,nabwp21=np.loadtxt('eHW13wp_avg_12bin.dat', unpack=True)


ab_s_cen19=fs_center
r=1
i=1

gs=plt.GridSpec(20, 20)
ax1=plt.subplot(gs[0:10,0:10])
ax2=plt.subplot(gs[0:10,10:20])
ax3=plt.subplot(gs[10:20,0:10])
ax4=plt.subplot(gs[10:20,10:20])

ax1.errorbar(ab_rp_cen19,0.1*wp19dr7,yerr=None,lw=r,markerfacecolor='k',color='k',fmt='o-',label='SDSS DR7')
ax1.fill_between(ab_rp_cen19,0.1*(wp19dr7+wp19dr7_err),0.1*(wp19dr7-wp19dr7_err),color='k', alpha=a)
ax1.errorbar(ab_rp_cen19,0.1*abwp19,yerr=None,color='k',fillstyle='none',markeredgecolor='k',lw=i,fmt='o--',label='HW13')
ax1.errorbar(ab_rp_cen19,wp20dr7,yerr=None,markerfacecolor='k',lw=r,color='k',fmt='o-')
ax1.fill_between(ab_rp_cen19,(wp20dr7+wp20dr7_err),(wp20dr7-wp20dr7_err),color='k', alpha=a)
ax1.errorbar(ab_rp_cen19,abwp20,yerr=None,color='k',fillstyle='none',markeredgecolor='k',lw=i,fmt='o--')
ax1.errorbar(ab_rp_cen19,10*wp21dr7,yerr=None,markerfacecolor='k',lw=r,color='k',fmt='o-')
ax1.fill_between(ab_rp_cen19,10*(wp21dr7+wp21dr7_err),10*(wp21dr7-wp21dr7_err),color='k', alpha=a)
ax1.errorbar(ab_rp_cen19,10*abwp21,yerr=None,fillstyle='none',markeredgecolor='k',color='k',lw=i,fmt='o--')

ax1.errorbar(ab_rp_cen19,0.1*nabwp19,yerr=None,color='k',fillstyle='none',markeredgecolor='k',lw=i,fmt='s:',label='Shuffled')
ax1.errorbar(ab_rp_cen19,nabwp20,yerr=None,color='k',fillstyle='none',markeredgecolor='k',lw=i,fmt='s:')
ax1.errorbar(ab_rp_cen19,10*nabwp21,yerr=None,fillstyle='none',markeredgecolor='k',color='k',lw=i,fmt='s:')


ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi19dr7_l2),yerr=None,lw=r,color='k',fmt='o-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi19dr7_l2+xi19dr7_error_l2),(ab_s_cen19**2)*(xi19dr7_l2-xi19dr7_error_l2),color='k', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi19_l2),yerr=None,lw=i,fillstyle='none',color='k',fmt='o--')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi19dr7_l0+20),yerr=None,lw=r,color='k',fmt='o-',label='HW13')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi19dr7_l0+xi19dr7_error_l0)+20,(ab_s_cen19**2)*(xi19dr7_l0-xi19dr7_error_l0)+20,color='k', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi19_l0+20),yerr=None,lw=i,fillstyle='none',color='k',fmt='o--',label='Shuffled')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi19dr7_l4-60),yerr=None,lw=r,color='k',fmt='o-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi19dr7_l4+xi19dr7_error_l4)-60,(ab_s_cen19**2)*(xi19dr7_l4-xi19dr7_error_l4)-60,color='k', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi19_l4-60),yerr=None,color='k',fillstyle='none',lw=i,fmt='o--')


ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi19_l2),yerr=None,lw=i,fillstyle='none',color='k',fmt='s:')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi19_l0+20),yerr=None,lw=i,fillstyle='none',color='k',fmt='s:',label='Shuffled')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi19_l4-60),yerr=None,color='k',fillstyle='none',lw=i,fmt='s:')


ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi20dr7_l2),yerr=None,lw=r,color='k',fmt='o-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi20dr7_l2+xi20dr7_error_l2),(ab_s_cen19**2)*(xi20dr7_l2-xi20dr7_error_l2),color='k', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi20_l2),yerr=None,fillstyle='none',lw=i,color='k',fmt='o--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi20dr7_l0+20),yerr=None,lw=r,color='k',fmt='o-',label='HW13')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi20dr7_l0+xi20dr7_error_l0)+20,(ab_s_cen19**2)*(xi20dr7_l0-xi20dr7_error_l0)+20,color='k', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi20_l0+20),yerr=None,lw=i,fillstyle='none',color='k',fmt='o--',label='Shuffled')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi20dr7_l4-60),yerr=None,lw=r,color='k',fmt='o-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi20dr7_l4+xi20dr7_error_l4)-60,(ab_s_cen19**2)*(xi20dr7_l4-xi20dr7_error_l4)-60,color='k', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi20_l4-60),yerr=None,lw=i,color='k',fillstyle='none',fmt='o--')


ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi20_l2),yerr=None,fillstyle='none',lw=i,color='k',fmt='s:')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi20_l0+20),yerr=None,lw=i,fillstyle='none',color='k',fmt='s:',label='Shuffled')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi20_l4-60),yerr=None,lw=i,color='k',fillstyle='none',fmt='s:')


ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi21dr7_l2),yerr=None,lw=r,color='k',fmt='o-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi21dr7_l2+xi21dr7_error_l2),(ab_s_cen19**2)*(xi21dr7_l2-xi21dr7_error_l2),color='k', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi21_l2),yerr=None,lw=i,color='k',fillstyle='none',fmt='o--')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi21dr7_l0+20),yerr=None,lw=r,color='k',fmt='o-',label='HW13')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi21dr7_l0+xi21dr7_error_l0)+20,(ab_s_cen19**2)*(xi21dr7_l0-xi21dr7_error_l0)+20,color='k', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi21_l0+20),yerr=None,lw=i,color='k',fmt='o--',fillstyle='none',label='Shuffled')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi21dr7_l4-60),yerr=None,lw=r,color='k',fmt='o-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi21dr7_l4+xi21dr7_error_l4)-60,(ab_s_cen19**2)*(xi21dr7_l4-xi21dr7_error_l4)-60,color='k', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fabxi21_l4-60),yerr=None,lw=i,color='k',fillstyle='none',fmt='o--')

ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi21_l2),yerr=None,lw=i,color='k',fillstyle='none',fmt='s:')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi21_l0+20),yerr=None,lw=i,color='k',fmt='s:',fillstyle='none',label='Shuffled')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*fnabxi21_l4-60),yerr=None,lw=i,color='k',fillstyle='none',fmt='s:')



ax1.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.tick_params('both', length=10, width=1, which='major',labelsize=20)
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major',labelsize=20)
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major',labelsize=20)
ax3.tick_params('both', length=5, width=1, which='minor')
ax4.tick_params('both', length=10, width=1, which='major',labelsize=20)
ax4.tick_params('both', length=5, width=1, which='minor')
ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')
ax1.set_yscale('log')
ax4.set_xscale('log')
ax1.set_xlim(0.1,25)
ax2.set_xlim(0.1,25)
ax3.set_xlim(0.1,25)
ax4.set_xlim(0.1,25)
ax1.set_ylim(0.1,20000)
ax2.set_ylim(-80,100)
ax3.set_ylim(-80,100)
ax4.set_ylim(-80,100)
ax1.set_xlabel('r$_p$ [h$^{-1}$Mpc]',fontsize=20)
ax2.set_xlabel('s [h$^{-1}$Mpc]',fontsize=20)
ax3.set_xlabel('s [h$^{-1}$Mpc]',fontsize=20)
ax4.set_xlabel('s [h$^{-1}$Mpc]',fontsize=20)
ax1.set_ylabel(r'w$_p$(r$_p$) [h$^{-1}$Mpc]',labelpad=-1,fontsize=20)
ax2.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-1,fontsize=20)
ax3.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-1,fontsize=20)
ax4.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-4,fontsize=20)
ax1.set_yticks([1,100,10000])
ax2.set_yticks(np.arange(-60,100,20))
ax3.set_yticks(np.arange(-60,100,20))
ax4.set_yticks(np.arange(-60,100,20))
ax2.text(0.2,80,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=20)
ax3.text(0.2,80,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=20)
ax4.text(0.2,80,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=20)
ax1.text(2,0.2,'M$_r$ <-19\n-1 dex',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax1.text(0.33,360,'M$_r$ < -20',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax1.text(5,600,'M$_r$ < -21\n+1 dex',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax2.text(0.15,-50,r's$^2$$\xi_4$-60',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax2.text(0.15,-15,r's$^2$$\xi_2$',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax2.text(0.15,40,r's$^2$$\xi_0$+20',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)

ax1.legend(loc='lower left')

plt.show()

#Fig. 8 Blue vs DR7
rbs_center,bxi19_l0,bxi19_l2,bxi19_l4,rxi19_l0,rxi19_l2,rxi19_l4=np.loadtxt('Xipoles19_HW13_bluered_avg_12.dat',unpack=True)
rbs_center,bxi20_l0,bxi20_l2,bxi20_l4,rxi20_l0,rxi20_l2,rxi20_l4=np.loadtxt('Xipoles20_HW13_bluered_avg_12.dat',unpack=True)
rbs_center,bxi21_l0,bxi21_l2,bxi21_l4,rxi21_l0,rxi21_l2,rxi21_l4=np.loadtxt('Xipoles21_HW13_bluered_avg_12.dat',unpack=True)


rp_dr7,bxi19dr7_l0,bxi19dr7_error_l0=np.loadtxt('xi0_dr72_mr19_blue.dat',unpack=True)
rp_dr7,bxi20dr7_l0,bxi20dr7_error_l0=np.loadtxt('xi0_dr72_mr20_blue.dat',unpack=True)
rp_dr7,bxi21dr7_l0,bxi21dr7_error_l0=np.loadtxt('xi0_dr72_mr21_blue.dat',unpack=True)
rp_dr7,bxi19dr7_l2,bxi19dr7_error_l2=np.loadtxt('xi2_dr72_mr19_blue.dat',unpack=True)
rp_dr7,bxi20dr7_l2,bxi20dr7_error_l2=np.loadtxt('xi2_dr72_mr20_blue.dat',unpack=True)
rp_dr7,bxi21dr7_l2,bxi21dr7_error_l2=np.loadtxt('xi2_dr72_mr21_blue.dat',unpack=True)
rp_dr7,bxi19dr7_l4,bxi19dr7_error_l4=np.loadtxt('xi4_dr72_mr19_blue.dat',unpack=True)
rp_dr7,bxi20dr7_l4,bxi20dr7_error_l4=np.loadtxt('xi4_dr72_mr20_blue.dat',unpack=True)
rp_dr7,bxi21dr7_l4,bxi21dr7_error_l4=np.loadtxt('xi4_dr72_mr21_blue.dat',unpack=True)
rp_dr7,bwp19dr7,bwp19dr7_err=np.loadtxt('wp_dr72_mr19_blue.dat',unpack=True)
rp_dr7,bwp20dr7,bwp20dr7_err=np.loadtxt('wp_dr72_mr20_blue.dat',unpack=True)
rp_dr7,bwp21dr7,bwp21dr7_err=np.loadtxt('wp_dr72_mr21_blue.dat',unpack=True)

ab_rp_cen19,bwp19,aberror_xi19=np.loadtxt('Mr19wp_blue.dat', unpack=True)
ab_rp_cen20,bwp20,aberror_xi20=np.loadtxt('Mr20wp_blue.dat', unpack=True)
ab_rp_cen21,bwp21,aberror_xi21=np.loadtxt('Mr21wp_blue.dat', unpack=True)


rp_dr7,rxi19dr7_l0,rxi19dr7_error_l0=np.loadtxt('xi0_dr72_mr19_red.dat',unpack=True)
rp_dr7,rxi20dr7_l0,rxi20dr7_error_l0=np.loadtxt('xi0_dr72_mr20_red.dat',unpack=True)
rp_dr7,rxi21dr7_l0,rxi21dr7_error_l0=np.loadtxt('xi0_dr72_mr21_red.dat',unpack=True)
rp_dr7,rxi19dr7_l2,rxi19dr7_error_l2=np.loadtxt('xi2_dr72_mr19_red.dat',unpack=True)
rp_dr7,rxi20dr7_l2,rxi20dr7_error_l2=np.loadtxt('xi2_dr72_mr20_red.dat',unpack=True)
rp_dr7,rxi21dr7_l2,rxi21dr7_error_l2=np.loadtxt('xi2_dr72_mr21_red.dat',unpack=True)
rp_dr7,rxi19dr7_l4,rxi19dr7_error_l4=np.loadtxt('xi4_dr72_mr19_red.dat',unpack=True)
rp_dr7,rxi20dr7_l4,rxi20dr7_error_l4=np.loadtxt('xi4_dr72_mr20_red.dat',unpack=True)
rp_dr7,rxi21dr7_l4,rxi21dr7_error_l4=np.loadtxt('xi4_dr72_mr21_red.dat',unpack=True)
rp_dr7,rwp19dr7,rwp19dr7_err=np.loadtxt('wp_dr72_mr19_red.dat',unpack=True)
rp_dr7,rwp20dr7,rwp20dr7_err=np.loadtxt('wp_dr72_mr20_red.dat',unpack=True)
rp_dr7,rwp21dr7,rwp21dr7_err=np.loadtxt('wp_dr72_mr21_red.dat',unpack=True)

ab_rp_cen19,rwp19,aberror_xi19=np.loadtxt('Mr19wp_red.dat', unpack=True)
ab_rp_cen20,rwp20,aberror_xi20=np.loadtxt('Mr20wp_red.dat', unpack=True)
ab_rp_cen21,rwp21,aberror_xi21=np.loadtxt('Mr21wp_red.dat', unpack=True)

mcmc_19red=np.loadtxt('MCMC_DR7red_Mr19.dat', unpack=False)
wp_19r=mcmc_19red[-1,10:22]
xi_0_19r=mcmc_19red[-1,22:34]
xi_2_19r=mcmc_19red[-1,34:46]
xi_4_19r=mcmc_19red[-1,46:58]
chi2_19r=mcmc_19red[-1,2]

mcmc_19blue=np.loadtxt('MCMC_DR7blue_Mr19.dat', unpack=False)
wp_19b=mcmc_19blue[-1,10:22]
xi_0_19b=mcmc_19blue[-1,22:34]
xi_2_19b=mcmc_19blue[-1,34:46]
xi_4_19b=mcmc_19blue[-1,46:58]
chi2_19b=mcmc_19blue[-1,2]

mcmc_20red=np.loadtxt('MCMC_DR7red_Mr20.dat', unpack=False)
wp_20r=mcmc_20red[-1,10:22]
xi_0_20r=mcmc_20red[-1,22:34]
xi_2_20r=mcmc_20red[-1,34:46]
xi_4_20r=mcmc_20red[-1,46:58]
chi2_20r=mcmc_20red[-1,2]

mcmc_20blue=np.loadtxt('MCMC_DR7blue_Mr20.dat', unpack=False)
wp_20b=mcmc_20blue[-1,10:22]
xi_0_20b=mcmc_20blue[-1,22:34]
xi_2_20b=mcmc_20blue[-1,34:46]
xi_4_20b=mcmc_20blue[-1,46:58]
chi2_20b=mcmc_20blue[-1,2]

mcmc_21red=np.loadtxt('MCMC_DR7red_Mr21.dat', unpack=False)
wp_21r=mcmc_21red[-1,10:22]
xi_0_21r=mcmc_21red[-1,22:34]
xi_2_21r=mcmc_21red[-1,34:46]
xi_4_21r=mcmc_21red[-1,46:58]
chi2_21r=mcmc_21red[-1,2]

mcmc_21blue=np.loadtxt('MCMC_DR7blue_Mr21.dat', unpack=False)
wp_21b=mcmc_21blue[-1,10:22]
xi_0_21b=mcmc_21blue[-1,22:34]
xi_2_21b=mcmc_21blue[-1,34:46]
xi_4_21b=mcmc_21blue[-1,46:58]
chi2_21b=mcmc_21blue[-1,2]

ab_s_cen19=rbs_center
r=1
i=1

gs=plt.GridSpec(20, 20)
ax1=plt.subplot(gs[0:10,0:10])
ax2=plt.subplot(gs[0:10,10:20])
ax3=plt.subplot(gs[10:20,0:10])
ax4=plt.subplot(gs[10:20,10:20])

ax1.errorbar(ab_rp_cen19,0.1*rwp19dr7,yerr=None,lw=r,markerfacecolor='r',color='r',fmt='s-',label='SDSS DR7$_{red}$')
ax1.fill_between(ab_rp_cen19,0.1*(rwp19dr7+rwp19dr7_err),0.1*(rwp19dr7-rwp19dr7_err),color='r', alpha=a)
ax1.errorbar(ab_rp_cen19,0.1*rwp19,yerr=None,color='r',fillstyle='none',markeredgecolor='r',lw=i,fmt='s--',label='HW13$_{red}$')

ax1.errorbar(ab_rp_cen19,rwp20dr7,yerr=None,markerfacecolor='r',lw=r,color='r',fmt='s-')
ax1.fill_between(ab_rp_cen19,(rwp20dr7+rwp20dr7_err),(rwp20dr7-rwp20dr7_err),color='r', alpha=a)
ax1.errorbar(ab_rp_cen19,rwp20,yerr=None,color='r',fillstyle='none',markeredgecolor='r',lw=i,fmt='s--')

ax1.errorbar(ab_rp_cen19,10*rwp21dr7,yerr=None,markerfacecolor='r',lw=r,color='r',fmt='s-')
ax1.fill_between(ab_rp_cen21,10*(rwp21dr7+rwp21dr7_err),10*(rwp21dr7-rwp21dr7_err),color='r', alpha=a)
ax1.errorbar(ab_rp_cen21,10*rwp21,yerr=None,fillstyle='none',markeredgecolor='r',color='r',lw=i,fmt='s--')

ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi19dr7_l2),yerr=None,lw=r,color='r',fmt='s-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(rxi19dr7_l2+rxi19dr7_error_l2),(ab_s_cen19**2)*(rxi19dr7_l2-rxi19dr7_error_l2),color='r', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi19_l2),yerr=None,lw=i,fillstyle='none',color='r',fmt='s--')

ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi19dr7_l0+40),yerr=None,lw=r,color='r',fmt='s-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(rxi19dr7_l0+rxi19dr7_error_l0)+40,(ab_s_cen19**2)*(rxi19dr7_l0-rxi19dr7_error_l0)+40,color='r', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi19_l0+40),yerr=None,lw=i,fillstyle='none',color='r',fmt='s--')

ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi19dr7_l4-60),yerr=None,lw=r,color='r',fmt='s-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(rxi19dr7_l4+rxi19dr7_error_l4)-60,(ab_s_cen19**2)*(rxi19dr7_l4-rxi19dr7_error_l4)-60,color='r', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi19_l4-60),yerr=None,color='r',fillstyle='none',lw=i,fmt='s--')

ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi20dr7_l2),yerr=None,lw=r,color='r',fmt='s-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(rxi20dr7_l2+rxi20dr7_error_l2),(ab_s_cen19**2)*(rxi20dr7_l2-rxi20dr7_error_l2),color='r', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi20_l2),yerr=None,lw=i,fillstyle='none',color='r',fmt='s--')

ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi20dr7_l0+40),yerr=None,lw=r,color='r',fmt='s-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(rxi20dr7_l0+rxi20dr7_error_l0)+40,(ab_s_cen19**2)*(rxi20dr7_l0-rxi20dr7_error_l0)+40,color='r', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi20_l0+40),yerr=None,lw=i,fillstyle='none',color='r',fmt='s--')

ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi20dr7_l4-60),yerr=None,lw=r,color='r',fmt='s-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(rxi20dr7_l4+rxi20dr7_error_l4)-60,(ab_s_cen19**2)*(rxi20dr7_l4-rxi20dr7_error_l4)-60,color='r', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi20_l4-60),yerr=None,color='r',fillstyle='none',lw=i,fmt='s--')

ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi21dr7_l2),yerr=None,lw=r,color='r',fmt='s-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(rxi21dr7_l2+rxi21dr7_error_l2),(ab_s_cen19**2)*(rxi21dr7_l2-rxi21dr7_error_l2),color='r', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi21_l2),yerr=None,lw=i,fillstyle='none',color='r',fmt='s--')

ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi21dr7_l0+40),yerr=None,lw=r,color='r',fmt='s-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(rxi21dr7_l0+rxi21dr7_error_l0)+40,(ab_s_cen19**2)*(rxi21dr7_l0-rxi21dr7_error_l0)+40,color='r', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi21_l0+40),yerr=None,lw=i,fillstyle='none',color='r',fmt='s--')

ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi21dr7_l4-60),yerr=None,lw=r,color='r',fmt='s-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(rxi21dr7_l4+rxi21dr7_error_l4)-60,(ab_s_cen19**2)*(rxi21dr7_l4-rxi21dr7_error_l4)-60,color='r', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi21_l4-60),yerr=None,color='r',fillstyle='none',lw=i,fmt='s--')

ax1.errorbar(ab_rp_cen19,0.1*bwp19dr7,yerr=None,lw=r,markerfacecolor='b',color='b',fmt='o-')
ax1.fill_between(ab_rp_cen19,0.1*(bwp19dr7+bwp19dr7_err),0.1*(bwp19dr7-bwp19dr7_err),color='b', alpha=a)
ax1.errorbar(ab_rp_cen19,0.1*bwp19,yerr=None,color='b',fillstyle='none',markeredgecolor='b',lw=i,fmt='o--')

ax1.errorbar(ab_rp_cen19,bwp20dr7,yerr=None,markerfacecolor='b',lw=r,color='b',fmt='o-')
ax1.fill_between(ab_rp_cen19,(bwp20dr7+bwp20dr7_err),(bwp20dr7-bwp20dr7_err),color='b', alpha=a)
ax1.errorbar(ab_rp_cen19,bwp20,yerr=None,color='b',fillstyle='none',markeredgecolor='b',lw=i,fmt='o--')

ax1.errorbar(ab_rp_cen19,10*bwp21dr7,yerr=None,markerfacecolor='b',lw=r,color='b',fmt='o-',label='SDSS DR7$_{blue}$')
ax1.fill_between(ab_rp_cen21,10*(bwp21dr7+bwp21dr7_err),10*(bwp21dr7-bwp21dr7_err),color='b', alpha=a)
ax1.errorbar(ab_rp_cen21,10*bwp21,yerr=None,fillstyle='none',markeredgecolor='b',color='b',lw=i,fmt='o--',label='HW13$_{blue}$')

ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi19dr7_l2),yerr=None,lw=r,color='b',fmt='o-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(bxi19dr7_l2+bxi19dr7_error_l2),(ab_s_cen19**2)*(bxi19dr7_l2-bxi19dr7_error_l2),color='b', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi19_l2),yerr=None,lw=i,fillstyle='none',color='b',fmt='o--')

ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi19dr7_l0+40),yerr=None,lw=r,color='b',fmt='o-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(bxi19dr7_l0+bxi19dr7_error_l0)+40,(ab_s_cen19**2)*(bxi19dr7_l0-bxi19dr7_error_l0)+40,color='b', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi19_l0+40),yerr=None,lw=i,fillstyle='none',color='b',fmt='o--')

ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi19dr7_l4-60),yerr=None,lw=r,color='b',fmt='o-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(bxi19dr7_l4+bxi19dr7_error_l4)-60,(ab_s_cen19**2)*(bxi19dr7_l4-bxi19dr7_error_l4)-60,color='b', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi19_l4-60),yerr=None,color='b',fillstyle='none',lw=i,fmt='o--')

ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi20dr7_l2),yerr=None,lw=r,color='b',fmt='o-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(bxi20dr7_l2+bxi20dr7_error_l2),(ab_s_cen19**2)*(bxi20dr7_l2-bxi20dr7_error_l2),color='b', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi20_l2),yerr=None,lw=i,fillstyle='none',color='b',fmt='o--')

ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi20dr7_l0+40),yerr=None,lw=r,color='b',fmt='o-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(bxi20dr7_l0+bxi20dr7_error_l0)+40,(ab_s_cen19**2)*(bxi20dr7_l0-bxi20dr7_error_l0)+40,color='b', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi20_l0+40),yerr=None,lw=i,fillstyle='none',color='b',fmt='o--')

ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi20dr7_l4-60),yerr=None,lw=r,color='b',fmt='o-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(bxi20dr7_l4+bxi20dr7_error_l4)-60,(ab_s_cen19**2)*(bxi20dr7_l4-bxi20dr7_error_l4)-60,color='b', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi20_l4-60),yerr=None,color='b',fillstyle='none',lw=i,fmt='o--')

ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi21dr7_l2),yerr=None,lw=r,color='b',fmt='o-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(bxi21dr7_l2+bxi21dr7_error_l2),(ab_s_cen19**2)*(bxi21dr7_l2-bxi21dr7_error_l2),color='b', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi21_l2),yerr=None,lw=i,fillstyle='none',color='b',fmt='o--')

ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi21dr7_l0+40),yerr=None,lw=r,color='b',fmt='o-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(bxi21dr7_l0+bxi21dr7_error_l0)+40,(ab_s_cen19**2)*(bxi21dr7_l0-bxi21dr7_error_l0)+40,color='b', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi21_l0+40),yerr=None,lw=i,fillstyle='none',color='b',fmt='o--')

ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi21dr7_l4-60),yerr=None,lw=r,color='b',fmt='o-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(bxi21dr7_l4+bxi21dr7_error_l4)-60,(ab_s_cen19**2)*(bxi21dr7_l4-bxi21dr7_error_l4)-60,color='b', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*bxi21_l4-60),yerr=None,color='b',fillstyle='none',lw=i,fmt='o--')

ax1.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.tick_params('both', length=10, width=1, which='major',labelsize=20)
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major',labelsize=20)
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major',labelsize=20)
ax3.tick_params('both', length=5, width=1, which='minor')
ax4.tick_params('both', length=10, width=1, which='major',labelsize=20)
ax4.tick_params('both', length=5, width=1, which='minor')
ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')
ax1.set_yscale('log')
ax4.set_xscale('log')
ax1.set_xlim(0.1,25)
ax2.set_xlim(0.1,25)
ax3.set_xlim(0.1,25)
ax4.set_xlim(0.1,25)
ax1.set_ylim(0.1,20500)
ax2.set_ylim(-80,140)
ax3.set_ylim(-80,140)
ax4.set_ylim(-80,140)
ax1.set_xlabel('r$_p$ [h$^{-1}$Mpc]',fontsize=20)
ax2.set_xlabel('s [h$^{-1}$Mpc]',fontsize=20)
ax3.set_xlabel('s [h$^{-1}$Mpc]',fontsize=20)
ax4.set_xlabel('s [h$^{-1}$Mpc]',fontsize=20)
ax1.set_ylabel(r'w$_p$(r$_p$) [h$^{-1}$Mpc]',labelpad=-1,fontsize=20)
ax2.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-1,fontsize=20)
ax3.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-1,fontsize=20)
ax4.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-4,fontsize=20)
ax1.set_yticks([1,100,10000])
ax2.set_yticks(np.arange(-60,140,20))
ax3.set_yticks(np.arange(-60,140,20))
ax4.set_yticks(np.arange(-60,140,20))
ax2.text(0.2,120,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=20)
ax3.text(0.2,120,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=20)
ax4.text(0.2,120,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=20)

ax1.text(1.5,0.2,'M$_r$ <-19\n-1 dex',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax1.text(5,600,'M$_r$ < -21\n+1 dex',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax2.text(0.15,-45,r's$^2$$\xi_4$-60',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax2.text(0.15,-15,r's$^2$$\xi_2$',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)
ax2.text(0.15,25,r's$^2$$\xi_0$+40',bbox=dict(facecolor='w', edgecolor='w'),fontsize=20)

ax1.legend(loc='lower left')

plt.show()


#Fig. 9 Red vs DR7
rp_dr7,xi19dr7_l0,xi19dr7_error_l0=np.loadtxt('xi0_dr72_mr19_red.dat',unpack=True)
rp_dr7,xi20dr7_l0,xi20dr7_error_l0=np.loadtxt('xi0_dr72_mr20_red.dat',unpack=True)
rp_dr7,xi21dr7_l0,xi21dr7_error_l0=np.loadtxt('xi0_dr72_mr21_red.dat',unpack=True)
rp_dr7,xi19dr7_l2,xi19dr7_error_l2=np.loadtxt('xi2_dr72_mr19_red.dat',unpack=True)
rp_dr7,xi20dr7_l2,xi20dr7_error_l2=np.loadtxt('xi2_dr72_mr20_red.dat',unpack=True)
rp_dr7,xi21dr7_l2,xi21dr7_error_l2=np.loadtxt('xi2_dr72_mr21_red.dat',unpack=True)
rp_dr7,xi19dr7_l4,xi19dr7_error_l4=np.loadtxt('xi4_dr72_mr19_red.dat',unpack=True)
rp_dr7,xi20dr7_l4,xi20dr7_error_l4=np.loadtxt('xi4_dr72_mr20_red.dat',unpack=True)
rp_dr7,xi21dr7_l4,xi21dr7_error_l4=np.loadtxt('xi4_dr72_mr21_red.dat',unpack=True)

rp_dr7,wp19dr7,wp19dr7_err=np.loadtxt('wp_dr72_mr19_red.dat',unpack=True)
rp_dr7,wp20dr7,wp20dr7_err=np.loadtxt('wp_dr72_mr20_red.dat',unpack=True)
rp_dr7,wp21dr7,wp21dr7_err=np.loadtxt('wp_dr72_mr21_red.dat',unpack=True)
ab_rp_cen19,rwp19,abwp19_err=np.loadtxt('Mr19wp_red.dat', unpack=True)
ab_rp_cen20,rwp20,aberror_xi20=np.loadtxt('Mr20wp_red.dat', unpack=True)
ab_rp_cen21,rwp21,aberror_xi21=np.loadtxt('Mr21wp_red.dat', unpack=True)

ab_s_cen19=rbs_center
r=1

i=1

gs=plt.GridSpec(20, 20)
ax1=plt.subplot(gs[0:10,0:10])
ax2=plt.subplot(gs[0:10,10:20])
ax3=plt.subplot(gs[10:20,0:10])
ax4=plt.subplot(gs[10:20,10:20])
ax1.errorbar(ab_rp_cen19,0.1*wp19dr7,yerr=0.1*wp19dr7_err,lw=r,markerfacecolor='k',color='k',fmt='o-',label='SDSS DR7$_{Red}$')
ax1.fill_between(ab_rp_cen19,0.1*(wp19dr7+wp19dr7_err),0.1*(wp19dr7-wp19dr7_err),color='k', alpha=a)
ax1.errorbar(ab_rp_cen19,0.1*rwp19,yerr=None,color='k',fillstyle='none',markeredgecolor='k',lw=i,fmt='o--',label='HW13$_{Red}$')
ax1.errorbar(ab_rp_cen19,wp20dr7,yerr=wp20dr7_err,markerfacecolor='k',lw=r,color='k',fmt='o-')
ax1.fill_between(ab_rp_cen19,(wp20dr7+wp20dr7_err),(wp20dr7-wp20dr7_err),color='k', alpha=a)
ax1.errorbar(ab_rp_cen19,rwp20,yerr=None,color='k',fillstyle='none',markeredgecolor='k',lw=i,fmt='o--')
ax1.errorbar(ab_rp_cen19,10*wp21dr7,yerr=10*wp21dr7_err,markerfacecolor='k',lw=r,color='k',fmt='o-')
ax1.fill_between(ab_rp_cen21,10*(wp21dr7+wp21dr7_err),10*(wp21dr7-wp21dr7_err),color='k', alpha=a)
ax1.errorbar(ab_rp_cen21,10*rwp21,yerr=None,fillstyle='none',markeredgecolor='k',color='k',lw=i,fmt='o--')

ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi19dr7_l2),yerr=((ab_s_cen19**2)*xi19dr7_error_l2),lw=r,color='k',fmt='o-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi19dr7_l2+xi19dr7_error_l2),(ab_s_cen19**2)*(xi19dr7_l2-xi19dr7_error_l2),color='k', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi19_l2),yerr=None,lw=i,fillstyle='none',color='k',fmt='o--')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi19dr7_l0+20),yerr=((ab_s_cen19**2)*xi19dr7_error_l0),lw=r,color='k',fmt='o-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi19dr7_l0+xi19dr7_error_l0)+20,(ab_s_cen19**2)*(xi19dr7_l0-xi19dr7_error_l0)+20,color='k', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi19_l0+20),yerr=None,lw=i,fillstyle='none',color='k',fmt='o--')
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi19dr7_l4-60),yerr=((ab_s_cen19**2)*xi19dr7_error_l4),lw=r,color='k',fmt='o-')
ax2.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi19dr7_l4+xi19dr7_error_l4)-60,(ab_s_cen19**2)*(xi19dr7_l4-xi19dr7_error_l4)-60,color='k', alpha=a)
ax2.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi19_l4-60),yerr=None,color='k',fillstyle='none',lw=i,fmt='o--')

ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi20dr7_l2),yerr=((ab_s_cen19**2)*xi20dr7_error_l2),lw=r,color='k',fmt='o-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi20dr7_l2+xi20dr7_error_l2),(ab_s_cen19**2)*(xi20dr7_l2-xi20dr7_error_l2),color='k', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi20_l2),yerr=None,fillstyle='none',lw=i,color='k',fmt='o--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi20dr7_l0+20),yerr=((ab_s_cen19**2)*xi20dr7_error_l0),lw=r,color='k',fmt='o-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi20dr7_l0+xi20dr7_error_l0)+20,(ab_s_cen19**2)*(xi20dr7_l0-xi20dr7_error_l0)+20,color='k', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi20_l0+20),yerr=None,lw=i,fillstyle='none',color='k',fmt='o--')
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi20dr7_l4-60),yerr=((ab_s_cen19**2)*xi20dr7_error_l4),lw=r,color='k',fmt='o-')
ax3.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi20dr7_l4+xi20dr7_error_l4)-60,(ab_s_cen19**2)*(xi20dr7_l4-xi20dr7_error_l4)-60,color='k', alpha=a)
ax3.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi20_l4-60),yerr=None,lw=i,color='k',fillstyle='none',fmt='o--')

ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi21dr7_l2),yerr=((ab_s_cen19**2)*xi21dr7_error_l2),lw=r,color='k',fmt='o-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi21dr7_l2+xi21dr7_error_l2),(ab_s_cen19**2)*(xi21dr7_l2-xi21dr7_error_l2),color='k', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi21_l2),yerr=None,lw=i,color='k',fillstyle='none',fmt='o--')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi21dr7_l0+20),yerr=((ab_s_cen19**2)*xi21dr7_error_l0),lw=r,color='k',fmt='o-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi21dr7_l0+xi21dr7_error_l0)+20,(ab_s_cen19**2)*(xi21dr7_l0-xi21dr7_error_l0)+20,color='k', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi21_l0+20),yerr=None,lw=i,color='k',fmt='o--',fillstyle='none')
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*xi21dr7_l4-60),yerr=((ab_s_cen19**2)*xi21dr7_error_l4),lw=r,color='k',fmt='o-')
ax4.fill_between(ab_s_cen19,(ab_s_cen19**2)*(xi21dr7_l4+xi21dr7_error_l4)-60,(ab_s_cen19**2)*(xi21dr7_l4-xi21dr7_error_l4)-60,color='k', alpha=a)
ax4.errorbar(ab_s_cen19,((ab_s_cen19**2)*rxi21_l4-60),yerr=None,lw=i,color='k',fillstyle='none',fmt='o--')
ax1.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='minor',axis='x',color='b',zorder=0,alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',zorder=0,alpha=0.5,linestyle='--')
ax1.tick_params('both', length=10, width=1, which='major')
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major')
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major')
ax3.tick_params('both', length=5, width=1, which='minor')
ax4.tick_params('both', length=10, width=1, which='major')
ax4.tick_params('both', length=5, width=1, which='minor')
ax1.set_xscale('log')
ax2.set_xscale('log')
ax3.set_xscale('log')
ax1.set_yscale('log')
ax4.set_xscale('log')
ax1.set_xlim(0.1,25)
ax2.set_xlim(0.1,25)
ax3.set_xlim(0.1,25)
ax4.set_xlim(0.1,25)
ax1.set_ylim(0.1,20000)
ax2.set_ylim(-80,120)
ax3.set_ylim(-80,120)
ax4.set_ylim(-80,120)
ax1.set_xlabel('r$_p$ [h$^{-1}$Mpc]',fontsize=18)
ax2.set_xlabel('s [h$^{-1}$Mpc]',fontsize=18)
ax3.set_xlabel('s [h$^{-1}$Mpc]',fontsize=18)
ax4.set_xlabel('s [h$^{-1}$Mpc]',fontsize=18)
ax1.set_ylabel(r'w$_p$(r$_p$) [h$^{-1}$Mpc]',labelpad=-1,fontsize=18)
ax2.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-1,fontsize=18)
ax3.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-1,fontsize=18)
ax4.set_ylabel(r's$^2$$\xi_l$(s) [h$^{-1}$Mpc]$^2$',labelpad=-4,fontsize=18)
ax2.set_yticks(np.arange(-80,140,20))
ax3.set_yticks(np.arange(-80,140,20))
ax4.set_yticks(np.arange(-80,140,20))
ax2.text(0.2,80,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=16)
ax3.text(0.2,80,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=16)
ax4.text(0.2,80,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=16)

ax1.text(4,0.2,'M$_r$ <-19\n-1 dex',bbox=dict(facecolor='w', edgecolor='w'),fontsize=14)
ax1.text(0.33,360,'M$_r$ < -20',bbox=dict(facecolor='w', edgecolor='w'),fontsize=14)
ax1.text(5,600,'M$_r$ < -21\n+1 dex',bbox=dict(facecolor='w', edgecolor='w'),fontsize=14)
ax2.text(0.15,-50,r's$^2$$\xi_4$-60',bbox=dict(facecolor='w', edgecolor='w'),fontsize=14)
ax2.text(0.15,-10,r's$^2$$\xi_2$',bbox=dict(facecolor='w', edgecolor='w'),fontsize=14)
ax2.text(0.15,30,r's$^2$$\xi_0$+20',bbox=dict(facecolor='w', edgecolor='w'),fontsize=14)

ax1.legend(loc='lower left')

plt.show()

