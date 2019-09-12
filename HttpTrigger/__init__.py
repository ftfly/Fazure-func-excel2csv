    
import json
import logging

import azure.functions as func
from azure.keyvault import KeyVaultClient
from azure.storage.blob import BlockBlobService
from msrestazure.azure_active_directory import MSIAuthentication

from .conversion.excel2csv import Excel2Csv


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    credentials = MSIAuthentication(resource='https://vault.azure.net')
    kvclient = KeyVaultClient(credentials)
    key = kvclient.get_secret("https://mnanalyticssandbox-vault.vault.azure.net/", "sakey", "").value
    
    converter = Excel2Csv(BlockBlobService(account_name='xlsxupload', account_key=key))
    converter.convert_and_upload()         
    
    return json.dumps({"result": "Conversion Finished!"})
