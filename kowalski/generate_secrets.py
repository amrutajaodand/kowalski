from cryptography import fernet
import json
from utils import random_alphanumeric_str


if __name__ == '__main__':
    with open('/app/secrets.json') as sjson:
        secrets = json.load(sjson)

    fernet_key = fernet.Fernet.generate_key().decode()
    aiohttp_secret_key = random_alphanumeric_str(32)
    jwt_secret_key = random_alphanumeric_str(32)

    for key in ('server', 'misc'):
        if key not in secrets:
            secrets[key] = dict()

    secrets['server']['SECRET_KEY'] = aiohttp_secret_key
    secrets['server']['JWT_SECRET_KEY'] = jwt_secret_key
    secrets['misc']['fernet_key'] = fernet_key

    # save
    with open('/app/secrets.json', 'w') as sjson:
        json.dump(secrets, sjson, indent=2)
