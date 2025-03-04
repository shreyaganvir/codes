"""
Date    20th July 2024
@author Shreyali Ganvir

n3 hub Challenge Devops / Python Developer
Q1- Python script for CSV file generation
"""

import os
import re
import random
import string
import pandas as pd
import argparse as ag
import logging as log
from pathlib import Path
from datetime import datetime
from typing import Union, List


def cmdargs() -> ag.Namespace:
    """
    function to take command line arguments as Input using argparse
    :return: Namespace object from argumentparser
    """
    parser = ag.ArgumentParser(description="Generate a CSV file with random data. "
                                           "Usage python3 gen.py --rows <rows> "
                                           "--column <column_name,type> "
                                           "--output_path <path>")

    parser.add_argument('--rows', type=int, default=50,
                        help="Number of rows in the CSV file. Default no.or rows is 50.")
    parser.add_argument('--output_path', type=str, default=os.getcwd(),
                        help="Directory to save the CSV file. Default path is the current working directory.")
    parser.add_argument('--column', action='append', required=True,
                        help="Specify required column option as column_name,type. Type can be 'integer' or 'string'")

    args_obj = parser.parse_args()
    return args_obj


def validate_cmdargs(args_obj: ag.Namespace) -> bool:
    """
    function to validate command line arguments
    :param args_obj: Namespace object from argument parser
    :return: bool
    """
    column = args_obj.column
    if not column:
        log.error("One column must be specified using --column.")
        return False
    for each_col in column:
        if len(each_col.split(',')) > 1:
            column_type = each_col.split(',')[-1]
            if not (re.match(r'^(int|integer|str|string)$', column_type, re.IGNORECASE)):
                raise ValueError("Unsupported column type: {}.".format(column_type))
        else:
            log.error("Invalid column option.  Column option should be provided as 'column_name,type.' ")
            return False
    return True


def generate_random_data(column_type: str) -> Union[int, str]:
    """
    function to generate random data in given datatype using random
    :param column_type: datatype of column
    :return: random data in integer or string
    """
    if column_type in ('integer', 'int'):
        return random.randint(1, 10000)
    elif column_type in ('string', 'str'):
        return ''.join(random.choices(string.ascii_letters, k=random.randint(1, 10)))


def create_dataframe(rows: int, columns: List[str]) -> pd.DataFrame:
    """
    function to create dataframe from given columns and rows
    :param rows: no. of rows
    :param columns: list of column name and type
    :return: dataframe
    """
    data = {col.split(',')[0]: [generate_random_data(col.split(',')[1]) for _ in range(rows)]
            for col in columns}
    return pd.DataFrame(data)


def save_dataframe_to_csv(df_obj: pd.DataFrame, output_path: str) -> None:
    """
    function to save dataframe as csv in given output path
    :param df_obj: dataframe object
    :param output_path: output path to save csv file
    :return: None
    """
    current_time = datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
    filename = "{}/{}.csv".format(Path(output_path), current_time)
    df_obj.to_csv(filename, index=False)
    log.info("CSV file generated at {}".format(filename))


if __name__ == '__main__':
    cmdargs_obj = cmdargs()
    if validate_cmdargs(cmdargs_obj):
        df = create_dataframe(cmdargs_obj.rows, cmdargs_obj.column)
        save_dataframe_to_csv(df, cmdargs_obj.output_path)
