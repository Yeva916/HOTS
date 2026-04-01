from core.base import BaseProcessor
from utils.helpers import format_data

class DataProcessor(BaseProcessor):
    def process(self, payload):
        clean_data = format_data(payload)
        return {"status": "success", "result": clean_data}
print('hello')
