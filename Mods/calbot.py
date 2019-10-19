import requests

def from_url(url):
    # Retrieve the filetype of the URL.
    filetype = url[-3:]

    # Downloading the file into our system.
    r = requests.get(url, allow_redirects=True)
    open('images/file.' + filetype, 'wb').write(r.content)
