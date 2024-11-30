#Used to extract Binwalk steganography Files

#Asks for steganography file
echo "Enter Steg File: "
read f
#Gets the directory and the filename
dirr=$(dirname "${f}")
filename=$(basename -- "$f")
#Sets the extraction path
edir="$dirr/_$filename.extracted"
#Runs Binwalk to list encoded files
binwalk $f
#changes to the main directory
cd $dirr
#Asks for the encoded file type
echo "Enter File Type: "
read e
#EXtracts files based on extention (Will have to extensions with future use)
case $e in
    png)
        binwalk -D 'png image:png' $f
    ;;
    *)
        echo "Must Have File Type"
    ;;
esac
#Opens the output folder (Will have to change 'caja' with your file manager)
caja $edir