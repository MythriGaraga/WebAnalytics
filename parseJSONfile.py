import json
import itertools


def loadJSONfile(fname):
    data = []
    fo = open(fname)
    for lines in itertools.islice(fo, 0, 10):
        content = json.loads(lines)
        data.append(content)
    fo.close()
    print data
 
if __name__=='__main__':
	loadJSONfile('yelp_academic_dataset_business.json')
