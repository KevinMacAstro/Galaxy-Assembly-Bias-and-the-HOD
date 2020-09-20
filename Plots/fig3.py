# Plots figure 3 from publication: fsig_8^ for HW13 and shuffled full and central only galaxy mocks.
# With ratrio panel.
# Also used for Fig. 4, 7, 9, and 10.

import numpy as np
import matplotlib.pyplot as plt

fs_center,cestimator_fab19,cestimator_fnab19,cestimator_fab20,cestimator_fnab20,cestimator_fab21,cestimator_fnab21=np.sqrt(np.loadtxt('estimator_centAVG_HW13.dat',unpack=True))
s2_center,cestimator_ab19_2,cestimator_nab19_2,cestimator_ab20_2,cestimator_nab20_2,cestimator_ab21_2,cestimator_nab21_2=np.sqrt(np.loadtxt('estimator_centAVGcut_HW13.dat',unpack=True))
fs_center,estimator_fab19,estimator_fnab19,estimator_fab20,estimator_fnab20,estimator_fab21,estimator_fnab21=np.sqrt(np.loadtxt('estimator_hw13_avg_new.dat',unpack=True))
s2_center,estimator_ab19_2,estimator_nab19_2,estimator_ab20_2,estimator_nab20_2,estimator_ab21_2,estimator_nab21_2=np.sqrt(np.loadtxt('estimator_hw13_avgcut_new.dat',unpack=True))

fs_center,estimator_f1h19,estimator_f2h19,estimator_f3h19,estimator_f4h19,estimator_f5h19,estimator_f1h20,estimator_f2h20,estimator_f3h20,estimator_f4h20,estimator_f5h20,estimator_f1h21,estimator_f2h21,estimator_f3h21,estimator_f4h21,estimator_f5h21=np.sqrt(np.loadtxt('estimator_models_avg_new.dat',unpack=True))
s2_center,estimator_1h19_2,estimator_2h19_2,estimator_3h19_2,estimator_4h19_2,estimator_5h19_2,estimator_1h20_2,estimator_2h20_2,estimator_3h20_2,estimator_4h20_2,estimator_5h20_2,estimator_1h21_2,estimator_2h21_2,estimator_3h21_2,estimator_4h21_2,estimator_5h21_2=np.sqrt(np.loadtxt('estimator_models_avgcut_new.dat',unpack=True))

s2_center,cestimator_1h19_2,cestimator_3h19_2,cestimator_4h19_2,cestimator_5h19_2,cestimator_1h20_2,cestimator_3h20_2,cestimator_4h20_2,cestimator_5h20_2,cestimator_1h21_2,cestimator_3h21_2,cestimator_4h21_2,cestimator_5h21_2=np.sqrt(np.loadtxt('estimator_models_cent_avgCUT.dat',unpack=True))



est_err19=np.loadtxt('est19_covar.dat',unpack=True)
est_err20=np.loadtxt('est20_covar.dat',unpack=True)
est_err21=np.loadtxt('est21_covar.dat',unpack=True)
est_err19=np.sqrt(np.diag(est_err19))
est_err20=np.sqrt(np.diag(est_err20))
est_err21=np.sqrt(np.diag(est_err21))


est_err19_2=np.loadtxt('est19_covar_2cut.dat',unpack=True)
est_err20_2=np.loadtxt('est20_covar_2cut.dat',unpack=True)
est_err21_2=np.loadtxt('est21_covar_2cut.dat',unpack=True)
est_err19_2=np.sqrt(np.diag(est_err19_2))
est_err20_2=np.sqrt(np.diag(est_err20_2))
est_err21_2=np.sqrt(np.diag(est_err21_2))

cest_err19=np.loadtxt('est19_cent_27covar.dat',unpack=True)
cest_err20=np.loadtxt('est20_cent_27covar.dat',unpack=True)
cest_err21=np.loadtxt('est21_cent_27covar.dat',unpack=True)
cest_err19=np.sqrt(np.diag(cest_err19))
cest_err20=np.sqrt(np.diag(cest_err20))
cest_err21=np.sqrt(np.diag(cest_err21))


cest_err19_2=np.loadtxt('est19_cent_27covar_2cut.dat',unpack=True)
cest_err20_2=np.loadtxt('est20_cent_27covar_2cut.dat',unpack=True)
cest_err21_2=np.loadtxt('est21_cent_27covar_2cut.dat',unpack=True)
cest_err19_2=np.sqrt(np.diag(cest_err19_2))
cest_err20_2=np.sqrt(np.diag(cest_err20_2))
cest_err21_2=np.sqrt(np.diag(cest_err21_2))


fs_center=fs_center**2
s2_center=s2_center**2


crat19_fnab=cestimator_fnab19/cestimator_fab19
crat20_fnab=cestimator_fnab20/cestimator_fab20
crat21_fnab=cestimator_fnab21/cestimator_fab21
crat19_fnab=cestimator_fnab19/cestimator_fab19
crat20_fnab=cestimator_fnab20/cestimator_fab20
crat21_fnab=cestimator_fnab21/cestimator_fab21

rat19_fnab=estimator_fnab19/estimator_fab19
rat20_fnab=estimator_fnab20/estimator_fab20
rat21_fnab=estimator_fnab21/estimator_fab21
rat19_fnab=estimator_fnab19/estimator_fab19
rat20_fnab=estimator_fnab20/estimator_fab20
rat21_fnab=estimator_fnab21/estimator_fab21


rat19_2_nab=estimator_nab19_2/estimator_ab19_2
rat20_2_nab=estimator_nab20_2/estimator_ab20_2
rat21_2_nab=estimator_nab21_2/estimator_ab21_2
rat19_2_nab=estimator_nab19_2/estimator_ab19_2
rat20_2_nab=estimator_nab20_2/estimator_ab20_2
rat21_2_nab=estimator_nab21_2/estimator_ab21_2


crat19_2_nab=cestimator_nab19_2/cestimator_ab19_2
crat20_2_nab=cestimator_nab20_2/cestimator_ab20_2
crat21_2_nab=cestimator_nab21_2/cestimator_ab21_2
crat19_2_nab=cestimator_nab19_2/cestimator_ab19_2
crat20_2_nab=cestimator_nab20_2/cestimator_ab20_2
crat21_2_nab=cestimator_nab21_2/cestimator_ab21_2

rat19f_h1=estimator_f1h19/estimator_fab19
rat20f_h1=estimator_f1h20/estimator_fab20
rat21f_h1=estimator_f1h21/estimator_fab21
rat19f_h2=estimator_f2h19/estimator_fab19
rat20f_h2=estimator_f2h20/estimator_fab20
rat21f_h2=estimator_f2h21/estimator_fab21
rat19f_h3=estimator_f3h19/estimator_fab19
rat20f_h3=estimator_f3h20/estimator_fab20
rat21f_h3=estimator_f3h21/estimator_fab21
rat19f_h4=estimator_f4h19/estimator_fab19
rat20f_h4=estimator_f4h20/estimator_fab20
rat21f_h4=estimator_f4h21/estimator_fab21
rat19f_h5=estimator_f5h19/estimator_fab19
rat20f_h5=estimator_f5h20/estimator_fab20
rat21f_h5=estimator_f5h21/estimator_fab21
rat19_2_h1=estimator_1h19_2/estimator_ab19_2
rat20_2_h1=estimator_1h20_2/estimator_ab20_2
rat21_2_h1=estimator_1h21_2/estimator_ab21_2
rat19_2_h2=estimator_2h19_2/estimator_ab19_2
rat20_2_h2=estimator_2h20_2/estimator_ab20_2
rat21_2_h2=estimator_2h21_2/estimator_ab21_2
rat19_2_h3=estimator_3h19_2/estimator_ab19_2
rat20_2_h3=estimator_3h20_2/estimator_ab20_2
rat21_2_h3=estimator_3h21_2/estimator_ab21_2
rat19_2_h4=estimator_4h19_2/estimator_ab19_2
rat20_2_h4=estimator_4h20_2/estimator_ab20_2
rat21_2_h4=estimator_4h21_2/estimator_ab21_2
rat19_2_h5=estimator_5h19_2/estimator_ab19_2
rat20_2_h5=estimator_5h20_2/estimator_ab20_2
rat21_2_h5=estimator_5h21_2/estimator_ab21_2


crat19_2_h1=cestimator_1h19_2/cestimator_ab19_2
crat20_2_h1=cestimator_1h20_2/cestimator_ab20_2
crat21_2_h1=cestimator_1h21_2/cestimator_ab21_2
crat19_2_h3=cestimator_3h19_2/cestimator_ab19_2
crat20_2_h3=cestimator_3h20_2/cestimator_ab20_2
crat21_2_h3=cestimator_3h21_2/cestimator_ab21_2
crat19_2_h4=cestimator_4h19_2/cestimator_ab19_2
crat20_2_h4=cestimator_4h20_2/cestimator_ab20_2
crat21_2_h4=cestimator_4h21_2/cestimator_ab21_2
crat19_2_h5=cestimator_5h19_2/cestimator_ab19_2
crat20_2_h5=cestimator_5h20_2/cestimator_ab20_2
crat21_2_h5=cestimator_5h21_2/cestimator_ab21_2


rat19_2_hoderr=np.loadtxt('est19_27rathod_covar_2cut.dat',unpack=False)
rat19_2_hoderr=np.sqrt(np.diag(rat19_2_hoderr))
rat20_2_hoderr=np.loadtxt('est20_27rathod_covar_2cut.dat',unpack=False)
rat20_2_hoderr=np.sqrt(np.diag(rat20_2_hoderr))
rat21_2_hoderr=np.loadtxt('est21_27rathod_covar_2cut.dat',unpack=False)
rat21_2_hoderr=np.sqrt(np.diag(rat21_2_hoderr))

rat19_2_maccerr=np.loadtxt('est19_27ratmacc_covar_2cut.dat',unpack=False)
rat19_2_maccerr=np.sqrt(np.diag(rat19_2_maccerr))
rat20_2_maccerr=np.loadtxt('est20_27ratmacc_covar_2cut.dat',unpack=False)
rat20_2_maccerr=np.sqrt(np.diag(rat20_2_maccerr))
rat21_2_maccerr=np.loadtxt('est21_27ratmacc_covar_2cut.dat',unpack=False)
rat21_2_maccerr=np.sqrt(np.diag(rat21_2_maccerr))

rat19_2_vaccerr=np.loadtxt('est19_27ratvacc_covar_2cut.dat',unpack=False)
rat19_2_vaccerr=np.sqrt(np.diag(rat19_2_vaccerr))
rat20_2_vaccerr=np.loadtxt('est20_27ratvacc_covar_2cut.dat',unpack=False)
rat20_2_vaccerr=np.sqrt(np.diag(rat20_2_vaccerr))
rat21_2_vaccerr=np.loadtxt('est21_27ratvacc_covar_2cut.dat',unpack=False)
rat21_2_vaccerr=np.sqrt(np.diag(rat21_2_vaccerr))

rat19_2_vpeakerr=np.loadtxt('est19_27ratvpeak_covar_2cut.dat',unpack=False)
rat19_2_vpeakerr=np.sqrt(np.diag(rat19_2_vpeakerr))
rat20_2_vpeakerr=np.loadtxt('est20_27ratvpeak_covar_2cut.dat',unpack=False)
rat20_2_vpeakerr=np.sqrt(np.diag(rat20_2_vpeakerr))
rat21_2_vpeakerr=np.loadtxt('est21_27ratvpeak_covar_2cut.dat',unpack=False)
rat21_2_vpeakerr=np.sqrt(np.diag(rat21_2_vpeakerr))


crat19_2_hoderr=np.loadtxt('cest19_27rathod_covar_2cut.dat',unpack=False)
crat19_2_hoderr=np.sqrt(np.diag(crat19_2_hoderr))
crat20_2_hoderr=np.loadtxt('cest20_27rathod_covar_2cut.dat',unpack=False)
crat20_2_hoderr=np.sqrt(np.diag(crat20_2_hoderr))
crat21_2_hoderr=np.loadtxt('cest21_27rathod_covar_2cut.dat',unpack=False)
crat21_2_hoderr=np.sqrt(np.diag(crat21_2_hoderr))


crat19_2_eerr=np.loadtxt('cest19_27rate_covar_2cut.dat',unpack=False)
crat19_2_eerr=np.sqrt(np.diag(crat19_2_eerr))
crat20_2_eerr=np.loadtxt('cest20_27rate_covar_2cut.dat',unpack=False)
crat20_2_eerr=np.sqrt(np.diag(crat20_2_eerr))
crat21_2_eerr=np.loadtxt('cest21_27rate_covar_2cut.dat',unpack=False)
crat21_2_eerr=np.sqrt(np.diag(crat21_2_eerr))


crat19_2_maccerr=np.loadtxt('cest19_27ratmacc_covar_2cut.dat',unpack=False)
crat19_2_maccerr=np.sqrt(np.diag(crat19_2_maccerr))
crat20_2_maccerr=np.loadtxt('cest20_27ratmacc_covar_2cut.dat',unpack=False)
crat20_2_maccerr=np.sqrt(np.diag(crat20_2_maccerr))
crat21_2_maccerr=np.loadtxt('cest21_27ratmacc_covar_2cut.dat',unpack=False)
crat21_2_maccerr=np.sqrt(np.diag(crat21_2_maccerr))

crat19_2_vaccerr=np.loadtxt('cest19_27ratvacc_covar_2cut.dat',unpack=False)
crat19_2_vaccerr=np.sqrt(np.diag(crat19_2_vaccerr))
crat20_2_vaccerr=np.loadtxt('cest20_27ratvacc_covar_2cut.dat',unpack=False)
crat20_2_vaccerr=np.sqrt(np.diag(crat20_2_vaccerr))
crat21_2_vaccerr=np.loadtxt('cest21_27ratvacc_covar_2cut.dat',unpack=False)
crat21_2_vaccerr=np.sqrt(np.diag(crat21_2_vaccerr))

crat19_2_vpeakerr=np.loadtxt('cest19_27ratvpeak_covar_2cut.dat',unpack=False)
crat19_2_vpeakerr=np.sqrt(np.diag(crat19_2_vpeakerr))
crat20_2_vpeakerr=np.loadtxt('cest20_27ratvpeak_covar_2cut.dat',unpack=False)
crat20_2_vpeakerr=np.sqrt(np.diag(crat20_2_vpeakerr))
crat21_2_vpeakerr=np.loadtxt('cest21_27ratvpeak_covar_2cut.dat',unpack=False)
crat21_2_vpeakerr=np.sqrt(np.diag(crat21_2_vpeakerr))

crat19_eerr=np.loadtxt('cest19_27rate_covar_full.dat',unpack=False)
crat19_eerr=np.sqrt(np.diag(crat19_eerr))
crat20_eerr=np.loadtxt('cest20_27rate_covar_full.dat',unpack=False)
crat20_eerr=np.sqrt(np.diag(crat20_eerr))
crat21_eerr=np.loadtxt('cest21_27rate_covar_full.dat',unpack=False)
crat21_eerr=np.sqrt(np.diag(crat21_eerr))





#Fig.5 HW13 vs models and centralsw with ratios, cut
r=2
m=2
e=30
g=2
i=3
b=0.25

gs=plt.GridSpec(20, 30)
ax1=plt.subplot(gs[0:14,0:10])
ax2=plt.subplot(gs[0:14,10:20])
ax3=plt.subplot(gs[0:14,20:30])
ax4=plt.subplot(gs[14:20,0:10])
ax5=plt.subplot(gs[14:20,10:20])
ax6=plt.subplot(gs[14:20,20:30])
gs.update(wspace=0.025, hspace=0.05)


line1=ax1.errorbar(s2_center,estimator_ab19_2,yerr=None,lw=m,color='k',fmt='o-',label='HW13$_{cut<r_p=2}$')
ax1.fill_between(s2_center,(estimator_ab19_2+est_err19_2),(estimator_ab19_2-est_err19_2),color='k', alpha=b)
line2=ax1.errorbar(s2_center,estimator_1h19_2,lw=i,color='orange',ls='--',label='HOD$_{cut<r_p=2}$')

line3=ax2.errorbar(s2_center,estimator_ab19_2,yerr=None,lw=m,color='k',fmt='o-',label='HW13$_{cut<r_p=2}$')
ax2.fill_between(s2_center,(estimator_ab19_2+est_err19_2),(estimator_ab19_2-est_err19_2),color='k', alpha=b)
line4=ax2.errorbar(s2_center,estimator_3h19_2,lw=i,color='purple',ls=':',label='M$acc_{cut<r_p=2}$')
line5=ax2.errorbar(s2_center,estimator_4h19_2,lw=i,color='r',ls='-.',label='V$acc_{cut<r_p=2}$')
line6=ax2.errorbar(s2_center,estimator_5h19_2,lw=i,color='y',ls='--',label='V$peak_{cut<r_p=2}$')

line7=ax3.errorbar(s2_center,cestimator_ab19_2,yerr=None,lw=m,color='b',fmt='o-',label='HW13$_{cut<r_p=2,cent}$')
ax3.fill_between(s2_center,(cestimator_ab19_2+cest_err19_2),(cestimator_ab19_2-cest_err19_2),color='b', alpha=b)
line8=ax3.errorbar(s2_center,cestimator_nab19_2,lw=i,color='b',fmt='o--',label='Shuffled$_{cut<r_p=2,cent}$')
line9=ax3.errorbar(s2_center,cestimator_1h19_2,lw=i,color='k',ls='-',label='HOD$_{cut<r_p=2,cent}$')
line10=ax3.errorbar(s2_center,cestimator_3h19_2,lw=i,color='purple',ls=':',label='M$acc_{cut<r_p=2,cent}$')
line11=ax3.errorbar(s2_center,cestimator_4h19_2,lw=i,color='r',ls='-.',label='V$acc_{cut<r_p=2,cent}$')
line12=ax3.errorbar(s2_center,cestimator_5h19_2,lw=i,color='y',ls='--',label='V$peak_{cut<r_p=2,cent}$')


ax4.fill_between(s2_center,(rat19_2_h1-rat19_2_hoderr),(rat19_2_h1+rat19_2_hoderr),color='orange', alpha=b)
ax4.errorbar(s2_center,rat19_2_h1,yerr=None,lw=i,color='orange',ls='--')
ax5.fill_between(s2_center,(rat19_2_h5-rat19_2_vpeakerr),(rat19_2_h5+rat19_2_vpeakerr),color='y', alpha=b)
ax5.errorbar(s2_center,rat19_2_h3,yerr=None,lw=i,color='purple',ls=':')
ax5.errorbar(s2_center,rat19_2_h4,yerr=None,lw=i,color='r',ls='-.')
ax5.errorbar(s2_center,rat19_2_h5,yerr=None,lw=i,color='y',ls='--')
ax6.fill_between(s2_center,(crat19_2_h5-crat19_2_vpeakerr),(crat19_2_h5+crat19_2_vpeakerr),color='y', alpha=b)
ax6.errorbar(s2_center,crat19_2_nab,yerr=None,lw=i,color='b',fmt='o--')
ax6.errorbar(s2_center,crat19_2_h1,yerr=None,lw=i,color='k',ls='-')
ax6.errorbar(s2_center,crat19_2_h3,yerr=None,lw=i,color='purple',ls=':')
ax6.errorbar(s2_center,crat19_2_h4,yerr=None,lw=i,color='r',ls='-.')
ax6.errorbar(s2_center,crat19_2_h5,yerr=None,lw=i,color='y',ls='--')



ax1.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--',label='Bolshoi $f\sigma_8$')
ax3.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.text(2.2,-0.07,'-- Bolshoi $f\sigma_8$', bbox=dict(facecolor='w', edgecolor='k'),fontsize=20)

ones=np.zeros(len(s2_center))+1
ax4.errorbar(s2_center,ones,yerr=None,lw=r,color='k')
ax5.errorbar(s2_center,ones,yerr=None,lw=r,color='k')
ax6.errorbar(s2_center,ones,yerr=None,lw=r,color='k')
ax1.set_ylabel(r'$\widehat{f\sigma_8}$',fontsize=24)
ax1.set_xscale('log')
ax1.set_xlim(2,50)
ax1.set_ylim(-.1,0.5)
ax1.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.set_yticks([0.0,0.2,0.4])
ax1.set_xticklabels([])

ax2.set_ylim(-.1,0.5)
ax2.set_xscale('log')
ax2.set_xlim(2,50)
ax2.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.set_yticklabels([])
ax2.set_xticklabels([])


ax3.set_ylim(-.1,.5)
ax3.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax3.set_xscale('log')
ax3.set_xlim(2,50)
ax3.set_yticklabels([])
ax3.set_xticklabels([])

ax4.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax4.set_yticks(np.arange(0.9,1.20,.1))
ax4.set_ylabel(r'$\widehat{f\sigma_8}_{\rm model}/\widehat{f\sigma_8}_{\rm mock}$',labelpad=10,fontsize=24)
ax4.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax4.set_xscale('log')
ax4.set_xlim(2,50)
ax4.set_ylim(.8,1.2)
ax5.grid(True)
ax5.set_yticks(np.arange(0.9,1.20,.1))
ax5.set_yticklabels([])
ax5.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax5.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax5.set_xscale('log')
ax5.set_xlim(2,50)
ax5.set_ylim(0.8,1.2)
ax6.grid(True)
ax6.set_yticks(np.arange(0.9,1.20,.1))
ax6.set_yticklabels([])
ax6.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax6.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax6.set_xscale('log')
ax6.set_xlim(2,50)
ax6.set_ylim(.8,1.2)

ax1.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax3.tick_params('both', length=5, width=1, which='minor')
ax4.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax4.tick_params('both', length=5, width=1, which='minor')
ax5.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax5.tick_params('both', length=5, width=1, which='minor')
ax6.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax6.tick_params('both', length=5, width=1, which='minor')


ax1.legend(handles=[line1,line2], loc='upper left',fontsize=20)
ax2.legend(handles=[line3,line4,line5,line6], loc='upper left',fontsize=20)
ax3.legend(handles=[line7,line8,line9,line10,line11,line12], loc='upper left',fontsize=20)

plt.show()






#Fig. 3 HW13 & central full vs shuffle
b=0.25
r=2
m=2
i=3

gs=plt.GridSpec(10, 30)
ax1=plt.subplot(gs[0:10,0:10])
ax2=plt.subplot(gs[0:10,10:20])
ax3=plt.subplot(gs[0:10,20:30])
gs.update(wspace=0.025, hspace=0.05)

mask1_19=fs_center>2.5
mask2_19=fs_center>2.5
mask3_19=fs_center>2.5
mask4_19=fs_center>2.5
mask1_20=fs_center>2.5
mask2_20=fs_center>2.5
mask3_20=fs_center>2.5
mask4_20=fs_center>2.5
mask1_21=fs_center>2.5
mask2_21=fs_center>2.5
mask3_21=fs_center>2.5
mask4_21=fs_center>2.5



ax1.errorbar(fs_center[mask1_19],estimator_fab19[mask1_19],yerr=None,lw=r,color='k',fmt='o-',label='HW13$_{full}$')
ax1.fill_between(fs_center[mask1_19],(estimator_fab19+est_err19)[mask1_19],(estimator_fab19-est_err19)[mask1_19],color='k', alpha=b)
ax1.errorbar(fs_center[mask2_19],estimator_fnab19[mask2_19],yerr=None,lw=i,color='k',fmt='o--',label='Shuffled$_{full}$')
ax1.errorbar(fs_center[mask3_19],cestimator_fab19[mask3_19],yerr=None,lw=r,color='b',ls='-',label='HW13$_{full,cent}$')
ax1.fill_between(fs_center[mask3_19],(cestimator_fab19+cest_err19)[mask3_19],(cestimator_fab19-cest_err19)[mask3_19],color='b', alpha=b)
ax1.errorbar(fs_center[mask4_19],cestimator_fnab19[mask4_19],yerr=None,lw=r,color='b',ls='--',label='Shuffled$_{full,cent}$')
#ax1.errorbar(s2_center,estimator_ab19_2,yerr=est_err19_2,lw=m,color='g',ls='-',label='HW13$_{r_p>2}$')
#ax1.fill_between(s2_center,(estimator_ab19_2+est_err19_2),(estimator_ab19_2-est_err19_2),color='g', alpha=b)
#ax1.errorbar(s2_center,estimator_nab19_2,lw=m,color='g',ls='--',label='Shuffled$_{r_p>2}$')
ax2.errorbar(fs_center[mask1_20],estimator_fab20[mask1_20],yerr=None,lw=r,color='k',fmt='o-')
ax2.fill_between(fs_center[mask1_20],(estimator_fab20+est_err20)[mask1_20],(estimator_fab20-est_err20)[mask1_20],color='k', alpha=b)
ax2.errorbar(fs_center[mask2_20],estimator_fnab20[mask2_20],yerr=None,lw=i,color='k',fmt='o--')
ax2.errorbar(fs_center[mask3_20],cestimator_fab20[mask3_20],yerr=None,lw=r,color='b',ls='-')
ax2.fill_between(fs_center[mask3_20],(cestimator_fab20+cest_err20)[mask3_20],(cestimator_fab20-cest_err20)[mask3_20],color='b', alpha=b)
ax2.errorbar(fs_center[mask4_20],cestimator_fnab20[mask4_20],yerr=None,lw=r,color='b',ls='--')
#ax2.errorbar(s2_center,estimator_ab20_2,yerr=est_err20_2,lw=m,color='g',ls='-')
#ax2.fill_between(s2_center,(estimator_ab20_2+est_err20_2),(estimator_ab20_2-est_err20_2),color='g', alpha=b)
#ax2.errorbar(s2_center,estimator_nab20_2,lw=m,color='g',ls='--')
ax3.errorbar(fs_center[mask1_21],estimator_fab21[mask1_21],yerr=None,lw=r,color='k',fmt='o-')
ax3.fill_between(fs_center[mask1_21],(estimator_fab21+est_err21)[mask1_21],(estimator_fab21-est_err21)[mask1_21],color='k', alpha=b)
ax3.errorbar(fs_center[mask2_21],estimator_fnab21[mask2_21],yerr=None,lw=i,color='k',fmt='o--')
ax3.errorbar(fs_center[mask3_21],cestimator_fab21[mask3_21],yerr=None,lw=r,color='b',ls='-')
ax3.fill_between(fs_center[mask3_21],(cestimator_fab21+cest_err21)[mask3_21],(cestimator_fab21-cest_err21)[mask3_21],color='b', alpha=b)
ax3.errorbar(fs_center[mask4_21],cestimator_fnab21[mask4_21],yerr=None,lw=r,color='b',ls='--')
#ax3.errorbar(s2_center,estimator_ab21_2,yerr=est_err21_2,lw=m,color='g',ls='-')
#ax3.fill_between(s2_center,(estimator_ab21_2+est_err21_2),(estimator_ab21_2-est_err21_2),color='g', alpha=b)
#ax3.errorbar(s2_center,estimator_nab21_2,lw=m,color='g',ls='--')

ax1.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--',label='Bolshoi $f\sigma_8$')
ax3.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.legend(loc='upper left',fontsize=24)
ax1.text(2.2,-0.07,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax2.text(2.2,-0.07,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax3.text(2.2,-0.07,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax1.set_ylabel(r'$\widehat{f\sigma_8}$',fontsize=24)
ax1.set_xscale('log')
ax1.set_xlim(2,50)
ax1.set_ylim(-.1,0.5)
ax1.set_yticks([0.0,0.2,0.4])
ax1.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.legend(loc='upper left',fontsize=24)
ax1.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax2.set_ylim(-.1,0.5)
ax2.set_xscale('log')
ax2.set_xlim(2,50)
ax2.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax2.set_yticklabels([])
ax3.set_ylim(-.1,.5)
ax3.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax3.set_xscale('log')
ax3.set_xlim(2,50)
ax3.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax3.set_yticklabels([])
ax1.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax3.tick_params('both', length=5, width=1, which='minor')


plt.show()


#Fig. 3.1 HW13 & central full vs shuffle (inner cut)
r=2
m=2
i=3

gs=plt.GridSpec(10, 30)
ax1=plt.subplot(gs[0:10,0:10])
ax2=plt.subplot(gs[0:10,10:20])
ax3=plt.subplot(gs[0:10,20:30])
gs.update(wspace=0.025, hspace=0.05)

#ax1.errorbar(s2_center,estimator_ab19_2,yerr=None,lw=m,color='k',fmt='o-',label='HW13$_{cut<r_p=2}$')
#ax1.fill_between(s2_center,(estimator_ab19_2+est_err19_2),(estimator_ab19_2-est_err19_2),color='k', alpha=b)
#ax1.errorbar(s2_center,estimator_nab19_2,lw=i,color='k',fmt='o--',label='Shuffled$_{cut<r_p=2}$')
ax1.errorbar(s2_center,cestimator_ab19_2,yerr=None,lw=r,color='b',ls='-',label='HW13$_{cut<r_p=2,cent}$')
ax1.fill_between(s2_center,(cestimator_ab19_2+cest_err19_2),(cestimator_ab19_2-cest_err19_2),color='b', alpha=b)

ax1.errorbar(s2_center,cestimator_nab19_2,yerr=None,lw=r,color='b',ls='--',label='Shuffled$_{cut<r_p=2,cent}$')
#ax2.errorbar(s2_center,estimator_ab20_2,yerr=None,lw=m,color='k',fmt='o-')
#ax2.fill_between(s2_center,(estimator_ab20_2+est_err20_2),(estimator_ab20_2-est_err20_2),color='k', alpha=b)
#ax2.errorbar(s2_center,estimator_nab20_2,lw=i,color='k',fmt='o--')
ax2.errorbar(s2_center,cestimator_ab20_2,yerr=None,lw=r,color='b',ls='-')
ax2.fill_between(s2_center,(cestimator_ab20_2+cest_err20_2),(cestimator_ab20_2-cest_err20_2),color='b', alpha=b)

ax2.errorbar(s2_center,cestimator_nab20_2,yerr=None,lw=r,color='b',ls='--')
ax3.errorbar(s2_center,estimator_ab21_2,yerr=None,lw=m,color='k',fmt='o-')
ax3.fill_between(s2_center,(estimator_ab21_2+est_err21_2),(estimator_ab21_2-est_err21_2),color='k', alpha=b)
ax3.errorbar(s2_center,estimator_nab21_2,lw=i,color='k',fmt='o--')
ax3.errorbar(s2_center,cestimator_ab21_2,yerr=None,lw=r,color='b',ls='-',label='HW13$Centrals_{cut<r_p=2}$')
ax3.fill_between(s2_center,(cestimator_ab21_2+cest_err21_2),(cestimator_ab21_2-cest_err21_2),color='b', alpha=b)

ax3.errorbar(s2_center,cestimator_nab21_2,yerr=None,lw=r,color='b',ls='--',label='Shuffled$Centrals_{cut<r_p=2}$')

ax1.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--',label='Bolshoi $f\sigma_8$')
ax3.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.legend(loc='upper left',fontsize=24)
ax1.text(2.2,-0.07,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax2.text(2.2,-0.07,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax3.text(2.2,-0.07,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax1.set_ylabel(r'$\widehat{f\sigma_8}$',fontsize=24)
ax1.set_xscale('log')
ax1.set_xlim(2,50)
ax1.set_ylim(-.1,0.5)
ax1.set_yticks([0.0,0.2,0.4])
ax1.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.legend(loc='upper left',fontsize=20)
ax1.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax2.set_ylim(-.1,0.5)
ax2.set_xscale('log')
ax2.set_xlim(2,50)
ax2.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax2.set_yticklabels([])
ax3.set_ylim(-.1,.5)
ax3.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax3.set_xscale('log')
ax3.set_xlim(2,50)
ax3.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax3.set_yticklabels([])
ax1.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax3.tick_params('both', length=5, width=1, which='minor')



plt.show()


#Fig.5 HW13 vs HOD's with ratios, full
r=2
m=2
e=30
g=2
i=3

mask1_19=fs_center>6.5
mask2_19=fs_center>6.5
mask3_19=fs_center>6.5
mask1_20=fs_center>6.5
mask2_20=fs_center>6.5
mask3_20=fs_center>6.5
mask1_21=fs_center>6.5
mask2_21=fs_center>6.5
mask3_21=fs_center>6.5



gs=plt.GridSpec(20, 30)
ax1=plt.subplot(gs[0:14,0:10])
ax2=plt.subplot(gs[0:14,10:20])
ax3=plt.subplot(gs[0:14,20:30])
ax4=plt.subplot(gs[14:20,0:10])
ax5=plt.subplot(gs[14:20,10:20])
ax6=plt.subplot(gs[14:20,20:30])
gs.update(wspace=0.025, hspace=0.05)


line1=ax1.errorbar(fs_center[mask1_19],estimator_fab19[mask1_19],yerr=None,lw=r,color='k',fmt='o-',label='HW13$_{full}$')
ax1.fill_between(fs_center[mask1_19],(estimator_fab19+est_err19)[mask1_19],(estimator_fab19-est_err19)[mask1_19],color='k', alpha=b)
line2=ax1.errorbar(fs_center[mask2_19],estimator_f1h19[mask2_19],yerr=None,lw=i,color='orange',fmt='--',label='HOD$_{full}$')
#line3=ax1.errorbar(fs_center[mask3_19],estimator_f2h19[mask3_19],yerr=None,lw=i,color='r',fmt='-.',label='HOD$ls-match_{full}$')
#line4=ax1.errorbar(s2_center,estimator_ab19_2,yerr=None,lw=m,color='g',ls='-',label='HW13')
#ax1.fill_between(s2_center,(estimator_ab19_2+est_err19_2),(estimator_ab19_2-est_err19_2),color='g', alpha=b)
#line5=ax1.errorbar(s2_center,estimator_1h19_2,lw=m,color='g',ls='--',label='HOD')
#line6=ax1.errorbar(s2_center,estimator_2h19_2,lw=m,color='g',ls='-.',label='ls-matched$_{FoG\; Excluded}$')
ax2.errorbar(fs_center[mask1_20],estimator_fab20[mask1_20],yerr=None,lw=r,color='k',fmt='o-')
ax2.fill_between(fs_center[mask1_20],(estimator_fab20+est_err20)[mask1_20],(estimator_fab20-est_err20)[mask1_20],color='k', alpha=b)
ax2.errorbar(fs_center[mask2_20],estimator_f1h20[mask2_20],yerr=None,lw=i,color='orange',ls='--')
#ax2.errorbar(fs_center[mask3_20],estimator_f2h20[mask3_20],yerr=None,lw=i,color='r',ls='-.')
#ax2.errorbar(s2_center,estimator_ab20_2,yerr=None,lw=m,color='g',ls='-')
#ax2.fill_between(s2_center,(estimator_ab20_2+est_err20_2),(estimator_ab20_2-est_err20_2),color='g', alpha=b)
#ax2.errorbar(s2_center,estimator_1h20_2,lw=m,color='g',ls='--')
#ax2.errorbar(s2_center,estimator_2h20_2,lw=m,color='g',ls='-.')
ax3.errorbar(fs_center[mask1_21],estimator_fab21[mask1_21],yerr=None,lw=r,color='k',fmt='o-')
ax3.fill_between(fs_center[mask1_21],(estimator_fab21+est_err21)[mask1_21],(estimator_fab21-est_err21)[mask1_21],color='k', alpha=b)
ax3.errorbar(fs_center[mask2_21],estimator_f1h21[mask2_21],yerr=None,lw=i,color='orange',ls='--')
#ax3.errorbar(fs_center[mask3_21],estimator_f2h21[mask3_21],yerr=None,lw=i,color='r',ls='-.')
#ax3.errorbar(s2_center,estimator_ab21_2,yerr=None,lw=m,color='g',ls='-')
#ax3.fill_between(s2_center,(estimator_ab21_2+est_err21_2),(estimator_ab21_2-est_err21_2),color='g', alpha=b)
#ax3.errorbar(s2_center,estimator_1h21_2,lw=m,color='g',ls='--')
#ax3.errorbar(s2_center,estimator_2h21_2,lw=m,color='g',ls='-.')



ax4.errorbar(fs_center[mask2_19],rat19f_h1[mask2_19],yerr=None,lw=i,color='orange',ls='--')
ax5.errorbar(fs_center[mask2_20],rat20f_h1[mask2_20],yerr=None,lw=i,color='orange',ls='--')
ax6.errorbar(fs_center[mask2_21],rat21f_h1[mask2_21],yerr=None,lw=i,color='orange',ls='--')
#ax4.errorbar(fs_center[mask3_19],rat19f_h2[mask3_19],yerr=None,lw=i,color='r',ls='-.')
#ax5.errorbar(fs_center[mask3_20],rat20f_h2[mask3_20],yerr=None,lw=i,color='r',ls='-.')
#ax6.errorbar(fs_center[mask3_21],rat21f_h2[mask3_21],yerr=None,lw=i,color='r',ls='-.')
#ax4.errorbar(s2_center,rat19_2_h1,yerr=None,lw=g,color='g',ls='--')
#ax5.errorbar(s2_center,rat20_2_h1,yerr=None,lw=g,color='g',ls='--')
#ax6.errorbar(s2_center,rat21_2_h1,yerr=None,lw=g,color='g',ls='--')
#ax4.errorbar(s2_center,rat19_2_h2,yerr=None,lw=g,color='g',ls='-.')
#ax5.errorbar(s2_center,rat20_2_h2,yerr=None,lw=g,color='g',ls='-.')
#ax6.errorbar(s2_center,rat21_2_h2,yerr=None,lw=g,color='g',ls='-.')
ax1.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--',label='Bolshoi $f\sigma_8$')
ax3.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.legend(loc='upper left',fontsize=24)
ones=np.zeros(len(fs_center))+1
#rat_err19=est_err19/estimator_fab19
#rat_err20=est_err20/estimator_fab20
#rat_err21=est_err21/estimator_fab21
ax4.errorbar(fs_center,ones,yerr=None,lw=r,color='k')
ax5.errorbar(fs_center,ones,yerr=None,lw=r,color='k')
ax6.errorbar(fs_center,ones,yerr=None,lw=r,color='k')
ax4.fill_between(fs_center[mask1_19],(ones)[mask1_19],(ones)[mask1_19],color='k', alpha=b)
ax5.fill_between(fs_center[mask1_20],(ones)[mask1_20],(ones)[mask1_20],color='k', alpha=b)
ax6.fill_between(fs_center[mask1_21],(ones)[mask1_21],(ones)[mask1_21],color='k', alpha=b)
#ones=np.zeros(len(s2_center))+1
#rat_err19_2=est_err19_2/estimator_ab19_2
#rat_err20_2=est_err20_2/estimator_ab20_2
#rat_err21_2=est_err21_2/estimator_ab21_2
#ax4.errorbar(s2_center,ones,yerr=None,lw=r,color='g')
#ax4.fill_between(s2_center,(ones+rat_err19_2),(ones-rat_err19_2),color='g', alpha=b)
#ax5.errorbar(s2_center,ones,yerr=None,lw=r,color='g')
#ax5.fill_between(s2_center,(ones+rat_err20_2),(ones-rat_err20_2),color='g', alpha=b)
#ax6.errorbar(s2_center,ones,yerr=None,lw=r,color='g')
#ax6.fill_between(s2_center,(ones+rat_err21_2),(ones-rat_err21_2),color='g', alpha=b)
ax1.text(17,-0.07,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax2.text(1.2,-0.07,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax3.text(1.2,-0.07,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax1.set_ylabel(r'$\widehat{f\sigma_8}$',fontsize=24)
ax1.set_xscale('log')
ax1.set_xlim(1,50)
ax1.set_ylim(-.1,0.5)
ax1.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.set_yticks(np.arange(0,0.5,.1))
ax1.set_xticklabels([])

ax2.set_ylim(-.1,0.5)
ax2.set_xscale('log')
ax2.set_xlim(1,50)
ax2.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.set_yticklabels([])
ax2.set_xticklabels([])


ax3.set_ylim(-.1,.5)
ax3.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax3.set_xscale('log')
ax3.set_xlim(1,50)
ax3.set_yticklabels([])
ax3.set_xticklabels([])

ax4.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax4.set_xticks(np.arange(0,50,1))
ax4.set_yticks(np.arange(0.25,2,.25))
ax4.set_ylabel(r'$\widehat{f\sigma_8}_{\rm model}/\widehat{f\sigma_8}_{\rm mock}$',labelpad=10,fontsize=24)
ax4.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax4.set_xscale('log')
ax4.set_xlim(1,50)
ax4.set_ylim(0,2)
ax5.grid(True)
ax5.set_yticklabels([])
ax5.set_yticks(np.arange(0.25,2,.25))
ax5.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax5.set_xticks(np.arange(0,50,1))
ax5.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax5.set_xscale('log')
ax5.set_xlim(1,50)
ax5.set_ylim(0,2)
ax6.grid(True)
ax6.set_yticklabels([])
ax6.set_yticks(np.arange(0,2.25,.25))
ax6.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax6.set_xticks(np.arange(0,50,1))
ax6.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax6.set_xscale('log')
ax6.set_xlim(1,50)
ax6.set_ylim(0,2)

#first_legend=ax1.legend(handles=[line1,line2,line3], loc='lower left',fontsize=15)
#ax1.add_artist(first_legend)
ax1.legend(handles=[line1,line2], loc='upper left',fontsize=24)



plt.show()








#Fig.5 HW13 vs HOD's with ratios, cut
r=2
m=2
e=30
g=2
i=3

gs=plt.GridSpec(20, 30)
ax1=plt.subplot(gs[0:14,0:10])
ax2=plt.subplot(gs[0:14,10:20])
ax3=plt.subplot(gs[0:14,20:30])
ax4=plt.subplot(gs[14:20,0:10])
ax5=plt.subplot(gs[14:20,10:20])
ax6=plt.subplot(gs[14:20,20:30])
gs.update(wspace=0.025, hspace=0.05)


line4=ax1.errorbar(s2_center,estimator_ab19_2,yerr=None,lw=m,color='k',fmt='o-',label='HW13$_{cut<r_p=2}$')
ax1.fill_between(s2_center,(estimator_ab19_2+est_err19_2),(estimator_ab19_2-est_err19_2),color='k', alpha=b)
line5=ax1.errorbar(s2_center,estimator_1h19_2,lw=i,color='orange',ls='--',label='HOD$_{cut<r_p=2}$')
#line6=ax1.errorbar(s2_center,estimator_2h19_2,lw=i,color='r',ls='-.',label='HOD$ls-match_{cut<r_p=2}$')

ax2.errorbar(s2_center,estimator_ab20_2,yerr=None,lw=m,color='k',fmt='o-')
ax2.fill_between(s2_center,(estimator_ab20_2+est_err20_2),(estimator_ab20_2-est_err20_2),color='k', alpha=b)
ax2.errorbar(s2_center,estimator_1h20_2,lw=i,color='orange',ls='--')
#ax2.errorbar(s2_center,estimator_2h20_2,lw=i,color='r',ls='-.')

ax3.errorbar(s2_center,estimator_ab21_2,yerr=None,lw=m,color='k',fmt='o-')
ax3.fill_between(s2_center,(estimator_ab21_2+est_err21_2),(estimator_ab21_2-est_err21_2),color='k', alpha=b)
ax3.errorbar(s2_center,estimator_1h21_2,lw=i,color='orange',ls='--')
#ax3.errorbar(s2_center,estimator_2h21_2,lw=i,color='r',ls='-.')
ax4.fill_between(s2_center,(rat19_2_h1-rat19_2_hoderr),(rat19_2_h1+rat19_2_hoderr),color='orange', alpha=b)
ax5.fill_between(s2_center,(rat20_2_h1-rat20_2_hoderr),(rat20_2_h1+rat20_2_hoderr),color='orange', alpha=b)
ax6.fill_between(s2_center,(rat21_2_h1-rat21_2_hoderr),(rat21_2_h1+rat21_2_hoderr),color='orange', alpha=b)

ax4.errorbar(s2_center,rat19_2_h1,yerr=None,lw=i,color='orange',ls='--')
ax5.errorbar(s2_center,rat20_2_h1,yerr=None,lw=i,color='orange',ls='--')
ax6.errorbar(s2_center,rat21_2_h1,yerr=None,lw=i,color='orange',ls='--')
#ax4.errorbar(s2_center,rat19_2_h2,yerr=None,lw=i,color='r',ls='-.')
#ax5.errorbar(s2_center,rat20_2_h2,yerr=None,lw=i,color='r',ls='-.')
#ax6.errorbar(s2_center,rat21_2_h2,yerr=None,lw=i,color='r',ls='-.')

ax1.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--',label='Bolshoi $f\sigma_8$')
ax3.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.legend(loc='upper left',fontsize=24)

ones=np.zeros(len(s2_center))+1
ax4.errorbar(s2_center,ones,yerr=None,lw=r,color='k')
ax5.errorbar(s2_center,ones,yerr=None,lw=r,color='k')
ax6.errorbar(s2_center,ones,yerr=None,lw=r,color='k')
ax1.text(2.2,-0.07,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax2.text(2.2,-0.07,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax3.text(2.2,-0.07,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax1.set_ylabel(r'$\widehat{f\sigma_8}$',fontsize=24)
ax1.set_xscale('log')
ax1.set_xlim(2,50)
ax1.set_ylim(-.1,0.5)
ax1.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.set_yticks([0.0,0.2,0.4])
ax1.set_xticklabels([])

ax2.set_ylim(-.1,0.5)
ax2.set_xscale('log')
ax2.set_xlim(2,50)
ax2.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.set_yticklabels([])
ax2.set_xticklabels([])


ax3.set_ylim(-.1,.5)
ax3.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax3.set_xscale('log')
ax3.set_xlim(2,50)
ax3.set_yticklabels([])
ax3.set_xticklabels([])

ax4.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax4.set_yticks(np.arange(0.9,1.20,.1))
ax4.set_ylabel(r'$\widehat{f\sigma_8}_{\rm model}/\widehat{f\sigma_8}_{\rm mock}$',labelpad=10,fontsize=24)
ax4.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax4.set_xscale('log')
ax4.set_xlim(2,50)
ax4.set_ylim(.8,1.2)
ax5.grid(True)
ax5.set_yticks(np.arange(0.9,1.20,.1))
ax5.set_yticklabels([])
ax5.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax5.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax5.set_xscale('log')
ax5.set_xlim(2,50)
ax5.set_ylim(0.8,1.2)
ax6.grid(True)
ax6.set_yticks(np.arange(0.9,1.20,.1))
ax6.set_yticklabels([])
ax6.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax6.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax6.set_xscale('log')
ax6.set_xlim(2,50)
ax6.set_ylim(.8,1.2)

ax1.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax3.tick_params('both', length=5, width=1, which='minor')
ax4.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax4.tick_params('both', length=5, width=1, which='minor')
ax5.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax5.tick_params('both', length=5, width=1, which='minor')
ax6.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax6.tick_params('both', length=5, width=1, which='minor')


ax1.legend(handles=[line4,line5], loc='upper left',fontsize=24)

plt.show()





#HW13 vs SCAM with ratios
r=2
m=2
e=30
g=2
i=3

mask1_19=fs_center>5.4
mask2_19=fs_center>5.4
mask3_19=fs_center>5.4
mask4_19=fs_center>5.4
mask1_20=fs_center>5.3
mask2_20=fs_center>5.3
mask3_20=fs_center>5.3
mask4_20=fs_center>5.3
mask1_21=fs_center>6.5
mask2_21=fs_center>6.5
mask3_21=fs_center>6.5
mask4_21=fs_center>6.5


gs=plt.GridSpec(20, 30)
ax1=plt.subplot(gs[0:14,0:10])
ax2=plt.subplot(gs[0:14,10:20])
ax3=plt.subplot(gs[0:14,20:30])
ax4=plt.subplot(gs[14:20,0:10])
ax5=plt.subplot(gs[14:20,10:20])
ax6=plt.subplot(gs[14:20,20:30])
gs.update(wspace=0.025, hspace=0.05)

line1=ax1.errorbar(fs_center[mask1_19],estimator_fab19[mask1_19],yerr=None,lw=r,color='k',fmt='o-',label='HW13$_{full}$')
ax1.fill_between(fs_center[mask1_19],(estimator_fab19+est_err19)[mask1_19],(estimator_fab19-est_err19)[mask1_19],color='k', alpha=b)
line2=ax1.errorbar(fs_center[mask2_19],estimator_f3h19[mask2_19],yerr=None,lw=i,color='purple',ls=':',label='M$acc_{full}$')
line3=ax1.errorbar(fs_center[mask3_19],estimator_f4h19[mask3_19],yerr=None,lw=i,color='r',ls='-.',label='V$acc_{full}$')
line4=ax1.errorbar(fs_center[mask4_19],estimator_f5h19[mask4_19],yerr=None,lw=i,color='y',ls='--',label='V$peak_{full}$')
ax2.errorbar(fs_center[mask1_20],estimator_fab20[mask1_20],yerr=None,lw=r,color='k',fmt='o-')
ax2.fill_between(fs_center[mask1_20],(estimator_fab20+est_err20)[mask1_20],(estimator_fab20-est_err20)[mask1_20],color='k', alpha=b)
ax2.errorbar(fs_center[mask2_20],estimator_f3h20[mask2_20],yerr=None,lw=i,color='purple',ls=':')
ax2.errorbar(fs_center[mask3_20],estimator_f4h20[mask3_20],yerr=None,lw=i,color='r',ls='-.')
ax2.errorbar(fs_center[mask4_20],estimator_f5h20[mask4_20],yerr=None,lw=i,color='y',ls='--')
ax3.errorbar(fs_center[mask1_21],estimator_fab21[mask1_21],yerr=None,lw=r,color='k',fmt='o-')
ax3.fill_between(fs_center[mask1_21],(estimator_fab21+est_err21)[mask1_21],(estimator_fab21-est_err21)[mask1_21],color='k', alpha=b)
ax3.errorbar(fs_center[mask2_21],estimator_f3h21[mask2_21],yerr=None,lw=i,color='purple',ls=':')
ax3.errorbar(fs_center[mask3_21],estimator_f4h21[mask3_21],yerr=None,lw=i,color='r',ls='-.')
ax3.errorbar(fs_center[mask4_21],estimator_f5h21[mask4_21],yerr=None,lw=i,color='y',ls='--')
ax4.errorbar(fs_center[mask2_19],rat19f_h3[mask2_19],yerr=None,lw=i,color='purple',ls=':')
ax5.errorbar(fs_center[mask2_20],rat20f_h3[mask2_20],yerr=None,lw=i,color='purple',ls=':')
ax6.errorbar(fs_center[mask2_21],rat21f_h3[mask2_21],yerr=None,lw=i,color='purple',ls=':')
ax4.errorbar(fs_center[mask3_19],rat19f_h4[mask3_19],yerr=None,lw=i,color='r',ls='-.')
ax5.errorbar(fs_center[mask3_20],rat20f_h4[mask3_20],yerr=None,lw=i,color='r',ls='-.')
ax6.errorbar(fs_center[mask3_21],rat21f_h4[mask3_21],yerr=None,lw=i,color='r',ls='-.')
ax4.errorbar(fs_center[mask4_19],rat19f_h5[mask4_19],yerr=None,lw=i,color='y',ls='--')
ax5.errorbar(fs_center[mask4_20],rat20f_h5[mask4_20],yerr=None,lw=i,color='y',ls='--')
ax6.errorbar(fs_center[mask4_21],rat21f_h5[mask4_21],yerr=None,lw=i,color='y',ls='--')
first_legend=ax1.legend(handles=[line1,line2,line3,line4], loc='upper left',fontsize=24)
ax1.add_artist(first_legend)
ax1.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--',label='Bolshoi $f\sigma_8$')
ax3.plot((1,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.legend(loc='upper left',fontsize=24)
ones=np.zeros(len(fs_center))+1
rat_err19=est_err19/estimator_fab19
rat_err20=est_err20/estimator_fab20
rat_err21=est_err21/estimator_fab21
ax4.errorbar(fs_center[mask1_19],ones[mask1_19],yerr=None,lw=r,color='k')
ax4.fill_between(fs_center[mask1_19],(ones+rat_err19)[mask1_19],(ones-rat_err19)[mask1_19],color='k', alpha=b)
ax5.errorbar(fs_center[mask1_20],ones[mask1_20],yerr=None,lw=r,color='k')
ax5.fill_between(fs_center[mask1_20],(ones+rat_err20)[mask1_20],(ones-rat_err20)[mask1_20],color='k', alpha=b)
ax6.errorbar(fs_center[mask1_21],ones[mask1_21],yerr=None,lw=r,color='k')
ax6.fill_between(fs_center[mask1_21],(ones+rat_err21)[mask1_21],(ones-rat_err21)[mask1_21],color='k', alpha=b)
ax1.text(17,-0.07,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax2.text(1.2,-0.07,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax3.text(1.2,-0.07,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax1.set_ylabel(r'$\widehat{f\sigma_8}$',fontsize=24)
ax1.set_xscale('log')
ax1.set_xlim(1,50)
ax1.set_ylim(-.1,0.5)
ax1.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.set_xticklabels([])
ax1.set_yticks(np.arange(0,.5,.1))

ax2.set_ylim(-.1,0.5)
ax2.set_xscale('log')
ax2.set_xlim(1,50)
ax2.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.set_yticklabels([])
ax2.set_xticklabels([])
ax3.set_ylim(-.1,.5)
ax3.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax3.set_xscale('log')
ax3.set_xlim(1,50)
ax3.set_yticklabels([])
ax3.set_xticklabels([])

ax4.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax4.set_xticks(np.arange(0,50,1))
ax4.set_yticks(np.arange(0.7,1.3,.1))
ax4.set_ylabel(r'$\widehat{f\sigma_8}_{\rm model}/\widehat{f\sigma_8}_{\rm HW13}$',labelpad=10,fontsize=24)
ax4.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax4.set_xscale('log')
ax4.set_xlim(1,50)
ax4.set_ylim(0.7,1.3)
ax5.grid(True)
ax5.set_yticklabels([])
ax5.set_yticks(np.arange(0,2.25,.25))
ax5.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax5.set_xticks(np.arange(0,50,1))
ax5.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax5.set_xscale('log')
ax5.set_xlim(1,50)
ax5.set_ylim(0.7,1.3)
ax6.grid(True)
ax6.set_yticklabels([])
ax6.set_yticks(np.arange(0,2.25,.25))
ax6.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax6.set_xticks(np.arange(0,50,1))
ax6.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax6.set_xscale('log')
ax6.set_xlim(1,50)
ax6.set_ylim(0.7,1.3)

plt.show()


#HW13 vs Shuffle models cut/centrals with ratios
r=2
m=2
e=30
g=2
i=3

gs=plt.GridSpec(20, 30)
ax1=plt.subplot(gs[0:14,0:10])
ax2=plt.subplot(gs[0:14,10:20])
ax3=plt.subplot(gs[0:14,20:30])
ax4=plt.subplot(gs[14:20,0:10])
ax5=plt.subplot(gs[14:20,10:20])
ax6=plt.subplot(gs[14:20,20:30])
gs.update(wspace=0.025, hspace=0.05)


line5=ax1.errorbar(s2_center,estimator_ab19_2,yerr=None,lw=m,color='k',fmt='o-',label='HW13$_{cut<r_p=2}$')
ax1.fill_between(s2_center,(estimator_ab19_2+est_err19_2),(estimator_ab19_2-est_err19_2),color='k', alpha=b)
line6=ax1.errorbar(s2_center,estimator_nab19_2,lw=i,color='k',fmt='o--',label='Shuffled$_{cut<r_p=2}$')
line7=ax1.errorbar(s2_center,cestimator_ab19_2,lw=i,color='b',ls='-',label='HW13$_{cut<r_p=2,cent}$')
ax1.fill_between(s2_center,(cestimator_ab19_2+cest_err19_2),(cestimator_ab19_2-cest_err19_2),color='b', alpha=b)
line8=ax1.errorbar(s2_center,cestimator_nab19_2,lw=i,color='b',ls='--',label='Shuffled$_{cut<r_p=2,cent}$')

ax2.errorbar(s2_center,estimator_ab20_2,yerr=None,lw=m,color='k',fmt='o-')
ax2.fill_between(s2_center,(estimator_ab20_2+est_err20_2),(estimator_ab20_2-est_err20_2),color='k', alpha=b)
ax2.errorbar(s2_center,estimator_nab20_2,lw=i,color='k',fmt='o--')
ax2.errorbar(s2_center,cestimator_ab20_2,lw=i,color='b',ls='-')
ax2.fill_between(s2_center,(cestimator_ab20_2+cest_err20_2),(cestimator_ab20_2-cest_err20_2),color='b', alpha=b)
ax2.errorbar(s2_center,cestimator_nab20_2,lw=i,color='b',ls='--')

ax3.errorbar(s2_center,estimator_ab21_2,yerr=None,lw=m,color='k',fmt='o-')
ax3.fill_between(s2_center,(estimator_ab21_2+est_err21_2),(estimator_ab21_2-est_err21_2),color='k', alpha=b)
ax3.errorbar(s2_center,estimator_nab21_2,lw=i,color='k',fmt='o--')
ax3.errorbar(s2_center,cestimator_ab21_2,lw=i,color='b',ls='-')
ax3.fill_between(s2_center,(cestimator_ab21_2+cest_err21_2),(cestimator_ab21_2-cest_err21_2),color='b', alpha=b)
ax3.errorbar(s2_center,cestimator_nab21_2,lw=i,color='b',ls='--')

ax4.fill_between(s2_center,(crat19_2_nab-crat19_2_eerr),(crat19_2_nab+crat19_2_eerr),color='b', alpha=b)
ax5.fill_between(s2_center,(crat20_2_nab-crat20_2_eerr),(crat20_2_nab+crat20_2_eerr),color='b', alpha=b)
ax6.fill_between(s2_center,(crat21_2_nab-crat21_2_eerr),(crat21_2_nab+crat21_2_eerr),color='b', alpha=b)

ax4.errorbar(s2_center,crat19_2_nab,yerr=None,lw=i,color='b',ls='--')
ax5.errorbar(s2_center,crat20_2_nab,yerr=None,lw=i,color='b',ls='--')
ax6.errorbar(s2_center,crat21_2_nab,yerr=None,lw=i,color='b',ls='--')

ax4.errorbar(s2_center,rat19_2_nab,yerr=None,lw=i,color='k',ls='--')
ax5.errorbar(s2_center,rat20_2_nab,yerr=None,lw=i,color='k',ls='--')
ax6.errorbar(s2_center,rat21_2_nab,yerr=None,lw=i,color='k',ls='--')

ax1.legend(handles=[line5,line6,line7,line8], loc='upper left',fontsize=24)

ax1.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--',label='Bolshoi $f\sigma_8$')
ax3.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.legend(loc='upper left',fontsize=24)

ones=np.zeros(len(s2_center))+1
ax4.errorbar(s2_center,ones,yerr=None,lw=r,color='k')
ax5.errorbar(s2_center,ones,yerr=None,lw=r,color='k')
ax6.errorbar(s2_center,ones,yerr=None,lw=r,color='k')



ax1.text(2.2,-0.07,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax2.text(2.2,-0.07,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax3.text(2.2,-0.07,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax1.set_ylabel(r'$\widehat{f\sigma_8}$',fontsize=24)
ax1.set_xscale('log')
ax1.set_xlim(2,50)
ax1.set_ylim(-.1,0.5)
ax1.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.set_xticklabels([])
ax1.set_yticks([0.0,0.2,0.4])

ax2.set_ylim(-.1,0.5)
ax2.set_xscale('log')
ax2.set_xlim(2,50)
ax2.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.set_yticklabels([])
ax2.set_xticklabels([])

ax3.set_ylim(-.1,.5)
ax3.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax3.set_xscale('log')
ax3.set_xlim(2,50)
ax3.set_yticklabels([])
ax3.set_xticklabels([])

ax4.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax4.set_yticks(np.arange(0.9,1.2,.1))
ax4.set_ylabel(r'$\widehat{f\sigma_8}_{\rm Shuffled}/\widehat{f\sigma_8}_{\rm HW13}$',labelpad=10,fontsize=24)
ax4.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax4.set_xscale('log')
ax4.set_xlim(2,50)
ax4.set_ylim(0.8,1.2)
ax5.grid(True)
ax5.set_yticks(np.arange(0.9,1.2,.1))
ax5.set_yticklabels([])
ax5.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax5.set_xticks(np.arange(0,50,1))
ax5.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax5.set_xscale('log')
ax5.set_xlim(2,50)
ax5.set_ylim(0.8,1.2)
ax6.grid(True)
ax6.set_yticks(np.arange(0.9,1.2,.1))
ax6.set_yticklabels([])
ax6.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax6.set_xticks(np.arange(0,50,1))
ax6.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax6.set_xscale('log')
ax6.set_xlim(2,50)
ax6.set_ylim(0.8,1.2)
ax1.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax3.tick_params('both', length=5, width=1, which='minor')
ax4.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax4.tick_params('both', length=5, width=1, which='minor')
ax5.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax5.tick_params('both', length=5, width=1, which='minor')
ax6.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax6.tick_params('both', length=5, width=1, which='minor')


plt.show()









#HW13 vs Shuffle models full/centrals with ratios
r=2
m=2
e=30
g=2
i=3

gs=plt.GridSpec(20, 30)
ax1=plt.subplot(gs[0:14,0:10])
ax2=plt.subplot(gs[0:14,10:20])
ax3=plt.subplot(gs[0:14,20:30])
ax4=plt.subplot(gs[14:20,0:10])
ax5=plt.subplot(gs[14:20,10:20])
ax6=plt.subplot(gs[14:20,20:30])
gs.update(wspace=0.025, hspace=0.05)


mask1_19=fs_center>2.5
mask2_19=fs_center>2.5
mask3_19=fs_center>2.5
mask4_19=fs_center>2.5
mask1_20=fs_center>2.5
mask2_20=fs_center>2.5
mask3_20=fs_center>2.5
mask4_20=fs_center>2.5
mask1_21=fs_center>2.5
mask2_21=fs_center>2.5
mask3_21=fs_center>2.5
mask4_21=fs_center>2.5


line5=ax1.errorbar(fs_center[mask1_19],estimator_fab19[mask1_19],yerr=None,lw=m,color='k',fmt='o-',label='HW13$_{full}$')
ax1.fill_between(fs_center[mask1_19],(estimator_fab19+est_err19)[mask1_19],(estimator_fab19-est_err19)[mask1_19],color='k', alpha=b)
line6=ax1.errorbar(fs_center[mask1_19],estimator_fnab19[mask1_19],lw=i,color='k',fmt='o--',label='Shuffled$_{full}$')
line7=ax1.errorbar(fs_center[mask1_19],cestimator_fab19[mask1_19],lw=i,color='b',ls='-',label='HW13$_{full,cent}$')
ax1.fill_between(fs_center[mask1_19],(cestimator_fab19+cest_err19)[mask1_19],(cestimator_fab19-cest_err19)[mask1_19],color='b', alpha=b)
line8=ax1.errorbar(fs_center[mask1_19],cestimator_fnab19[mask1_19],lw=i,color='b',ls='--',label='Shuffled$_{full,cent}$')

ax2.errorbar(fs_center[mask1_19],estimator_fab20[mask1_19],yerr=None,lw=m,color='k',fmt='o-')
ax2.fill_between(fs_center[mask1_19],(estimator_fab20+est_err20)[mask1_19],(estimator_fab20-est_err20)[mask1_19],color='k', alpha=b)
ax2.errorbar(fs_center[mask1_19],estimator_fnab20[mask1_19],lw=i,color='k',fmt='o--')
ax2.errorbar(fs_center[mask1_19],cestimator_fab20[mask1_19],lw=i,color='b',ls='-')
ax2.fill_between(fs_center[mask1_19],(cestimator_fab20+cest_err20)[mask1_19],(cestimator_fab20-cest_err20)[mask1_19],color='b', alpha=b)
ax2.errorbar(fs_center[mask1_19],cestimator_fnab20[mask1_19],lw=i,color='b',ls='--')

ax3.errorbar(fs_center[mask1_19],estimator_fab21[mask1_19],yerr=None,lw=m,color='k',fmt='o-')
ax3.fill_between(fs_center[mask1_19],(estimator_fab21+est_err21)[mask1_19],(estimator_fab21-est_err21)[mask1_19],color='k', alpha=b)
ax3.errorbar(fs_center[mask1_19],estimator_fnab21[mask1_19],lw=i,color='k',fmt='o--')
ax3.errorbar(fs_center[mask1_19],cestimator_fab21[mask1_19],lw=i,color='b',ls='-')
ax3.fill_between(fs_center[mask1_19],(cestimator_fab21+cest_err21)[mask1_19],(cestimator_fab21-cest_err21)[mask1_19],color='b', alpha=b)
ax3.errorbar(fs_center[mask1_19],cestimator_fnab21[mask1_19],lw=i,color='b',ls='--')

ax4.fill_between(fs_center[mask1_19],(crat19_fnab-crat19_eerr)[mask1_19],(crat19_fnab+crat19_eerr)[mask1_19],color='b', alpha=b)
ax5.fill_between(fs_center[mask1_19],(crat20_fnab-crat20_eerr)[mask1_19],(crat20_fnab+crat20_eerr)[mask1_19],color='b', alpha=b)
ax6.fill_between(fs_center[mask1_19],(crat21_fnab-crat21_eerr)[mask1_19],(crat21_fnab+crat21_eerr)[mask1_19],color='b', alpha=b)

ax4.errorbar(fs_center[mask1_19],crat19_fnab[mask1_19],yerr=None,lw=i,color='b',ls='--')
ax5.errorbar(fs_center[mask1_19],crat20_fnab[mask1_19],yerr=None,lw=i,color='b',ls='--')
ax6.errorbar(fs_center[mask1_19],crat21_fnab[mask1_19],yerr=None,lw=i,color='b',ls='--')


ax4.errorbar(fs_center[mask1_19],rat19_fnab[mask1_19],yerr=None,lw=i,color='k',ls='--')
ax5.errorbar(fs_center[mask1_19],rat20_fnab[mask1_19],yerr=None,lw=i,color='k',ls='--')
ax6.errorbar(fs_center[mask1_19],rat21_fnab[mask1_19],yerr=None,lw=i,color='k',ls='--')


ax1.legend(handles=[line5,line6,line7,line8], loc='upper left',fontsize=24)


ax1.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--',label='Bolshoi $f\sigma_8$')
ax3.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.legend(loc='upper left',fontsize=24)

ones=np.zeros(len(fs_center))+1
ax4.errorbar(fs_center[mask1_19],ones[mask1_19],yerr=None,lw=r,color='k')
ax5.errorbar(fs_center[mask1_19],ones[mask1_19],yerr=None,lw=r,color='k')
ax6.errorbar(fs_center[mask1_19],ones[mask1_19],yerr=None,lw=r,color='k')

ax1.text(2.2,-0.07,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax2.text(2.2,-0.07,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax3.text(2.2,-0.07,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax1.set_ylabel(r'$\widehat{f\sigma_8}$',fontsize=24)
ax1.set_xscale('log')
ax1.set_xlim(2,50)
ax1.set_ylim(-.1,0.5)
ax1.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.set_xticklabels([])
ax1.set_yticks([0.0,0.2,0.4])

ax2.set_ylim(-.1,0.5)
ax2.set_xscale('log')
ax2.set_xlim(2,50)
ax2.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.set_yticklabels([])
ax2.set_xticklabels([])

ax3.set_ylim(-.1,.5)
ax3.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax3.set_xscale('log')
ax3.set_xlim(2,50)
ax3.set_yticklabels([])
ax3.set_xticklabels([])

ax4.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax4.set_yticks(np.arange(0.9,1.2,.1))
ax4.set_ylabel(r'$\widehat{f\sigma_8}_{\rm Shuffled}/\widehat{f\sigma_8}_{\rm HW13}$',labelpad=10,fontsize=24)
ax4.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax4.set_xscale('log')
ax4.set_xlim(2,50)
ax4.set_ylim(0.8,1.2)
ax5.grid(True)
ax5.set_yticks(np.arange(0.9,1.2,.1))
ax5.set_yticklabels([])
ax5.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax5.set_xticks(np.arange(0,50,1))
ax5.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax5.set_xscale('log')
ax5.set_xlim(2,50)
ax5.set_ylim(0.8,1.2)
ax6.grid(True)
ax6.set_yticks(np.arange(0.9,1.2,.1))
ax6.set_yticklabels([])
ax6.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax6.set_xticks(np.arange(0,50,1))
ax6.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax6.set_xscale('log')
ax6.set_xlim(2,50)
ax6.set_ylim(0.8,1.2)
ax1.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax3.tick_params('both', length=5, width=1, which='minor')
ax4.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax4.tick_params('both', length=5, width=1, which='minor')
ax5.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax5.tick_params('both', length=5, width=1, which='minor')
ax6.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax6.tick_params('both', length=5, width=1, which='minor')


plt.show()



   
#HW13 vs SCAM models cut with ratios
r=2
m=2
e=30
g=2
i=3

gs=plt.GridSpec(20, 30)
ax1=plt.subplot(gs[0:14,0:10])
ax2=plt.subplot(gs[0:14,10:20])
ax3=plt.subplot(gs[0:14,20:30])
ax4=plt.subplot(gs[14:20,0:10])
ax5=plt.subplot(gs[14:20,10:20])
ax6=plt.subplot(gs[14:20,20:30])
gs.update(wspace=0.025, hspace=0.05)

line5=ax1.errorbar(s2_center,estimator_ab19_2,yerr=None,lw=m,color='k',fmt='o-',label='HW13$_{cut<r_p=2}$')
ax1.fill_between(s2_center,(estimator_ab19_2+est_err19_2),(estimator_ab19_2-est_err19_2),color='k', alpha=b)
line6=ax1.errorbar(s2_center,estimator_3h19_2,lw=i,color='purple',ls=':',label='M$acc_{cut<r_p=2}$')
line7=ax1.errorbar(s2_center,estimator_4h19_2,lw=i,color='r',ls='-.',label='V$acc_{cut<r_p=2}$')
line8=ax1.errorbar(s2_center,estimator_5h19_2,lw=i,color='y',ls='--',label='V$peak_{cut<r_p=2}$')
ax2.errorbar(s2_center,estimator_ab20_2,yerr=None,lw=m,color='k',fmt='o-')
ax2.fill_between(s2_center,(estimator_ab20_2+est_err20_2),(estimator_ab20_2-est_err20_2),color='k', alpha=b)
ax2.errorbar(s2_center,estimator_3h20_2,lw=i,color='purple',ls=':')
ax2.errorbar(s2_center,estimator_4h20_2,lw=i,color='r',ls='-.')
ax2.errorbar(s2_center,estimator_5h20_2,lw=i,color='y',ls='--')
ax3.errorbar(s2_center,estimator_ab21_2,yerr=None,lw=m,color='k',fmt='o-')
ax3.fill_between(s2_center,(estimator_ab21_2+est_err21_2),(estimator_ab21_2-est_err21_2),color='k', alpha=b)
ax3.errorbar(s2_center,estimator_3h21_2,lw=i,color='purple',ls=':')
ax3.errorbar(s2_center,estimator_4h21_2,lw=i,color='r',ls='-.')
ax3.errorbar(s2_center,estimator_5h21_2,lw=i,color='y',ls='--')
ax4.fill_between(s2_center,(rat19_2_h5-rat19_2_vpeakerr),(rat19_2_h5+rat19_2_vpeakerr),color='y', alpha=b)
ax5.fill_between(s2_center,(rat20_2_h5-rat20_2_vpeakerr),(rat20_2_h5+rat20_2_vpeakerr),color='y', alpha=b)
ax6.fill_between(s2_center,(rat21_2_h5-rat21_2_vpeakerr),(rat21_2_h5+rat21_2_vpeakerr),color='y', alpha=b)


ax4.errorbar(s2_center,rat19_2_h3,yerr=None,lw=i,color='purple',ls=':')
ax5.errorbar(s2_center,rat20_2_h3,yerr=None,lw=i,color='purple',ls=':')
ax6.errorbar(s2_center,rat21_2_h3,yerr=None,lw=i,color='purple',ls=':')
ax4.errorbar(s2_center,rat19_2_h4,yerr=None,lw=i,color='r',ls='-.')
ax5.errorbar(s2_center,rat20_2_h4,yerr=None,lw=i,color='r',ls='-.')
ax6.errorbar(s2_center,rat21_2_h4,yerr=None,lw=i,color='r',ls='-.')
ax4.errorbar(s2_center,rat19_2_h5,yerr=None,lw=i,color='y',ls='--')
ax5.errorbar(s2_center,rat20_2_h5,yerr=None,lw=i,color='y',ls='--')
ax6.errorbar(s2_center,rat21_2_h5,yerr=None,lw=i,color='y',ls='--')
ax1.legend(handles=[line5,line6,line7,line8], loc='upper left',fontsize=24)


ax1.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--',label='Bolshoi $f\sigma_8$')
ax3.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.legend(loc='upper left',fontsize=24)

ones=np.zeros(len(s2_center))+1
ax4.errorbar(s2_center,ones,yerr=None,lw=r,color='k')
ax5.errorbar(s2_center,ones,yerr=None,lw=r,color='k')
ax6.errorbar(s2_center,ones,yerr=None,lw=r,color='k')

ax1.text(2.2,-0.07,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax2.text(2.2,-0.07,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax3.text(2.2,-0.07,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax1.set_ylabel(r'$\widehat{f\sigma_8}$',fontsize=24)
ax1.set_xscale('log')
ax1.set_xlim(2,50)
ax1.set_ylim(-.1,0.5)
ax1.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.set_xticklabels([])
ax1.set_yticks([0.0,0.2,0.4])

ax2.set_ylim(-.1,0.5)
ax2.set_xscale('log')
ax2.set_xlim(2,50)
ax2.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.set_yticklabels([])
ax2.set_xticklabels([])

ax3.set_ylim(-.1,.5)
ax3.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax3.set_xscale('log')
ax3.set_xlim(2,50)
ax3.set_yticklabels([])
ax3.set_xticklabels([])

ax4.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax4.set_yticks(np.arange(0.9,1.2,.1))
ax4.set_ylabel(r'$\widehat{f\sigma_8}_{\rm model}/\widehat{f\sigma_8}_{\rm HW13}$',labelpad=10,fontsize=24)
ax4.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax4.set_xscale('log')
ax4.set_xlim(2,50)
ax4.set_ylim(0.8,1.2)
ax5.grid(True)
ax5.set_yticks(np.arange(0.9,1.2,.1))
ax5.set_yticklabels([])
ax5.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax5.set_xticks(np.arange(0,50,1))
ax5.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax5.set_xscale('log')
ax5.set_xlim(2,50)
ax5.set_ylim(0.8,1.2)
ax6.grid(True)
ax6.set_yticks(np.arange(0.9,1.2,.1))
ax6.set_yticklabels([])
ax6.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax6.set_xticks(np.arange(0,50,1))
ax6.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax6.set_xscale('log')
ax6.set_xlim(2,50)
ax6.set_ylim(0.8,1.2)
ax1.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax3.tick_params('both', length=5, width=1, which='minor')
ax4.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax4.tick_params('both', length=5, width=1, which='minor')
ax5.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax5.tick_params('both', length=5, width=1, which='minor')
ax6.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax6.tick_params('both', length=5, width=1, which='minor')


plt.show()


   
#HW13 vs models cut central only ratio
r=2
m=2
e=30
g=2
i=3

gs=plt.GridSpec(20, 30)
ax1=plt.subplot(gs[0:14,0:10])
ax2=plt.subplot(gs[0:14,10:20])
ax3=plt.subplot(gs[0:14,20:30])
ax4=plt.subplot(gs[14:20,0:10])
ax5=plt.subplot(gs[14:20,10:20])
ax6=plt.subplot(gs[14:20,20:30])
gs.update(wspace=0.025, hspace=0.05)

line5=ax1.errorbar(s2_center,cestimator_ab19_2,yerr=None,lw=m,color='b',fmt='o-',label='HW13$_{cut<r_p=2,cent}$')
ax1.fill_between(s2_center,(cestimator_ab19_2+cest_err19_2),(cestimator_ab19_2-cest_err19_2),color='b', alpha=b)
line6=ax1.errorbar(s2_center,cestimator_nab19_2,lw=i,color='b',fmt='o--',label='Shuffled$_{cut<r_p=2,cent}$')
line7=ax1.errorbar(s2_center,cestimator_1h19_2,lw=i,color='k',ls='-',label='HOD$_{cut<r_p=2,cent}$')
line8=ax1.errorbar(s2_center,cestimator_3h19_2,lw=i,color='purple',ls=':',label='M$acc_{cut<r_p=2,cent}$')
line9=ax1.errorbar(s2_center,cestimator_4h19_2,lw=i,color='r',ls='-.',label='V$acc_{cut<r_p=2,cent}$')
line10=ax1.errorbar(s2_center,cestimator_5h19_2,lw=i,color='y',ls='--',label='V$peak_{cut<r_p=2,cent}$')
ax2.errorbar(s2_center,cestimator_ab20_2,yerr=None,lw=m,color='b',fmt='o-')
ax2.fill_between(s2_center,(cestimator_ab20_2+cest_err20_2),(cestimator_ab20_2-cest_err20_2),color='b', alpha=b)
ax2.errorbar(s2_center,cestimator_nab20_2,lw=i,color='b',fmt='o--')
ax2.errorbar(s2_center,cestimator_1h20_2,lw=i,color='k',ls='-')
ax2.errorbar(s2_center,cestimator_3h20_2,lw=i,color='purple',ls=':')
ax2.errorbar(s2_center,cestimator_4h20_2,lw=i,color='r',ls='-.')
ax2.errorbar(s2_center,cestimator_5h20_2,lw=i,color='y',ls='--')
ax3.errorbar(s2_center,cestimator_ab21_2,yerr=None,lw=m,color='b',fmt='o-')
ax3.fill_between(s2_center,(cestimator_ab21_2+cest_err21_2),(cestimator_ab21_2-cest_err21_2),color='b', alpha=b)
ax3.errorbar(s2_center,cestimator_nab21_2,lw=i,color='b',fmt='o--')
ax3.errorbar(s2_center,cestimator_1h21_2,lw=i,color='k',ls='-')
ax3.errorbar(s2_center,cestimator_3h21_2,lw=i,color='purple',ls=':')
ax3.errorbar(s2_center,cestimator_4h21_2,lw=i,color='r',ls='-.')
ax3.errorbar(s2_center,cestimator_5h21_2,lw=i,color='y',ls='--')

#ax4.fill_between(s2_center,(crat19_2_nab-crat19_2_eerr),(crat19_2_nab+crat19_2_eerr),color='b', alpha=b)
#ax5.fill_between(s2_center,(crat20_2_nab-crat20_2_eerr),(crat20_2_nab+crat20_2_eerr),color='b', alpha=b)
#ax6.fill_between(s2_center,(crat21_2_nab-crat21_2_eerr),(crat21_2_nab+crat21_2_eerr),color='b', alpha=b)
#ax4.fill_between(s2_center,(crat19_2_h1-crat19_2_hoderr),(crat19_2_h1+crat19_2_hoderr),color='k', alpha=b)
#ax5.fill_between(s2_center,(crat20_2_h1-crat20_2_hoderr),(crat20_2_h1+crat20_2_hoderr),color='k', alpha=b)
#ax6.fill_between(s2_center,(crat21_2_h1-crat21_2_hoderr),(crat21_2_h1+crat21_2_hoderr),color='k', alpha=b)
#ax4.fill_between(s2_center,(crat19_2_h3-crat19_2_maccerr),(crat19_2_h3+crat19_2_maccerr),color='purple', alpha=b)
#ax5.fill_between(s2_center,(crat20_2_h3-crat20_2_maccerr),(crat20_2_h3+crat20_2_maccerr),color='purple', alpha=b)
#ax6.fill_between(s2_center,(crat21_2_h3-crat21_2_maccerr),(crat21_2_h3+crat21_2_maccerr),color='purple', alpha=b)
#ax4.fill_between(s2_center,(crat19_2_h4-crat19_2_vaccerr),(crat19_2_h4+crat19_2_vaccerr),color='r', alpha=b)
#ax5.fill_between(s2_center,(crat20_2_h4-crat20_2_vaccerr),(crat20_2_h4+crat20_2_vaccerr),color='r', alpha=b)
#ax6.fill_between(s2_center,(crat21_2_h4-crat21_2_vaccerr),(crat21_2_h4+crat21_2_vaccerr),color='r', alpha=b)
ax4.fill_between(s2_center,(crat19_2_h5-crat19_2_vpeakerr),(crat19_2_h5+crat19_2_vpeakerr),color='y', alpha=b)
ax5.fill_between(s2_center,(crat20_2_h5-crat20_2_vpeakerr),(crat20_2_h5+crat20_2_vpeakerr),color='y', alpha=b)
ax6.fill_between(s2_center,(crat21_2_h5-crat21_2_vpeakerr),(crat21_2_h5+crat21_2_vpeakerr),color='y', alpha=b)



ax4.errorbar(s2_center,crat19_2_nab,yerr=None,lw=i,color='b',fmt='o--')
ax5.errorbar(s2_center,crat20_2_nab,yerr=None,lw=i,color='b',fmt='o--')
ax6.errorbar(s2_center,crat21_2_nab,yerr=None,lw=i,color='b',fmt='o--')
ax4.errorbar(s2_center,crat19_2_h1,yerr=None,lw=i,color='k',ls='-')
ax5.errorbar(s2_center,crat20_2_h1,yerr=None,lw=i,color='k',ls='-')
ax6.errorbar(s2_center,crat21_2_h1,yerr=None,lw=i,color='k',ls='-')
ax4.errorbar(s2_center,crat19_2_h3,yerr=None,lw=i,color='purple',ls=':')
ax5.errorbar(s2_center,crat20_2_h3,yerr=None,lw=i,color='purple',ls=':')
ax6.errorbar(s2_center,crat21_2_h3,yerr=None,lw=i,color='purple',ls=':')
ax4.errorbar(s2_center,crat19_2_h4,yerr=None,lw=i,color='r',ls='-.')
ax5.errorbar(s2_center,crat20_2_h4,yerr=None,lw=i,color='r',ls='-.')
ax6.errorbar(s2_center,crat21_2_h4,yerr=None,lw=i,color='r',ls='-.')
ax4.errorbar(s2_center,crat19_2_h5,yerr=None,lw=i,color='y',ls='--')
ax5.errorbar(s2_center,crat20_2_h5,yerr=None,lw=i,color='y',ls='--')
ax6.errorbar(s2_center,crat21_2_h5,yerr=None,lw=i,color='y',ls='--')
ax1.legend(handles=[line5,line6,line7,line8,line9,line10], loc='upper left',fontsize=20)


ax1.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--',label='Bolshoi $f\sigma_8$')
ax3.plot((2,50),(0.396180,0.396180),lw=4,color='k',ls='--')
ax2.legend(loc='upper left',fontsize=24)

ones=np.zeros(len(s2_center))+1
ax4.errorbar(s2_center,ones,yerr=None,lw=r,color='b')
ax5.errorbar(s2_center,ones,yerr=None,lw=r,color='b')
ax6.errorbar(s2_center,ones,yerr=None,lw=r,color='b')

ax1.text(2.2,-0.07,'M$_r$ < -19', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax2.text(2.2,-0.07,'M$_r$ < -20', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax3.text(2.2,-0.07,'M$_r$ < -21', bbox=dict(facecolor='w', edgecolor='k'),fontsize=24)
ax1.set_ylabel(r'$\widehat{f\sigma_8}$',fontsize=24)
ax1.set_xscale('log')
ax1.set_xlim(2,50)
ax1.set_ylim(-.1,0.5)
ax1.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax1.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax1.set_xticklabels([])
ax1.set_yticks([0.0,0.2,0.4])

ax2.set_ylim(-.1,0.5)
ax2.set_xscale('log')
ax2.set_xlim(2,50)
ax2.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax2.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax2.set_yticklabels([])
ax2.set_xticklabels([])

ax3.set_ylim(-.1,.5)
ax3.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax3.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax3.set_xscale('log')
ax3.set_xlim(2,50)
ax3.set_yticklabels([])
ax3.set_xticklabels([])

ax4.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax4.set_yticks(np.arange(0.9,1.2,.1))
ax4.set_ylabel(r'$\widehat{f\sigma_8}_{\rm model}/\widehat{f\sigma_8}_{\rm HW13}$',labelpad=10,fontsize=24)
ax4.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax4.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax4.set_xscale('log')
ax4.set_xlim(2,50)
ax4.set_ylim(0.8,1.2)
ax5.grid(True)
ax5.set_yticks(np.arange(0.9,1.2,.1))
ax5.set_yticklabels([])
ax5.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax5.set_xticks(np.arange(0,50,1))
ax5.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax5.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax5.set_xscale('log')
ax5.set_xlim(2,50)
ax5.set_ylim(0.8,1.2)
ax6.grid(True)
ax6.set_yticks(np.arange(0.9,1.2,.1))
ax6.set_yticklabels([])
ax6.set_xlabel('s [h$^{-1}$Mpc]', fontsize=24)
ax6.set_xticks(np.arange(0,50,1))
ax6.grid(b=True, which='minor',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='x',color='b',alpha=0.5,linestyle='--')
ax6.grid(b=True, which='major',axis='y',color='b',alpha=0.5,linestyle='--')
ax6.set_xscale('log')
ax6.set_xlim(2,50)
ax6.set_ylim(0.8,1.2)
ax1.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax1.tick_params('both', length=5, width=1, which='minor')
ax2.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax2.tick_params('both', length=5, width=1, which='minor')
ax3.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax3.tick_params('both', length=5, width=1, which='minor')
ax4.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax4.tick_params('both', length=5, width=1, which='minor')
ax5.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax5.tick_params('both', length=5, width=1, which='minor')
ax6.tick_params('both', length=10, width=1, which='major',labelsize=24)
ax6.tick_params('both', length=5, width=1, which='minor')


plt.show()


