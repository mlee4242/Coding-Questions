import unittest
import timeseries

#test cases for timeseries.py
class TimeSeriesTestCases(unittest.TestCase):
    #edge case - if the ones in the minutes value is 0
    def test_determine_bucket_edge1(self):
        self.assertEqual(timeseries.determine_bucket("2018-08-01T18:30:00.000Z"), "2018-08-01T18:30:00.000Z to 2018-08-01T18:34:59.999Z")

    #edge case - if the ones in the minutes value is 5, it should be in a different bucket than the test above
    def test_determine_bucket_edge2(self):
        self.assertEqual(timeseries.determine_bucket("2018-08-01T18:35:00.000Z"), "2018-08-01T18:35:00.000Z to 2018-08-01T18:39:59.999Z")        
        
    #if in the 0:00.000 to 4:59.999 bucket
    def test_determine_bucket_0_to_4(self):
        self.assertEqual(timeseries.determine_bucket("2018-09-01T19:32:30.900Z"), "2018-09-01T19:30:00.000Z to 2018-09-01T19:34:59.999Z")

    #if in the 5:00:000 to 5:59:999 bucket
    def test_determine_bucket_5_to_9(self):
        self.assertEqual(timeseries.determine_bucket("2018-09-01T19:38:30.900Z"), "2018-09-01T19:35:00.000Z to 2018-09-01T19:39:59.999Z")

    #read in an empty file
    def test_populate_interval_dict_empty_file(self):
        self.assertEqual(timeseries.populate_interval_dict("empty_test.csv"), {})

    #read in a non-empty file
    def test_populate_interval_dict_nonempty_file(self):
        self.assertEqual(timeseries.populate_interval_dict("test_timeseries.csv"), 
            {'2018-08-01T18:50:00.000Z to 2018-08-01T18:54:59.999Z': [('memory', '0.47'), ['disk', '0.60'], ['cpu', '0.18'], ['memory', '0.26'], ['disk', '0.59'], ['cpu', '0.88']],
             '2018-08-01T18:25:00.000Z to 2018-08-01T18:29:59.999Z': [('cpu', '0.10'), ['memory', '0.11'], ['disk', '0.73']],
             '2018-08-01T19:10:00.000Z to 2018-08-01T19:14:59.999Z': [('memory', '0.09'), ['disk', '0.51'], ['cpu', '0.0']]})

    #1 number in list
    def test_calculate_mean_one_number(self):
        self.assertEqual(timeseries.calculate_mean([3]), 3)

    #>1 number in list
    def test_calculate_mean_general_list(self):
        self.assertEqual(timeseries.calculate_mean([3, 6, 2, 5]), 4)

    #general test case for calculating std
    def test_calculate_std(self):
        self.assertAlmostEqual(timeseries.calculate_std([1,6,2,3], 3), 1.870828693387)

    #general test case for extracting values of a specified label out of a dictionary
    def test_extract_label_values(self):
        self.assertEqual(timeseries.extract_label_values(
            {'2018-08-01T18:50:00.000Z to 2018-08-01T18:54:59.999Z': [('memory', '0.47'), ['disk', '0.60'], ['cpu', '0.18'], ['memory', '0.26'], ['disk', '0.59'], ['cpu', '0.88']],
            '2018-08-01T18:25:00.000Z to 2018-08-01T18:29:59.999Z': [('cpu', '0.10'), ['memory', '0.11'], ['disk', '0.73']]},
            '2018-08-01T18:50:00.000Z to 2018-08-01T18:54:59.999Z',
            'memory'
            ), 
            [0.47, 0.26])

if __name__ == '__main__':
    unittest.main()