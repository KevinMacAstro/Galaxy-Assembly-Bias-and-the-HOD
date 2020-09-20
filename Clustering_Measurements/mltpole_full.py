# Pulls in xi(s,u) measurements, after having been averaged over the lines-of-sight (x,y,z), with a seperate code created by Z.Z.
# Calculates xi_0, xi_2, and xi_4 for the full observation, shuffled observation, HOD, and 3 SCAMS.
# Here are shown the measurement file inputs for the central-only galaxy mocks.

import numpy as np
import matplotlib.pyplot as plt

#Import xi(s,u) values of mocks:
ab_s_cen19,ab_u_cen19,abxi19=np.loadtxt('Mr19su_cent_avg.dat', unpack=True)
ab_s_cen19,ab_u_cen19,nabxi19=np.loadtxt('eMr19su_cent_avg.dat', unpack=True)
ab_s_cen20,ab_u_cen20,abxi20=np.loadtxt('Mr20su_cent_avg.dat', unpack=True)
ab_s_cen20,ab_u_cen20,nabxi20=np.loadtxt('eMr20su_cent_avg.dat', unpack=True)
ab_s_cen21,ab_u_cen21,abxi21=np.loadtxt('Mr21su_cent_avg.dat', unpack=True)
ab_s_cen21,ab_u_cen21,nabxi21=np.loadtxt('eMr21su_cent_avg.dat', unpack=True)
ab_s_cen19,ab_u_cen19,h1xi19=np.loadtxt('hodMr19su_cent_avg.dat', unpack=True)
ab_s_cen20,ab_u_cen20,h1xi20=np.loadtxt('hodMr20su_cent_avg.dat', unpack=True)
ab_s_cen21,ab_u_cen21,h1xi21=np.loadtxt('hodMr21su_cent_avg.dat', unpack=True)
ab_s_cen19,ab_u_cen19,h2xi19=np.loadtxt('hodlsMr19su_cent_avg.dat', unpack=True)
ab_s_cen20,ab_u_cen20,h2xi20=np.loadtxt('hodlsMr20su_cent_avg.dat', unpack=True)
ab_s_cen21,ab_u_cen21,h2xi21=np.loadtxt('hodlsMr21su_cent_avg.dat', unpack=True)
ab_s_cen19,ab_u_cen19,h3xi19=np.loadtxt('maccMr19su_cent_avg.dat', unpack=True)
ab_s_cen20,ab_u_cen20,h3xi20=np.loadtxt('maccMr20su_cent_avg.dat', unpack=True)
ab_s_cen21,ab_u_cen21,h3xi21=np.loadtxt('maccMr21su_cent_avg.dat', unpack=True)
ab_s_cen19,ab_u_cen19,h4xi19=np.loadtxt('vaccMr19su_cent_avg.dat', unpack=True)
ab_s_cen20,ab_u_cen20,h4xi20=np.loadtxt('vaccMr20su_cent_avg.dat', unpack=True)
ab_s_cen21,ab_u_cen21,h4xi21=np.loadtxt('vaccMr21su_cent_avg.dat', unpack=True)
ab_s_cen19,ab_u_cen19,h5xi19=np.loadtxt('vpeakMr19su_cent_avg.dat', unpack=True)
ab_s_cen20,ab_u_cen20,h5xi20=np.loadtxt('vpeakMr20su_cent_avg.dat', unpack=True)
ab_s_cen21,ab_u_cen21,h5xi21=np.loadtxt('vpeakMr21su_cent_avg.dat', unpack=True)


#Multipole Calculation
uBin=20
sBin=12
abxi19=abxi19.reshape(uBin,sBin)
nabxi19=nabxi19.reshape(uBin,sBin)
ab_u_cen19=ab_u_cen19.reshape(uBin,sBin)
ab_s_cen19=ab_s_cen19.reshape(uBin,sBin)
h1xi19=h1xi19.reshape(uBin,sBin)
h2xi19=h2xi19.reshape(uBin,sBin)
h3xi19=h3xi19.reshape(uBin,sBin)
h4xi19=h4xi19.reshape(uBin,sBin)
h5xi19=h5xi19.reshape(uBin,sBin)

abxi20=abxi20.reshape(uBin,sBin)
nabxi20=nabxi20.reshape(uBin,sBin)
ab_u_cen20=ab_u_cen20.reshape(uBin,sBin)
ab_s_cen20=ab_s_cen20.reshape(uBin,sBin)
h1xi20=h1xi20.reshape(uBin,sBin)
h2xi20=h2xi20.reshape(uBin,sBin)
h3xi20=h3xi20.reshape(uBin,sBin)
h4xi20=h4xi20.reshape(uBin,sBin)
h5xi20=h5xi20.reshape(uBin,sBin)

abxi21=abxi21.reshape(uBin,sBin)
nabxi21=nabxi21.reshape(uBin,sBin)
ab_u_cen21=ab_u_cen21.reshape(uBin,sBin)
ab_s_cen21=ab_s_cen21.reshape(uBin,sBin)
h1xi21=h1xi21.reshape(uBin,sBin)
h2xi21=h2xi21.reshape(uBin,sBin)
h3xi21=h3xi21.reshape(uBin,sBin)
h4xi21=h4xi21.reshape(uBin,sBin)
h5xi21=h5xi21.reshape(uBin,sBin)

ab_s_cen19=ab_s_cen19[0,:]
ab_s_cen20=ab_s_cen20[0,:]
ab_s_cen21=ab_s_cen21[0,:]
du=0.05

abxi19_l0=[]
abxi19_l2=[]
abxi19_l4=[]
for i in range(0,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
		for j in range(0,uBin):
			if j < uBin:
				xi0=xi0+abxi19[j,i]*du
				xi2=xi2+abxi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
				xi4=xi4+abxi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
		abxi19_l0.append(xi0)
		abxi19_l2.append(xi2)
		abxi19_l4.append(xi4)
abxi19_l0=np.array(abxi19_l0)
abxi19_l2=np.array(abxi19_l2)
abxi19_l4=np.array(abxi19_l4)

nabxi19_l0=[]
nabxi19_l2=[]
nabxi19_l4=[]
for i in range(0,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+nabxi19[j,i]*du
                                xi2=xi2+nabxi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+nabxi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                nabxi19_l0.append(xi0)
                nabxi19_l2.append(xi2)
                nabxi19_l4.append(xi4)

nabxi19_l0=np.array(nabxi19_l0)
nabxi19_l2=np.array(nabxi19_l2)
nabxi19_l4=np.array(nabxi19_l4)

h1xi19_l0=[]
h1xi19_l2=[]
h1xi19_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h1xi19[j,i]*du
                                xi2=xi2+h1xi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+h1xi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                h1xi19_l0.append(xi0)
                h1xi19_l2.append(xi2)
                h1xi19_l4.append(xi4)
h1xi19_l0=np.array(h1xi19_l0)
h1xi19_l2=np.array(h1xi19_l2)
h1xi19_l4=np.array(h1xi19_l4)

h2xi19_l0=[]
h2xi19_l2=[]
h2xi19_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h2xi19[j,i]*du
                                xi2=xi2+h2xi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+h2xi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                h2xi19_l0.append(xi0)
                h2xi19_l2.append(xi2)
                h2xi19_l4.append(xi4)
h2xi19_l0=np.array(h2xi19_l0)
h2xi19_l2=np.array(h2xi19_l2)
h2xi19_l4=np.array(h2xi19_l4)


h3xi19_l0=[]
h3xi19_l2=[]
h3xi19_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h3xi19[j,i]*du
                                xi2=xi2+h3xi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+h3xi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                h3xi19_l0.append(xi0)
                h3xi19_l2.append(xi2)
                h3xi19_l4.append(xi4)

h3xi19_l0=np.array(h3xi19_l0)
h3xi19_l2=np.array(h3xi19_l2)
h3xi19_l4=np.array(h3xi19_l4)

h4xi19_l0=[]
h4xi19_l2=[]
h4xi19_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h4xi19[j,i]*du
                                xi2=xi2+h4xi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+h4xi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                h4xi19_l0.append(xi0)
                h4xi19_l2.append(xi2)
                h4xi19_l4.append(xi4)

h4xi19_l0=np.array(h4xi19_l0)
h4xi19_l2=np.array(h4xi19_l2)
h4xi19_l4=np.array(h4xi19_l4)

h5xi19_l0=[]
h5xi19_l2=[]
h5xi19_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h5xi19[j,i]*du
                                xi2=xi2+h5xi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+h5xi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                h5xi19_l0.append(xi0)
                h5xi19_l2.append(xi2)
                h5xi19_l4.append(xi4)

h5xi19_l0=np.array(h5xi19_l0)
h5xi19_l2=np.array(h5xi19_l2)
h5xi19_l4=np.array(h5xi19_l4)

abxi20_l0=[]
abxi20_l2=[]
abxi20_l4=[]
for i in range(0,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
		for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+abxi20[j,i]*du
                                xi2=xi2+abxi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+abxi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                abxi20_l0.append(xi0)
                abxi20_l2.append(xi2)
                abxi20_l4.append(xi4)

abxi20_l0=np.array(abxi20_l0)
abxi20_l2=np.array(abxi20_l2)
abxi20_l4=np.array(abxi20_l4)

nabxi20_l0=[]
nabxi20_l2=[]
nabxi20_l4=[]
for i in range(0,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
		for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+nabxi20[j,i]*du
                                xi2=xi2+nabxi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+nabxi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                nabxi20_l0.append(xi0)
                nabxi20_l2.append(xi2)
                nabxi20_l4.append(xi4)

nabxi20_l0=np.array(nabxi20_l0)
nabxi20_l2=np.array(nabxi20_l2)
nabxi20_l4=np.array(nabxi20_l4)

h1xi20_l0=[]
h1xi20_l2=[]
h1xi20_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h1xi20[j,i]*du
                                xi2=xi2+h1xi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+h1xi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                h1xi20_l0.append(xi0)
                h1xi20_l2.append(xi2)
                h1xi20_l4.append(xi4)

h1xi20_l0=np.array(h1xi20_l0)
h1xi20_l2=np.array(h1xi20_l2)
h1xi20_l4=np.array(h1xi20_l4)

h2xi20_l0=[]
h2xi20_l2=[]
h2xi20_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h2xi20[j,i]*du
                                xi2=xi2+h2xi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+h2xi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                h2xi20_l0.append(xi0)
                h2xi20_l2.append(xi2)
                h2xi20_l4.append(xi4)

h2xi20_l0=np.array(h2xi20_l0)
h2xi20_l2=np.array(h2xi20_l2)
h2xi20_l4=np.array(h2xi20_l4)

h3xi20_l0=[]
h3xi20_l2=[]
h3xi20_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h3xi20[j,i]*du
                                xi2=xi2+h3xi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+h3xi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                h3xi20_l0.append(xi0)
                h3xi20_l2.append(xi2)
                h3xi20_l4.append(xi4)
h3xi20_l0=np.array(h3xi20_l0)
h3xi20_l2=np.array(h3xi20_l2)
h3xi20_l4=np.array(h3xi20_l4)

h4xi20_l0=[]
h4xi20_l2=[]
h4xi20_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h4xi20[j,i]*du
                                xi2=xi2+h4xi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+h4xi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                h4xi20_l0.append(xi0)
                h4xi20_l2.append(xi2)
                h4xi20_l4.append(xi4)
h4xi20_l0=np.array(h4xi20_l0)
h4xi20_l2=np.array(h4xi20_l2)
h4xi20_l4=np.array(h4xi20_l4)

h5xi20_l0=[]
h5xi20_l2=[]
h5xi20_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h5xi20[j,i]*du
                                xi2=xi2+h5xi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+h5xi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                h5xi20_l0.append(xi0)
                h5xi20_l2.append(xi2)
                h5xi20_l4.append(xi4)
h5xi20_l0=np.array(h5xi20_l0)
h5xi20_l2=np.array(h5xi20_l2)
h5xi20_l4=np.array(h5xi20_l4)

abxi21_l0=[]
abxi21_l2=[]
abxi21_l4=[]
for i in range(0,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
		for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+abxi21[j,i]*du
                                xi2=xi2+abxi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+abxi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                abxi21_l0.append(xi0)
                abxi21_l2.append(xi2)
                abxi21_l4.append(xi4)

abxi21_l0=np.array(abxi21_l0)
abxi21_l2=np.array(abxi21_l2)
abxi21_l4=np.array(abxi21_l4)

nabxi21_l0=[]
nabxi21_l2=[]
nabxi21_l4=[]
for i in range(0,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
		for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+nabxi21[j,i]*du
                                xi2=xi2+nabxi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+nabxi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                nabxi21_l0.append(xi0)
                nabxi21_l2.append(xi2)
                nabxi21_l4.append(xi4)
nabxi21_l0=np.array(nabxi21_l0)
nabxi21_l2=np.array(nabxi21_l2)
nabxi21_l4=np.array(nabxi21_l4)

h1xi21_l0=[]
h1xi21_l2=[]
h1xi21_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                               xi0=xi0+h1xi21[j,i]*du
                               xi2=xi2+h1xi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                               xi4=xi4+h1xi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                h1xi21_l0.append(xi0)
                h1xi21_l2.append(xi2)
                h1xi21_l4.append(xi4)
h1xi21_l0=np.array(h1xi21_l0)
h1xi21_l2=np.array(h1xi21_l2)
h1xi21_l4=np.array(h1xi21_l4)


h2xi21_l0=[]
h2xi21_l2=[]
h2xi21_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                               xi0=xi0+h2xi21[j,i]*du
                               xi2=xi2+h2xi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                               xi4=xi4+h2xi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                h2xi21_l0.append(xi0)
                h2xi21_l2.append(xi2)
                h2xi21_l4.append(xi4)
h2xi21_l0=np.array(h2xi21_l0)
h2xi21_l2=np.array(h2xi21_l2)
h2xi21_l4=np.array(h2xi21_l4)


h3xi21_l0=[]
h3xi21_l2=[]
h3xi21_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h3xi21[j,i]*du
                                xi2=xi2+h3xi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+h3xi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                h3xi21_l0.append(xi0)
                h3xi21_l2.append(xi2)
                h3xi21_l4.append(xi4)

h3xi21_l0=np.array(h3xi21_l0)
h3xi21_l2=np.array(h3xi21_l2)
h3xi21_l4=np.array(h3xi21_l4)

h4xi21_l0=[]
h4xi21_l2=[]
h4xi21_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h4xi21[j,i]*du
                                xi2=xi2+h4xi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+h4xi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                h4xi21_l0.append(xi0)
                h4xi21_l2.append(xi2)
                h4xi21_l4.append(xi4)

h4xi21_l0=np.array(h4xi21_l0)
h4xi21_l2=np.array(h4xi21_l2)
h4xi21_l4=np.array(h4xi21_l4)

h5xi21_l0=[]
h5xi21_l2=[]
h5xi21_l4=[]
for i in range(0,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h5xi21[j,i]*du
                                xi2=xi2+h5xi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+h5xi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                h5xi21_l0.append(xi0)
                h5xi21_l2.append(xi2)
                h5xi21_l4.append(xi4)

h5xi21_l0=np.array(h5xi21_l0)
h5xi21_l2=np.array(h5xi21_l2)
h5xi21_l4=np.array(h5xi21_l4)

smin=-1.
smax=1.4
lnbinsize=np.log10(np.power(10,smax)/np.power(10,smin))/sBin
s_center=np.zeros(sBin)
for i in range(0,sBin):
	if i < sBin:
		s_center[i]=np.power(10,((smin+i*lnbinsize+smin+(i+1)*lnbinsize)/2))

s_center=s_center[s_center>0]

xipole19_hw13=np.vstack((s_center,nabxi19_l0,nabxi19_l2,nabxi19_l4)).T
xipole20_hw13=np.vstack((s_center,nabxi20_l0,nabxi20_l2,nabxi20_l4)).T
xipole21_hw13=np.vstack((s_center,nabxi21_l0,nabxi21_l2,nabxi21_l4)).T

xipole19_models=np.vstack((s_center,h1xi19_l0,h1xi19_l2,h1xi19_l4,h3xi19_l0,h3xi19_l2,h3xi19_l4,h4xi19_l0,h4xi19_l2,h4xi19_l4,h5xi19_l0,h5xi19_l2,h5xi19_l4)).T
xipole20_models=np.vstack((s_center,h1xi20_l0,h1xi20_l2,h1xi20_l4,h3xi20_l0,h3xi20_l2,h3xi20_l4,h4xi20_l0,h4xi20_l2,h4xi20_l4,h5xi20_l0,h5xi20_l2,h5xi20_l4)).T
xipole21_models=np.vstack((s_center,h1xi21_l0,h1xi21_l2,h1xi21_l4,h3xi21_l0,h3xi21_l2,h3xi21_l4,h4xi21_l0,h4xi21_l2,h4xi21_l4,h5xi21_l0,h5xi21_l2,h5xi21_l4)).T


file1='Xipoles_LINehwearly_avg_centnoVB_12bin.dat'
file2='Xipoles_LINhwlate_avg_centVB2_12bin.dat'
file3='Xipoles21_eHW13_avg_12bin.dat'
file4='Xipoles19_models_cent_avg.dat'
file5='Xipoles20_models_cent_avg.dat'
file6='Xipoles21_models_cent_avg.dat'

np.savetxt(file1,xipole19_hw13,fmt=['%10.3f','%5e','%5e','%5e'])
np.savetxt(file2,xipole20_hw13,fmt=['%10.3f','%5e','%5e','%5e'])
np.savetxt(file3,xipole21_hw13,fmt=['%10.3f','%5e','%5e','%5e'])
np.savetxt(file4,xipole19_models,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e'])
np.savetxt(file5,xipole20_models,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e'])
np.savetxt(file6,xipole21_models,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e'])




