# encode: utf8
import sys

class Optimum(object):
    def __init__(self, **argv):
        self.z_opt = argv.get("z_opt")
        self.x_opt = argv.get("x_opt")
        self.lmbd_opt = argv.get("lmbd_opt")
        self.basis = argv.get("basis")
        self.x_basis = argv.get("x_basis")
        self.lu_basis = argv.get("lu_basis") 
        self.num_col = len(self.x_opt) if self.x_opt is not None else 0
        self.num_row = len(self.basis) if self.basis is not None else 0

    def __str__(self):
        return "\nOptimum\t%s\nx_opt\t%s\nbasis\t%s\n" % (self.z_opt, str(self.x_opt), str(self.basis))
