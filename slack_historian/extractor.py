import os
import zipfile
from datetime import datetime 

def extract_zipfile(filename):
    chatlog_archive = zipfile.ZipFile(filename)
    directory_name = "slack-archive-" + datetime.now().strftime("%Y-%m-%dT%H%M%S") 
    extracted_path  = os.path.join(os.getcwd(), directory_name)
    chatlog.extractall(extracted_path)

    chatlog.close()
    return extracted_path
