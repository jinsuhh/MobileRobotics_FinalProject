import numpy as np
m1, m2=np.load("array2_demo.npy"), np.load("array3_demo.npy")
eps=0.0001
alpha=0.8

# Shape m2 as m1: m1=T(m2)
# grid=np.zeros((m1.shape[0], m1.shape[1]))

# Prepare m1 into sparse
arr=np.array(np.where(m1==100)).T
arr=np.flip(arr, axis=1)
arr=np.concatenate((arr, np.ones((arr.shape[0], 1))), axis=1).astype('int32')   # Note: This is x,y,1

# Prepare m2 into sparse
brr=np.array(np.where(m2==100)).T
brr=np.flip(brr, axis=1)
brr=np.concatenate((brr, np.ones((brr.shape[0], 1))), axis=1).astype('int32')   # Note: This is x,y,1

def form_t(theta, tx, ty):
    return np.array([[np.cos(theta), -np.sin(theta), tx], 
                     [np.sin(theta), np.cos(theta), ty], 
                     [0, 0, 1]])

def match1(A, B): # How many elements of a are also in b
    ans=np.array([x for x in set(tuple(x) for x in A[:, :2]) & set(tuple(x) for x in B[:, :2])])
    return ans.shape[0]/(np.sqrt(A.shape[0]+eps)*np.sqrt(B.shape[0]+eps))

# # Define the function to calculate delta
def delta(m1, m2, t):
    transformed=np.matrix.round(np.matmul(t, m2.T).T)
    return match1(m1, transformed)

# Define the function to update s and mu
def update(t, prev_t, prev_s):
    # Exponentially Weighted Moving Average
    alpha= 2/(M+1)
    new_mu = alpha * t + (1-alpha) * np.mean(prev_t)

    # Exponentially Weighted Moving Standard Deviation
    # print((t - new_mu).shape)
    try:
        new_s = np.sqrt(np.abs(alpha * np.outer((t - new_mu), (t - new_mu)) + (1-alpha) * np.matmul(prev_s, prev_s)))
    except:
        new_s=prev_s
    print("mu", new_mu, "sigma", new_s)
    return new_s, new_mu

# Define variables
numSteps = 10  
sstart = np.array([0, 10, 10])   
sinit = np.array([[1, 0, 0], [0, 5, 0], [0, 0, 5]])     
muinit = np.array([0, 0, 0])  # theta, x, y     
M = 2      

# Initialize variables
k = 0
tk = sstart
sk = sinit
muk = muinit
Tstart=form_t(sstart[0], sstart[1], sstart[2])
ck = delta(arr, brr, Tstart)
prev_t_list=[]

# Loop until k reaches numSteps
while k < numSteps:
    # Generate a new sample
    # print(muk, sk)
    try:
        s = tk + np.random.multivariate_normal(muk, sk, size=1).squeeze()  # replace vk with your desired sample generation code
    except:
        s=tk
    # print(tk, s)
    # Calculate cs and check conditions
    cs = delta(arr, brr,  form_t(s[0], s[1], s[2]))
    # print(s, cs, ck)
    if cs > ck: # or np.random.uniform()>0.95:
        # Update variables and counters
        k += 1
        tk = s
        ck = cs

        # Update s and mu
        tk_list = [tk] + prev_t_list
        sk, muk = update(tk, tk_list[:M], sk)
        print(cs, tk)
    else:
        # Discard the sample
        pass
