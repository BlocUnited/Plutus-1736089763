import os

class Config:
    DATABASE_URI = os.environ.get('DATABASE_URI')
    AZURE_SIGNALR_CONNECTION_STRING = os.environ.get('AzureSignalRConnectionString')
    AZURE_STORAGE_CONNECTION_STRING = os.environ.get('AZURE_STORAGE_CONNECTION_STRING')

    def __init__(self):
        if not self.DATABASE_URI:
            raise ValueError('DATABASE_URI environment variable is required.')
        if not self.AZURE_SIGNALR_CONNECTION_STRING:
            raise ValueError('AzureSignalRConnectionString environment variable is required.')
        if not self.AZURE_STORAGE_CONNECTION_STRING:
            raise ValueError('AZURE_STORAGE_CONNECTION_STRING environment variable is required.')
