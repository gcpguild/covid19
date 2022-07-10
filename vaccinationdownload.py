#---------------------------------------------------------------
initialdirectoryconfig = 'initialization.py'
#------------------------------------------------------------------
who_data_url = 'https://covid19.who.int/who-data/vaccination-data.csv'
#----------------------------------------------------------------
#---------No changes after this line -------------------
#---------------------------------------------------------------------
import requests,re, os, sys
from pathlib import Path
from subprocess import check_output
#------------------------------------------------------------------------
N="\\"
#-------------------------------------------------------------------------
def sorryfilemissing(necessaryfile):
        pi="\'File is missing ! \' :"
        p = ("{} {}".format(pi,necessaryfile))
        print(p)
        exit(1)
#-------------------------------------------------------------------------
def checkfile(inputfile):
    path = Path(inputfile)
    if path.is_file():
        return path     
#---------------------------------------------------------------------
def removen(string):
    for m in ('\n', '\r'):
        clean_string = re.sub(m, '', string)
        clean_string = clean_string.replace(m, '')
        clean_string = clean_string.rstrip()
        clean_string = clean_string.strip(m)
        clean_string = re.sub(m,' ', clean_string)
        clean_string = [re.sub(r'[^a-zA-Z,=":_0-9\\]+','', clean_string)]
        mymano = ''
        for x in clean_string:
            mymano += ''+ x
        return mymano
#-----------------------------------------------------------------
def fullyqualifydirs(mylist):
    mydircode = N.join(mylist)
    return mydircode
#-----------------------------------------------------------------
def downloading(download_url,local_file_data):
    
    file_stream = requests.get(download_url, stream=True)
    with open(local_file_data, 'wb') as local_file:
        for data in file_stream:
            local_file.write(data)
#------------------------------------------------------------------
def remove_if_exists(removefile):
    try:
        if os.path.exists(removefile):
            os.remove(removefile)
            
    except:
        print("Error while deleting file ", removefile)
#------------------------------------------------------------------                
whodata=re.sub(r'^.+/([^/]+)$', r'\1', who_data_url)
mycheck = checkfile(initialdirectoryconfig)
getdirectory = check_output([sys.executable, initialdirectoryconfig], universal_newlines=True)
mydownloadir = N.join(removen(getdirectory).split(N))
#------------------------------------------------------------------  
mylist = [mydownloadir,whodata]

fq = fullyqualifydirs(mylist)
#----------------------------------------------------------------
if not fq:
    sorryfilemissing(fq) 
#----------------------------------------------------------------
mycheck = checkfile(fq)

if (mycheck):
    remove_if_exists(fq)    
#-----------------------------------------------------------------
downloading(download_url = who_data_url,local_file_data = fq)
mycheck = checkfile(fq)
print(mycheck)







