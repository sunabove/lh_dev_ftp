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
print( "LIST files ....." )
list = ftp.retrlines('LIST') 
print( list )

print( line2 )
print( "Good bye!" )