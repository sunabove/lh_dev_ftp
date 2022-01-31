import os, time, uuid, ftplib, psycopg2
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
    filename = " ".join( col[8: ] )
    
    date = date.split( " " )
    date = " ".join( [ date[2], date[0], date[1] ] )
    
    #print( f"[{idx:02}] {line}" )
    print( f"[{idx:02}] size = {size}, date = {date}, filename = {filename}" )
    
    file_info = { "filename" : filename, "date" : date, "size" : size }
    
    file_infos.append( file_info )
pass

if file_infos :
    if True : 
        print( line2 )
        print( "Change local folder." )
        local_dir = "data"
        if not os.path.exists( local_dir ):
            os.makedirs( local_dir )
            print( f"directory {local_dir} was created." )
        pass
        os.chdir( "data" )
    pass
    
    db_name = "landbigdata"
    db_user = "landbigdata"
    db_pass = "landbigdata"
    print( line2 )
    print( "Connecting database ... " )
    conn = psycopg2.connect( f"dbname={db_name} user={db_user} password={db_pass}" )
    print( "Done. connecting database." )
    
    with conn.cursor() as cursor : 
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        
        print( f"version = {record}" )
    pass
    
    with conn.cursor() as cursor : 
        for file_info in file_infos : 
            filename = file_info["filename"]
            sql = """SELECT data_id, org_file, dest_loc, data_src, file_fmt, file_usage
                , TO_CHAR( get_date, 'YYYY Mon DD HH:MI:SS') get_date
                , TO_CHAR( upload_date, 'YYYY Mon DD HH:MI:SS' ) upload_date
                , TO_CHAR( model_apply_date, 'YYYY Mon DD HH:MI:SS' ) model_apply_date
                , model_apply_user_id
                from meta_data
                where org_file = %s
                LIMIT 1
            """
            cursor.execute( sql, [filename] )
            # Fetch result
            rows = cursor.fetchall();
            print( f"row len = {len(rows)} filename = {filename}" )
            
            for row in rows : 
                print( f"row = {row}" )
            pass
        
            if len( rows ) == 0 :
                data_id = uuid.uuid4().hex
                org_file = filename
                dest_loc = f"data/{filename}"
                data_src = "KLIS" if "KLIS" in filename else "LH"
                file_format = filename.split( "." )[-1]
                file_usage = "모형" if "모형" in filename else "데이터"
                model_apply_user_id = "admin"
                
                sql = f"""INSERT INTO meta_data
                (data_id, org_file, dest_loc, data_src, file_fmt, file_usage, get_date, upload_date, model_apply_user_id )
                VALUES( '', '')
                """ 
            pass
        pass
    pass

    if False : 
        for file_info in file_infos : 
            filename = file_info["filename"]
            
            with open( f'{filename}', 'wb') as fp: 
                print( f"Downloading file {filename} ..." )
                ftp.retrbinary( f'RETR {filename}', fp.write)
                print( f"Done. downloading file {filename} ..." )
            pass
        pass
    pass
pass
    
print( line2 )
print( "Good bye!" )