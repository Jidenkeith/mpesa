import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

class MpesaC2bCredential:
    consumer_key = 'OrldoopdaxAUKOmOr7ED0RAi1VGUC44r'
    consumer_secret = 'Scf9Gd14hAEpL4Il'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'