import requests

def from_url(url, user, attachmentId):
    # Retrieve the filetype of the URL.
    filetype = url[-3:]

    # Downloading the file into our system.
    r = requests.get(url, allow_redirects=True)
    filePath = 'images/' + str(user) + '-' + str(attachmentId) + '.' + str(filetype)
    open(filePath, "wb").write(r.content)
    # Returns the path and filename.
    return filePath
