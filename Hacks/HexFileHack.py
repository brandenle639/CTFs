#Reads the Hex of a file and looks for the flag and gets the flag output

#Declares the arroutput
arr=[]

#Enter the file
fil=input("File to look for flag: ")

#Look for the flag code
spli=input("Key Text Flag to find: ")

#Reads through the hex code of file
def group(a, *ns):
        for n in ns:
                a = [a[i:i+n] for i in range(0, len(a), n)]
                return a

#Joins the hex code
def join(a, *cs):
  return [cs[0].join(join(t, *cs[1:])) for t in a] if cs else a

#Manages the hex dump
def hexdump(data):
  toHex = lambda c: '{:02X}'.format(c)
  toChr = lambda c: chr(c) if 32 <= c < 127 else '.'
  make = lambda f, *cs: join(group(list(map(f, data)), 8, 2), *cs)
  hs = make(toHex, '  ', ' ')
  cs = make(toChr, ' ', '')
  for i, (h, c) in enumerate(zip(hs, cs)):
    ar='{:16}'.format(c)
    arr.append(ar.replace(" ", ""))

#Opens the file and gets the hex dump
with (open (fil,'br')) as file:
    data=file.read()
    arr.append(hexdump(data))
#Output string
output=""
#Array Length
i = 0
#Loops through the array and looks for the flag code and prints the output
while i < len(arr):
    output="%s%s" % (output,arr[i])
    i += 1
try:
    ln1=output.split(spli+"{")
    ln2=ln1[1].split("}")
    print(ln2[0])
except:
    print(output)