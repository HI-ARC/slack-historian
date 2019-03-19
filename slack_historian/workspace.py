import os
import json

class Workspace:
    """
    class Workspace

    * Stores information of Messenger's Workspace
      * Hashed value of Channel, User
    """
    def __init__(self, archive_path):
        self.archive_path = archive_path
        self.export_path = archive_path + '-result'
        self.channels = {}
        self.users = {}

    def load(self):
        loaded_channels = json.load(os.path.join(archive_path, 'channels.json'))
        loaded_users = json.load(os.path.join(archive_path, 'users.json'))
        
        for channel in loaded_channels:
            self.channels[channel['id']] = channel['name']
        
        for user in loaded_users:
            self.users[user['id']] = user['name']

    def archive_logs(self):
        channel_directories = []
        
        for entry in filter(os.isdir, os.listdir(self.archive_path)):
            channel_directory_path = os.path.join(self.archive_path, entry)
            channel_directories.append(channel_directory_path)

        for channel in channel_directories:
            for chat_log_file in os.listdir(channel):
                chat_log_path = os.path.join(channel, chat_log_file)
                loaded_logs = json.load(chat_log_path)

                for log in loaded_logs:
                    pass
            
