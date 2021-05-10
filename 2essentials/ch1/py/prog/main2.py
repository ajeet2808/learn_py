from sys import path
path.append('../packages') #packages folder added in path

import extra.iota
extra.iota.funI()

from extra import iota
iota.funI()

from extra.iota import funI
funI()

from extra.good.best import sigma
sigma.funS()

from extra.good.best import tau
tau.funT()

from extra.good import alpha
alpha.funA()