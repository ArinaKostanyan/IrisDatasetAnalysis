from iris_statistics.iris_data_analysis import StatisticsCalculator


def statistics_calculator():
    data_path = "data/iris_bezdekIris.xlsx"
    out_filename = "output/iris_dataset_statistics"
    output_type = ".xlsx"

    calculator = StatisticsCalculator(data_path)
    calculator.compute_statistics()

    calculator.export_to_excel(out_filename + output_type)


if __name__ == "__main__":
    statistics_calculator()
