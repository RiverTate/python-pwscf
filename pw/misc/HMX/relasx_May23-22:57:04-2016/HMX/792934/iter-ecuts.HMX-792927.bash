#!/bin/bash
#
#
# Copyright (c) 2016 altoidnerd                                                 
#################################################################################
#                      								#
# Permission is hereby granted, free of charge, to any person obtaining a 	#
# copy of this software and associated documentation files (the "Software"),	#
# to deal in the Software without restriction, including without limitation 	#
# the rights to use, copy, modify, merge, publish, distribute, sublicense, 	#
# and/or sell copies of the Software, and to permit persons to whom the 	#
# Software is furnished to do so, subject to the following conditions:		#
#										#
# The above copyright notice and this permission notice shall be included 	#
# in all copies or substantial portions of the Software.			#
#										#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 	#
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 	#
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL 	#
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 	#
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,	#
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE	#
# THE SOFTWARE.									#
#################################################################################
#
#
#
# run from directory where this script is
# cd `echo $0 | sed 's/\(.*\)\/.*/\1/'` # extract pathname
#
#


example_dir=`pwd`

# check whether echo has the -e option
e="echo -e"

$e
$e "$example_dir : starting"
$e

$e  
$e "...setting the needed environment variables..."
$e

#. ./environment_variables

$e "done."
$e

# required executables and pseudopotentials
bin_list="pw.x"
structure="HMX"

hmxprefix="792829"

pseudo_dir="$HOME/.data/PSEUDOPOTENTIALS"
tmp_dir="./scratch"
bin_dir="$HOME/espresso-5.3.0/bin"
np=32

$e
$e "  executables directory: $bin_dir"
$e "  pseudo directory:      $pseudo_dir"
$e "  temporary directory:   $tmp_dir"
$e "  checking that needed directories and files exist..."
$e
$e " OK"
$e

for ecut in 60 100 140 180 220 260 300; do
    cat > scf.pbe.kp444.ec-$ecut.hmx-$hmxprefix.in << EOF
    &CONTROL 
calculation ='scf'
title='$structure-scf-pbe-n-kjpaw-kp242-ec-$ecut-nofor-nostress-conv-em4'
prefix='scf.pbe-ec-$ecut-kp444.HMX-$hmxprefix-nofor.nostress'
pseudo_dir = '$HOME/.data/PSEUDOPOTENTIALS'
outdir='$tmp_dir'
verbosity='high'
!tstress=.true.
!tprnfor = .true.
!forc_conv_thr=1.0d-4
nstep=200
/
    &SYSTEM 
ibrav=0
celldm(1)=1.889726
nat=56
ntyp=4 
ecutwfc=$ecut
ecutrho=${ecut}0
/ 
    &ELECTRONS
mixing_beta=0.7
!conv_thr =  1.0d-4
electron_maxstep=200
/
   &IONS
trust_radius_max=0.2
/
    &CELL
cell_dynamics='bfgs'
/


ATOMIC_SPECIES
  N  14.0067  N.pbe-n-kjpaw_psl.1.0.0.UPF
  C  12.0110  C.pbe-n-kjpaw_psl.1.0.0.UPF
  H   1.0079  H.pbe-kjpaw_psl.1.0.0.UPF
  O  15.9994  O.pbe-n-kjpaw_psl.1.0.0.UPF

CELL_PARAMETERS (alat) 
   6.5250000000    0.0000000000    0.0000000000
   0.0000000000   10.8400000000    0.0000000000
  -1.5559110639    0.0000000000    7.1534459704

ATOMIC_POSITIONS (crystal)
 N       0.981310000     0.623630000     0.459130000
 O       1.273560000     0.720740000     0.434110000
 N       1.141250000     0.704130000     0.529090000
 N       0.856670000     0.527080000     0.707410000
 O       0.724030000     0.429320000     0.924200000
 N       0.695090000     0.502840000     0.793730000
 O       1.142250000     0.749330000     0.682450000
 C       0.807880000     0.616980000     0.551870000
 H       0.679600000     0.591000000     0.461800000
 H       0.782000000     0.699300000     0.601100000
 O       0.531790000     0.561810000     0.736400000
 C       0.978090000     0.564930000     0.279260000
 H       0.841800000     0.526100000     0.240400000
 H       0.994800000     0.623900000     0.183900000
 H       0.494800000    -0.123900000    -0.316100000
 H       0.341800000    -0.026100000    -0.259600000
 C       0.478090000    -0.064930000    -0.220740000
 O       0.031790000    -0.061810000     0.236400000
 H       0.282000000    -0.199300000     0.101100000
 H       0.179600000    -0.091000000    -0.038200000
 C       0.307880000    -0.116980000     0.051870000
 O       0.642250000    -0.249330000     0.182450000
 N       0.195090000    -0.002840000     0.293730000
 O       0.224030000     0.070680000     0.424200000
 N       0.356670000    -0.027080000     0.207410000
 N       0.641250000    -0.204130000     0.029090000
 O       0.773560000    -0.220740000    -0.065890000
 N       0.481310000    -0.123630000    -0.040870000
 H       1.005200000     0.376100000     0.816100000
 H       1.158200000     0.473900000     0.759600000
 C       1.021910000     0.435070000     0.720740000
 O       1.468210000     0.438190000     0.263600000
 H       1.218000000     0.300700000     0.398900000
 H       1.320400000     0.409000000     0.538200000
 C       1.192120000     0.383020000     0.448130000
 O       0.857750000     0.250670000     0.317550000
 N       1.304910000     0.497160000     0.206270000
 O       1.275970000     0.570680000     0.075800000
 N       1.143330000     0.472920000     0.292590000
 N       0.858750000     0.295870000     0.470910000
 O       0.726440000     0.279260000     0.565890000
 N       1.018690000     0.376370000     0.540870000
 H       0.505200000     0.123900000     0.316100000
 H       0.658200000     0.026100000     0.259600000
 C       0.521910000     0.064930000     0.220740000
 O       0.968210000     0.061810000    -0.236400000
 H       0.718000000     0.199300000    -0.101100000
 H       0.820400000     0.091000000     0.038200000
 C       0.692120000     0.116980000    -0.051870000
 O       0.357750000     0.249330000    -0.182450000
 N       0.804910000     0.002840000    -0.293730000
 O       0.775970000    -0.070680000    -0.424200000
 N       0.643330000     0.027080000    -0.207410000
 N       0.358750000     0.204130000    -0.029090000
 O       0.226440000     0.220740000     0.065890000
 N       0.518690000     0.123630000     0.040870000
K_POINTS {automatic}
 4 4 4  1 1 1 

EOF
    $e " " >> debug.log
    $e "############SCF LOG ENTRY############" >> debug.log 
    $e "$0 by $(whoami) running on $HOSTNAME " >> debug.log
    $e "$(date +%b%d-%T-%Y)" >> debug.log
    $e "$structure $hmxprefix" >>debug.log
    $e " ...running pw.x on $np cores ... ecut = $ecut" >> debug.log
    $e " " >> debug.log

    mpirun -n $np nice -n 19 pw.x < scf.pbe.kp444.ec-$ecut.hmx-$hmxprefix.in > scf.pbe.kp444.ec-$ecut.hmx-$hmxprefix.out

done