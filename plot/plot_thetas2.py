#!/usr/bin/env python3

from get_thetas import *
from nqr_parser5 import f32
import os
import matplotlib.pyplot as plt



def get_all_thetas():
  _THETA_X = []
  _THETA_Y = []

  for i in range(2500):
    infile = 'scfs/efg.{}.out'.format(i)

    try:
      _THETA_X.append(get_angles(infile)[0])
    except IndexError:
      pass
  

    try:
      _THETA_Y.append(get_angles(infile)[1])
    except IndexError:
      pass

  _THETA_X_SQ = [ k**2 for k in _THETA_X ]
  _THETA_Y_SQ = [ k**2 for k in _THETA_Y ]
  return np.array([ _THETA_X, _THETA_Y, _THETA_X_SQ, _THETA_Y_SQ])





def main():
  thetas = get_all_thetas()
  THETA_X,THETA_Y,THETA_X_SQ,THETA_Y_SQ = thetas[0],thetas[1],thetas[2],thetas[3]
  

  lex = len(THETA_X)
  ley = len(THETA_Y)
  avgx = np.mean(THETA_X)
  avgy = np.mean(THETA_Y)
  avgx_sq = np.mean(THETA_X_SQ)
  avgy_sq = np.mean(THETA_Y_SQ)

  Cq0  = 69.2296
  eta0 = 0.09844

  coefficient = 1 - 3/2*(avgx_sq + avgy_sq) - eta0/2*(avgx_sq - avgy_sq)

  Cqprime = coefficient * Cq0

  fq0 = f32(Cq0,eta0)
  fqprime = f32(Cqprime,eta0)


  print("""
        
        len(THETA_X):      {}
        len(THETA_Y):      {}
        <theta_x>   :      {}
        <theta_y>   :      {}
        <theta_x^2> :      {}
        <theta_y^2> :      {}
        coefficient :      {}
        Cq0         :      {}
        Cqprime     :      {}
        fq0         :      {}
        fqprime     :      {}
        
        """.format(lex,ley, avgx, avgy,  avgx_sq, avgy_sq, coefficient, Cq0, Cqprime, fq0, fqprime)
        )

#### SCATTER PLOT ####
#
#
#  plt.scatter(range(ley), THETA_Y, color='g', label='theta_y', marker=',',s=10 )
#  plt.scatter(range(lex), THETA_X , color='r', label='theta_x', marker='.',s=15 )
#
####
#### LINE PLOT
#
#
  plt.plot(range(ley), THETA_Y, color='g', label='theta_y' )
  plt.plot(range(lex), THETA_X , color='r', label='theta_x')
#
####

  
  plt.title('theta_x, theta_y')
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


