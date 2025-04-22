from flask.sessions import SecureCookieSessionInterface
from flask import Flask

# app = Flask(__name__)
# app.secret_key = 'a_very_not_secret_key'
# cookie_value = ".eJyrVkpJTSpNV7IqKSpN1VEqLU4tii9OLS7OzM-Lz06tjDdUskIVLEvMAQrWAgBONhTa.aAeSJw.npxHyYc4u-2D7FPCpjD9iJn9u4s"
# serializer = SecureCookieSessionInterface().get_signing_serializer(app)
# data = serializer.loads(cookie_value)
# print(data)


from itsdangerous import URLSafeTimedSerializer
from flask.json.tag import TaggedJSONSerializer

secret_key = 'a_very_not_secret_key'
salt = 'cookie-session'  # default salt used by Flask
serializer = URLSafeTimedSerializer(
    secret_key=secret_key,
    salt=salt,
    serializer=TaggedJSONSerializer(),  # same serializer Flask uses
    signer_kwargs={'key_derivation': 'hmac', 'digest_method': 'sha1'}  # matches Flask's default signer config
)

cookie_value = ".eJyrVkpJTSpNV7IqKSpN1VEqLU4tii9OLS7OzM-Lz06tjDdUskIVLEvMAQrWAgBONhTa.aAeSJw.npxHyYc4u-2D7FPCpjD9iJn9u4s"
session_data = serializer.loads(cookie_value)  # This should now work!
print(session_data)


# if __name__ == "__main__":
#     app.run("127.0.0.1", port=5001, debug=True)
