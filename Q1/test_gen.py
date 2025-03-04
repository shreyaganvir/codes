"""
Date    20th July 2024
@author Shreyali Ganvir

Test for gen.py
"""
import unittest
from gen import *
from unittest.mock import MagicMock


class TestValidateCmdArgs(unittest.TestCase):

    def setUp(self):
        self.args_obj = MagicMock()

    def test_no_column_specified(self):
        self.args_obj.column = []
        self.assertFalse(validate_cmdargs(args_obj=self.args_obj))

    def test_invalid_column_format(self):
        self.args_obj.column = ["col1"]
        self.assertFalse(validate_cmdargs(args_obj=self.args_obj))

    def test_valid_integer_column_type(self):
        self.args_obj.column = ["col1,int"]
        self.assertTrue(validate_cmdargs(args_obj=self.args_obj))

    def test_valid_string_column_type(self):
        self.args_obj.column = ["col1,string"]
        self.assertTrue(validate_cmdargs(args_obj=self.args_obj))

    def test_valid_mixed_column_types(self):
        self.args_obj.column = ["col1,int", "col2,string", "col3,integer", "col4,str"]
        self.assertTrue(validate_cmdargs(args_obj=self.args_obj))


class TestGenCSV(unittest.TestCase):

    def test_generate_random_data_integer(self):
        data = generate_random_data(column_type='integer')
        self.assertIsInstance(data, int)
        self.assertTrue(1 <= data <= 10000)

    def test_generate_random_data_string(self):
        data = generate_random_data(column_type='string')
        self.assertIsInstance(data, str)
        self.assertTrue(1 <= len(data) <= 10)

    def test_create_dataframe(self):
        rows = 10
        columns = ['name,string', 'age,integer']
        df_obj = create_dataframe(rows=rows, columns=columns)
        self.assertEqual(len(df_obj), rows)
        self.assertListEqual(list(df_obj.columns), ['name', 'age'])

    def test_save_dataframe_to_csv(self):
        rows = 10
        columns = ['name,string', 'age,integer']
        df_obj = create_dataframe(rows=rows, columns=columns)
        save_dataframe_to_csv(df_obj=df_obj, output_path=os.getcwd())
        current_time = datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
        filename = "{}.csv".format(current_time)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)


if __name__ == '__main__':
    unittest.main()
