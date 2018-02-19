# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

f = open('hmx-data.txt','r').readlines()[2:]

# rip the temperatures from every other line
# len(temperatures) == 34
temperatures  		= [ line.split()[0] for line in f ][::2]

# v+ for the two sites, axial is higher in frequency
vplus_axial    		= [ line.split()[1] for line in f ][0::2]
vplus_equitorial    	= [ line.split()[1] for line in f ][1::2]

# v- for the two sites respectively
vminus_axial  		= [ line.split()[2] for line in f ][0::2]
vminus_equitorial    	= [ line.split()[2] for line in f ][1::2]

# asymmetry parameter for the two sites
eta_axial      		= [ line.split()[3] for line in f ][0::2]
eta_equitorial       	= [ line.split()[3] for line in f ][1::2]

# coupling constants for the two sites
cq_axial       		= [ line.split()[4] for line in f ][0::2]
cq_equitorial        	= [ line.split()[4] for line in f ][1::2]


# GIPAW values here??
#gipawtemps            = [ 123,    173,    198,    223,    248,    273,    293,    303   ]
gipawtemps            = [ 123,    173,    198,    223,        273,    293,      ]
#ecut100
#gipaw_cq_axial        = [ 6218.1, 6213.4, 6222.4, 6225.1, 0.000, 6237.6, 6233.2, 0.0000 ] # NEED THESE
#gipaw_cq_equitorial   = [ 6076.9, 6081.4, 6083.6, 6095.1, 0.000, 6088.1, 6104.2, 0.0000 ] # NEED THESE

gipaw_cq_axial        = [ 6218.1, 6213.4, 6222.4, 6225.1,  6237.6, 6233.2  ] # NEED THESE
gipaw_cq_equitorial   = [ 6076.9, 6081.4, 6083.6, 6095.1,  6088.1, 6104.2  ] # NEED THESE

#gipaw_eta_axial       = [.51103, .50995, .50811, .5076,   .50852,  .50189, .50603, 0.00   ]
#gipaw_eta_equitorial  = [.47346, .47237, .47316, .47615,  .47132,  .47091, .46757, 0.00   ]


gipaw_eta_axial       = [.51103, .50995, .50811, .5076,   .50189, .50603   ]
gipaw_eta_equitorial  = [.47346, .47237, .47316, .47615,  .47091, .46757   ]


#gipaw_vplus_axial     = [5457.9, 5452.2, 5457.2, 5458.8,  0.00,  5460.8, 5463.5, 0.00   ] 
#gipaw_vplus_equitorial= [5276.9, 5279.2, 5282.3, 5290.0,  0.00,  5282.8, 5291.7, 0.00   ]

gipaw_vplus_axial     = [5457.9, 5452.2, 5457.2, 5458.8,   5460.8, 5463.5  ] 
gipaw_vplus_equitorial= [5276.9, 5279.2, 5282.3, 5290.0,   5282.8, 5291.7   ]

def main():
  
  #beta = unichr(0x3b2).encode('utf-8')
  beta = 'beta'
  title = "Calculated and exptl. asymmetry parameter \nfor 14N sites in beta-HMX \n vs Temperature at 1 atm\n"
  plt.scatter(temperatures, eta_axial,      marker='^', color='b', s=46, label='expt\'l eta, axial sites')
  plt.scatter(temperatures, eta_equitorial, marker='<', color='k', s=46, label='expt\'l eta, equitorial sites')
  plt.scatter(gipawtemps, gipaw_eta_axial,     marker="s", color='g', s=46, label='GIPAW eta, axial sites') 
  plt.scatter(gipawtemps, gipaw_eta_equitorial,     marker="o", color='r', s=46, label='GIPAW eta, equitorial sites') 

  plt.title(title)
  plt.xlabel("T (K)")
  plt.ylabel("KHz")
  plt.legend(loc=3)
  plt.show()

if __name__ == '__main__':
  main()

