#!/usr/bin/env python3

from get_thetas import *
from nqr_parser6 import f32
import os
import matplotlib.pyplot as plt



def get_all_thetas(range_like):
  """
  get_all_thetas(range_like) -> np.array(
	[ 
	list, 
	list, 
	list, 
	list ]
	)
	==
				np.array(
	[ 
	THETA_X, 
	THETA_Y, 
	THETA_X_SQ,
	THETA_Y_SQ
	]
  
  Pass the function "range_like", a range object
  to specify the indices of input files of 
  format scfs/efg.{}.out.
  
  """
  
  _THETA_X = []
  _THETA_Y = []

  for i in range_like:
    infile = 'scfs/efg.{}.out'.format(i)

    try:
      _THETA_X.append(get_angles(infile)[0])
    except FileNotFoundError:
      pass
    except IndexError:
      pass
     

    try:
      _THETA_Y.append(get_angles(infile)[1])
    except FileNotFoundError:
      pass
    except IndexError:
      pass

  _THETA_X_SQ = [ k**2 for k in _THETA_X ]
  _THETA_Y_SQ = [ k**2 for k in _THETA_Y ]
  return np.array([ _THETA_X, _THETA_Y, _THETA_X_SQ, _THETA_Y_SQ])


def get_primed(cq0=None,et0=None):
  
  Cq0  = 69.2296
  eta0 = 0.09844

  ################################
  # if optional args are passed, #
  # reassign Cq0, eta0           #
  ################################
  if cq0 is not None:
    if et0 is not None:
      Cq0, eta0 = cq0, et0


  thetas = get_all_thetas(range(0,3000,5))
  THETA_X,THETA_Y,THETA_X_SQ,THETA_Y_SQ = thetas[0],thetas[1],thetas[2],thetas[3]
  

  lex = len(THETA_X)
  ley = len(THETA_Y)
  avgx = np.mean(THETA_X)
  avgy = np.mean(THETA_Y)
  avgx_sq = np.mean(THETA_X_SQ)
  avgy_sq = np.mean(THETA_Y_SQ)
  # define the sum and difference of the average of the square 
  # of the angles
  anglesum = avgx_sq + avgy_sq
  anglediff= avgx_sq - avgy_sq


  #
  # cq_coefficient  is the factor by which Cq  
  # is multiplied to obtain Cq';
  #
  # eta_coefficient is the factor by which eta 
  # is multiplied to obtain eta';
  #  
  
  
  cq_coefficient	= 1 - 3/2*anglesum - 1/2*eta0*anglediff + 1/2*( 3-eta0 )*avgx_sq*avgy_sq
  Cqprime 		= cq_coefficient * Cq0
  

  etaprime 	= Cq0/Cqprime*( eta0 - 3/2*anglediff - 1/2*eta0*anglesum + 1/2*( 3-eta0 )*avgx_sq*avgy_sq ) 

  fq0 = f32(Cq0,eta0)
  fqprime = f32(Cqprime,etaprime)

  return {      
		"Cq0":		Cq0, 
		"Cqprime":	Cqprime, 
		"Cq": 		Cqprime,
		"eta0":		eta0, 
		"etaprime":	etaprime, 
		"eta": 		etaprime,
		"fq0":		fq0, 
		"fqprime":	fqprime,
		"thetax":	avgx,
		"thetay":	avgy,
		"thetaxsq":	avgx_sq,
		"thetaysq":	avgy_sq,
		"thetax2":	avgx_sq,
		"thetay2":	avgy_sq,
		"anglediff":	anglediff,
		"anglesum":	anglesum,
		"cq_coef":	cq_coefficient,
		"eta_coef":	etaprime/eta0

	}



def main():
  thetas = get_all_thetas(range(0,3000))
  THETA_X,THETA_Y,THETA_X_SQ,THETA_Y_SQ = thetas[0],thetas[1],thetas[2],thetas[3]
  

  lex = len(THETA_X)
  ley = len(THETA_Y)
  avgx = np.mean(THETA_X)
  avgy = np.mean(THETA_Y)
  avgx_sq = np.mean(THETA_X_SQ)
  avgy_sq = np.mean(THETA_Y_SQ)
  # define the sum and difference of the average of the square 
  # of the angles
  anglesum = avgx_sq + avgy_sq
  anglediff= avgx_sq - avgy_sq


  Cq0  = 69.2296
  eta0 = 0.09844

  #
  # cq_coefficient  is the factor by which Cq  
  # is multiplied to obtain Cq';
  #
  # eta_coefficient is the factor by which eta 
  # is multiplied to obtain eta';
  #  
  
  
  cq_coefficient	= 1 - 3/2*anglesum - 1/2*eta0*anglediff + 1/2*( 3-eta0 )*avgx_sq*avgy_sq
  Cqprime 		= cq_coefficient * Cq0
  

  etaprime 	= Cq0/Cqprime*( eta0 - 3/2*anglediff - 1/2*eta0*anglesum + 1/2*( 3-eta0 )*avgx_sq*avgy_sq ) 
  eta_coefficient = etaprime/eta0

  fq0 = f32(Cq0,eta0)
  fqprime = f32(Cqprime,etaprime)
  fq_coefficient = fqprime/fq0

  print(anglediff, anglesum)

  print("""
        
        len(THETA_X)	:      {}
        len(THETA_Y)	:      {}
        <theta_x>   	:      {}
        <theta_y>   	:      {}
        <theta_x^2> 	:      {}
        <theta_y^2> 	:      {}
        cq_coefficient 	:      {}
        eta_coefficient :      {} 
	Cq0         	:      {}
        Cqprime     	:      {}
	eta0		:      {}
	etaprime	:      {}
        fq0         	:      {}
        fqprime     	:      {}
	fq_coefficient	:      {}
        
        """.format(
			lex,
			ley, 
			avgx, 
			avgy,  
			avgx_sq, 
			avgy_sq, 
			cq_coefficient, 
			eta_coefficient, 
			Cq0, 
			Cqprime,
			eta0, 
			etaprime, 
			fq0, 
			fqprime,
			fq_coefficient)
        )

#### SCATTER PLOT ####
#
#
  plt.scatter(range(ley), THETA_Y, color='g', label='theta_y', marker=',',s=2 )
  plt.scatter(range(lex), THETA_X , color='r', label='theta_x', marker='.',s=4 )
#
####
#### LINE PLOT
#
#
#  plt.plot(range(ley), THETA_Y, color='g', label='theta_y' )
#  plt.plot(range(lex), THETA_X , color='r', label='theta_x')
#
####

  
  plt.title('Angular displacements of Cl1 computed from EFG principal axes')
  plt.ylabel("radians ")
  plt.xlabel("MD step")
        
  

  plt.legend(loc=2)

  
  width_inches=20
  height_inches=8
  aspect=width_inches/height_inches
 
  fig = plt.gcf()
  fig.set_size_inches(20,8, forward=True)
  fig.savefig("thetas.{:.3f}.pdf".format(aspect))


  plt.show()




if __name__ == '__main__':
  main()


