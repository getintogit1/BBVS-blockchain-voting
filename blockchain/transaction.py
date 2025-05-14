
class Transaction:
    def __init__(self, sender_wallet, receiver_wallet):
        self.sender = sender_wallet.hash
        self.receiver = receiver_wallet.hash

    def to_dict(self):
        return {
            "from": self.sender,
            "to": self.receiver,
        }

    def __repr__(self):
        sender_short = self.sender[:6]
        receiver_short = self.receiver[:6]
        return f"Transaction({sender_short} ➔ {receiver_short})"

