# Imports different galaxy mocks for manipulation (catalog file handling), such as shift into redshift-space for selected line-of-sight through simulation box.


import numpy as np

H=100.


cat_opt=int(input('ANN_HW13_Mock,HW13_Mock, HW13_shuffled, Models, or .01% DM particle catalog (0,1, 2, 3, or 4 respectively): '))
if cat_opt==4:
	num=int(input('What number particle pull (1,2,3...):'))
	ID_opt=int(input('Include ID tags? (yes=1 no=0)'))
	infile='dmpart_{}.csv'.format(num)
	cent_opt=0
	los=int(input('What is the line of sight (noshift=0,x=1,y=2,z=3);  '))
else:
	cent_opt=int(input('Just centrals (yes=1 no=0): '))
	if cat_opt==3:
		ID_opt=0
		sft_opt=int(input('Redshift or configuration space? (redshift=1 configuration=0): '))
		los=int(input('What is the desired line-of-sight (x=1,y=2,z=3): '))
		lum_thres=int(input('What luminosity threshold is desired (enter only 19, 20, or 21)?  '))
		SCAM_mod=raw_input('Which model (macc,vacc,vpeak,hod,hodls,eHOD,vaccHOD) ?  ')
		boot_opt3=int(input('Bootstrap sample? (yes=1 no=0): '))
		boot_opt=2
		color_choice=0
	else:
		ID_opt=int(input('Include ID tags? (yes=1 no=0)'))
		los=int(input('What is the line of sight (noshift=0,x=1,y=2,z=3);  '))
		lum_thres=float(input('What luminosity threshold is desired (ex. for absolute mag less than (brighter than) -19, enter -19.0): '))
		boot_opt=int(input('Bootstrap sample? (yes=1 no=0): '))
		boot_opt3=2
percent=float(input('What percentage of available galaxies (particles) do you want draw at random? '))
if cat_opt==1:
        rerr=int(input('Redshift errors (yes=1 no=0): '))
        if rerr==1:
                FILE='Mr19mock_rederror.dat'
        if rerr==0:
                FILE='Mr19Mock.dat'
drawfrac=percent/100.

if cat_opt==0:
        zeroID,zeroMvir,zerox,zeroy,zeroz,zerovx,zerovy,zerovz,zeroMr=np.loadtxt('ANN_HW13_mock_200k_stoTEST.dat',unpack=True)
        cut=zeroMr<=lum_thres
	x=zerox[cut]
        y=zeroy[cut]
        z=zeroz[cut]
        vy=zerovy[cut]
        vz=zerovz[cut]
        vx=zerovx[cut]
        partID=zeroID[cut]
if cat_opt==1:
	color_choice=int(input('Red/blue cut sample (0=No 1=Yes): '))
	vbias=int(input('Velocity bias for centrals (0=No 1=yes): '))
	oneID,onex,oney,onez,onevx,onevy,onevz,oneMvir,oneVpeak,oneMr,onegr,oneM,onePID=np.loadtxt(FILE,unpack=True)
	x=onex[oneMr<=lum_thres]
	y=oney[oneMr<=lum_thres]
	z=onez[oneMr<=lum_thres]
	vy=onevy[oneMr<=lum_thres]
	vz=onevz[oneMr<=lum_thres]
	vx=onevx[oneMr<=lum_thres]
	partID=oneID[oneMr<=lum_thres]
	partPID=onePID[oneMr<=lum_thres]
	gr=onegr[oneMr<=lum_thres]
	Mr=oneMr[oneMr<=lum_thres]
	if vbias==1:
		alpha_c=input('What is the value of alpha_c: ')
		Mvir=oneMvir[oneMr<=lum_thres]
		sigma_m=140*(Mvir/(10**12))
		sigma_g=alpha_c*sigma_m
		delvbias=np.zeros(len(Mvir))
		for i in range(0,len(Mvir)):
			if i < len(Mvir):
				if partPID[i] <0:
					delvbias[i]=np.random.normal(loc=0.0, scale=sigma_g[i])
				else: 	
					delvbias[i]=0
	if color_choice==1:
		N=len(x)
		redblue=np.zeros(N)
		for i in range(0,N):
        		if i < N:
                		grcut=0.21-0.03*Mr[i]
                		if gr[i]>grcut:
                        		redblue[i]=1

		redcut=redblue==1
		bluecut=redblue==0
		bluex=x[bluecut]
		bluey=y[bluecut]
		bluez=z[bluecut]
		bluevz=vz[bluecut]
		bluevy=vy[bluecut]
		bluevx=vx[bluecut]
		bluePID=partPID[bluecut]
		redx=x[redcut]
		redy=y[redcut]
		redz=z[redcut]
		redvz=vz[redcut]
		redvy=vy[redcut]
		redvx=vx[redcut]
		redPID=partPID[redcut]

		
if cat_opt==2:
	color_choice=0
	twoID,twoPID,twox,twoy,twoz,twovx,twovy,twovz,twomag,twogr,twoM=np.loadtxt('Shuffled_Mr19mock.dat',unpack=True)
        vbias=int(input('Velocity bias for centrals (0=No 1=yes): '))
	x=twox[twomag<=lum_thres]
	y=twoy[twomag<=lum_thres]
	z=twoz[twomag<=lum_thres]	
	vx=twovx[twomag<=lum_thres]
	vy=twovy[twomag<=lum_thres]
	vz=twovz[twomag<=lum_thres]
	partID=twoID[twomag<=lum_thres]
	partPID=twoPID[twomag<=lum_thres]
        if vbias==1:
                alpha_c=input('What is the value of alpha_c: ')
                M=twoM[twomag<=lum_thres]
                sigma_m=140*(M/(10**12))
                sigma_g=alpha_c*sigma_m
                delvbias=np.zeros(len(M))
                for i in range(0,len(M)):
                        if i < len(M):
                                if partPID[i] <0:
                                        delvbias[i]=np.random.normal(loc=0.0, scale=sigma_g[i])
                                else:
                                        delvbias[i]=0

if cat_opt==3:
	infile='mock_HW13_{}_Mr{}_NEW.dat'.format(SCAM_mod,lum_thres)
	PID,loghostmass,x,y,z,vx,vy,vz,delx,dely,delz,delx_2,dely_2,delz_2=np.loadtxt(infile,unpack=True)

if cat_opt==4:
	threerowID,threeID,threex,threey,threez,threevx,threevy,threevz=np.loadtxt(infile, delimiter=',',unpack=True)
	x=threex
	y=threey
	z=threez
	vx=threevx
	vy=threevy
	vz=threevz
	partID=threeID


if cent_opt==1:
	if cat_opt==1 or cat_opt==2 or cat_opt==4:
		if color_choice==1:
                        bluex=bluex[bluePID<0]
                        bluey=bluey[bluePID<0]
                        bluez=bluez[bluePID<0]
                        bluevx=bluevx[bluePID<0]
                        bluevy=bluevy[bluePID<0]
                        bluevz=bluevz[bluePID<0]
                        redx=redx[redPID<0]
                        redy=redy[redPID<0]
                        redz=redz[redPID<0]
                        redvx=redvx[redPID<0]
                        redvy=redvy[redPID<0]
                        redvz=redvz[redPID<0]

		else:
			x=x[partPID<0]
			y=y[partPID<0]
			z=z[partPID<0]
			vx=vx[partPID<0]
			vy=vy[partPID<0]
			vz=vz[partPID<0]
			partID=partID[partPID<0]
	else:
		x=x[PID==0]
		y=y[PID==0]
		z=z[PID==0]
		delx=delx[PID==0]
		dely=dely[PID==0]
		delz=delz[PID==0]
		delx_2=delx_2[PID==0]
                dely_2=dely_2[PID==0]
                delz_2=delz_2[PID==0]


if boot_opt==1:
	Nparts=len(x)
	randsel=np.array(Nparts*np.random.random_sample(Nparts),dtype=int)
	x=x[randsel]
	y=y[randsel]
	z=z[randsel]
	vx=vx[randsel]
	vy=vy[randsel]
	vz=vz[randsel]
	partID=partID[randsel]
	if los==1:
		x=np.around((x+vx/H),decimals=3)
	if los==2:
		y=np.around((y+vy/H),decimals=3)
	if los==3:
		z=np.around((z+vz/H),decimals=3)

if boot_opt3==1:
	Nparts=len(x)
	xs=np.zeros(Nparts)
	ys=np.zeros(Nparts)
	zs=np.zeros(Nparts)
	vzs=np.zeros(Nparts)
	for i in range(0,Nparts):
		if i < Nparts:
			s=int(Nparts*np.random.random_sample())
			xs[i]=x[s]
			ys[i]=y[s]
			zs[i]=z[s]
			vzs[i]=vz[s]
	if sft_opt==0:
		x=xs
		y=ys
		z=np.around((zs-vzs/H),decimals=3)
	else:
		x=xs
		y=ys
		z=zs

if boot_opt==0:
	if percent < 100:
		N=float(len(z))
		randdraw=np.random.randint(0,N,size=drawfrac*N)
		randdraw1=np.unique(randdraw)
		s=float(len(randdraw1))
		print('Actual Precent Returned:  {}'.format(np.around((s/N),decimals=4)))
		x=x[randdraw1]
		y=y[randdraw1]
		z=z[randdraw1]
		partID=partID[randdraw1]

	if color_choice==1:
                if los==1:
                        bluex=np.around((bluex+bluevx/H),decimals=3)
                        redx=np.around((redx+redvx/H),decimals=3)
                if los==2:
                        bluey=np.around((bluey+bluevy/H),decimals=3)
                        redy=np.around((redy+redvy/H),decimals=3)
		if los==3:
                        bluez=np.around((bluez+bluevz/H),decimals=3)
                        redz=np.around((redz+redvz/H),decimals=3)

	else:
		if vbias==1:
	                if los==1:
	                        x=np.around((x+vx/H+delvbias/H),decimals=3)
        	        if los==2:
                	        y=np.around((y+vy/H+delvbias/H),decimals=3)
               		if los==3:
                        	z=np.around((z+vz/H+delvbias/H),decimals=3)
		else:
			if los==1:
				x=np.around((x+vx/H),decimals=3)
			if los==2:
				y=np.around((y+vy/H),decimals=3)
			if los==3:
				z=np.around((z+vz/H),decimals=3)
if boot_opt3==0:
	if percent < 100:
		N=float(len(z))
		randdraw=np.random.randint(0,N,size=drawfrac*N)
		randdraw1=np.unique(randdraw)
		s=float(len(randdraw1))
		print('Actual Precent Returned:  {}'.format(np.around((s/N),decimals=4)))
		x=x[randdraw1]
		y=y[randdraw1]
		z=z[randdraw1]
		vz=vz[randdraw1]
		partID=partID[randdraw1]
	if sft_opt==1:
		if los==1:
			x=x+delx+delx_2
		if los==2:
			y=y+dely+dely_2
		if los==3:
			z=z+delz+delz_2
	


if color_choice==1:
	if los==1:
		los='x'
	if los==2:
		los='y'
	if los==3:
		los='z'
	if cent_opt==1:
		outfl_blue='Mr{}sp_blue_sft{}_cent.dat'.format(int(abs(lum_thres)),los)
                outfl_red='Mr{}sp_red_sft{}_cent.dat'.format(int(abs(lum_thres)),los)
	else:
                outfl_blue='Mr{}sp_blue_sft{}.dat'.format(int(abs(lum_thres)),los)
                outfl_red='Mr{}sp_red_sft{}.dat'.format(int(abs(lum_thres)),los)

	bsp=np.vstack((bluex,bluey,bluez)).T
        rsp=np.vstack((redx,redy,redz)).T

        np.savetxt(outfl_blue,bsp,fmt=['%10.3f','%10.3f','%10.3f'])
        np.savetxt(outfl_red,rsp,fmt=['%10.3f','%10.3f','%10.3f'])

else:
	outfl=raw_input('Enter output file name (outputting only spatial positions x,y,z): ')
	if ID_opt==1:
		spid=np.vstack((partPID,x,y,z,vx,vy,vz)).T
		np.savetxt(outfl,spid,fmt=['%15d','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f'])
	if ID_opt==0:
		sp=np.vstack((x,y,z)).T
		np.savetxt(outfl,sp,fmt=['%10.3f','%10.3f','%10.3f'])

print("Subset catalog prepared. File written!")








	   
