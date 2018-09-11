class Blockchain(object):
    def __init__(self):
        self.current_transaction = []
        self.chain = []
        
        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        # Create a new Block and adds it to the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """
        Create a new transaction to go into the next mined Block

        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transaction.append({
            'sender': sender,
            'recipient': recipient,
            'amont': amount,
        })
        
        return self.last_block
    
    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass