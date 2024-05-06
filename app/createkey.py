import secrets

def generate_secret_key():
    return secrets.token_hex(16)

new_secret_key = generate_secret_key()
print(new_secret_key)
