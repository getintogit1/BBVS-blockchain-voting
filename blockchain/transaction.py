
class Transaction:
    def __init__(self, sender_wallet, receiver_wallet):
        self.sender = sender_wallet.address
        self.receiver = receiver_wallet.address

    def to_dict(self):
        return {
            "from": self.sender,
            "to": self.receiver,
        }

    def __repr__(self):
        sender_short = self.sender[:8]
        receiver_short = self.receiver[:8]
        return f"Transaction({sender_short} ➔ {receiver_short})"

