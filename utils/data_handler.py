import random
import string
import pandas as pd

class DataHandler():

    # Read data from csv files
    # name - the header of a column
    # row_value - de desired email for witch you want to get account information
    def test_data(self, header, row_value):

        # name of file to read from
        #r_filenameCSV = '../../AutomationTesting/features'+file_name+'.csv'

        r_filenameCSV ='C:/Users/ierima/PycharmProjects/AutomationTesting/utils/data/accounts_information_test_data.csv'

        # read the data
        csv_read = pd.read_csv(r_filenameCSV)
        for index,value in enumerate(csv_read['email']):
            if value == row_value:
                location_in_csv = index
                break
        else:
            raise Exception('Value %s not found in CSV' %row_value)
        return csv_read[header][location_in_csv]



    domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
    letters = string.ascii_lowercase[:12]

    def generate_random_emails(self):
        return [self.get_one_random_name(self.letters) + '@' + self.get_one_random_domain(self.domains) for i in range(1)][0]

    def get_one_random_domain(self,domains):
        return random.choice(domains)

    def get_one_random_name(selff,letters):
        return ''.join(random.choice(letters) for i in range(7))



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
