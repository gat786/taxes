import os
from dotenv import load_dotenv
import logging

load_dotenv()

logging.basicConfig(
  level=logging.INFO,
  format='%(asctime)s [%(levelname)s] %(filename)s:%(lineno)d - %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S'
)
statements_dir = os.getenv("STATEMENTS_DIR","/Users/ganeshtiwari/projects/personal/python/taxes/statements")
