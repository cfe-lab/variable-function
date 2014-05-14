#!/opt/local/Library/Frameworks/Python.framework/Versions/2.7/bin/python
from scipy import stats
import cgi,sys,re

print "Content-Type: text/html\n"
print """<html>
<head>
<link rel="stylesheet" href="jquery/themes/blue/style.css">
<link rel="stylesheet" href="../dan/style.css">
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
<script src="jquery/jquery.tablesorter.js"></script>
<script src="jquery/myscript.js"></script>
</head>
<body><div class="container">
"""
print 

def median(input_list):
	input_list.sort()
	if(len(input_list) % 2 == 1):
		return input_list[len(input_list)/2]
	else:
		return (input_list[(len(input_list)-1)/2] + input_list[(len(input_list)+1)/2]) / float(2)

def normalizeNewlines(string):
	return re.sub(r'(\r\n|\r|\n)', '\n', string)

""" EXAMPLE OF VALID INPUT

A01\tA02\tB07\tB15\tC07\tC08\t0.1
A02\tA02\tB07\tB51\tC02\tC05\t0.2
A01\tA03\tB07\tB30\tC05\tC08\t0.3"""

form = cgi.FieldStorage()
forminput = form.getvalue("textinput")
formbutton = form.getvalue("csv")
print formbutton

# This will print the string with special characters shown
#print repr(forminput)

normalized_data = normalizeNewlines(forminput)
result = [x.split("\t") for x in normalized_data.split("\n")]
unique_categories = set([inner for outer in result for inner in outer[:-1]])
unique_categories = [x for x in unique_categories if x]

# The following is to print html
print "<table id='myTable' class='tablesorter'>"
print """<thead><tr class="header">
<th>Category</th>
<th>n-with</th>
<th>n-without</th>
<th>Median(with)</th>
<th>Median(without)</th>
<th>p-value</th>
</tr></thead><tbody>"""
for category in unique_categories:
	positive = [float(x[-1]) for x in result if category in x[:-1]]
	pos_median = median(positive)
	negative = [float(x[-1]) for x in result if category not in x[:-1]]
	neg_median = median(negative)
	u, p = stats.mannwhitneyu(positive, negative)
	print """<tr>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td>{}</td>
	<td>{:.8f}</td></tr>
	""".format(category,len(positive),len(negative),pos_median,neg_median,p)
	
print "</tbody></table></body></div>"

# The following is to print csv style
"""
print "category,median(with),median(without),p"
for category in unique_categories:
	positive = [float(x[-1]) for x in result if category in x[:-1]]
	pos_median = median(positive)
	negative = [float(x[-1]) for x in result if category not in x[:-1]]
	neg_median = median(negative)
	u, p = stats.mannwhitneyu(positive, negative)
	print "{},{},{},{}".format(category, pos_median, neg_median, p)
"""
sys.exit()
