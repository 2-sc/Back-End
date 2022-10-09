import jwt
import datetime
from studymate.settings import SECRET_KEY

def create_access_token(user):
    access_token_payload = {
        "id": user.id,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
    }
    access_token = jwt.encode(
        access_token_payload, SECRET_KEY, algorithm='HS256'
    )

    return access_token

def create_refrest_token(user):
    refresh_token_payload = {
        "id": user.id,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=14),
    }
    
    refresh_token = jwt.encode(
        refresh_token_payload, SECRET_KEY, algorithm='HS256'
    )

    return refresh_token