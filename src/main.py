import setup
import pandas as pd
import numpy as np
import logging
import get_data

logger = logging.getLogger()

def process_statement():
  statement = get_data.load_statement("2023-24")

  # this was to evaluate what an empty value looks like
  # empty_value = statement["DR"][975]
  # logger.info(type(empty_value))
  # logger.info(len(empty_value))
  # logger.info(empty_value == " ") # <- returned true

  statement["DR"] = statement["DR"].fillna(0).astype(int)
  statement["CR"] = statement["CR"].fillna(0).astype(int)
  credit_records = statement[statement["DR"] == 0]
  debit_records  = statement[statement["CR"] == 0]

  
  logger.info(credit_records,debit_records)  

  # logger.info(total_credits, total_debits)
  
if __name__ == "__main__":
  process_statement()
