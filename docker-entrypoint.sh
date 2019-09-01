#!/bin/bash
service nginx start
# Write the credentials file from the env var.
echo $CREDENTIALS_DOT_JSON > /app/credentials.json
echo $CREDENTIALS_DOT_TOKEN_DOT_B64 > /app/token.pickle.b64
cd /app && \
    python3 make_token_pickle_bin.py && \
    python3 emailer.py
tail -f /dev/null
