import dropbox
import os
import sys
import webbrowser
from configobj import ConfigObj
 
# Get your app key and secret from the Dropbox developer website
app_key = 'appkey'
app_secret = 'secret'
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
#code = raw_input("_n4WAg1W_0sAAAAAAAAAQ8klfddpv7DFWRmXUHxHxeE").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish("_n4WAg1W_0sAAAAAAAAATY79bW6Cz6ARlCkXDNJIDzk")
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

# uploading working-draft.txt as magnum-opus.txt in dropbox folder
f = open('working-draft.txt', 'rb')
response = client.put_file('/magnum-opus.txt', f)
print "uploaded:", response

# printing all folder names in dropbox 
folder_metadata = client.metadata('/')
print "metadata:", folder_metadata

# downloading keys.txt from dropbox to desktop as magnum-opus.txt 
f, metadata = client.get_file_and_metadata('/keys.txt')
out = open('magnum-opus.txt', 'wb')
out.write(f.read())
out.close()
print metadata