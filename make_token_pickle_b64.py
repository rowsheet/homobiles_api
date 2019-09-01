import pickle
import base64

with open('token.pickle','rb') as bin_file:
    bin_read = bin_file.read()
    token_b64_str = base64.b64encode(bin_read).decode("utf-8")
    with open('token.pickle.b64', 'w') as b64_file:
        b64_file.write(token_b64_str)
