#Encodes a sentence in a set number of times in a random order in base16, base32, and base64.

#Imports OS For File Writer
import os
#Imports For Base Encryption
import base64
#Importas For Random Order
import random
#Message To Be Encoded
encoded = b'{ENTER MESSAGE HERE}'
#Number of times to encode
times=4
#t\f if file exists
fex="f"
#File Output counter
i=1
#Output Directory
outdir="{Output DIR}"
#File Output
file_path=f'{outdir}/baseourput{i}.txt'
#Lo until file is created
while not fex=="t":
    #File Output
    file_path=f'{outdir}/baseourput{i}.txt'
    print(file_path)
    #Checks if file exists
    exists = os.path.isfile(file_path)
    if not exists:
        #Creates File If doesn't Exist
        a= open(file_path,"w+")
        a.close()
        #Sets file created true
        fex="t"
    else:
        #Increases the index if file is exists
        i=i+1
#Output String
stren=""
#t\f for first line 
fir="t"
#Opens file for output
f = open(file_path, 'a+')
#Loops the numbering of times that was set
for x in range(times):
    #Generates random number for what base it is
    a=random.randint(1,3)
    #If random is 1 then do base16 encryption
    if a == 1:
        if fir == "t":
            f.write(f"{x} base16\n")
            stren=base64.b16encode(encoded)
            fir="n"
        else:
            f.write(f"{x} base16\n")
            stren=base64.b16encode(stren)
    #If random is 2 then do base32 encryption
    if a == 2:
        if fir == "t":
            f.write(f"{x} base32\n")
            stren=base64.b32encode(encoded)
            fir="n"
        else:
            f.write(f"{x} base32\n")
            stren=base64.b32encode(stren)
    #If random is 3 then do base64 encryption
    if a == 3:
        if fir == "t":
            f.write(f"{x} base64\n")
            stren=base64.b64encode(encoded)
            fir="n"
        else:
            f.write(f"{x} base64\n")
            stren=base64.b64encode(stren)
#Wirtes the output encoded and closes the file
f.write(f"{stren}")
f.close()
