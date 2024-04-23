#https://arxiv.org/abs/1810.05183
The Effects of Galaxy Assembly Bias on the Inference of Growth Rate from Redshift-Space Distortions
Kevin Spencer McCarthy, Zheng Zheng, and Hong Guo
Accepted MNRAS, Volume 487, Issue 2, August 2019, Pages 2424_2440
----------------------------------------------------------------------------

This project involved the measurement of the linear growth rate (f*sigma_8(s)), as calculated with a correlation-space version of an estimator built by Percival & White (2009), through modeling of the two-point correlation function (2PCF) measurements of galaxy clustering in a universe with a positive galaxy assembly bias (AB) signal (HW13; Hearin & Watson 2013). I modeled HW13 with the halo occupation distribution (HOD; Zheng et al. 2005) and the sub-halo clustering abundance matching (SCAM; Guo et al. 2016) frameworks.

The HOD specifically does not accommodate for galaxy assembly bias. We employed three different halo properties to tie in the galaxy luminosity with SCAM with each accommodate for galaxy assembly bias in different ways. They were: maximum circular velocity of halo at time of accretion (V_acc), halo mass at the time of accretion (M_acc), and peak circular velocity of halo during lifetime (V_peak).

Our goal was to explore the dependence on the need for an occupation model that accounted for AB on the scales of clustering observations, i.e., how much clustering information from observations is useful to constrain linear growth-rate without knowing the specific details of galaxy AB? Since the cosmologically meaningful information arises from an understanding of the Kaiser squashing (Kaiser 1987) of the linear (according to cosmic density perturbation growth mode) velocity-induced galaxy-galaxy signal in redshift-space, and not from the non-linear velocity-induced clustering elongation at small transverse separations (FoG), we core the galaxy pairs at r_p<2.0 h^-1Mpc and extrapolate the multipole 2PCF signals from the truncated measurements. With our HOD and SCAM model fits to the projected correlation function (w_p) and the linear non-zero multipoles (monopole, xi_0; quadrupole, xi_2; hexadecapole, xi_4), we predict the estimator of fsig_8 into the quasi- to non-linear regimes (s<30 h^-1Mpc) and compare to the actual growth-rate curve of the simulated universe. We also consider the differences if we model the 2PCF for central and satellites galaxies or if we only 'observe' the centrals galaxies (central galaxies though to have the strongest cosmological signal).

I find that when considering the signal from both central and satellite galaxies, only the true galaxy-halo connection (V_peak for HW13) is able to reproduce the growth-rate curve down to scales lower than s=15 h^-1Mpc (for M_r <-20.0). If we only consider the central galaxies, we can ignore the need to accommodate for galaxy AB down to separations of s=7-8 h^-1Mpc. 

Measurements of the linear growth-rate (fsig_8(z)) are complementary to that of the Hubble expansion rate (H(z)) when constraining cosmological models. Specifically, in an effort to provide precision-level errors on the value of the Dark Energy equation-of-state parameter (w), with a w!=-1.0 pointing towards a non-constant form of dark energy- a departure from lambdaCDM. Present uncertainty associated with fsig_8 arise mostly from lack of statistical power present on linear-scales (s>=30 h^-1Mpc) where the likelihood is calculated analytically. Extracting cosmological information from smaller-scales provides a substantial boost in statistical constraining power. The details of galaxy formation physics, however, leave many assumptions about how galaxies connect with their formation sites unconfirmed. Our research shows that if we can successfully differentiate central from satellites galaxies, we do not need to invent new halo occupation techniques to utilize galaxy clustering above separations of s~7-8 h^-1Mpc.

** The redshift-space galaxy-galaxy clustering signal from the SDSS DR7 differs from that 'observed' in this study. Therefore, to place this study on more empirical grounds, we must explore further the galaxy assembly bias signal of the actual universe. This is reserved for future studies.


CODE FILES
-----------------------------------------------------------
Fileprep_Galaxies
- eraseABnew.py (erases 2-halo AB signal)
- sft_draw.py (mock galaxy catalog manipulation; including placing galaxies into redshift-space) 

Clustering_Measurements
- mltpole_full.py (calculated monopole,quadrupole, and hexadecapole from xi(s,u) measurment)
- mltpole_cut.py (calculated truncated multipoles from xi(s,u), removing pairs from small-scale seps, and extrapolating to modified multipole)
- covar.py (measures the covariance matrix of the multipole measurements from jackknife subsampling)
- estimator.py (calculated the growth-rate curve from fsig_8 estimator)

Plots
- fig1.py (for 2PCF in linear rp,r_pi 2D space)
- fig2.py (for 2PCF (wp,xi_0,xi_2,xi_4) measurement as function of rp or s)
- fig3.py (for fsig_8 estimator)
- fig5.py (for chi^2 and n_g values from HOD/SCAM fits)
 


