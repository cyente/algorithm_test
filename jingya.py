import numpy as np


def normPdf(x,mu,sigma):
    return (1./np.sqrt(2*np.pi))*(np.exp(-(x-mu)**2/(2*sigma**2)))


#K, N, M
#K_init
#dataarray



def em(dataArray,k,mu,sigma,step):
    #
    n = len(k)
    #
    dataNum = len(dataArray)
    #
    gamaArray = np.zeros((n,dataNum))
    for s in range(step):
        for i in range(n):
            for j in range(dataNum):
                Sum = sum([k[t]*normPdf(dataArray[j],mu[t],sigma[t]) for t in range(n)])
                gamaArray[i][j] = k[i]*normPdf(dataArray[j],mu[i],sigma[i])/float(Sum)
        #
        for i in range(n):
            mu[i] = np.sum(gamaArray[i]*dataArray)/np.sum(gamaArray[i])
        #
        for i in range(n):
            sigma[i] = np.sqrt(np.sum(gamaArray[i]*(dataArray - mu[i])**2)/np.sum(gamaArray[i]))
        #
        for i in range(n):
            k[i] = np.sum(gamaArray[i])/dataNum

    return [k,mu,sigma]





if __name__ == '__main__':
    #k = [0.5,0.3,0.2]
    #mu = [0.5,5.5,7]
    #sigma = [1,2,6]
    #
    dataNum = 20
    dataArray = [0.82, 0.22, -0.03, -1.00, -0.97, 5.81, -1.50, 0.46, 4.52, 6.32, 19.44, 0.59, -10.05, -0.09, 3.49, 1.68, -1.88, 1.31, 7.75, 2.02]
    k0 = [0.5,0.3,0.2]
    mu0 = [0.5,5.5,7]
    sigma0 = [1,2,6]
    step = 3
    k1,mu1,sigma1 = em(dataArray,k0,mu0,sigma0,step)
    print("k1:",k1)
    print("mu1:",mu1)
    print("sigma1:",sigma1)