from unittest import TestCase
import pandas as pd


filepath1 = "./data/test_table.csv"
filepath2 = "./data/user_table.csv"

class TestCsv_to_dataframe(TestCase):
    def test_csv_to_dataframe(self):
        from build import csv_to_dataframe
        res = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res, pd.DataFrame))
        res = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_merge_dataframe(self):
        from build import csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')
        self.assertTrue(isinstance(res, pd.DataFrame))

    def test_dtype_category(self):
        from build import dtype_category, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')

        new_res = dtype_category(res, ["user_id", "sex", "country", "date", "source", "device", "browser_language", "ads_channel", "browser"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_centre_and_scale(self):
        from build import centre_and_scale, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')

        new_res = centre_and_scale(res, ["age"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_label_encoder(self):
        from build import label_encoder, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')

        new_res = label_encoder(res, ["sex","country", "source", "ads_channel", "browser"])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_one_hot_encoder(self):
        from build import one_hot_encoder, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')

        new_res = one_hot_encoder(res, ['device', 'browser_language'])
        self.assertTrue(isinstance(new_res, pd.DataFrame))

    def test_skewness(self):
        from build import skewness, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')

        new_res = skewness(res, ["age"])
        self.assertTrue(isinstance(new_res, list))

    def test_sqrt_transform(self):
        from build import sqrt_transform, csv_to_dataframe, merge_dataframe
        res1 = csv_to_dataframe(filepath1)
        self.assertTrue(isinstance(res1, pd.DataFrame))
        res2 = csv_to_dataframe(filepath2)
        self.assertTrue(isinstance(res2, pd.DataFrame))
        res = merge_dataframe(res1, res2, 'user_id')

        new_res = sqrt_transform(res, ["age"])
        self.assertTrue(isinstance(new_res, list))