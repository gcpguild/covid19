import re, os
from operator import itemgetter
from pathlib import Path
#------------------------------------------------------------------
basepath = ["C:\google\serpapi\indias\medicine\covid19"]
#-----------------------------------------------------------------
def mkingdirs(givenlist):
    mymanog = ''.join(givenlist)
    mk_dir = Path(mymanog)
    mk_dir.mkdir(parents=True, exist_ok=True)
    return mk_dir
#-------------------------------------------------------------------
workingdir = mkingdirs(basepath)
os.chdir(workingdir)
#-------------------------------------------------------------------
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
            mymano += ' '+ x

        return mymano
#-----------------------------------------------------------------
N = "\\"
cwd = os.getcwd()
myd = cwd.split(N)
#-----------------------------------------------------------------
def getstringswitch(check_string_name):
  
    dict={
           's0' : myd[0], 
           's1' : myd[1], 
           's2' : myd[2], 
           's3' : myd[3],
           's4' : myd[4],
           's5' : myd[5],
           'd'  : 'data',
           'max_gs' : 10
          }
    return dict.get(check_string_name, cwd)
#-----------------------------------------------------------------
s = []
for n in range(0,len(myd)):
    assign  = ("{}{}".format('s',n))
    a = ''
    a = assign
    assign = removen(myd[n])
    i = ''
    i = ("{}{}{}".format(a,' = ',assign))
    s.append(i)
#-----------------------------------------------------------------
indices = itemgetter(0,1,2,3,4,len(s)-1)
bd = (N.join(map(str, indices(myd))))

givenlist = [bd,N,getstringswitch(check_string_name = 'd')]

mkdirlist = mkingdirs(givenlist)

print (mkdirlist)




