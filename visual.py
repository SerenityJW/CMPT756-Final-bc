from flask import Flask,jsonify
from flask import url_for, render_template,send_from_directory
import os
import json
app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

@app.route('/<node>')
def show_txt(node):
    try:
        with open(f"blockchain-{node}.txt", mode='r') as f:
            file_content = f.readlines()
            data=json.loads(file_content[0][:-1])
            peer=file_content[2]
            open_transactions=json.loads(file_content[1][:-1])
            # for i in data:
            #     if not i['transactions']:
            #         i['transactions'].append(
            #             {'sender': 'NONE', 'amount': 0, 'product_name': 'NONE', 'recipient': 'NONE', 'price': 0,
            #              'signature': 'NONE'})
            # if not open_transactions:
            #     open_transactions.append({'sender': 'NONE', 'amount': 0, 'product_name': 'NONE', 'recipient': 'NONE', 'price': 0, 'signature': 'NONE'})
        with open(f"wallet-{node}.txt", mode='r') as f:
            keys = f.readlines()
            public_key = keys[0][:-1]
            private_key = keys[1]
        return render_template("index.html", node=node, bc=data ,opt=open_transactions, peernode=peer, pubkey=public_key,
                               prikey=private_key)

    except IOError:
        response = {
            "message": "loading failed!"
        }
        return jsonify(response), 500

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
    # show_txt(5000)
    app.run()
