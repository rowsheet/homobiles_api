import pickle
import base64

"""
with open("token.pickle.b64","r") as b64_file:
    b64_string = b64_file.read()
    b64_bytes = b64_string.encode('utf-8')
    parsed_bin_read = pickle.loads(base64.b64decode(b64_bytes))
    with open("token.pickle.test_bin","wb") as bin_file:
        pickle.dump(parsed_bin_read, bin_file)
"""
    
def load_from_string(b64_string):
    b64_bytes = b64_string.encode('utf-8')
    parsed_bin_read = pickle.loads(base64.b64decode(b64_bytes))
    # with open("token.pickle.test_bin","wb") as bin_file:
    with open("app/token.pickle","wb") as bin_file:
        pickle.dump(parsed_bin_read, bin_file)

import os
load_from_string(os.environ['CREDENTIALS_DOT_TOKEN_DOT_B64'])
