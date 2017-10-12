import numpy as np
import matplotlib.pyplot as plt

alpha = 1
beta = 0

top_percentile = []

#Ns = np.logspace(3,5,800) #Ns for finding n* for P > 0.99
Ns = [1e3,1e4,1e5] #Ns for plotting the evolution of the probability, and 
                   # the table
for N in Ns:
    probs = []
    ns = []
    alpha = 1
    beta = 0
    for n in range(1,301):
        new_alpha = (alpha*(1-4/N) - beta*2/np.sqrt(N))
        new_beta = alpha*2/np.sqrt(N) + beta

        alpha = new_alpha
        beta = new_beta

        p = 1-alpha**2*(1-1./N)

        probs.append(p)
        ns.append(n)
        """
        Comment the if-statement before plotting the evolution of the
        probability
        """
        if p >= 0.99:
             top_percentile.append(n)
             break


"""Uncomment for plotting the evolution of the probability"""
#    plt.plot(ns,probs)
#    plt.title("Probability for N ={}".format(N))
#    plt.xlabel("n")
#    plt.ylabel(r"$P(i^*)$")
#    plt.show()


"""Comment all below before using the plot above"""
log_top = np.log(np.array(top_percentile))
log_Ns = np.log(Ns)

print("The speed for looking up i* goes as N to the power of ", \
      np.mean((log_top[:-1] - log_top[1:])/(log_Ns[:-1] - log_Ns[1:])))

""" For making the table"""
for n,N in zip(top_percentile,Ns):
    print("---------")
    print("N = {}, n* = {}".format(N,n))

plt.loglog(Ns,top_percentile)
plt.title("Loglog plot of the evolution of the prbability")
plt.xlabel("log(N)")
plt.ylabel(r"$\log(n*)$")
plt.show()


#plt.plot(Ns,top_percentile)
#plt.title("Evolution of the prbability")
#plt.xlabel("N")
#plt.ylabel(r"$n*$")
#plt.show()
