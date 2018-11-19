from base.BaseModel import BaseModel

class BaseAction(BaseModel):
    def __init__(self):
        super().__init__()
        print("BaseAction")
