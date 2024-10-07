import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

## TASK DESCRIPTION
# The program should take pandas dataframe as input, iterate through each of the columns in the
#    dataframe and based on column datatype, create summary statistics for each, and print them out in a
#    table.


class StatisticsCalculator:
    def __init__(self, data_path: str):
        """
        Initialize the StatisticsCalculator with the path to the dataset.

        :param data_path: Path to the CSV dataset.
        """
        self.data_path = data_path
        self.iris_df = self.load_data()
        self.statistics_df = pd.DataFrame()

    def load_data(self) -> pd.DataFrame:
        """
        Load the dataset into a pandas DataFrame.

        :return: pandas DataFrame containing the dataset.
        """
        try:
            df = pd.read_excel("data/iris_bezdekIris.xlsx", skiprows=1)
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_path} does not exist.")

    def compute_statistics(self):
        self.statistics_df = pd.DataFrame(
            index=[
                "column_type",
                "median",
                "mode",
                "percent_of_zeros",
                "variation",
                "interquartile_range",
                "quartile_deviation",
                "coefficient_of_variation",
                "number_of_distinct_values",
            ],
            columns=self.iris_df.columns,
        )

        # Loop over the columns of iris_df
        for column_name, column in list(self.iris_df.items()):
            column_type = column.dtype
            self.statistics_df.loc["column_type", column_name] = column_type
            self.statistics_df.loc["mode", column_name] = (
                column.mode().iloc[0] if not column.mode().empty else np.nan
            )
            self.statistics_df.loc["percent_of_zeros", column_name] = (
                column == 0
            ).mean() * 100
            self.statistics_df.loc["number_of_distinct_values", column_name] = (
                column.nunique()
            )

            if isinstance(column_type, np.dtypes.Float64DType):
                self.statistics_df.loc["median", column_name] = column.median()
                self.statistics_df.loc["variation", column_name] = column.var()
                self.statistics_df.loc["interquartile_range", column_name] = (
                    column.quantile(0.75) - column.quantile(0.25)
                )
                self.statistics_df.loc["quartile_deviation", column_name] = (
                    column.quantile(0.75) - column.quantile(0.25)
                ) / 2
                self.statistics_df.loc["coefficient_of_variation", column_name] = (
                    (column.std() / column.mean()) if column.mean() != 0 else np.nan
                )

        self.statistics_df = pd.concat([self.statistics_df, self.iris_df.describe()])
        self.statistics_df.loc["count", "species"] = column.count()

    def export_to_excel(self, output_path: str):
        """
        :param output_path: Path where the Excel file will be saved.
        """
        if self.statistics_df.empty:
            raise ValueError(
                "No statistics to export. Please run compute_statistics() first."
            )

        self.statistics_df.to_excel(output_path, sheet_name="Statistics Summary")
        print(f"Summary statistics have been saved to {output_path}")


#
#


iris_df = pd.read_excel("data/iris_bezdekIris.xlsx", skiprows=1)
out_filename = "output/iris_dataset_statistics"
output_type = ".xlsx"
