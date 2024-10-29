# import Python modules
import math # math module
import sys # argv
# initialize script arguments
c_in = float('nan')    
h_in = float('nan')        
w_in = float('nan')
n_filt = float('nan')
h_filt = float('nan')
w_filt = float('nan')    
s = float('nan')        
p = float('nan')
if len(sys.argv) == 9:
    c_in = sys.argv[1]    
    h_in = sys.argv[2]        
    w_in = sys.argv[3]
    n_filt = sys.argv[4]
    h_filt = sys.argv[5]
    w_filt = sys.argv[6]    
    s = sys.argv[7]        
    p = sys.argv[8]
else:
    print('Usage: python3 Conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p')
    exit()
c_out = 0
h_out = ((h_in+2*p-h_filt)/s + 1)
w_out = ((w_in+2*p-w_filt)/s + 1)
adds = n_filt*h_out*w_out*c_in*h_filt*w_filt
muls = n_filt*h_out*w_out*c_in*h_filt*w_filt
divs = 0
print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed