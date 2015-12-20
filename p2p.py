import os
import sys

def p2p(filedir,filename):
    file = filedir+filename
    print (file)
    mainpath = os.getcwd()
    ghostscriptpath = mainpath+"\\Ghostscript\\bin\\"
    ghostscriptstr1 = ghostscriptpath+"gswin64 -sDEVICE=pngalpha -o" 
    ghostscriptstr2 = "-%03d.png -sDEVICE=pngalpha -r80 "
    ghostscriptsend  = ghostscriptstr1+filename+ghostscriptstr2+file
    print (ghostscriptsend)
    os.system(ghostscriptsend)

#test run	
#filedir = "e:\\cse\\pdf\\"
#filename= "mesho.pdf"
#ptp(filedir, filename)