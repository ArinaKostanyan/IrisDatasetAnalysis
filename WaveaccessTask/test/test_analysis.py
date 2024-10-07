import unittest
import pandas as pd
import numpy as np
from iris_statistics.iris_data_analysis import StatisticsCalculator


class TestStatisticsCalculator(unittest.TestCase):
    def setUp(self):
        self.data_path = "data/iris_bezdekIris.xlsx"
        self.calculator = StatisticsCalculator(self.data_path)
        self.calculator.compute_statistics()

    def test_load_data(self):
        self.assertIsInstance(self.calculator.iris_df, pd.DataFrame)
        self.assertFalse(self.calculator.iris_df.empty)

    def test_coefficient_of_variation(self):
        for column in self.calculator.iris_df.select_dtypes(
            include=[np.number]
        ).columns:
            mean = self.calculator.iris_df[column].mean()
            std = self.calculator.iris_df[column].std()
            if mean != 0:
                cv = std / mean
                self.assertAlmostEqual(
                    self.calculator.statistics_df.loc[
                        "coefficient_of_variation", column
                    ],
                    cv,
                    places=5,
                )
            else:
                self.assertTrue(
                    np.isnan(
                        self.calculator.statistics_df.loc[
                            "coefficient_of_variation", column
                        ]
                    )
                )


if __name__ == "__main__":
    unittest.main()
