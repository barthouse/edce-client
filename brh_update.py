import sys
if sys.version_info.major < 3:
	print("You need to use Python 3.x, e.g. python3 <filename>")
	exit()

import configparser
import edce.query
import edce.error
import edce.util
import edce.eddn
import edce.config
import edce.globals

import json

edce.globals.interactive = True
edce.globals.debug = False
edce.eddn.testSchema = False

try:
	res = edce.query.performQuery()
		
	data = edce.util.edict(res)
	
	filename = "database/{a}-{b}.json".format(a=data.lastSystem.name, b=data.lastStarport.name)
	jsonstr = json.dumps(data, ensure_ascii=False)
	with open(filename, "w", encoding='utf8') as f:
		f.write(jsonstr)
		f.close()			
		
	print("Done.")
	
except edce.error.Error as e:
	print("EDCE: " + e.message)
except:
	print("Unexpected error:", sys.exc_info()[0])
	raise


