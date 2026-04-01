from core.processor import DataProcessor
from constants import VERSION

def run():
    print(f"Starting System v{VERSION}")
    proc = DataProcessor()
    print(proc.process("  TEST DATA  "))

if __name__ == "__main__":
    run()
