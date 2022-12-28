import sys

cipher=sys.argv[1]
key=sys.argv[2]
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num_cipher=[]
num_key=[]
plaintext=""
for i in cipher:
    if i==" ":
        num_cipher.append(" ")
    else:
        num_cipher.append(alpha.index(i))
for j in key:
    num_key.append(alpha.index(j))
def decode(nkey,ncipher):
    count=0
    cir_cou=0
    space_cou=0
    plain=[]
    while count<len(ncipher):
        for i in range(1,len(nkey)+1):
            if count>=len(ncipher):
                break
            else:
                if ncipher[count]==" ":
                    plain.append(" ")
                    space_cou+=1
                    count+=1
                    
                else:
                    plain.append(ncipher[count]-nkey[count%4-space_cou%4])
                    count+=1
        cir_cou+=1
    return plain
num_plain=decode(num_key,num_cipher)
for t in range(len(num_plain)):
    if num_plain[t]==" ":
        plaintext+=" "
    else:
        if num_plain[t]<0:
            num_plain[t]+=26
        plaintext+=alpha[(num_plain[t])]
print(f"[cipher:]={cipher}")
print(f"[key:]={key}")
print(f"[plaintext:]={plaintext}")









