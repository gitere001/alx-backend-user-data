import base64

data = 'hello world!'
data_bytes = data.encode('ascii')
encoded_data = base64.b64encode(data_bytes)
string_encoded_data = encoded_data.decode('ascii')
print(encoded_data)
print(string_encoded_data)
decoded_data = base64.b64decode(encoded_data)
print(decoded_data.decode('ascii'))