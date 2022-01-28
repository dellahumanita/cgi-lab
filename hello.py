#!/usr/bin/python3

import os 
import json 

# print all env variables as plain text 
# print("Content-type: text/plain\n")
# print(os.environ)

# print env variables as json
# print("Content-type: application/json\n")
# print(json.dumps(dict(os.environ), indent=2))

print('Content-Type: text/html\n')
print(f'<p>QUERY_STRING: {os.environ["QUERY_STRING"]}</p>')
print(f'<p>HTTP_USER_AGENT: {os.environ["HTTP_USER_AGENT"]}</p>')