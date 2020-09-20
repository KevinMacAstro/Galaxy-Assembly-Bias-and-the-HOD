# Program takes in the mock galaxy catalog with assemby bias (HW13) and shuffles the central-sat systems within halo mass bins.
# This removes the 2-halo AB signal.


import numpy as np
from datetime import datetime
print('Program started at {}.'.format(datetime.now().time()))

def binarySearch(alist, item):
	first = 0
	last = len(alist)-1
	found = False
	while first<=last and not found:
	        midpoint = (first + last)//2
	        if alist[midpoint] == item:
	            found = True
	        else:
	            if item < alist[midpoint]:
	                last = midpoint-1
	            else:
	                first = midpoint+1
	if found:
		return midpoint
	else:
		print('false')

#Import Data
mockdata=np.loadtxt('Mr19Mock.dat')
boldata=np.loadtxt('Bolshoi_z0.dat')

#Bolshoi Halos
haloID=np.array([boldata[:,1]]).T
haloPID=np.array([boldata[:,5]]).T
haloUPID=np.array([boldata[:,6]]).T
halospvl=np.around(boldata[:,17:23],decimals=3)
Mhalo=np.array([np.log10(boldata[:,10])]).T
Rhalo=np.array([boldata[:,11]]).T
haloVmax=np.array([boldata[:,16]]).T
Mhalolin=np.array([boldata[:,10]]).T
halosp=boldata[:,17:20]
halo4comp=np.concatenate((haloID,haloVmax,Mhalolin,halosp),axis=1)
halo4comps=halo4comp[np.argsort(halo4comp[:,0])]

halo=np.concatenate((haloID,haloPID,haloUPID,halospvl,Mhalo,Rhalo), axis=1)
halos=halo[np.argsort(halo[:,0])]
haloIDs=halos[:,0]
haloPIDs=halos[:,1]
halospvls=halos[:,3:9]
Mhalos=halos[:,9]


hosthalocut=haloPIDs<0
hosthaloIDs=haloIDs[hosthalocut]
hosthalospvls=halospvls[hosthalocut]
hosthalologMs=Mhalos[hosthalocut]

#Mock Galaxies
galID=np.array(mockdata[:,0],dtype=int)
galPID=np.array(mockdata[:,-1],dtype=int)
galspvl=mockdata[:,1:7]
galmrgr=mockdata[:,9:11]
galMhost=np.log10(mockdata[:,11])
galMvir=np.log10(mockdata[:,7])


centgalcut=galPID<0
centgalID=galID[centgalcut]
centgalPID=galPID[centgalcut]
centgalspvl=galspvl[centgalcut,:]
centgalmrgr=galmrgr[centgalcut,:]
centgalhalologM=galMhost[centgalcut]                        

satgalcut=galPID>0
nonhostgalID=galID[satgalcut]
nonhostgalPID=galPID[satgalcut]
nonhostgalspvl=galspvl[satgalcut,:]
nonhostgalmrgr=galmrgr[satgalcut,:]

#Loops to trace back each satellite galaxy to its host halo (some are in sub-sub halos where one or multiple subhalos do not have a central galaxy but the host halo does). If the host halo has a central galaxy, the satellite is placed in satgal, if not..ncsatgal. The host centric spatial positon and velocity are computed. Host halo ID and mass are also assigned (if they were not already).
satgalID=[]
satgalhosthaloID=[]
satgaldelspvl=[]
satgalmrgr=[]
satgalhosthalologM=[]

ncsatgalID=[]
ncsatgalhosthaloID=[]
ncsatgaldelspvl=[]
ncsatgalmrgr=[]
ncsatgalhosthalologM=[]

dmax=125
Nsat=len(nonhostgalID)
for i in range(0,Nsat):
	#print('{}'.format(i))
	if i < Nsat:
		haloindex=binarySearch(haloIDs,nonhostgalPID[i])
		if haloPIDs[haloindex]<1:
			if np.in1d(haloIDs[haloindex],centgalID)[0]:
				centindex=binarySearch(centgalID,haloIDs[haloindex])
				nonhostgalspvl[i]=nonhostgalspvl[i]-centgalspvl[centindex]
				if np.abs(nonhostgalspvl[i][0])>dmax:
					nonhostgalspvl[i][0]=250-np.abs(nonhostgalspvl[i][0])
				if np.abs(nonhostgalspvl[i][1])>dmax:
					nonhostgalspvl[i][1]=250-np.abs(nonhostgalspvl[i][1])
				if np.abs(nonhostgalspvl[i][2])>dmax:
					nonhostgalspvl[i][2]=250-np.abs(nonhostgalspvl[i][2])
				satgalID.append(nonhostgalID[i])
                                satgalhosthaloID.append(haloIDs[haloindex])
                                satgaldelspvl.append(nonhostgalspvl[i])
                                satgalmrgr.append(nonhostgalmrgr[i])
                                satgalhosthalologM.append(Mhalos[haloindex])
                        else:
				nonhostgalspvl[i]=nonhostgalspvl[i]-halospvls[haloindex]
                                if np.abs(nonhostgalspvl[i][0])>dmax:
                                        nonhostgalspvl[i][0]=250-np.abs(nonhostgalspvl[i][0])
                                if np.abs(nonhostgalspvl[i][1])>dmax:
                                        nonhostgalspvl[i][1]=250-np.abs(nonhostgalspvl[i][1])
                                if np.abs(nonhostgalspvl[i][2])>dmax:
                                        nonhostgalspvl[i][2]=250-np.abs(nonhostgalspvl[i][2])
                                ncsatgalID.append(nonhostgalID[i])
                                ncsatgalhosthaloID.append(haloIDs[haloindex])
                                ncsatgaldelspvl.append(nonhostgalspvl[i])
                                ncsatgalmrgr.append(nonhostgalmrgr[i])
                                ncsatgalhosthalologM.append(Mhalos[haloindex])
		else:
			halo2index=binarySearch(haloIDs,haloPIDs[haloindex])
                        if haloPIDs[halo2index]<1:
				if np.in1d(haloIDs[halo2index],centgalID)[0]:
					centindex=binarySearch(centgalID,haloIDs[halo2index])
                                	nonhostgalspvl[i]=nonhostgalspvl[i]-centgalspvl[centindex]
	                                if np.abs(nonhostgalspvl[i][0])>dmax:
        	                        	nonhostgalspvl[i][0]=250-np.abs(nonhostgalspvl[i][0])
                	                if np.abs(nonhostgalspvl[i][1])>dmax:
                        	        	nonhostgalspvl[i][1]=250-np.abs(nonhostgalspvl[i][1])
                               		if np.abs(nonhostgalspvl[i][2])>dmax:
                                       		nonhostgalspvl[i][2]=250-np.abs(nonhostgalspvl[i][2])
                                	satgalID.append(nonhostgalID[i])
                                	satgalhosthaloID.append(haloIDs[halo2index])
                                	satgaldelspvl.append(nonhostgalspvl[i])
                                	satgalmrgr.append(nonhostgalmrgr[i])
                                	satgalhosthalologM.append(Mhalos[halo2index])
                        	else:
                                	nonhostgalspvl[i]=nonhostgalspvl[i]-halospvls[halo2index]
	                                if np.abs(nonhostgalspvl[i][0])>dmax:
        	                                nonhostgalspvl[i][0]=250-np.abs(nonhostgalspvl[i][0])
        	                        if np.abs(nonhostgalspvl[i][1])>dmax:
                	                        nonhostgalspvl[i][1]=250-np.abs(nonhostgalspvl[i][1])
                	                if np.abs(nonhostgalspvl[i][2])>dmax:
                        	                nonhostgalspvl[i][2]=250-np.abs(nonhostgalspvl[i][2])
                                	ncsatgalID.append(nonhostgalID[i])
                                	ncsatgalhosthaloID.append(haloIDs[halo2index])
                                	ncsatgaldelspvl.append(nonhostgalspvl[i])
                                	ncsatgalmrgr.append(nonhostgalmrgr[i])
                                	ncsatgalhosthalologM.append(Mhalos[halo2index])
			else:
				halo3index=binarySearch(haloIDs,haloPIDs[halo2index])
                        	if haloPIDs[halo3index]<1:
                                	if np.in1d(haloIDs[halo3index],centgalID)[0]:
						centindex=binarySearch(centgalID,haloIDs[halo3index])
                                        	nonhostgalspvl[i]=nonhostgalspvl[i]-centgalspvl[centindex]
	                                	if np.abs(nonhostgalspvl[i][0])>dmax:
        	                                	nonhostgalspvl[i][0]=250-np.abs(nonhostgalspvl[i][0])
               		                	if np.abs(nonhostgalspvl[i][1])>dmax:
                        	                	nonhostgalspvl[i][1]=250-np.abs(nonhostgalspvl[i][1])
                               		 	if np.abs(nonhostgalspvl[i][2])>dmax:
                                        		nonhostgalspvl[i][2]=250-np.abs(nonhostgalspvl[i][2])
                                        	satgalID.append(nonhostgalID[i])
                                        	satgalhosthaloID.append(haloIDs[halo3index])
                                        	satgaldelspvl.append(nonhostgalspvl[i])
                                        	satgalmrgr.append(nonhostgalmrgr[i])
                                        	satgalhosthalologM.append(Mhalos[halo3index])
                                	else:
                                        	nonhostgalspvl[i]=nonhostgalspvl[i]-halospvls[halo3index]
		                                if np.abs(nonhostgalspvl[i][0])>dmax:
               			                	nonhostgalspvl[i][0]=250-np.abs(nonhostgalspvl[i][0])
                                		if np.abs(nonhostgalspvl[i][1])>dmax:
                                        		nonhostgalspvl[i][1]=250-np.abs(nonhostgalspvl[i][1])
                                		if np.abs(nonhostgalspvl[i][2])>dmax:
                                        		nonhostgalspvl[i][2]=250-np.abs(nonhostgalspvl[i][2])
                                        	ncsatgalID.append(nonhostgalID[i])
                                        	ncsatgalhosthaloID.append(haloIDs[halo3index])
                                        	ncsatgaldelspvl.append(nonhostgalspvl[i])
                                        	ncsatgalmrgr.append(nonhostgalmrgr[i])
                                        	ncsatgalhosthalologM.append(Mhalos[halo3index])

				else:
					print('Satellite galaxy {} does not have a home.'.format(nonhostgalID[i]))

#None central satellites checked. None of the ncsatgal PID belong to the galaxy catalog. All the corresponding halo's PID's are <0. Since all host central galaxy's can be found in the host halo's list (which have PID<0), no central galaxies were missed during the trace back. Moreover, all none central sats are at most only satellites of subhalos. Central Satellites can be at most satellites of a sub-sub halo making their home halo a sub-sub-sub halo. 
#N=len(ncsatgalID)
#for i in range(0,N):
#	if i < N:
#		ncindex=binarySearch(galID,ncsatgalID[i])
#                nc2index=binarySearch(galID,galPID[ncindex])l
#for i in range(0,N):
#	if i < N:
#		ncindex=binarySearch(galID,ncsatgalID[i])
#		haloin=binarySearch(haloIDs,galPID[ncindex])
#		if haloPIDs[haloin]>0:
#			halo2in=binarySearch(haloIDs,haloPIDs[haloin])
#			print('{}'.format(binarySearch(galID,haloIDs[halo2in])))




hosthaloID=np.array([hosthaloIDs]).T
hosthalologM=np.array([hosthalologMs]).T
hostgalID=np.array([centgalID]).T
hostgalhosthalologM=np.array([centgalhalologM]).T
satgalID=np.array([satgalID]).T
satgalhosthaloID=np.array([satgalhosthaloID]).T
satgalhosthalologM=np.array([satgalhosthalologM]).T
ncsatgalID=np.array([ncsatgalID]).T
ncsatgalhosthaloID=np.array([ncsatgalhosthaloID]).T
ncsatgalhosthalologM=np.array([ncsatgalhosthalologM]).T

#Ready for binning by mass.
hosthalo=np.concatenate((hosthaloID,hosthalospvls,hosthalologM), axis=1)
hostgal=np.concatenate((hostgalID,centgalspvl,centgalmrgr,hostgalhosthalologM), axis=1)
satgal=np.concatenate((satgalID,satgalhosthaloID,satgaldelspvl,satgalmrgr,satgalhosthalologM), axis=1)
ncsatgal=np.concatenate((ncsatgalID,ncsatgalhosthaloID,ncsatgaldelspvl,ncsatgalmrgr,ncsatgalhosthalologM), axis=1)

#hostgal=np.insert(hostgal,1,-1,axis=1)
#mocktracegal=np.vstack((hostgal,satgal,ncsatgal))
#mocktracegal[:,-1]=10**mocktracegal[:,-1]
#mocktracegal=mocktracegal[np.argsort(mocktracegal[:,0])]
#mocktracesp=mocktracegal[:,2:5]
#Output traced back mock catalog with original galaxy coordinates but with reference to original host halo ID and mass.
#np.savetxt('mocktrace.dat',mocktracegal, fmt=['%d','%10d','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3e'])

#XYZ cat for xi calc.
#np.savetxt('mocktracegalsp.dat',mocktracesp, fmt=['%10.3f','%10.3f','%10.3f'])


#Bin by mass
satgals=satgal[np.argsort(satgal[:,-1])]
ncsatgals=ncsatgal[np.argsort(ncsatgal[:,-1])]
hostgals=hostgal[np.argsort(hostgal[:,-1])]
hosthalos=hosthalo[np.argsort(hosthalo[:,-1])]
hosthalologMs=hosthalos[:,-1]
hostgallogMs=hostgals[:,-1]
satlogMs=satgals[:,-1]
ncsatlogMs=ncsatgals[:,-1]

bins=np.arange(9.72,14.98,0.07)
hosthalobin=np.array([np.digitize(hosthalologMs,bins)]).T
hostgalbin=np.array([np.digitize(hostgallogMs,bins)]).T
satbin=np.array([np.digitize(satlogMs,bins)]).T
ncsatbin=np.array([np.digitize(ncsatlogMs,bins)]).T

hosthalosbind=np.concatenate((hosthalos, hosthalobin), axis=1)
hostgalsbind=np.concatenate((hostgals, hostgalbin), axis=1)
satgalsbind=np.concatenate((satgals, satbin), axis=1)
ncsatgalsbind=np.concatenate((ncsatgals, ncsatbin), axis=1)

#Halos have been grouped by mass bin and shuffled within each bin. Ex/ Access groups of halos within each bin: hosthalosgroups[1,0] /*returns all halos in bin 1 which corresponds to halos with masses: 9.72<= logM/M_sun< 9.72+0.07. Access certain values for each halo within a specific bin: hosthalosgroups[1,0][:,0] /*returns halo ID number for each halo in bin 1. Note that there are halos in bin 0 but they have masses out of the range of the host halos we are looking for.
hosthalosgroups=np.array([np.split(hosthalosbind, np.where(np.diff(hosthalosbind[:,-1]))[0]+1)]).T

hosthalosgroupnum=len(hosthalosgroups)
for i in range(0, hosthalosgroupnum):
        if i < hosthalosgroupnum:
                np.random.shuffle(hosthalosgroups[i,0])

#Ex/ hostgalsgroups[1,0] has one central galaxy from mass bin 2. Halos in this same mass bin can be found in hosthalosgroups[2,0].
hostgalsgroups=np.array([np.split(hostgalsbind, np.where(np.diff(hostgalsbind[:,-1]))[0]+1)]).T

#Satellites have been grouped by host ID within each mass bin. Ex/ satgalsgroups[38,0] selects all the systems of satellites corresponding to bin number 55 from the original logM sort. Ex/ satgalsgroups[38,0][0] is the first system of satellites in mass bin 55 that belonged to host halo 2868993141 which had a logM~13.57. satgalsgroups[38,0][1] is the second system of satellites in mass bin 55 that belonged to host halo 2869003979 which had a logM~13.52.
satgalsgroups=np.array([np.split(satgalsbind, np.where(np.diff(satgalsbind[:,-1]))[0]+1)]).T
ncsatgalsgroups=np.array([np.split(ncsatgalsbind, np.where(np.diff(ncsatgalsbind[:,-1]))[0]+1)]).T

satgalsgroupsnum=len(satgalsgroups)
for i in range(0,satgalsgroupsnum):
        if i < satgalsgroupsnum:
                satgalsgroups[i,0]=satgalsgroups[i,0][np.argsort(satgalsgroups[i,0][:,1])]
                satgalsgroups[i,0]=np.split(satgalsgroups[i,0], np.where(np.diff(satgalsgroups[i,0][:,1]))[0]+1)

ncsatgalsgroupsnum=len(ncsatgalsgroups)
for i in range(0,ncsatgalsgroupsnum):
        if i < ncsatgalsgroupsnum:
                ncsatgalsgroups[i,0]=ncsatgalsgroups[i,0][np.argsort(ncsatgalsgroups[i,0][:,1])]
                ncsatgalsgroups[i,0]=np.split(ncsatgalsgroups[i,0], np.where(np.diff(ncsatgalsgroups[i,0][:,1]))[0]+1)

#Assign new space/velocity values to central galaxies. Also transfering new ID number hostgalID=hosthaloID.
hostgalsgroupsnum=len(hostgalsgroups)
for i in range (0,hostgalsgroupsnum):
        if i < hostgalsgroupsnum:
                if hostgalsgroups[i,0][:,-1][0]==hosthalosgroups[i+1,0][:,-1][0]:
                        hostgalsgroupnum=len(hostgalsgroups[i,0])
                        for t in range(0,hostgalsgroupnum):
				if t>len(hosthalosgroups[i+1,0]):
					print('Not enough halos to assign central galaxies in hosthalosgroups[{},0].'.format(i+1))
				else:
					if t < hostgalsgroupnum:
                                        	hostgalsgroups[i,0][t,0:7]=hosthalosgroups[i+1,0][t,0:7]
                                        	hosthalosgroups[i+1,0][t,0]=-1
		else:
			print('Host galaxy and host halo bin number did not match.')

#Assign new spatial and velocity coords to satellites without central galaxies by finding halos in the appropriate bin that have not already been assigned to a central. New hosthaloID also passed to satellite groups.
ncsatgalsbinnum=len(ncsatgalsgroups)
for i in range (0,ncsatgalsbinnum):
        if i < ncsatgalsbinnum:
		hosthalobinindex=ncsatgalsgroups[i,0][0][0][-1]
		ncsatgalsgroupnum=len(ncsatgalsgroups[i,0])
		for t in range(0,ncsatgalsgroupnum):
			if t < ncsatgalsgroupnum:
				hosthalonum=len(hosthalosgroups[hosthalobinindex,0])
				for j in range(0,hosthalonum):
					if j < hosthalonum:
						if hosthalosgroups[hosthalobinindex,0][j][0]==-1:
							continue
						else:
							haloinfo=hosthalosgroups[hosthalobinindex,0][j][0:7]
							ncsatgalsnum=len(ncsatgalsgroups[i,0][t])
							for k in range(0,ncsatgalsnum):
								if k < ncsatgalsnum:
									ncsatgalsgroups[i,0][t][k][1]=haloinfo[0]
									ncsatgalsgroups[i,0][t][k][2:8]=haloinfo[1:7]+ncsatgalsgroups[i,0][t][k][2:8]
							hosthalosgroups[hosthalobinindex,0][j][0]=-1
							break
				else:
					if j == hosthalonum-1:
						print('Ran through all halos in hosthalosgroups[{},0] without finding a halo that had not already been assigned to a central.'.format(hosthalobinindex)) 

#Assign new spatial and velocity coords to satellites with central galaxies. Central galaxies have been shuffled within mass bins and sat systems in corresponding bins assigned 1 for 1 from start of index. New hosthaloID also passed to satellite groups.
newhostgalsbinnum=len(hostgalsgroups)
for i in range(0, newhostgalsbinnum):
        if i < newhostgalsbinnum:
                np.random.shuffle(hostgalsgroups[i,0])

hostgalsbin=[]
Nhostgalsgroups=len(hostgalsgroups)
for i in range(0,Nhostgalsgroups):
	if i < Nhostgalsgroups:
		hostgalsbin.append(hostgalsgroups[:,0][i][0][-1])	

satgalsbinnum=len(satgalsgroups)
for i in range (0,satgalsbinnum):
        if i < satgalsbinnum:
                hostgalsbinindex=binarySearch(hostgalsbin,satgalsgroups[i,0][0][0][-1])
                satgalsgroupnum=len(satgalsgroups[i,0])
                for t in range(0,satgalsgroupnum):
                        if t < satgalsgroupnum:
				hostgalinfo=hostgalsgroups[hostgalsbinindex,0][t][0:7]
				satgalsnum=len(satgalsgroups[i,0][t])	
				for k in range(0,satgalsnum):
					if k < satgalsnum:
						satgalsgroups[i,0][t][k][1]=hostgalinfo[0]
						satgalsgroups[i,0][t][k][2:8]=hostgalinfo[1:7]+satgalsgroups[i,0][t][k][2:8]
						

#Combine galaxies for output. De-group by system (for sats) and mass bin (for all). Remove bin number column. Add in column of hosthaloID=-1 for central galaxies. 
ncsatgalaxies=[]
Nncbin=len(ncsatgalsgroups)
for i in range(0,Nncbin):
	if i < Nncbin:
		Nncgroups=len(ncsatgalsgroups[i,0])
		for j in range(0,Nncgroups):
			if j < Nncgroups:
				Nncgals=len(ncsatgalsgroups[i,0][j])
				for t in range(0,Nncgals):
					if t < Nncgals:
						ncsatgalaxies.append(ncsatgalsgroups[i,0][j][t])

ncsatnewbind=np.array(ncsatgalaxies)

satgalaxies=[]
Nsbin=len(satgalsgroups)
for i in range(0,Nsbin):
        if i < Nsbin:
                Nsgroups=len(satgalsgroups[i,0])
                for j in range(0,Nsgroups):
                        if j < Nsgroups:
                                Nsgals=len(satgalsgroups[i,0][j])
                                for t in range(0,Nsgals):
                                        if t < Nsgals:
                                                satgalaxies.append(satgalsgroups[i,0][j][t])
satnewbind=np.array(satgalaxies)

centgalaxies=[]
Ncbin=len(hostgalsgroups)
for i in range(0,Ncbin):
        if i < Ncbin:
                Ncgals=len(hostgalsgroups[i,0])
                for j in range(0,Ncgals):
                        if j < Ncgals:
                                centgalaxies.append(hostgalsgroups[i,0][j])

centnewbind=np.insert(np.array(centgalaxies),1,-1,axis=1)

galaxies_bind=np.vstack((centnewbind,satnewbind,ncsatnewbind))

galaxies_bind[:,2][galaxies_bind[:,2]<0]=galaxies_bind[:,2][galaxies_bind[:,2]<0]+250
galaxies_bind[:,3][galaxies_bind[:,3]<0]=galaxies_bind[:,3][galaxies_bind[:,3]<0]+250
galaxies_bind[:,4][galaxies_bind[:,4]<0]=galaxies_bind[:,4][galaxies_bind[:,4]<0]+250
galaxies_bind[:,2][galaxies_bind[:,2]>250]=galaxies_bind[:,2][galaxies_bind[:,2]>250]-250
galaxies_bind[:,3][galaxies_bind[:,3]>250]=galaxies_bind[:,3][galaxies_bind[:,3]>250]-250
galaxies_bind[:,4][galaxies_bind[:,4]>250]=galaxies_bind[:,4][galaxies_bind[:,4]>250]-250

#Prepare for export
galaxies_erasedAB=np.delete(galaxies_bind,-1,1)
galaxies_erasedAB[:,-1]=10**galaxies_erasedAB[:,-1]
mock_galaxy_erasedAB=galaxies_erasedAB[np.argsort(galaxies_erasedAB[:,0])]
erasedABsp=mock_galaxy_erasedAB[:,2:5]
erasedABspvl=mock_galaxy_erasedAB[:,2:8]

#Output erasedAB catalog.
np.savetxt('ErasedAB_cat_1.dat',mock_galaxy_erasedAB, fmt=['%d','%10d','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3e'])

#XYZ cat for xi calc.
np.savetxt('erasedABsp_1.dat',erasedABsp, fmt=['%10.3f','%10.3f','%10.3f'])

#XYZVxVyVz cat for redshift xi calc.
#np.savetxt('erasedABspvl_new11.dat',erasedABspvl, fmt=['%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f'])


print('Program finished at {}.'.format(datetime.now().time()))
quitline=something+something2

#Erased cat iteration test.
#erasedcentbin60=centnewbind[centnewbind[:,-1]==60]
#erasedsatbin60=satnewbind[satnewbind[:,-1]==60]
#erasedncsatbin60=ncsatnewbind[ncsatnewbind[:,-1]==60]
#erasedgalsbin60=np.vstack((erasedcentbin60,erasedsatbin60,erasedncsatbin60))
#erasedgalsbin60=np.delete(erasedgalsbin60[np.argsort(erasedgalsbin60[:,0])],-1,1)

#np.savetxt('erasedgalsbin60_6.dat',erasedgalsbin60,fmt=['%d','%10d','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3f','%10.3e'])

#Comparison of mock vs erased cats.
oldinnew=np.in1d(hostgal[:,0],centnewbind[:,0])
newinold=np.in1d(centnewbind[:,0],hostgal[:,0])
newnotinold=np.invert(newinold)
oldnotinnew=np.invert(oldinnew)

inboth=centnewbind[:,0][newinold]
onlynew=centnewbind[:,0][newnotinold]
onlyold=hostgals[:,0][oldnotinnew]

Nboth=len(inboth)
bothM=[]
bothV=[]
bothsp=[]
for i in range(0,Nboth):
	if i < Nboth:
		bothindex=binarySearch(halo4comps[:,0],inboth[i])
		bothM.append(halo4comps[:,2][bothindex])
		bothV.append(halo4comps[:,1][bothindex])
		bothsp.append(halo4comps[:,3:7][bothindex])

bothM=np.array(bothM)
bothV=np.array(bothV)
bothsp=np.array(bothsp)

Nold=len(onlyold)
oldM=[]
oldV=[]
oldsp=[]
for i in range(0,Nold):
        if i < Nold:
                oldindex=binarySearch(halo4comps[:,0],onlyold[i])
                oldM.append(halo4comps[:,2][oldindex])
                oldV.append(halo4comps[:,1][oldindex])
		oldsp.append(halo4comps[:,3:7][oldindex])

oldM=np.array(oldM)
oldV=np.array(oldV)
oldsp=np.array(oldsp)

Nnew=len(onlynew)
newM=[]
newV=[]
newsp=[]
for i in range(0,Nnew):
        if i < Nnew:
                newindex=binarySearch(halo4comps[:,0],onlynew[i])
                newM.append(halo4comps[:,2][newindex])
                newV.append(halo4comps[:,1][newindex])
		newsp.append(halo4comps[:,3:7][newindex])

newM=np.array(newM)
newV=np.array(newV)
newsp=np.array(newsp)

np.savetxt('erasedAB_comsp_new11.dat',bothsp, fmt=['%10.3f','%10.3f','%10.3f'])
np.savetxt('erasedAB_newsp_new11.dat',newsp, fmt=['%10.3f','%10.3f','%10.3f'])
np.savetxt('erasedAB_oldsp_new11.dat',oldsp, fmt=['%10.3f','%10.3f','%10.3f'])

quitline=something1+something2

erasedgalshist,mockgalsbin_edges=np.histogram(np.hstack((centnewbind[:,-2],satnewbind[:,-2],ncsatnewbind[:,-2])),bins)
mockgalshist,mockgalsbin_edges=np.histogram(np.hstack((hostgal[:,-1],satgal[:,-1],ncsatgal[:,-1])),bins)
erasedgalshist=np.array(erasedgalshist,dtype=float)
mockgalshist=np.array(mockgalshist,dtype=float)

mockcenthist,mockcentbin_edges=np.histogram(hostgal[:,-1],bins)
erasecenthist,erasecentbin_edges=np.histogram(centnewbind[:,-2],bins)
mocksathist,mocksatbin_edges=np.histogram(satgal[:,-1],bins)
erasesathist,satgalbin_edges=np.histogram(satnewbind[:,-2],bins)
mockncsathist,mockncsatbin_edges=np.histogram(ncsatgal[:,-1],bins)
erasencsathist,erasencsatbin_edges=np.histogram(ncsatnewbind[:,-2],bins)
hosthalohist,hosthalobin_edges=np.histogram(hosthalo[:,-1],bins)

massbin_central=hosthalobin_edges+0.035
massbin_central=massbin_central[0:75]

mockcenthist=np.array(mockcenthist,dtype=float)
erasecenthist=np.array(erasecenthist,dtype=float)
mocksathist=np.array(mocksathist,dtype=float)
erasesathist=np.array(erasesathist,dtype=float)
mockncsathist=np.array(mockncsathist,dtype=float)
erasencsathist=np.array(erasencsathist,dtype=float)
hosthalohist=np.array(hosthalohist,dtype=float)

Pmockcenthalo=mockcenthist[0:73]/hosthalohist[0:73]
Perasecenthalo=erasecenthist[0:73]/hosthalohist[0:73]
Pmocksathalo=mocksathist[0:73]/hosthalohist[0:73]
Perasesathalo=erasesathist[0:73]/hosthalohist[0:73]
Pmockncsathalo=mockncsathist[0:73]/hosthalohist[0:73]
Perasencsathalo=erasencsathist[0:73]/hosthalohist[0:73]
Pmockgalshalo=mockgalshist[0:73]/hosthalohist[0:73]
Perasedgalshalo=erasedgalshist[0:73]/hosthalohist[0:73]

bins=np.arange(9.72,14.98,0.07)
halo_bin=np.array([np.digitize(hosthalo[:,-1],bins)]).T
cent_bin=np.array([np.digitize(hostgal[:,-1],bins)]).T
sat_bin=np.array([np.digitize(satgal[:,-1],bins)]).T
ncsat_bin=np.array([np.digitize(ncsatgal[:,-1],bins)]).T

halo_bind=np.concatenate((hosthalo, halo_bin), axis=1)
cent_bind=np.concatenate((hostgal, cent_bin), axis=1)
sat_bind=np.concatenate((satgal, sat_bin), axis=1)
ncsat_bind=np.concatenate((ncsatgal, ncsat_bin), axis=1)

N=len(bins)+1
Nsatspercent=[]
Nsatspercentperbin=[]
for i in range(1,N):
	if i < N:
		Ncentsperbin=len(cent_bind[cent_bind[:,-1]==i])
		for j in range(0,Ncentsperbin):
			if j < Ncentsperbin:
				Nsatspercent.append(len(sat_bind[sat_bind[:,1][sat_bind[:,-1]==i]==cent_bind[:,0][cent_bind[:,-1]==i][j]]))
		Nsatspercent=np.array(Nsatspercent).T
		Nsatspercentperbin.append(Nsatspercent)
		Nsatspercent=[]


Nnewsatspercent=[]
Nnewsatspercentperbin=[]
for i in range(1,N):
        if i < N:
                Ncentsperbin=len(centnewbind[centnewbind[:,-1]==i])
                for j in range(0,Ncentsperbin):
                        if j < Ncentsperbin:
                                Nnewsatspercent.append(len(satnewbind[satnewbind[:,1][satnewbind[:,-1]==i]==centnewbind[:,0][centnewbind[:,-1]==i][j]]))
                Nnewsatspercent=np.array(Nnewsatspercent).T
                Nnewsatspercentperbin.append(Nnewsatspercent)
                Nnewsatspercent=[]


Nsatspercentperbin=np.array(Nsatspercentperbin)
Nnewsatspercentperbin=np.array(Nnewsatspercentperbin)
newsatcount=np.concatenate(Nnewsatspercentperbin)
satcount=np.concatenate(Nsatspercentperbin)

#Original mock output
#galsp=galspvl[:,0:3]
#np.savetxt('mocksp_new.dat',galsp, fmt=['%10.3f','%10.3f','%10.3f'])

#Plots
import matplotlib.pyplot as plt
f, ax1 = plt.subplots(1, sharex=True, sharey=True)
plt.scatter(massbin_central[0:len(Pmockgalshalo)],Pmockgalshalo,s=100, facecolor='red',label='HW13 Mock Cat.')
plt.scatter(massbin_central[0:len(Perasedgalshalo)],Perasedgalshalo,label='Erased Assembly Bias Mock Cat.')
plt.title('Mock vs ErasedAB Galaxy Catalogs', fontsize=18)
plt.xlabel('log(M/M$_\odot$) at bin center (bin width=0.07dex)', fontsize=18)
plt.ylabel('P(galaxy|halo)', fontsize=18)
ax1.tick_params('both', length=10, width=1, which='major')
ax1.tick_params('both', length=5, width=1, which='minor')
plt.yscale('log')
plt.ylim(0.000001,1.6*np.max(Pmockgalshalo))
plt.legend(loc='lower right')
plt.show()

f, ax1 = plt.subplots(1, sharex=True, sharey=True)
plt.scatter(massbin_central[0:len(Pmockcenthalo)],Pmockcenthalo,s=100, facecolor='red',label='HW13 Mock Cat.')
plt.scatter(massbin_central[0:len(Perasecenthalo)],Perasecenthalo,label='Erased Assembly Bias Mock Cat.')
plt.title('Mock vs ErasedAB Galaxy Catalogs', fontsize=18)
plt.xlabel('log(M/M$_\odot$) at bin center (bin width=0.07dex)', fontsize=18)
plt.ylabel('P(cent|halo)', fontsize=18)
ax1.tick_params('both', length=10, width=1, which='major')
ax1.tick_params('both', length=5, width=1, which='minor')
plt.yscale('log')
plt.ylim(0.000001,1.6*np.max(Pmockcenthalo))
plt.legend(loc='lower right')
plt.show()

f, ax1 = plt.subplots(1, sharex=True, sharey=True)
plt.scatter(massbin_central[0:len(Pmocksathalo)],Pmocksathalo,s=100,facecolor='red',label='HW13 Mock Cat.')
plt.scatter(massbin_central[0:len(Perasesathalo)],Perasesathalo, label='Erased Assembly Bias Mock Cat.')
plt.title('Mock vs Erased Galaxy Catalogs', fontsize=18)
plt.xlabel('log(M/M$_\odot$) at bin center (bin width=0.07dex)', fontsize=18)
plt.ylabel('P(sat|halo) w/ $observed$ central galaxy', fontsize=18)
ax1.tick_params('both', length=10, width=1, which='major')
ax1.tick_params('both', length=5, width=1, which='minor')
plt.yscale('log')
plt.ylim(0.000001,1.6*np.max(Pmocksathalo))
plt.legend(loc='upper left')
plt.show()

f, ax1 = plt.subplots(1, sharex=True, sharey=True)
plt.scatter(massbin_central[0:len(Pmockncsathalo)],Pmockncsathalo,s=100,facecolor='red',label='HW13 Mock Cat.')
plt.scatter(massbin_central[0:len(Perasencsathalo)],Perasencsathalo, label='Erased Assembly Bias Mock Cat.')
plt.title('Mock vs Erased Galaxy Catalogs', fontsize=18)
plt.xlabel('log(M/M$_\odot$) at bin center (bin width=0.07dex)', fontsize=18)
plt.ylabel('P(sat|halo) w/o $observed$ central galaxy', fontsize=18)
ax1.tick_params('both', length=10, width=1, which='major')
ax1.tick_params('both', length=5, width=1, which='minor')
plt.yscale('log')
plt.ylim(0.000001,1.6*np.max(Pmockncsathalo))
plt.legend(loc='lower right')
plt.show()

clustbins=np.arange(np.min(Nsatspercentperbin[70]),np.max(Nsatspercentperbin[70]),1)
clusthist,clustbin_edge=np.histogram(Nsatspercentperbin[70],clustbins)
plt.hist(Nsatspercentperbin[70],clustbins,histtype='stepfilled',label='HW13 Mock Cat.')
plt.hist(Nnewsatspercentperbin[70],clustbins, histtype='stepfilled',facecolor='red', alpha=0.5, label='Erased Assembly Bias Mock Cat')
plt.title('Satellite Clustering per Mass Log bin', fontsize=18)
plt.xlabel('# of satellites per central galaxy', fontsize=18)
plt.ylabel('Frequency of clustering', fontsize=18)
plt.xticks(clustbins+.5, (clustbins),rotation='vertical')
#plt.yticks((0,1))
plt.ylim(0,(1.2*np.max(clusthist)))
plt.text(73.5,1.1,'LogM/M$_\odot$ Bin 70\nMass range: 14.62-14.68 dex',fontsize=12,bbox=dict(facecolor='white'))
plt.legend(loc='upper right')
plt.show()

fig,ax1 = plt.subplots(1, sharex=True, sharey=True)
plt.scatter(oldV,oldM,facecolor='w',s=30,edgecolor='r',marker='o',label='Unique to Assembly-Biased Catalog')
plt.scatter(newV,newM,facecolor='w',s=30,edgecolor='g',marker='D',label='Unique to Randomized Catalog')
plt.scatter(bothV,bothM,facecolor='k',s=1,marker='s',label='Common to Both Catalogs')
plt.title('Halos with Central Galaxies', fontsize=18)
plt.xlabel('V$_{max}$ (km/s)', fontsize=18)
plt.ylabel('M$_{vir}$/M$_\odot$', fontsize=18)
ax1.tick_params('both', length=10, width=1, which='major')
ax1.tick_params('both', length=5, width=1, which='minor')
plt.legend(loc='lower right')
plt.xlim(np.min(newV),1.2*np.max(bothV))
plt.xscale('log')
plt.yscale('log')
plt.show()                                               
