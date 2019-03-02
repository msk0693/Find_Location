import webbrowser, sys

if len(sys.argv) > 1:
	address = ' '.join(sys.argv[1:]) #returns single string of command args
else:
	address = raw_input("Enter a Location to Open it in Google Maps: ")

webbrowser.open('https://www.google.com/maps/place/' + address)

