
import dropbox
token = ''
dbx = dropbox.Dropbox(token)

for entry in dbx.files_list_folder('/Population/Population Project').entries:
    print(entry.name)

   
def getMeta():
    return dbx.files_get_metadata('/Population/Population Project/worldIndex.js').server_modified

print(getMeta())

