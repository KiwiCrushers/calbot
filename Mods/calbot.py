import requests

def from_url(url, user, id):
    # Retrieve the filetype of the URL.
    filetype = url[-3:]

    # Downloading the file into our system.
    r = requests.get(url, allow_redirects=True)
    open('images/' + user + '-' + id + '.' + filetype, 'wb').write(r.content)
