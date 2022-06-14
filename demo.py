from all_functions import *


##################################### Testing functions ####################################

# generate a random (n,r,w)-QC-MDPC matrix H
#text = open('demo.txt', 'r').readlines()
text = open('ldpc_reg6.txt', 'r').readlines()
lines = []
for line in text:
    lines.append(line.split())

for i in lines:
    for ind, j in enumerate(i):
        i[ind] = int(j)

H = np.array(lines)

##################################### Setting parameters ###################################

# code parameters
n0 = 2
r = len(lines)
#r = 5
wi = 3

N = 20
k = r // 2
#decryption parameters
t = 11

n = n0 * r
w = wi * n0

H = genQCMDPC(n, r, w)
print(H)

# Generate the corresponding generator matrix G
G = genGenQCMDPC(H)
#print("G:\n", G)
# generate a random message m of weight k
m = genRandomVector(r, k)

print("\nPlaintext m:", m)

# generate a random error vector e of weight t
success = 0
fails = 0
for i in range(1000):
    e = genRandomVector(n, t)
    # encrypt the message m
    y = encryptMcEliece(G, m, e)

    # decrypt the ciphertext
    decryptedText = demo(H, y)

    # check if decryption is correct
    if decryptSuccess(m, decryptedText):
        success += 1
    else:
        fails += 1
print('Number of successes: {} & fails: {} & {} %'.format(success, fails, 100*success/(success+fails)))

#text = open('noise.txt', 'r').readlines()
#lines = []
#for line in text:
#    lines.append(line.split())
#
#for i in lines:
#    for ind, j in enumerate(i):
#        i[ind] = int(j)
#
#e = np.array(lines)
#with open('noise.txt', 'wb') as f:
#    np.savetxt(f, e, fmt='%d')
#    print("noise matrix in noise.txt file")

