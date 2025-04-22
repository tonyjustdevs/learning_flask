from itsdangerous import URLSafeTimedSerializer

secret_key = 'a_very_not_secret_key'
salt = 'cookie-session' # Flask uses this salt for session cookies
serializer = URLSafeTimedSerializer(secret_key, salt=salt) # Create the serializer using Flask's default settings

cookie_value = ".eJyrVkpJTSpNV7IqKSpN1VEqLU4tii9OLS7OzM-Lz06tjDdUskIVLEvMAQrWAgBONhTa.aAeSJw.npxHyYc4u-2D7FPCpjD9iJn9u4s"
# data = serializer.loads(cookie_value) # error: BadTimeSignature
# data = serializer.loads(cookie_value, max_age=None)    
data = serializer.loads(cookie_value, max_age=3600)  # optional: add max_age
# data = serializer.load_payload(cookie_value)
print(data)


