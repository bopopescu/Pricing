from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'lgklataforma' # Must be replaced by your <storage_account_name>
    account_key = 'SpHagQjk7C4dBPv1cse9w36zmAtweXIMjcw9DWve7ipgXgf2Fa5l+vw2k57EM8uinlUOkfxt34BQpC9FBHE+Yg==' # Must be replaced by your <storage_account_key>
    azure_container = 'archivospricing'
    expiration_secs = None