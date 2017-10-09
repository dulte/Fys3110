import numpy as np
import matplotlib.pyplot as plt

def get_alpha(beta,N):
    return -(np.sqrt(N*(N-beta**2*(N-1))) + b*np.sqrt(N))/(N)


alpha = 1
beta = 0

top_percentile = []

Ns = np.logspace(3,5,800)
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
        if p >= 0.999:
             top_percentile.append(n)
             break



    # plt.plot(ns,probs)
    # plt.title("For N ={}".format(N))
    # plt.show()

log_top = np.log(np.array(top_percentile))
log_Ns = np.log(Ns)

print(np.mean((log_top[:-1] - log_top[1:])/(log_Ns[:-1] - log_Ns[1:])))

plt.loglog(Ns,top_percentile)
plt.show()
