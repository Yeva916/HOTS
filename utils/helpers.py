from utils.logger import get_logger

logger = get_logger("HelperModule")

def format_data(data):
    logger.info("Formatting data...")
    return f"Data: {data.strip().lower()}"
print('')
