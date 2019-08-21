import http.client, urllib.request, urllib.parse, urllib.error, base64, uuid
import sys
import os
from app.main import create_app

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')


def create_api_user():
    headers = {
        # Request headers
        'X-Reference-Id': '',
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': app.config['OCP_APIM_SUBSCRIPTION_KEY'],
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
        conn.request("POST", "/v1_0/apiuser?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


def get_api_key():
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': app.config['OCP_APIM_SUBSCRIPTION_KEY'],
    }

    params = urllib.parse.urlencode({
    })

    try:
        conn = http.client.HTTPSConnection('ericssonbasicapi2.azure-api.net')
        conn.request("POST", "/v1_0/apiuser/5a0d989b-c3b3-47f7-a076-bd4a652f2274/apikey?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))
