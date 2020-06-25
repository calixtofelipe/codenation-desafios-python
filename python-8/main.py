import jwt


def create_token(data, secret):
    return jwt.encode(data, secret)


def verify_signature(token):
    key = "acelera"
    msg = {}
    try:
        msg = jwt.decode(token, key)
    except Exception as e:
        if str(e) == "Signature verification failed":
            msg = {"error": 2}
    return msg
