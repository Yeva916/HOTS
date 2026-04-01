from core.processor import DataProcessor
from constants import VERSION
import utils.hel
import utils.helpers
import utils.logger
import core.base
import core.processor
def run():
    print(f"Starting System v{VERSION}")
    proc = DataProcessor()
    print(proc.process("  TEST DATA  "))

if __name__ == "__main__":
    run()
