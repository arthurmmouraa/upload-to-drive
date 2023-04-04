from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import os
import os.path

# GETTING ALL THE DATA NEEDED

CLIENT_SECRET_FILE = 'C:\\Users\\User\\CREDENTIALS_REPOSITORY.json' # CREDENTIALS FROM DRIVE PROJECT NEEDED 
API_NAME= 'drive'
API_VERSION='v3'
SCOPES= ['https://www.googleapis.com/auth/drive'] 

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES) # THE GOOGLE.PY ARCHIVE ALSO NEEDED AND IMPORT HERE

## print(dir(service))

folder_id = 'FOLDERS_ID' # THE FOLDER'S ID ON G DRIVE

# STARTING THE UPLOAD

for file_name in os.listdir('C:\\Users\\User\\FILES_FOLDER'): # THE FILE'S FOLDER (FROM YOUR COMPUTER) YOU WANT TO UPLOAD
    file_metadata = {
        'name':file_name,
        'parents': [folder_id]
    }
    media = MediaFileUpload(f'C:/Users/User/FILES_FOLDER/{file_name}')   # THE FILE'S FOLDER (FROM YOUR COMPUTER) YOU WANT TO UPLOAD

    file = service.files().create(  
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
    print('===========- ID -=============')
    print('File ID: %s' % file.get('id'))   # GET THE ID FROM THE ARCHIVES UPLOADED
    
    file_id = file.get('id')
    request_body = {
        'role': 'reader',
        'type': 'anyone'
    }

    response_permission = service.permissions().create(
        fileId = file_id,
        body=request_body
    ).execute()

    response_share_link = service.files().get(
        fileId=file_id,
        fields='webViewLink'
    ).execute()
    print('============LINK=============')
    print(response_share_link['webViewLink'])   # GET THE LINK OF THE ARCHIVE

    

