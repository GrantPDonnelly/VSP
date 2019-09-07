import os

def find_contents():
    contents = os.listdir()
    directories = list()
    files = list()
    for c in contents:
        try:
            os.chdir(c)
            os.chdir('..')
            directories.append(c)
        except:
            files.append(c)
            pass
    return [directories, files]

def check_dirs(key):
    
    images = list()

    dirlist = find_contents()[0]
    for d in dirlist:
        if d.find('rotse') != -1:
            os.chdir(d)
            then = find_contents()[0]
            for f in then:
                if f.find('data') != -1:
                    os.chdir(f)
                    if 'rotse3' in find_contents()[0]:
                        os.chdir('rotse3')
                        for g in find_contents()[0]:
                            if integer_test(g) == True:
                                os.chdir(g)
                                try:
                                    os.chdir('image')
                                    for v in print_path(find_contents()[1],key):
                                        images.append(v)
                                    os.chdir('..')
                                    os.chdir('prod')
                                    for b in print_path(find_contents()[1],key):
                                        images.append(b)
                                    os.chdir('..')
                                except:
                                    pass
                                os.chdir('..')
                        os.chdir('..')
                        os.chdir('..')
                    else:
                        os.chdir('..')
                elif f.find('disk') != -1:
                    os.chdir(f)
                    if 'rotse3' in find_contents()[0]:
                        os.chdir('rotse3')
                        for h in find_contents()[0]:
                            if integer_test(h) == True:
                                os.chdir(h)
                                try:
                                    os.chdir('image')
                                    for n in print_path(find_contents()[1],key):
                                        images.append(n)
                                    os.chdir('..')
                                    os.chdir('prod')
                                    for m in print_path(find_contents()[1],key):
                                        images.append(m)
                                    os.chdir('..')
                                except:
                                    pass 
                                os.chdir('..')
                        os.chdir('..')
                    else:
                        for j in find_contents()[0]:
                            if integer_test(j) == True:
                                os.chdir(j)
                                try:
                                    os.chdir('image')
                                    print_path(find_contents()[1],key)
                                    os.chdir('..')
                                    os.chdir('prod')
                                    print_path(find_contents()[1],key)
                                    os.chdir('..')
                                except:
                                    pass 
                                os.chdir('..')
                    os.chdir('..')                
            os.chdir('..')

    print('Process executed successfully.')
    return images

def integer_test(inp):
    try:
        int(inp)
        res = True
    except:
        res = False
    return res

def print_path(files,key):
    output = list()
    for f in files:
        check = f.find(key)
        if check != -1:
            image = os.getcwd()+'/'+f
            output.append(image)
            print(image)
    return output

def copier(use,key,destination,name):

    imdir = list()
    prodir = list()

    for i in use:
        if i.find('image') != -1:
            imdir.append(i)
        elif i.find('prod') != -1:
            prodir.append(i)

    os.chdir(destination)
    os.system('mkdir '+name)
    os.chdir(name)
    os.system('mkdir image')
    os.system('mkdir prod')

    for q in imdir:
        os.system('cp '+q+' '+destination+'/'+name+'/image')

    for w in prodir:
        os.system('cp '+w+' '+destination+'/'+name+'/prod')

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("key")
parser.add_argument("name", nargs='?',default=None)
parser.add_argument("destination", nargs='?', default=os.getcwd())
args = parser.parse_args()
key = args.key
destination = args.destination
name = args.name

if name == None:
    name = key

os.chdir('/scratch/group/astro/data/ROTSE')

contents = check_dirs(key)
copy = copier(contents,key,destination,name)









    

