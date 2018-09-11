# Blockchain in Python
This is a simple blockchain program, which built in Python. I used this tutorial to learn how blockchain "technology" is working. \
Tutorial link: https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

One block in the chain will look like this, but you can store in it what ever you want.
```json
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```