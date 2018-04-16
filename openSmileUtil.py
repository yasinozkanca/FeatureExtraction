import subprocess
import os
def openSmileCall(wavFile,outFile):

    OpenSmile = 'F:\\openSMILE-2.1.0\\bin\Win32\\SMILExtract_Release.exe'
    configAddr = 'F:\openSMILE-2.1.0\scripts\\avec2013\\avec2013_functionals.conf'
    os.system(OpenSmile+ ' -C '+ configAddr+' '+ ' -I' +' '+wavFile +' -O'+' '+outFile)
