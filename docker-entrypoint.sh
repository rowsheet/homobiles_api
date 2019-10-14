#!/bin/bash
service nginx start
cd /app && python3 server.py >> logs
tail -f /dev/null
