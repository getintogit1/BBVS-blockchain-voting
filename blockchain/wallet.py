import hashlib
from Crypto.PublicKey import RSA


class Wallet:
    def __init__(self):
        key = RSA.generate(2048)
        self.private_key = key
        self.public_key = key.publickey()
        self._token = 0
        self._send = None
        self.address = hashlib.sha256(self.public_key.export_key()).hexdigest()

    def __repr__(self):
        return f"Wallet(pub_key={self.public_key}...)"

    def get_address(self):
        return str(self.address)

    def sendToken(self, recipient):
        if self._token != 1:
            raise Exception(
                f"Wallet {self.address[:8]} tried to send without having a token."
            )
        self._token = 0
        recipient.receiveToken()

    def receiveToken(self):
        if self._token >= 1:
            raise Exception(
                f"Wallet {self.address[:8]} tried to receive more than 1 token."
            )
        self._token += 1

    def tokenRestriction(self):
        return self._token == 0 or self._token == 1


class CandidateWallet(Wallet):
    def __init__(self, MAX_ALLOWED_TOKENS):
        super().__init__()
        self.MAX_ALLOWED_TOKENS = MAX_ALLOWED_TOKENS

    def receiveToken(self):
        if self._token >= self.MAX_ALLOWED_TOKENS:
            raise Exception(
                f"Candidate wallet {self.address[:8]} exceeded allowed tokens."
            )
        self._token += 1


class InitialWallet(Wallet):
    def __init__(self, MAX_ALLOWED_TOKENS):
        super().__init__()
        self._tokens = MAX_ALLOWED_TOKENS
        self._send = 0

    def sendToken(self, recipient):
        if self._tokens <= 0:
            raise Exception(
                f"Initial Wallet {self.address[:8]} tried to send without having a token."
            )
        self._tokens -= 1
        self._send += 1
        recipient.receiveToken()
