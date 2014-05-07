import re

userurl = raw_input("Please enter a url: ")

match = re.search(r'^https://www\.youtube\.com/watch\?v=([^&]+)&?', userurl)

if match:
	print "The embed html for the video is: \n"
	print "<iframe width=\"560\" height=\"315\" src=\"//www.youtube.com/embed/" + match.group(1) + "\" frameborder=\"0\" allowfullscreen></iframe>\n"

else:
	print "Not a valid youtube url."