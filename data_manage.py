import os, time
import ftplib
from ftplib import FTP

line = "*"*40
line2 = f"\n{line}"

print( line2 )
print( f"Hello...." )

host = "localhost"
user = "icarus"
passwd = "vmffotvha123!"
ftp = FTP( host )
ftp.login( user, passwd )
print( "login_success" )

print( line2 )

data = []

ftp.dir( data.append ) 

file_infos = []

for idx, line in enumerate( data ):
    col = line.split()
    size = col[4]
    date = ' '.join(line.split()[5:8])
    filename = col[8]
    
    #print( f"[{idx:02}] {line}" )
    print( f"[{idx:02}] size = {size}, date = {date}, filename = {filename}" )
    
    file_info = { "filename" : filename, "date" : date, "size" : size }
    
    file_infos.append( file_info )
pass

if file_infos :
    local_dir = "data"
    if not os.path.exists( local_dir ):
        os.makedirs( local_dir )
        print( f"directory {local_dir} was created." )
    pass

    print( "Change local folder." )
    os.chdir( "data" ) 

    file_info = file_infos[0]
    filename = file_info["filename"]
    
    with open( f'{filename}', 'wb') as fp: 
        print( f"Downloading file {filename} ..." )
        ftp.retrbinary( f'RETR {filename}', fp.write)
        print( f"Done. downloading file {filename} ..." )
    pass
pass
    
print( line2 )
print( "Good bye!" )