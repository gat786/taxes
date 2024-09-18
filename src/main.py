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

  statement["CR"] = statement["CR"].str.strip()
  statement["DR"] = statement["DR"].str.strip()

  statement["DR"] = statement["DR"].replace(to_replace="",value="0.00")
  statement["CR"] = statement["CR"].replace(to_replace="",value="0.00")

  statement["DR"] = statement["DR"].astype(float).astype(int)
  statement["CR"] = statement["CR"].astype(float).astype(int)

  credit_records = statement[statement["DR"] == 0]
  debit_records  = statement[statement["CR"] == 0]

  # logger.info(credit_records)
  # logger.info(debit_records)

  total_credits = credit_records["CR"].sum()
  total_debits  = debit_records["DR"].sum()

  logger.info(f"Total Credits: {total_credits}")
  logger.info(f"Total Debits: {total_debits}")

  # credits which have USD in their PARTICULARS column
  usd_credits = credit_records[credit_records["PARTICULARS"].str.contains("USD")]
  usd_credits_total = usd_credits["CR"].sum()

  # Print each USD credit record with Tran Date, BAL and SOL
  for index, row in usd_credits.iterrows():
    print(f"{index}: {row["Tran Date"]}\t{row["PARTICULARS"]}\t{row["CR"]}\t{row["BAL"]}\t{row["SOL"]}")
  logger.info(f"USD Credits: {usd_credits_total}")

  
if __name__ == "__main__":
  process_statement()
