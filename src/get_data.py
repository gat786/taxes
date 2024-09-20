import pandas as pd
import setup
import logging

logger = logging.getLogger()

def load_statement(financial_year: str) -> pd.DataFrame:
  file_path = f"{setup.statements_dir}/cleaned/{financial_year}.csv"
  try:
    statemnent_df = pd.read_csv(file_path)
    return statemnent_df
  except Exception as e:
    logger.error(f"Unable to fetch statement file for the provided: {financial_year}, exiting.")
    logger.error(f"Please make sure that the file exists on path: {file_path}")
    exit(-1)
