import numpy

def wycen(self,rocznik,przebieg):
        cenaStartowa = 100000
        cenaKoncowa=cenaStartowa-((2018-rocznik)*100)-(przebieg*0.05)
        return cenaKoncowa