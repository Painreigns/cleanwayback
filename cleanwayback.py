from urllib.parse import urlparse,urljoin
import sys
query_list=[]
final_list=[]
second_list=[]

def filter(i,o):
	input=open(i)
	output=open(o,'w')
	global query_list
	global final_list
	global second_list
	for i in input:
		parsed_url=urlparse(i)
		if parsed_url.query!='':
			query_list.append(i)
	
	query_list=list(set(query_list))
	for i in query_list:
		parsed_url=urlparse(i)
		z=urljoin(i,parsed_url.path)
		if z not in second_list:
			second_list.append(z)
			final_list.append(i)

	final_list=list(set(final_list))
	for i in final_list:
		output.write(i)
	input.close()
	output.close()

arg=sys.argv
if arg[1]=='-i' and arg[3]=='-o':
	i=arg[2]
	o=arg[4]
	filter(i,o)
else:
	print('Invalid Syntax')
#python filanem.py -i input -o output