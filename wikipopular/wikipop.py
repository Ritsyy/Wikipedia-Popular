import urllib2
from BeautifulSoup import BeautifulSoup
import operator
import wikipedia
# import urllib3.contrib.pyopenssl
# urllib3.contrib.pyopenssl.inject_into_urllib3()

# pgtitle= raw_input("Enter the title\n")
def wikipop(title):
	print "coming inside func"
	try:
		pg = wikipedia.page(title)
		print pg
		stitle = pg.title
		print pg.title

		result={}
		# arr = pg.links
		# if len(arr)>10:
		# 	arr = arr[0:4]
		# print arr
		for link in pg.links:
			try:
				i=0
				link1={""}
				pg1 = wikipedia.page(link)
				page = urllib2.urlopen(pg1.url)
				soup = BeautifulSoup(page.read())
				link1 = soup.findAll('a', title=stitle)
				if len(link1)==None:
					print "0 links"
				else:
				# 	i=len(link1)
					result[pg1.url] = len(link1)
					print pg1, "is redirected", len(link1), "no. of times"

			except Exception,e:
				print "not found"
				continue
		newresult = result
		newresult= sorted(newresult.iteritems(), key=operator.itemgetter(1,0),reverse=True)
		print newresult
		newresult = newresult[0:3]
		print newresult
		return newresult
	except Exception,e:
		newresult = "Not A valid title"
		return newresult
	# 	for link1 in pg1.links:
	# 		if link1 == pg.title:
	# 			i = i+1
	# 			result[pg1] = i
	# 			print pgtitle, "was redirected from", pg1
			
	# for key,value in result.iteritems():
	# 	print key,"=",value