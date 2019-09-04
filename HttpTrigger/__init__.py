import json
import logging

import azure.functions as func
from azure.keyvault import KeyVaultClient
from azure.storage.blob import BlockBlobService
from msrestazure.azure_active_directory import MSIAuthentication

from .conversion.excel2csv import Excel2Csv


def main(req: func.HttpRequest) -> func.HttpResponse:
    return "Hello Python!"
