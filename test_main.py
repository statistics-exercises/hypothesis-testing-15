import unittest
import inspect
from main import *

class UnitTests(unittest.TestCase) :
    def test_pvalue(self) : 
        delx = 8 / 20
        for i in range(20) : 
        x = -4 + i*delx
        px = scipy.stats.norm.cdf(x)
        self.assertTrue( np.abs(pvalue(x) - px)<1e-7, "the pvalue function is not working" )
