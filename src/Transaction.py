from datetime import datetime

class Transaction:

    def __init__(self, fromAdress, toAdress, amount):
        self.fromAdress = fromAdress
        self.toAdress = toAdress
        self.amount = amount

        now = datetime.now()
        now = now.strftime("%d/%m/%Y %H:%M:%S")
        self.timestamp = now

    def isValid():
        #vedeti sa o faceti
        return True