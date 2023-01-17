"""
A simple Blockchain in Python
tuto from : https://geekflare.com/fr/create-a-blockchain-with-python/
"""

import hashlib

class GeekCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


#exercice de simplification :
message = "Python is great"
h1 = hashlib.sha256(message.encode())

print(h1)
#réponse : 0x000002ED65989850
print(h1.hexdigest())
#réponse : a40cf9cca5eaa9d6e3e25d78a004099a89a075da5facee107a3cd5ae1142ab97
#la fonction hexdigest() renvoie les données au format hexadécimal

h2 = hashlib.sha256(b"Python is not great")
print(h2.hexdigest())
#réponse : fefe510a6a15e1f5892234e0e6e311134e4a30a6752127d9d7d697e010c0ea34


#maintenant, utilions la class block:
t1 = "Noah sends 50 euros to Mark"
t2 = "Mark sends 23 euros to James"
t3 = "James sends 4000 euros to Alisson"
t4 = "Alisson sends 1000 euros to Noah"

block1 = GeekCoinBlock('firstblock', [t1, t2])

print(f"Block 1 data: {block1.block_data}")
#réponse : Noah sends 50 euros to Mark - Mark sends 23 euros to James - firstblock
print(f"Block 1 hash: {block1.block_hash}")
#réponse : 71e263717bb4616d55e31d39fcaebcb06a9d21267fc24a07510b5fa4873b8602
#le message a été encodé et exdigéré

block2 = GeekCoinBlock(block1.block_hash, [t3, t4])

print(f"Block 2 data: {block2.block_data}")
#réponse : James sends 4000 euros to Alisson - Alisson sends 1000 euros to Noah - 71e263717bb4616d55e31d39fcaebcb06a9d21267fc24a07510b5fa4873b8602
#ici on a les transactions t3 et t4 ainsi que le hash du block 1
print(f"Block 2 hash: {block2.block_hash}")
#réponse : 9c7d49d8879e765f4212809cb4d8b2eb78198786a5a2a4c20971904f640502a0
#le nouveau hash du block 2

#on va essayer de coder une blockchain :


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(GeekCoinBlock("0", ['Genesis Block']))
    
    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(GeekCoinBlock(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]

t1 = "George sends 3.1 GC to Joe"
t2 = "Joe sends 2.5 GC to Adam"
t3 = "Adam sends 1.2 GC to Bob"
t4 = "Bob sends 0.5 GC to Charlie"
t5 = "Charlie sends 0.2 GC to David"
t6 = "David sends 0.1 GC to Eric"

myblockchain = Blockchain()

myblockchain.create_block_from_transaction([t1, t2])
myblockchain.create_block_from_transaction([t3, t4])
myblockchain.create_block_from_transaction([t5, t6])

print(myblockchain.display_chain())

#réponse : 
#Data 1: Genesis Block - 0
#Hash 1: 39331a6a2ea1cf31a5014b2a7c9e8dfad82df0b0666e81ce04cf8173cc5aed3e

#Data 2: George sends 3.1 GC to Joe - Joe sends 2.5 GC to Adam - 39331a6a2ea1cf31a5014b2a7c9e8dfad82df0b0666e81ce04cf8173cc5aed3e
#Hash 2: 98cf363aecb33989aea0425a3c1287268bd86f63851bc08c0734a31db08506d5

#Data 3: Adam sends 1.2 GC to Bob - Bob sends 0.5 GC to Charlie - 98cf363aecb33989aea0425a3c1287268bd86f63851bc08c0734a31db08506d5
#Hash 3: 6f1cfcc3082488b97db8fdf8ed33f9ac7519be3e285a37a6fcc2f1904f373589

#Data 4: Charlie sends 0.2 GC to David - David sends 0.1 GC to Eric - 6f1cfcc3082488b97db8fdf8ed33f9ac7519be3e285a37a6fcc2f1904f373589
#Hash 4: 869df2f03c9860767d35b30a46233fbeea89a3000ae5019d1491e3829d1ab929

