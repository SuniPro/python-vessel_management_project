import json

from django.contrib.auth import authenticate
import jwt
import requests

from vessel_management_sample.secrets import JWT_AUDIENCE, JWT_ISSUER


def jwt_get_username_from_payload_handler(payload):
    username = payload.get('sub').replace('|', '.')
    authenticate(remote_user=username)
    return username


def jwt_decode_token(token):
    header = jwt.get_unverified_header(token)
    jwks = requests.get('https://{}/.well-known/jwks.json'
                        .format(JWT_ISSUER)).json()
    public_key = None

    for jwk in jwks['keys']:
        if jwk['kid'] == header['kid']:
            public_key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(jwk))

    if public_key is None:
        raise Exception('Public key not found.')

    issuer = 'https://{}/'.format(JWT_ISSUER)
    return jwt.decode(token, public_key, audience=JWT_AUDIENCE, issuer=issuer,
                      algorithms=['RS256'])
