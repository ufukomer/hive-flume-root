import os
import os.path
import datetime
import sys
import random
from random import randrange
from random import randint

# Current time
time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%dT%H:%M:%S')
countries = ["TR", "SO", "MZ", "JP", "VU", "EG", "QA", "YE", "BO"]
country = countries[randint(0,8)]
path = "/var/log/eventlog-demo.log"
array = []

# Random IP Adress
if __name__=="__main__":
    not_valid = [10,127,169,172,192]

    first = randrange(1,256)

    while first in not_valid:
    	first = randrange(1,256)

    ip = ".".join([str(first),str(randrange(1,256)),
    str(randrange(1,256)),str(randrange(1,256))])

try:
    if os.path.isfile(path):
        with open(path, "r") as file:
            for line in file:
                array.append(line)
            file.close()

    file = open(path, "w")

    new_line = time + "|" + ip + "|" + country

    array.append(new_line + "\n")

    file.writelines(array)
    file.close()

except IOError:
    print "There was an error while processing the file!"
