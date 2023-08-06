#from polar_router import recv_over_weak_noisy_channel#how it works doesn't matter, u don't need this lib, just ignore it
from Crypto.Util.number import long_to_bytes#really useful! 
from noisemsg import noisemsg

def hamming_correct(bitblock):
    for i in range(16):
        if bitblock[1]^bitblock[3]^bitblock[5]^bitblock[7]^bitblock[9]^bitblock[11]^bitblock[13]^bitblock[15]!=0 or bitblock[2]^bitblock[3]^bitblock[6]^bitblock[7]^bitblock[10]^bitblock[11]^bitblock[14]^bitblock[15]!=0 or bitblock[4]^bitblock[5]^bitblock[6]^bitblock[7]^bitblock[12]^bitblock[13]^bitblock[14]^bitblock[15]!=0 or bitblock[8]^bitblock[9]^bitblock[10]^bitblock[11]^bitblock[12]^bitblock[13]^bitblock[14]^bitblock[15]!=0:
            bitblock[i]=int(not bitblock[i])
            if bitblock[1]^bitblock[3]^bitblock[5]^bitblock[7]^bitblock[9]^bitblock[11]^bitblock[13]^bitblock[15]==0 and bitblock[2]^bitblock[3]^bitblock[6]^bitblock[7]^bitblock[10]^bitblock[11]^bitblock[14]^bitblock[15]==0 and bitblock[4]^bitblock[5]^bitblock[6]^bitblock[7]^bitblock[12]^bitblock[13]^bitblock[14]^bitblock[15]==0 and bitblock[8]^bitblock[9]^bitblock[10]^bitblock[11]^bitblock[12]^bitblock[13]^bitblock[14]^bitblock[15]==0:
                bitblock[i]=int(not bitblock[i])
                #print(i)
                return i
            else:bitblock[i]=int(not bitblock[i])
        #else :print('no')
    return 0
    #you should write this function, to help polar decode the msg
    #Good luck and take it easy!

def decode(msg):
    blocks=len(msg)
    bitlist=[]
    #Let's cancel the noise...
    for i in range(blocks):
        wrongbitpos=hamming_correct(msg[i])
        msg[i][wrongbitpos]=int(not msg[i][wrongbitpos])
        #add corrected bits to a big list
        bitlist.extend([msg[i][3]]+msg[i][5:8]+msg[i][9:16])
    #...then, decode it!
    totallen=len(bitlist)
    bigint=0
    for i in range(totallen):
        bigint<<=1
        bigint+=bitlist[i]
    return long_to_bytes(bigint)

msg=decode(noisemsg)
print(msg)#Well done