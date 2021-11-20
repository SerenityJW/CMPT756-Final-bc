from flask import Flask,jsonify
from flask import url_for, render_template,send_from_directory
import os
import json
def show_txt(node):
    with open(f"blockchain-{node}.txt", mode='r') as f:
        file_content = f.readlines()
        data=json.loads(file_content[0][:-1])
        peer=file_content[2]
        transactions=json.loads(file_content[1][:-1])
    with open(f"wallet-{node}.txt", mode='r') as f:
        keys = f.readlines()
        public_key = keys[0][:-1]
        private_key = keys[1]
    return 0

# def show_txt(node):
#     try:
#         with open(f"blockchain-{node}.txt", mode='r') as f:
#             file_content = f.readlines()
#             data=json.loads(file_content[0][:-1])
#             print(type(data))
#         with open(f"wallet-{node}.txt", mode='r') as f:
#             keys = f.readlines()
#             public_key = keys[0][:-1]
#             private_key = keys[1]
#     except IOError:
#         print('loading failed!')
#     return 0
if __name__ == "__main__":
    show_txt(5000)
