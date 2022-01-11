from google.auth.transport import requests
from google.oauth2 import id_token


class Google:
    #Google class to fetch the user info and return it

    @staticmethod
    def validate(auth_token):
        
       # Validate method Queries the Google oAUTH2 api to fetch the user info
       # Docs https://developers.google.com/identity/sign-in/web/backend-auth?hl=en
        

        try:
            idinfo = id_token.verify_oauth2_token(
            auth_token, requests.Request(), None)
                
            if 'accounts.google.com' in idinfo['iss']:
                return idinfo
        except:
            return "The token is either invalid or has expired"
