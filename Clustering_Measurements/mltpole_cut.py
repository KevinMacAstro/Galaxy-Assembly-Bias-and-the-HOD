# Pulls in xi(s,u) measurements, calculated in a seperate program created by Z.Z., truncates the pairs within a specified transverse seperation (r_p)
# Calculates the truncated 2PCF multipoles and extrapolates the resulting modified mono-, quadra-, and hexadeca-pole.

import numpy as np
import matplotlib.pyplot as plt

def I00(u):
	result=u
	return result
def I02(u):
	result=u**3/2.-u/2.
	return result
def I04(u):
	result=7.*u**5/8.-5.*u**3/4.+3.*u/8.
	return result
def I22(u):
	result=9.*u**5/20.-u**3/2.+u/4.
	return result
def I24(u):
	result=15.*u**7/16.-25.*u**5/16.+13.*u**3/16.-3.*u/16.
	return result
def I44(u):
	result=1225.*u**9/576.-75.*u**7/16.+111.*u**5/32. -15.*u**3/16.+9.*u/64.
	return result
def det(u):
	result=np.abs(45.*(I00(u)*I22(u)*I44(u)-I00(u)*I24(u)**2-I02(u)**2*I44(u)+2.*I02(u)*I04(u)*I24(u)-I04(u)**2*I22(u)))
	return result
def xi0_true(xi0,xi2,xi4,u):
	result=(45.*(I22(u)*I44(u)-I24(u)**2)*xi0-9.*(I02(u)*I44(u)-I24(u)*I04(u))*xi2+5.*(I02(u)*I24(u)-I04(u)*I22(u))*xi4)/det(u)
	return result	
def xi2_true(xi0,xi2,xi4,u):
	result=(-45.*(I02(u)*I44(u)-I24(u)*I04(u))*xi0+9.*(I00(u)*I44(u)-I04(u)**2)*xi2-5.*(I00(u)*I24(u)-I04(u)*I02(u))*xi4)/det(u)
	return result
def xi4_true(xi0,xi2,xi4,u):
	result=(45.*(I02(u)*I24(u)-I22(u)*I04(u))*xi0-9.*(I00(u)*I24(u)-I04(u)*I02(u))*xi2+5.*(I00(u)*I22(u)-I02(u)**2)*xi4)/det(u)
	return result

#Import xi(s,u) values of mocks:
ab_s_cen19,ab_u_cen19,abxi19=np.loadtxt('hodMr19su_cent_avg.dat', unpack=True)
nab_s_cen19,nab_u_cen19,nabxi19=np.loadtxt('eMr19su_avg_p1.dat', unpack=True)
ab_s_cen20,ab_u_cen20,abxi20=np.loadtxt('hodMr20su_cent_avg.dat', unpack=True)
nab_s_cen20,nab_u_cen20,nabxi20=np.loadtxt('eMr20su_avg_p1.dat', unpack=True)
ab_s_cen21,ab_u_cen21,abxi21=np.loadtxt('Mr21su_avg_p1.dat', unpack=True)
nab_s_cen21,nab_u_cen21,nabxi21=np.loadtxt('eMr21su_avg_p1.dat', unpack=True)
ab_s_cen19,ab_u_cen19,h1xi19=np.loadtxt('hodMr19su_cent_avg.dat', unpack=True)
ab_s_cen20,ab_u_cen20,h1xi20=np.loadtxt('hodMr20su_cent_avg.dat', unpack=True)
ab_s_cen21,ab_u_cen21,h1xi21=np.loadtxt('hodMr21su_cent_avg.dat', unpack=True)
ab_s_cen19,ab_u_cen19,h2xi19=np.loadtxt('hodlsMr19su_avg_new.dat', unpack=True)
ab_s_cen20,ab_u_cen20,h2xi20=np.loadtxt('hodlsMr20su_avg_new.dat', unpack=True)
ab_s_cen21,ab_u_cen21,h2xi21=np.loadtxt('hodlsMr21su_avg_new.dat', unpack=True)
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
sBin=27
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

u_min=0.
u_max=1.
uBin=20
du=(u_max-u_min)/uBin
u_outer=np.zeros(20)
for i in range(0,20):
	if i < 20:
		u_outer[i]=(i+1)*du

s_min=-1.
s_max=1.7 
sBin=27      
ds=np.log10(np.power(10,s_max)/np.power(10,s_min))/sBin
s_inner=np.zeros((sBin)) 
for i in range(0,sBin):
        if i < sBin:
                s_inner[i]=np.power(10,(s_min+i*ds))

r_cut=2.
for i in range(0,sBin):
	if i < sBin:
		if s_inner[i]>r_cut:
			si=i
			break

abxi19_l0=[]
abxi19_l2=[]
abxi19_l4=[]
for i in range(si,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
		umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
		uBin=umax
		for j in range(0,uBin):
			if j < uBin:
				xi0=xi0+abxi19[j,i]*du
				xi2=xi2+abxi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
				xi4=xi4+abxi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
		if uBin < 20:
			xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
			xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
			xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
			xi0=xi0_t
			xi2=xi2_t
			xi4=xi4_t

		abxi19_l0.append(xi0)
		abxi19_l2.append(xi2)
		abxi19_l4.append(xi4)

abxi19_l0=np.array(abxi19_l0)
abxi19_l2=np.array(abxi19_l2)
abxi19_l4=np.array(abxi19_l4)

nabxi19_l0=[]
nabxi19_l2=[]
nabxi19_l4=[]
for i in range(si,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+nabxi19[j,i]*du
                                xi2=xi2+nabxi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+nabxi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
		if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t

                nabxi19_l0.append(xi0)
                nabxi19_l2.append(xi2)
                nabxi19_l4.append(xi4)

nabxi19_l0=np.array(nabxi19_l0)
nabxi19_l2=np.array(nabxi19_l2)
nabxi19_l4=np.array(nabxi19_l4)

h1xi19_l0=[]
h1xi19_l2=[]
h1xi19_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h1xi19[j,i]*du
                                xi2=xi2+h1xi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+h1xi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t

                h1xi19_l0.append(xi0)
                h1xi19_l2.append(xi2)
                h1xi19_l4.append(xi4)

h1xi19_l0=np.array(h1xi19_l0)
h1xi19_l2=np.array(h1xi19_l2)
h1xi19_l4=np.array(h1xi19_l4)

h2xi19_l0=[]
h2xi19_l2=[]
h2xi19_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h2xi19[j,i]*du
                                xi2=xi2+h2xi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+h2xi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t

                h2xi19_l0.append(xi0)
                h2xi19_l2.append(xi2)
                h2xi19_l4.append(xi4)

h2xi19_l0=np.array(h2xi19_l0)
h2xi19_l2=np.array(h2xi19_l2)
h2xi19_l4=np.array(h2xi19_l4)


h3xi19_l0=[]
h3xi19_l2=[]
h3xi19_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h3xi19[j,i]*du
                                xi2=xi2+h3xi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+h3xi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t

                h3xi19_l0.append(xi0)
                h3xi19_l2.append(xi2)
                h3xi19_l4.append(xi4)

h3xi19_l0=np.array(h3xi19_l0)
h3xi19_l2=np.array(h3xi19_l2)
h3xi19_l4=np.array(h3xi19_l4)

h4xi19_l0=[]
h4xi19_l2=[]
h4xi19_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h4xi19[j,i]*du
                                xi2=xi2+h4xi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+h4xi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t

                h4xi19_l0.append(xi0)
                h4xi19_l2.append(xi2)
                h4xi19_l4.append(xi4)

h4xi19_l0=np.array(h4xi19_l0)
h4xi19_l2=np.array(h4xi19_l2)
h4xi19_l4=np.array(h4xi19_l4)

h5xi19_l0=[]
h5xi19_l2=[]
h5xi19_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h5xi19[j,i]*du
                                xi2=xi2+h5xi19[j,i]*du*(3.*ab_u_cen19[j,i]**2-1.)*5./2.
                                xi4=xi4+h5xi19[j,i]*du*(35.*ab_u_cen19[j,i]**4-30.*ab_u_cen19[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t

                h5xi19_l0.append(xi0)
                h5xi19_l2.append(xi2)
                h5xi19_l4.append(xi4)

h5xi19_l0=np.array(h5xi19_l0)
h5xi19_l2=np.array(h5xi19_l2)
h5xi19_l4=np.array(h5xi19_l4)

abxi20_l0=[]
abxi20_l2=[]
abxi20_l4=[]
for i in range(si,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
		for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+abxi20[j,i]*du
                                xi2=xi2+abxi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+abxi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t

                abxi20_l0.append(xi0)
                abxi20_l2.append(xi2)
                abxi20_l4.append(xi4)

abxi20_l0=np.array(abxi20_l0)
abxi20_l2=np.array(abxi20_l2)
abxi20_l4=np.array(abxi20_l4)

nabxi20_l0=[]
nabxi20_l2=[]
nabxi20_l4=[]
for i in range(si,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
		for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+nabxi20[j,i]*du
                                xi2=xi2+nabxi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+nabxi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t

                nabxi20_l0.append(xi0)
                nabxi20_l2.append(xi2)
                nabxi20_l4.append(xi4)

nabxi20_l0=np.array(nabxi20_l0)
nabxi20_l2=np.array(nabxi20_l2)
nabxi20_l4=np.array(nabxi20_l4)

h1xi20_l0=[]
h1xi20_l2=[]
h1xi20_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h1xi20[j,i]*du
                                xi2=xi2+h1xi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+h1xi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t

                h1xi20_l0.append(xi0)
                h1xi20_l2.append(xi2)
                h1xi20_l4.append(xi4)

h1xi20_l0=np.array(h1xi20_l0)
h1xi20_l2=np.array(h1xi20_l2)
h1xi20_l4=np.array(h1xi20_l4)

h2xi20_l0=[]
h2xi20_l2=[]
h2xi20_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h2xi20[j,i]*du
                                xi2=xi2+h2xi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+h2xi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t

                h2xi20_l0.append(xi0)
                h2xi20_l2.append(xi2)
                h2xi20_l4.append(xi4)

h2xi20_l0=np.array(h2xi20_l0)
h2xi20_l2=np.array(h2xi20_l2)
h2xi20_l4=np.array(h2xi20_l4)


h3xi20_l0=[]
h3xi20_l2=[]
h3xi20_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h3xi20[j,i]*du
                                xi2=xi2+h3xi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+h3xi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t
                h3xi20_l0.append(xi0)
                h3xi20_l2.append(xi2)
                h3xi20_l4.append(xi4)
h3xi20_l0=np.array(h3xi20_l0)
h3xi20_l2=np.array(h3xi20_l2)
h3xi20_l4=np.array(h3xi20_l4)

h4xi20_l0=[]
h4xi20_l2=[]
h4xi20_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h4xi20[j,i]*du
                                xi2=xi2+h4xi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+h4xi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t
                h4xi20_l0.append(xi0)
                h4xi20_l2.append(xi2)
                h4xi20_l4.append(xi4)
h4xi20_l0=np.array(h4xi20_l0)
h4xi20_l2=np.array(h4xi20_l2)
h4xi20_l4=np.array(h4xi20_l4)

h5xi20_l0=[]
h5xi20_l2=[]
h5xi20_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h5xi20[j,i]*du
                                xi2=xi2+h5xi20[j,i]*du*(3.*ab_u_cen20[j,i]**2-1.)*5./2.
                                xi4=xi4+h5xi20[j,i]*du*(35.*ab_u_cen20[j,i]**4-30.*ab_u_cen20[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t
                h5xi20_l0.append(xi0)
                h5xi20_l2.append(xi2)
                h5xi20_l4.append(xi4)
h5xi20_l0=np.array(h5xi20_l0)
h5xi20_l2=np.array(h5xi20_l2)
h5xi20_l4=np.array(h5xi20_l4)

abxi21_l0=[]
abxi21_l2=[]
abxi21_l4=[]
for i in range(si,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
		for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+abxi21[j,i]*du
                                xi2=xi2+abxi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+abxi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                if uBin < 20:
                	xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t
                abxi21_l0.append(xi0)
                abxi21_l2.append(xi2)
                abxi21_l4.append(xi4)

abxi21_l0=np.array(abxi21_l0)
abxi21_l2=np.array(abxi21_l2)
abxi21_l4=np.array(abxi21_l4)

nabxi21_l0=[]
nabxi21_l2=[]
nabxi21_l4=[]
for i in range(si,sBin):
	if i < sBin:
		xi0=0.0
		xi2=0.0
		xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
		for j in range(0,uBin):
                	if j < uBin:
                        	xi0=xi0+nabxi21[j,i]*du
                                xi2=xi2+nabxi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+nabxi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
		if uBin < 20:
                	xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t
                nabxi21_l0.append(xi0)
                nabxi21_l2.append(xi2)
                nabxi21_l4.append(xi4)
nabxi21_l0=np.array(nabxi21_l0)
nabxi21_l2=np.array(nabxi21_l2)
nabxi21_l4=np.array(nabxi21_l4)
h1xi21_l0=[]
h1xi21_l2=[]
h1xi21_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                	if j < uBin:
                        	xi0=xi0+h1xi21[j,i]*du
                                xi2=xi2+h1xi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+h1xi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
		if uBin < 20:
                	xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t
                h1xi21_l0.append(xi0)
                h1xi21_l2.append(xi2)
                h1xi21_l4.append(xi4)
h1xi21_l0=np.array(h1xi21_l0)
h1xi21_l2=np.array(h1xi21_l2)
h1xi21_l4=np.array(h1xi21_l4)

h2xi21_l0=[]
h2xi21_l2=[]
h2xi21_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h2xi21[j,i]*du
                                xi2=xi2+h2xi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+h2xi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t
                h2xi21_l0.append(xi0)
                h2xi21_l2.append(xi2)
                h2xi21_l4.append(xi4)
h2xi21_l0=np.array(h2xi21_l0)
h2xi21_l2=np.array(h2xi21_l2)
h2xi21_l4=np.array(h2xi21_l4)

h3xi21_l0=[]
h3xi21_l2=[]
h3xi21_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h3xi21[j,i]*du
                                xi2=xi2+h3xi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+h3xi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t
                h3xi21_l0.append(xi0)
                h3xi21_l2.append(xi2)
                h3xi21_l4.append(xi4)

h3xi21_l0=np.array(h3xi21_l0)
h3xi21_l2=np.array(h3xi21_l2)
h3xi21_l4=np.array(h3xi21_l4)

h4xi21_l0=[]
h4xi21_l2=[]
h4xi21_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h4xi21[j,i]*du
                                xi2=xi2+h4xi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+h4xi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t
                h4xi21_l0.append(xi0)
                h4xi21_l2.append(xi2)
                h4xi21_l4.append(xi4)

h4xi21_l0=np.array(h4xi21_l0)
h4xi21_l2=np.array(h4xi21_l2)
h4xi21_l4=np.array(h4xi21_l4)

h5xi21_l0=[]
h5xi21_l2=[]
h5xi21_l4=[]
for i in range(si,sBin):
        if i < sBin:
                xi0=0.0
                xi2=0.0
                xi4=0.0
                umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[i])**2)])
                uBin=umax
                for j in range(0,uBin):
                        if j < uBin:
                                xi0=xi0+h5xi21[j,i]*du
                                xi2=xi2+h5xi21[j,i]*du*(3.*ab_u_cen21[j,i]**2-1.)*5./2.
                                xi4=xi4+h5xi21[j,i]*du*(35.*ab_u_cen21[j,i]**4-30.*ab_u_cen21[j,i]**2+3.)*9./8.
                if uBin < 20:
                        xi0_t=xi0_true(xi0,xi2,xi4,u_outer[j])
                        xi2_t=xi2_true(xi0,xi2,xi4,u_outer[j])
                        xi4_t=xi4_true(xi0,xi2,xi4,u_outer[j])
                        xi0=xi0_t
                        xi2=xi2_t
                        xi4=xi4_t
                h5xi21_l0.append(xi0)
                h5xi21_l2.append(xi2)
                h5xi21_l4.append(xi4)

h5xi21_l0=np.array(h5xi21_l0)
h5xi21_l2=np.array(h5xi21_l2)
h5xi21_l4=np.array(h5xi21_l4)

smin=-1.
smax=1.7
lnbinsize=np.log10(np.power(10,smax)/np.power(10,smin))/sBin
s_center=np.zeros(sBin)
for i in range(si,sBin):
	if i < sBin:
		s_center[i]=np.power(10,((smin+i*lnbinsize+smin+(i+1)*lnbinsize)/2))

s_center=s_center[s_center>0]


xipole19_hw13=np.vstack((s_center,abxi19_l0,abxi19_l2,abxi19_l4,nabxi19_l0,nabxi19_l2,nabxi19_l4)).T
xipole20_hw13=np.vstack((s_center,abxi20_l0,abxi20_l2,abxi20_l4,nabxi20_l0,nabxi20_l2,nabxi20_l4)).T
xipole21_hw13=np.vstack((s_center,abxi21_l0,abxi21_l2,abxi21_l4,nabxi21_l0,nabxi21_l2,nabxi21_l4)).T

xipole19_models=np.vstack((s_center,h1xi19_l0,h1xi19_l2,h1xi19_l4,h3xi19_l0,h3xi19_l2,h3xi19_l4,h4xi19_l0,h4xi19_l2,h4xi19_l4,h5xi19_l0,h5xi19_l2,h5xi19_l4)).T
xipole20_models=np.vstack((s_center,h1xi20_l0,h1xi20_l2,h1xi20_l4,h3xi20_l0,h3xi20_l2,h3xi20_l4,h4xi20_l0,h4xi20_l2,h4xi20_l4,h5xi20_l0,h5xi20_l2,h5xi20_l4)).T
xipole21_models=np.vstack((s_center,h1xi21_l0,h1xi21_l2,h1xi21_l4,h3xi21_l0,h3xi21_l2,h3xi21_l4,h4xi21_l0,h4xi21_l2,h4xi21_l4,h5xi21_l0,h5xi21_l2,h5xi21_l4)).T

file1='hodMr19xipoles_cent_avgCUT.dat'
file2='hodMr20xipoles_cent_avgCUT.dat'
file3='Xipoles21_hw13_avg4cut_new.dat'
file4='Xipoles19_models_cent_avgCUT.dat'
file5='Xipoles20_models_cent_avgCUT.dat'
file6='Xipoles21_models_cent_avgCUT.dat'


np.savetxt(file1,xipole19_hw13,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e'])
np.savetxt(file2,xipole20_hw13,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e'])
np.savetxt(file3,xipole21_hw13,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e'])
np.savetxt(file4,xipole19_models,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e'])
np.savetxt(file5,xipole20_models,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e'])
np.savetxt(file6,xipole21_models,fmt=['%10.3f','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e','%5e'])
####



