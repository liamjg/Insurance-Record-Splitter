import split_insurance_records
import unittest


class SplitInsuranceRecordsTest(unittest.TestCase):

    def test_sort_csv_by_last_name(self):
        test_rows = [["fstone", "Fred Bravo", 1, "insurance_1"],
                     ["barney", "Barney Charlie", 1, "insurance_2"],
                     ["wilma", "Wilma Alfa", 1, "insurance_1"]]

        expected_rows = [
            ["wilma", "Wilma Alfa", 1, "insurance_1"],
            ["fstone", "Fred Bravo", 1, "insurance_1"],
            ["barney", "Barney Charlie", 1, "insurance_2"]]

        sorted_rows = split_insurance_records.sort_csv_by_last_name(test_rows)
        self.assertEqual(expected_rows, sorted_rows)

    def test_process_csv(self):
        test_rows = [["fstone", "Fred Bravo", 1, "insurance_1"],
                     ["barney", "Barney Charlie", 1, "insurance_2"],
                     ["wilma", "Wilma Alfa", 1, "insurance_3"],
                     ["scoob", "Scooby Doo", 1, "insurance_2"],
                     ["wilma", "Wilma Alfa", 2, "insurance_3"]]

        expected_seperated_files = {"insurance_1": [["fstone", "Fred Bravo", 1, "insurance_1"]],
                                    "insurance_2": [["barney", "Barney Charlie", 1, "insurance_2"], ["scoob", "Scooby Doo", 1, "insurance_2"]],
                                    "insurance_3": [["wilma", "Wilma Alfa", 2, "insurance_3"]]}

        seperated_files = split_insurance_records.process_csv(test_rows)
        self.assertEqual(expected_seperated_files, seperated_files)


if __name__ == '__main__':
    unittest.main()
