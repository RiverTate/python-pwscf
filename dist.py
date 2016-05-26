#!/usr/bin/env python3

import sys

class Dist(object):

  def __init__(self, infile):
    self.infile = infile
    self.file_array = open(infile, 'r').readlines()
    
    
  def __repr__(self):
    return "<infile:{}  length:{} lines>".format(self.infile, len(self.file_array))

  def __str__(self):
    s = ""
    for line in self.file_array:
      s += line
    return s

  def prnt(self):
    for line in self.file_array:
      sys.stdout.write(line)

  def get_species(self, symbol=None):
    relevant_lines = []
    species_dict = dict()
    for line in self.get_bond_lines():
      atom_id_1 = line[0]
      atom_id_2 = line[1]    
      species_1 = line[2].split('-')[0]
      species_2 = line[2].split('-')[1]
      species_dict[int(atom_id_1)] = species_1
      species_dict[int(atom_id_2)] = species_2
    if symbol is not None:
      if not type(symbol) == str:
        raise TypeError("get_species takes an optional parameter of type str.")
      return [ species_dict[k] for k in species_dict.keys() if species_dict[k] == atom ]
    else:
      return species_dict

  def get_bond_length_lines(self):
    relevant_lines = []
    bondlen_dict = dict()
    for line in self.file_array:
      if line.endswith(' A  \n') or line.endswith(' A *\n'):
        relevant_lines.append(line)
    return relevant_lines

  def get_bond_lines(self, atom=None):
    return [ line.split() for line in self.file_array if ( line.endswith(' A  \n') or line.endswith(' A *\n') ) ]


  def get_neighbors(self):
    neighbors = []
    atom_lines = [ line for line in self.file_array if 'neighbors' in line ][1:]
    for line in atom_lines:
      nearest = line.split()[7:11]
      neighbors.append(nearest)
    return neighbors

  def get_angles(self):
    angles = []
    angle_lines = [ line for line in self.file_array if 'angles' in line]
    for line in angle_lines:
      angles.append(line.split()[5:11])
    return angles

def main():
  mydist = Dist('dist.out')
  bonds = mydist.get_bondlens()
  angles = mydist.get_angles()
#  species = mydist.get_species()
  neighbors = mydist.get_neighbors()
  print(bonds, angles, neighbors)


if __name__ == '__main__':
  main()
