
from io_util import get_file_list,arff_to_data
from openSmileUtil import openSmileCall

flist = get_file_list('C:\\Users\yasin\Downloads\gitRepos\dcapswoz.ict.usc.edu\wwwdaicwoz\wavsVad\\dev','.wav')
for i in range(len(flist)):
    file_path = flist[i] + '.arff'
    openSmileCall(flist[i], file_path)