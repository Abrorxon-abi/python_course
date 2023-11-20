from uuid import uuid4

class TechOrder:
    def __init__(self, description, severity, status, order_id=None) -> None:
        self.order_id = order_id or uuid4()
        self.description = description
        self.status = status
        self.severity = severity
        
    def create_order(self):
        print(f'making order with id: {self.order_id}')

        
order_1 = TechOrder(1, 2, 3)

order_1.create_order()
        