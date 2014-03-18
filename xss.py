#!/usr/bin/python
# module for CGI
import cgi
# for CGI debugging purposes - tb = traceback
import cgitb; cgitb.enable()
# regular expression module
import re

def print_page():
	print '''
	Content-type: text/html\n\n

	<html lang="en">
	<head>
		<title>XSS Test Page</title>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="style.css" />
		<style>
			body {background: #EEE}
		</style>
	</head>

	<body>
		<div id="main">
			<h1>XSS Test Page</h1>
			<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. Praesent et diam eget libero egestas mattis sit amet vitae augue. Nam tincidunt congue enim, ut porta lorem lacinia consectetur. Donec ut libero sed arcu vehicula ultricies a non tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut gravida lorem. Ut turpis felis, pulvinar a semper sed, adipiscing id dolor. Pellentesque auctor nisi id magna consequat sagittis. Curabitur dapibus enim sit amet elit pharetra tincidunt feugiat nisl imperdiet. </p>

			<p>Please subscribe to our mailing list. </p>
			<form action="" method="GET">
				<fieldset>
					<legend>Vulnerable Form</legend>
					<label>Name: </label><input type="text" name="name" required><br>
					<label>Email: </label><input type="email" name="email" required><br>
				</fieldset>
				<input id="submit" type="submit" value="Submit">
			</form>
		</div>
	</body>

	</html>
	'''

form = cgi.FieldStorage()
if (form.has_key("submit")):
	user_input=get_form(form)
else:
	print_page()


