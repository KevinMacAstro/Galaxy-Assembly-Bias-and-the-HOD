# Calculates fsig_8(s) from a correlation-space version of an estimator developed by Percival & White 2009

import numpy as np
import matplotlib.pyplot as plt 

pi=3.14159265359

fs_center,wp,fabxi19_l0,fabxi19_l2,fabxi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,fnabxi19_l0,fnabxi19_l2,fnabxi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,abxi19_l0,abxi19_l2,abxi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,nabxi19_l0,nabxi19_l2,nabxi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,fh1xi19_l0,fh1xi19_l2,fh1xi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,h1xi19_l0,h1xi19_l2,h1xi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,fh2xi19_l0,fh2xi19_l2,fh2xi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,h2xi19_l0,h2xi19_l2,h2xi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,fh3xi19_l0,fh3xi19_l2,fh3xi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,h3xi19_l0,h3xi19_l2,h3xi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,fh4xi19_l0,fh4xi19_l2,fh4xi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,h4xi19_l0,h4xi19_l2,h4xi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,fh5xi19_l0,fh5xi19_l2,fh5xi19_l4=np.loadtxt('',unpack=True)
fs_center,wp,h5xi19_l0,h5xi19_l2,h5xi19_l4=np.loadtxt('',unpack=True)

r_outer,r_ave,r_center,mmxi,mmerror_xi,mmavgxi,mmerror_avgxi,mmavgavgxi,mmerror_avgavgxi,mmNpair,mmNpspair,mmavgpair,mmavgrand,mmavgavgpair,mmavgavgrand=np.loadtxt('dmxi3d_log_L.dat', unpack=True)

sigma8=.82
sigma8_sq=sigma8**2

mmxi=mmxi/sigma8_sq
mmavgxi=mmavgxi/sigma8_sq
mmavgavgxi=mmavgavgxi/sigma8_sq

s=len(mmxi)-len(abxi19_2l0)
mmxi2=mmxi[s:]
mmavgxi2=mmavgxi[s:]
mmavgavgxi2=mmavgavgxi[s:]

fabxi19prime_l0=fabxi19_l0/mmxi
fnabxi19prime_l0=fnabxi19_l0/mmxi
fabxi20prime_l0=fabxi20_l0/mmxi
fnabxi20prime_l0=fnabxi20_l0/mmxi
fabxi21prime_l0=fabxi21_l0/mmxi
fnabxi21prime_l0=fnabxi21_l0/mmxi

fabxi19prime_l2=fabxi19_l2/(mmxi-mmavgxi)
fnabxi19prime_l2=fnabxi19_l2/(mmxi-mmavgxi)
fabxi20prime_l2=fabxi20_l2/(mmxi-mmavgxi)
fnabxi20prime_l2=fnabxi20_l2/(mmxi-mmavgxi)
fabxi21prime_l2=fabxi21_l2/(mmxi-mmavgxi)
fnabxi21prime_l2=fnabxi21_l2/(mmxi-mmavgxi)

abxi19prime_2l0=abxi19_2l0/mmxi2
nabxi19prime_2l0=nabxi19_2l0/mmxi2
abxi20prime_2l0=abxi20_2l0/mmxi2
nabxi20prime_2l0=nabxi20_2l0/mmxi2
abxi21prime_2l0=abxi21_2l0/mmxi2
nabxi21prime_2l0=nabxi21_2l0/mmxi2

abxi19prime_2l2=abxi19_2l2/(mmxi2-mmavgxi2)
nabxi19prime_2l2=nabxi19_2l2/(mmxi2-mmavgxi2)
abxi20prime_2l2=abxi20_2l2/(mmxi2-mmavgxi2)
nabxi20prime_2l2=nabxi20_2l2/(mmxi2-mmavgxi2)
abxi21prime_2l2=abxi21_2l2/(mmxi2-mmavgxi2)
nabxi21prime_2l2=nabxi21_2l2/(mmxi2-mmavgxi2)

fh1xi19prime_l0=fh1xi19_l0/mmxi
fh1xi20prime_l0=fh1xi20_l0/mmxi
fh1xi21prime_l0=fh1xi21_l0/mmxi

fh1xi19prime_l2=fh1xi19_l2/(mmxi-mmavgxi)
fh1xi20prime_l2=fh1xi20_l2/(mmxi-mmavgxi)
fh1xi21prime_l2=fh1xi21_l2/(mmxi-mmavgxi)


h1xi19prime_2l0=h1xi19_2l0/mmxi2
h1xi20prime_2l0=h1xi20_2l0/mmxi2
h1xi21prime_2l0=h1xi21_2l0/mmxi2


h1xi19prime_2l2=h1xi19_2l2/(mmxi2-mmavgxi2)
h1xi20prime_2l2=h1xi20_2l2/(mmxi2-mmavgxi2)
h1xi21prime_2l2=h1xi21_2l2/(mmxi2-mmavgxi2)

fh3xi19prime_l0=fh3xi19_l0/mmxi
fh4xi19prime_l0=fh4xi19_l0/mmxi
fh3xi20prime_l0=fh3xi20_l0/mmxi
fh4xi20prime_l0=fh4xi20_l0/mmxi
fh3xi21prime_l0=fh3xi21_l0/mmxi
fh4xi21prime_l0=fh4xi21_l0/mmxi

fh3xi19prime_l2=fh3xi19_l2/(mmxi-mmavgxi)
fh4xi19prime_l2=fh4xi19_l2/(mmxi-mmavgxi)
fh3xi20prime_l2=fh3xi20_l2/(mmxi-mmavgxi)
fh4xi20prime_l2=fh4xi20_l2/(mmxi-mmavgxi)
fh3xi21prime_l2=fh3xi21_l2/(mmxi-mmavgxi)
fh4xi21prime_l2=fh4xi21_l2/(mmxi-mmavgxi)

h3xi19prime_2l0=h3xi19_2l0/mmxi2
h4xi19prime_2l0=h4xi19_2l0/mmxi2
h3xi20prime_2l0=h3xi20_2l0/mmxi2
h4xi20prime_2l0=h4xi20_2l0/mmxi2
h3xi21prime_2l0=h3xi21_2l0/mmxi2
h4xi21prime_2l0=h4xi21_2l0/mmxi2

h3xi19prime_2l2=h3xi19_2l2/(mmxi2-mmavgxi2)
h4xi19prime_2l2=h4xi19_2l2/(mmxi2-mmavgxi2)
h3xi20prime_2l2=h3xi20_2l2/(mmxi2-mmavgxi2)
h4xi20prime_2l2=h4xi20_2l2/(mmxi2-mmavgxi2)
h3xi21prime_2l2=h3xi21_2l2/(mmxi2-mmavgxi2)
h4xi21prime_2l2=h4xi21_2l2/(mmxi2-mmavgxi2)

fh5xi19prime_l0=fh5xi19_l0/mmxi
fh5xi20prime_l0=fh5xi20_l0/mmxi
fh5xi21prime_l0=fh5xi21_l0/mmxi

fh5xi19prime_l2=fh5xi19_l2/(mmxi-mmavgxi)
fh5xi20prime_l2=fh5xi20_l2/(mmxi-mmavgxi)
fh5xi21prime_l2=fh5xi21_l2/(mmxi-mmavgxi)

h5xi19prime_2l0=h5xi19_2l0/mmxi2
h5xi20prime_2l0=h5xi20_2l0/mmxi2
h5xi21prime_2l0=h5xi21_2l0/mmxi2

h5xi19prime_2l2=h5xi19_2l2/(mmxi2-mmavgxi2)
h5xi20prime_2l2=h5xi20_2l2/(mmxi2-mmavgxi2)
h5xi21prime_2l2=h5xi21_2l2/(mmxi2-mmavgxi2)


estimator_fab19=(7.0/48.0)*(5.0*(7.0*fabxi19prime_l0+fabxi19prime_l2)-np.sqrt(35.0*(35.0*fabxi19prime_l0**2+10.0*fabxi19prime_l0*fabxi19prime_l2-7.0*fabxi19prime_l2**2)))
estimator_fnab19=(7.0/48.0)*(5.0*(7.0*fnabxi19prime_l0+fnabxi19prime_l2)-np.sqrt(35.0*(35.0*fnabxi19prime_l0**2+10.0*fnabxi19prime_l0*fnabxi19prime_l2-7.0*fnabxi19prime_l2**2)))
estimator_fab20=(7.0/48.0)*(5.0*(7.0*fabxi20prime_l0+fabxi20prime_l2)-np.sqrt(35.0*(35.0*fabxi20prime_l0**2+10.0*fabxi20prime_l0*fabxi20prime_l2-7.0*fabxi20prime_l2**2)))
estimator_fnab20=(7.0/48.0)*(5.0*(7.0*fnabxi20prime_l0+fnabxi20prime_l2)-np.sqrt(35.0*(35.0*fnabxi20prime_l0**2+10.0*fnabxi20prime_l0*fnabxi20prime_l2-7.0*fnabxi20prime_l2**2)))
estimator_fab21=(7.0/48.0)*(5.0*(7.0*fabxi21prime_l0+fabxi21prime_l2)-np.sqrt(35.0*(35.0*fabxi21prime_l0**2+10.0*fabxi21prime_l0*fabxi21prime_l2-7.0*fabxi21prime_l2**2)))
estimator_fnab21=(7.0/48.0)*(5.0*(7.0*fnabxi21prime_l0+fnabxi21prime_l2)-np.sqrt(35.0*(35.0*fnabxi21prime_l0**2+10.0*fnabxi21prime_l0*fnabxi21prime_l2-7.0*fnabxi21prime_l2**2)))

estimator_ab19_2=(7.0/48.0)*(5.0*(7.0*abxi19prime_2l0+abxi19prime_2l2)-np.sqrt(35.0*(35.0*abxi19prime_2l0**2+10.0*abxi19prime_2l0*abxi19prime_2l2-7.0*abxi19prime_2l2**2)))
estimator_nab19_2=(7.0/48.0)*(5.0*(7.0*nabxi19prime_2l0+nabxi19prime_2l2)-np.sqrt(35.0*(35.0*nabxi19prime_2l0**2+10.0*nabxi19prime_2l0*nabxi19prime_2l2-7.0*nabxi19prime_2l2**2)))
estimator_ab20_2=(7.0/48.0)*(5.0*(7.0*abxi20prime_2l0+abxi20prime_2l2)-np.sqrt(35.0*(35.0*abxi20prime_2l0**2+10.0*abxi20prime_2l0*abxi20prime_2l2-7.0*abxi20prime_2l2**2)))
estimator_nab20_2=(7.0/48.0)*(5.0*(7.0*nabxi20prime_2l0+nabxi20prime_2l2)-np.sqrt(35.0*(35.0*nabxi20prime_2l0**2+10.0*nabxi20prime_2l0*nabxi20prime_2l2-7.0*nabxi20prime_2l2**2)))
estimator_ab21_2=(7.0/48.0)*(5.0*(7.0*abxi21prime_2l0+abxi21prime_2l2)-np.sqrt(35.0*(35.0*abxi21prime_2l0**2+10.0*abxi21prime_2l0*abxi21prime_2l2-7.0*abxi21prime_2l2**2)))
estimator_nab21_2=(7.0/48.0)*(5.0*(7.0*nabxi21prime_2l0+nabxi21prime_2l2)-np.sqrt(35.0*(35.0*nabxi21prime_2l0**2+10.0*nabxi21prime_2l0*nabxi21prime_2l2-7.0*nabxi21prime_2l2**2)))

estimator_f1h19=(7.0/48.0)*(5.0*(7.0*fh1xi19prime_l0+fh1xi19prime_l2)-np.sqrt(35.0*(35.0*fh1xi19prime_l0**2+10.0*fh1xi19prime_l0*fh1xi19prime_l2-7.0*fh1xi19prime_l2**2)))
estimator_f1h20=(7.0/48.0)*(5.0*(7.0*fh1xi20prime_l0+fh1xi20prime_l2)-np.sqrt(35.0*(35.0*fh1xi20prime_l0**2+10.0*fh1xi20prime_l0*fh1xi20prime_l2-7.0*fh1xi20prime_l2**2)))
estimator_f1h21=(7.0/48.0)*(5.0*(7.0*fh1xi21prime_l0+fh1xi21prime_l2)-np.sqrt(35.0*(35.0*fh1xi21prime_l0**2+10.0*fh1xi21prime_l0*fh1xi21prime_l2-7.0*fh1xi21prime_l2**2)))

estimator_f3h19=(7.0/48.0)*(5.0*(7.0*fh3xi19prime_l0+fh3xi19prime_l2)-np.sqrt(35.0*(35.0*fh3xi19prime_l0**2+10.0*fh3xi19prime_l0*fh3xi19prime_l2-7.0*fh3xi19prime_l2**2)))
estimator_f4h19=(7.0/48.0)*(5.0*(7.0*fh4xi19prime_l0+fh4xi19prime_l2)-np.sqrt(35.0*(35.0*fh4xi19prime_l0**2+10.0*fh4xi19prime_l0*fh4xi19prime_l2-7.0*fh4xi19prime_l2**2)))
estimator_f3h20=(7.0/48.0)*(5.0*(7.0*fh3xi20prime_l0+fh3xi20prime_l2)-np.sqrt(35.0*(35.0*fh3xi20prime_l0**2+10.0*fh3xi20prime_l0*fh3xi20prime_l2-7.0*fh3xi20prime_l2**2)))
estimator_f4h20=(7.0/48.0)*(5.0*(7.0*fh4xi20prime_l0+fh4xi20prime_l2)-np.sqrt(35.0*(35.0*fh4xi20prime_l0**2+10.0*fh4xi20prime_l0*fh4xi20prime_l2-7.0*fh4xi20prime_l2**2)))
estimator_f3h21=(7.0/48.0)*(5.0*(7.0*fh3xi21prime_l0+fh3xi21prime_l2)-np.sqrt(35.0*(35.0*fh3xi21prime_l0**2+10.0*fh3xi21prime_l0*fh3xi21prime_l2-7.0*fh3xi21prime_l2**2)))
estimator_f4h21=(7.0/48.0)*(5.0*(7.0*fh4xi21prime_l0+fh4xi21prime_l2)-np.sqrt(35.0*(35.0*fh4xi21prime_l0**2+10.0*fh4xi21prime_l0*fh4xi21prime_l2-7.0*fh4xi21prime_l2**2)))

estimator_f5h19=(7.0/48.0)*(5.0*(7.0*fh5xi19prime_l0+fh5xi19prime_l2)-np.sqrt(35.0*(35.0*fh5xi19prime_l0**2+10.0*fh5xi19prime_l0*fh5xi19prime_l2-7.0*fh5xi19prime_l2**2)))
estimator_f5h20=(7.0/48.0)*(5.0*(7.0*fh5xi20prime_l0+fh5xi20prime_l2)-np.sqrt(35.0*(35.0*fh5xi20prime_l0**2+10.0*fh5xi20prime_l0*fh5xi20prime_l2-7.0*fh5xi20prime_l2**2)))
estimator_f5h21=(7.0/48.0)*(5.0*(7.0*fh5xi21prime_l0+fh5xi21prime_l2)-np.sqrt(35.0*(35.0*fh5xi21prime_l0**2+10.0*fh5xi21prime_l0*fh5xi21prime_l2-7.0*fh5xi21prime_l2**2)))

estimator_1h19_2=(7.0/48.0)*(5.0*(7.0*h1xi19prime_2l0+h1xi19prime_2l2)-np.sqrt(35.0*(35.0*h1xi19prime_2l0**2+10.0*h1xi19prime_2l0*h1xi19prime_2l2-7.0*h1xi19prime_2l2**2)))
estimator_1h20_2=(7.0/48.0)*(5.0*(7.0*h1xi20prime_2l0+h1xi20prime_2l2)-np.sqrt(35.0*(35.0*h1xi20prime_2l0**2+10.0*h1xi20prime_2l0*h1xi20prime_2l2-7.0*h1xi20prime_2l2**2)))
estimator_1h21_2=(7.0/48.0)*(5.0*(7.0*h1xi21prime_2l0+h1xi21prime_2l2)-np.sqrt(35.0*(35.0*h1xi21prime_2l0**2+10.0*h1xi21prime_2l0*h1xi21prime_2l2-7.0*h1xi21prime_2l2**2)))

estimator_3h19_2=(7.0/48.0)*(5.0*(7.0*h3xi19prime_2l0+h3xi19prime_2l2)-np.sqrt(35.0*(35.0*h3xi19prime_2l0**2+10.0*h3xi19prime_2l0*h3xi19prime_2l2-7.0*h3xi19prime_2l2**2)))
estimator_4h19_2=(7.0/48.0)*(5.0*(7.0*h4xi19prime_2l0+h4xi19prime_2l2)-np.sqrt(35.0*(35.0*h4xi19prime_2l0**2+10.0*h4xi19prime_2l0*h4xi19prime_2l2-7.0*h4xi19prime_2l2**2)))
estimator_3h20_2=(7.0/48.0)*(5.0*(7.0*h3xi20prime_2l0+h3xi20prime_2l2)-np.sqrt(35.0*(35.0*h3xi20prime_2l0**2+10.0*h3xi20prime_2l0*h3xi20prime_2l2-7.0*h3xi20prime_2l2**2)))
estimator_4h20_2=(7.0/48.0)*(5.0*(7.0*h4xi20prime_2l0+h4xi20prime_2l2)-np.sqrt(35.0*(35.0*h4xi20prime_2l0**2+10.0*h4xi20prime_2l0*h4xi20prime_2l2-7.0*h4xi20prime_2l2**2)))
estimator_3h21_2=(7.0/48.0)*(5.0*(7.0*h3xi21prime_2l0+h3xi21prime_2l2)-np.sqrt(35.0*(35.0*h3xi21prime_2l0**2+10.0*h3xi21prime_2l0*h3xi21prime_2l2-7.0*h3xi21prime_2l2**2)))
estimator_4h21_2=(7.0/48.0)*(5.0*(7.0*h4xi21prime_2l0+h4xi21prime_2l2)-np.sqrt(35.0*(35.0*h4xi21prime_2l0**2+10.0*h4xi21prime_2l0*h4xi21prime_2l2-7.0*h4xi21prime_2l2**2)))
estimator_5h19_2=(7.0/48.0)*(5.0*(7.0*h5xi19prime_2l0+h5xi19prime_2l2)-np.sqrt(35.0*(35.0*h5xi19prime_2l0**2+10.0*h5xi19prime_2l0*h5xi19prime_2l2-7.0*h5xi19prime_2l2**2)))
estimator_5h20_2=(7.0/48.0)*(5.0*(7.0*h5xi20prime_2l0+h5xi20prime_2l2)-np.sqrt(35.0*(35.0*h5xi20prime_2l0**2+10.0*h5xi20prime_2l0*h5xi20prime_2l2-7.0*h5xi20prime_2l2**2)))
estimator_5h21_2=(7.0/48.0)*(5.0*(7.0*h5xi21prime_2l0+h5xi21prime_2l2)-np.sqrt(35.0*(35.0*h5xi21prime_2l0**2+10.0*h5xi21prime_2l0*h5xi21prime_2l2-7.0*h5xi21prime_2l2**2)))


estimator_hw13_avg=np.vstack((fs_center,estimator_fab19,estimator_fnab19,estimator_fab20,estimator_fnab20,estimator_fab21,estimator_fnab21)).T
estimator_hw13_avgcut=np.vstack((s2_center,estimator_ab19_2,estimator_nab19_2,estimator_ab20_2,estimator_nab20_2,estimator_ab21_2,estimator_nab21_2)).T

estimator_models_avg=np.vstack((fs_center,estimator_f1h19,estimator_f3h19,estimator_f4h19,estimator_f5h19,estimator_f1h20,estimator_f3h20,estimator_f4h20,estimator_f5h20,estimator_f1h21,estimator_f3h21,estimator_f4h21,estimator_f5h21)).T
estimator_models_avgcut=np.vstack((s2_center,estimator_1h19_2,estimator_3h19_2,estimator_4h19_2,estimator_5h19_2,estimator_1h20_2,estimator_3h20_2,estimator_4h20_2,estimator_5h20_2,estimator_1h21_2,estimator_3h21_2,estimator_4h21_2,estimator_5h21_2)).T


np.savetxt('hodMr20estimator_cent_avg.dat',estimator_hw13_avg,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e'])
np.savetxt('hodMr20estimator_cent_avgCUT.dat',estimator_hw13_avgcut,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e'])

np.savetxt('estimator_models_cent_avg.dat',estimator_models_avg,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e',])
np.savetxt('estimator_models_cent_avgCUT.dat',estimator_models_avgcut,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e'])




