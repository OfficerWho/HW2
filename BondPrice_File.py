
import numpy as np 

def getBondPrice(y,face,couponRate,m,ppy=1):
    cf = np.repeat(face*couponRate/ppy,m*ppy)
    cf[m*ppy-1] = cf[m*ppy-1] + face
    t = np.array(range(1,m*ppy+1))
    pv = np.array((1+y/ppy)**(-t))
    pvcfsum = np.sum(pv * cf)
    return(pvcfsum)

