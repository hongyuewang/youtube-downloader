import webbrowser

url = input("Enter your YouTube video url in the following format: 'https://www.youtube.com/watch?v=URL'\n")
url = url[:12] + "ss" +url[12:]

webbrowser.open(url)