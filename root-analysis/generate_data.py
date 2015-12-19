import pyhs2
import os
import os.path

def split(txt, seps):
    default_sep = seps[0]
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    return [i.strip() for i in txt.split(default_sep)]

# Replace this ip with your own host ip
with pyhs2.connect(host = '192.168.140.134',
	               port = 10000,
                   authMechanism = "PLAIN",
                   user = 'root',
                   password = 'test',
                   database = 'default') as conn:
    with conn.cursor() as cur:

    	#Execute query
        cur.execute("SELECT country, COUNT(*) AS c_count FROM country_logs GROUP BY country ORDER BY c_count")

        #Fetch table results
        list = cur.fetch()

if  os.path.exists("./data") == False:
    os.mkdir("./data");
try:
    # Create dat file has same name as country code
    for li in list:
        li = str(li)
        arr = split(li, ('[', ',', ']', "'"))
        file = open("./data/" + arr[2] + ".dat", "wb")
        file.write(arr[4] + "\n")
        file.close()

except Exception, e:
    print str(e)
