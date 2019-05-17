import os

import pandas as pd

class DataHandler():

    def test_data(self,name):

        # names of files to read from
        #r_filenameCSV = '../../AutomationTesting/features'+file_name+'.csv'

        r_filenameCSV ='C:/Users/ierima/PycharmProjects/AutomationTesting/utils/data/create_new_account_test_data.csv'
        # read the data
        csv_read = pd.read_csv(r_filenameCSV,header=0)
        return csv_read[name][0]
"""
class DataHandler():

    ## Constructor initialize test data file path
    def __init__(self, test_data_sys_var_name, test_data_file_name):
        self._test_area_name = test_data_sys_var_name

        if test_data_sys_var_name in os.environ:
            self._test_area = os.environ[test_data_sys_var_name]
        else:
            raise Exception("Can't find key= %s in environment variables " % test_data_sys_var_name)

        self._test_data_file_path = findFile("testdata", test_data_file_name)
        self.dataset = testData.dataset(self._test_data_file_path)

    ## Gets test data
    # @param[in] self The self object pointer.
    # @return dictionary
    def get_test_data(self):
        d = {}
        for index, row in enumerate(self.dataset):
            col1 = testData.field(row, self._test_area_name)
            if col1 == self._test_area:
                for i, row_name in enumerate(testData.fieldNames(row)):
                    d[row_name] = testData.field(row, i)
                return d
        else:
            raise Exception("Can't find specified %s : %s in test data" % (self._test_area, self._test_area_name))

    ## Gets map region
    # @param[in] self The self object pointer.
    # @param[in] test_data_sys_var_name
    # @return string
    def get_map_region(self, test_data_sys_var_name):

        if test_data_sys_var_name in os.environ:
            self._test_area = os.environ[test_data_sys_var_name]
        else:
            raise Exception("Can't find key= %s in environment variables " % test_data_sys_var_name)

        return str(self._test_area)"""
