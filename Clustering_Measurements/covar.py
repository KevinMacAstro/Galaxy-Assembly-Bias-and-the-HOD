# Measures covariance matrix for mltpole and estimator calculations.


import numpy as np


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

err_opt=int(input('Error type (mlt=1,est_full=2,est_cut=3): '))
bins=int(input('12-bin or 27-bin (12 or 27): '))
mag=int(input('Magnitude Threshhold (19,20,21): '))


if err_opt==1:
        its=np.loadtxt('Mr{0}su_{1}_jackits_{2}avg.dat'.format(mag,color,bins), unpack=False)
        Nsubs=8
        uBin=20
        du=0.05
	sBin=bins
        s_cen=its[:,0]
	u_cen=its[:,1]
	it=its[:,2:10]
	s_cen=s_cen.reshape(uBin,sBin)
        u_cen=u_cen.reshape(uBin,sBin)
        xi_it_l0=np.zeros((sBin,Nsubs))
        xi_it_l2=np.zeros((sBin,Nsubs))
        xi_it_l4=np.zeros((sBin,Nsubs))
        for i in range(0,Nsubs):
                if i < Nsubs:
                        xi_it=it[:,i]
                        xi_it=xi_it.reshape(uBin,sBin)
                        for j in range(0,sBin):
                                if j < sBin:
                                        xi0=0.0
                                        xi2=0.0
                                        xi4=0.0
                                        for k in range(0,uBin):
                                                if k < uBin:
                                                        xi0=xi0+xi_it[k,j]*du
                                                        xi2=xi2+xi_it[k,j]*du*(3.*u_cen[k,j]**2-1.)*5./2.
                                                        xi4=xi4+xi_it[k,j]*du*(35.*u_cen[k,j]**4-30.*u_cen[k,j]**2+3.)*9./8.
                                        xi_it_l0[j,i]=xi0
                                        xi_it_l2[j,i]=xi2
                                        xi_it_l4[j,i]=xi4
        xi_itavg_l0=np.average(xi_it_l0,axis=1)
        xi_itavg_l2=np.average(xi_it_l2,axis=1)
        xi_itavg_l4=np.average(xi_it_l4,axis=1)

        c_l0=np.zeros((sBin,sBin))
        c_l2=np.zeros((sBin,sBin))
        c_l4=np.zeros((sBin,sBin))
        for i in range(0,sBin):
                if i < sBin:
                        for k in range(0,sBin):
                                if k < sBin:
                                        for j in range(0,Nsubs):
                                                if j < Nsubs:
                                                        c_l0[i,k]=c_l0[i,k]+(xi_it_l0[i,j]-xi_itavg_l0[i])*(xi_it_l0[k,j]-xi_itavg_l0[k])
                                                        c_l2[i,k]=c_l2[i,k]+(xi_it_l2[i,j]-xi_itavg_l2[i])*(xi_it_l2[k,j]-xi_itavg_l2[k])
                                                        c_l4[i,k]=c_l4[i,k]+(xi_it_l4[i,j]-xi_itavg_l4[i])*(xi_it_l4[k,j]-xi_itavg_l4[k])

        err_l0=(1.-1./Nsubs)*c_l0
        err_l2=(1.-1./Nsubs)*c_l2
        err_l4=(1.-1./Nsubs)*c_l4
        np.savetxt('Mr{0}mono_{1}_{2}covar.dat'.format(mag,color,bins),err_l0)
        np.savetxt('Mr{0}quad_{1}_{2}covar.dat'.format(mag,color,bins),err_l2)
        np.savetxt('Mr{0}hexa_{1}_{2}covar.dat'.format(mag,color,bins),err_l4)

if err_opt==2:
        its=np.loadtxt('eMr{0}su_cent_jackits_{1}avg.dat'.format(mag,bins),unpack=False)
        its=np.loadtxt('Mr{0}su_cent_jackits.dat'.format(mag), unpack=False)
        s_cen=its[:,0]
        u_cen=its[:,1]
        it=its[:,2:10]
        if bins==27:
                r_outer,r_ave,r_center,mmxi,mmerror_xi,mmavgxi,mmerror_avgxi,mmavgavgxi,mmerror_avgavgxi,mmNpair,mmNpspair,mmavgpair,mmavgrand,mmavgavgpair,mmavgavgrand=np.loadtxt('dmxi3d_log_L.dat', unpack=True)
        else:
                r_out,r_ave,mmxi,mmavgxi,dmavgavgxi=np.loadtxt('dmxi_12bin_avg.dat',unpack=True)
        sigma8=.82
        sigma8_sq=sigma8**2
        mmxi=mmxi/sigma8_sq
        mmavgxi=mmavgxi/sigma8_sq

        Nsubs=8
        uBin=20
        sBin=bins
        du=0.05
        s_cen=s_cen.reshape(uBin,sBin)
        u_cen=u_cen.reshape(uBin,sBin)
        xi_it_l0=np.zeros(sBin)
        xi_it_l2=np.zeros(sBin)
        estimatorMODEL=np.zeros((sBin,Nsubs))
        for i in range(0,Nsubs):
                if i < Nsubs:
                        xi_it=it[:,i]
                        xi_it=xi_it.reshape(uBin,sBin)
                        for j in range(0,sBin):
                                if j < sBin:
                                        xi0=0.0
                                        xi2=0.0
                                        xi4=0.0
                                        for k in range(0,uBin):
                                                if k < uBin:
                                                        xi0=xi0+xi_it[k,j]*du
                                                        xi2=xi2+xi_it[k,j]*du*(3.*u_cen[k,j]**2-1.)*5./2.
                                        xi_it_l0[j]=xi0
                                        xi_it_l2[j]=xi2
                        xiprime_l0=xi_it_l0/mmxi
                        xiprime_l2=xi_it_l2/(mmxi-mmavgxi)
                        estimatorMODEL[:,i]=np.sqrt((7.0/48.0)*(5.0*(7.0*xiprime_l0+xiprime_l2)-np.sqrt(35.0*(35.0*xiprime_l0**2+10.0*xiprime_l0*xiprime_l2-7.0*xiprime_l2**2))))



        its=np.loadtxt('Mr{0}su_cent_jackits_{1}avg.dat'.format(mag,bins),unpack=False)	
        its=np.loadtxt('Mr{0}su_cent_jackits.dat'.format(mag), unpack=False)


        it=its[:,2:10]

        xi_it_l0=np.zeros(sBin)
        xi_it_l2=np.zeros(sBin)
        estimatorOBS=np.zeros((sBin,Nsubs))
        for i in range(0,Nsubs):
                if i < Nsubs:
                        xi_it=it[:,i]
                        xi_it=xi_it.reshape(uBin,sBin)
                        for j in range(0,sBin):
                                if j < sBin:
                                        xi0=0.0
                                        xi2=0.0
                                        xi4=0.0
                                        for k in range(0,uBin):
                                                if k < uBin:
                                                        xi0=xi0+xi_it[k,j]*du
                                                        xi2=xi2+xi_it[k,j]*du*(3.*u_cen[k,j]**2-1.)*5./2.
                                        xi_it_l0[j]=xi0
                                        xi_it_l2[j]=xi2
                        xiprime_l0=xi_it_l0/mmxi
                        xiprime_l2=xi_it_l2/(mmxi-mmavgxi)
                        estimatorOBS[:,i]=np.sqrt((7.0/48.0)*(5.0*(7.0*xiprime_l0+xiprime_l2)-np.sqrt(35.0*(35.0*xiprime_l0**2+10.0*xiprime_l0*xiprime_l2-7.0*xiprime_l2**2))))

        rat=np.zeros((sBin,Nsubs))
        for i in range(0,Nsubs):
                rat[:,i]=estimatorMODEL[:,i]/estimatorOBS[:,i]

        rat_avg=np.average(rat,axis=1)
        r_est=np.zeros((sBin,sBin))
        for i in range(0,sBin):
                if i < sBin:
                        for k in range(0,sBin):
                                if k < sBin:
                                        for j in range(0,Nsubs):
                                                if j < Nsubs:
                                                        r_est[i,k]=r_est[i,k]+(rat[i,j]-rat_avg[i])*(rat[k,j]-rat_avg[k])

        err_rat=(1.-1./Nsubs)*r_est


        np.savetxt('cest{0}_27rate_covar_full.dat'.format(mag),err_rat)






        estimator_avg=np.average(estimator,axis=1)
        c_est=np.zeros((sBin,sBin))
        for i in range(0,sBin):
        	if i < sBin:
        		for k in range(0,sBin):
        			if k < sBin:
                                        for j in range(0,Nsubs):
                                                if j < Nsubs:
                                                        c_est[i,k]=c_est[i,k]+(estimator[i,j]-estimator_avg[i])*(estimator[k,j]-estimator_avg[k])
        err_est=(1.-1./Nsubs)*c_est
        np.savetxt('est{0}_cent_{1}covar.dat'.format(mag,bins),err_est)

if err_opt==3:
	ITS=np.loadtxt('vpeakMr{}su_cent_jackits_27avg.dat'.format(mag), unpack=False)
        its=np.loadtxt('Mr{0}su_jackits_avg.dat'.format(mag,bins), unpack=False)
        s_cen=ITS[:,0]
        u_cen=ITS[:,1]
        it=ITS[:,2:]
        r_outer,r_ave,r_center,mmxi,mmerror_xi,mmavgxi,mmerror_avgxi,mmavgavgxi,mmerror_avgavgxi,mmNpair,mmNpspair,mmavgpair,mmavgrand,mmavgavgpair,mmavgavgrand=np.loadtxt('dmxi3d_log_L.dat', unpack=True)
        sigma8=.82
        sigma8_sq=sigma8**2
        mmxi=mmxi/sigma8_sq
        mmavgxi=mmavgxi/sigma8_sq
        mmavgavgxi=mmavgavgxi/sigma8_sq
        s=len(mmxi)-13 #Second length is how many s2_center bins there are from the mltpole_avg2cut_hw13.dat file.
        mmxi2=mmxi[s:]
        mmavgxi2=mmavgxi[s:]      

 
        Nsubs=8
        u_min=0.
        u_max=1.
        uBin=20
        du=(u_max-u_min)/uBin
        u_outer=np.zeros(20)
        for i in range(0,20):
                if i < 20:
                        u_outer[i]=(i+1)*du

        s_min=-1.
	if bins==27:
        	s_max=1.7
        if bins==12:
		s_max=1.4
	sBin=bins
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

        s_cen=s_cen.reshape(uBin,sBin)
        u_cen=u_cen.reshape(uBin,sBin)
        estimatorMODEL=np.zeros((13,Nsubs))
        for i in range(0,Nsubs):
                if i < Nsubs:
                        uBin=20
                        xi_it_l0=[]
                        xi_it_l2=[]
                        xi_it_l4=[]
                        xi_it=it[:,i]
                        xi_it=xi_it.reshape(uBin,sBin)
                        for j in range(si,sBin):
                                if j < sBin:
                                        xi0=0.0
                                        xi2=0.0
                                        xi4=0.0
                                        umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[j])**2)])
                                        uBin=umax
                                        for k in range(0,uBin):
                                                if k < uBin:
                                                        xi0=xi0+xi_it[k,j]*du
                                                        xi2=xi2+xi_it[k,j]*du*(3.*u_cen[k,j]**2-1.)*5./2.
                                                        xi4=xi4+xi_it[k,j]*du*(35.*u_cen[k,j]**4-30.*u_cen[k,j]**2+3.)*9./8.
                                        if uBin < 20:
                                                xi0_t=xi0_true(xi0,xi2,xi4,u_outer[k])
                                                xi2_t=xi2_true(xi0,xi2,xi4,u_outer[k])

                                                xi0=xi0_t
                                                xi2=xi2_t


                                        xi_it_l0.append(xi0)
                                        xi_it_l2.append(xi2)
                        xi_it_l0=np.array(xi_it_l0)
                        xi_it_l2=np.array(xi_it_l2)
                        xiprime_l0=xi_it_l0/mmxi2
                        xiprime_l2=xi_it_l2/(mmxi2-mmavgxi2)
                        estimatorMODEL[:,i]=np.sqrt((7.0/48.0)*(5.0*(7.0*xiprime_l0+xiprime_l2)-np.sqrt(35.0*(35.0*xiprime_l0**2+10.0*xiprime_l0*xiprime_l2-7.0*xiprime_l2**2))))

        ITS=np.loadtxt('vpeakMr19su_avg_jackits.dat'.format(mag,bins), unpack=False)
        it=np.loadtxt('Mr{0}su_cent_jackits_27avg.dat'.format(mag,bins), unpack=False)
        it=it[:,2:]
	u_outer=np.zeros(20)
        for i in range(0,20):
                if i < 20:
                        u_outer[i]=(i+1)*du

        s_min=-1.
        if bins==27:
                s_max=1.7
        if bins==12:
                s_max=1.4
        sBin=bins
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

       
      
        estimatorOBS=np.zeros((13,Nsubs))
        for i in range(0,Nsubs):
                if i < Nsubs:
                        uBin=20
                        xi_it_l0=[]
                        xi_it_l2=[]
                        xi_it_l4=[]
                        xi_it=it[:,i]
                        xi_it=xi_it.reshape(uBin,sBin)
                        for j in range(si,sBin):
                                if j < sBin:
                                        xi0=0.0
                                        xi2=0.0
                                        xi4=0.0
                                        umax= len(u_outer[u_outer<np.sqrt(1-(r_cut/s_inner[j])**2)])
                                        uBin=umax
                                        for k in range(0,uBin):
                                                if k < uBin:
                                                        xi0=xi0+xi_it[k,j]*du
                                                        xi2=xi2+xi_it[k,j]*du*(3.*u_cen[k,j]**2-1.)*5./2.
                                                        xi4=xi4+xi_it[k,j]*du*(35.*u_cen[k,j]**4-30.*u_cen[k,j]**2+3.)*9./8.
                                        if uBin < 20:
                                                xi0_t=xi0_true(xi0,xi2,xi4,u_outer[k])
                                                xi2_t=xi2_true(xi0,xi2,xi4,u_outer[k])

                                                xi0=xi0_t
                                                xi2=xi2_t


                                        xi_it_l0.append(xi0)
                                        xi_it_l2.append(xi2)
                        xi_it_l0=np.array(xi_it_l0)
                        xi_it_l2=np.array(xi_it_l2)
                        xiprime_l0=xi_it_l0/mmxi2
                        xiprime_l2=xi_it_l2/(mmxi2-mmavgxi2)
                        estimatorOBS[:,i]=np.sqrt((7.0/48.0)*(5.0*(7.0*xiprime_l0+xiprime_l2)-np.sqrt(35.0*(35.0*xiprime_l0**2+10.0*xiprime_l0*xiprime_l2-7.0*xiprime_l2**2))))


	rat=np.zeros((13,Nsubs))
	for i in range(0,Nsubs):
		rat[:,i]=estimatorMODEL[:,i]/estimatorOBS[:,i]

        rat_avg=np.average(rat,axis=1)
        r_est=np.zeros((13,13))
        for i in range(0,13):
                if i < 13:
                        for k in range(0,13):
                                if k < 13:
                                        for j in range(0,Nsubs):
                                                if j < Nsubs:
                                                        r_est[i,k]=r_est[i,k]+(rat[i,j]-rat_avg[i])*(rat[k,j]-rat_avg[k])

	err_rat=(1.-1./Nsubs)*r_est
	

	np.savetxt('cest{0}_27ratvpeak_covar_2cut.dat'.format(mag),err_rat)

