import random
import string
import pandas as pd


class DataHandler():

    # Read data from csv files
    # name - the header of a column
    # row_value - de desired email for witch you want to get account information
    def test_data(self, header, row_value):

        # name of file to read from
        file_name = 'accounts_information_test_data'
        r_filename_csv = 'C:/Users/ierima/PycharmProjects/AutomationTesting/utils/data/' + file_name + '.csv'

        # read the data
        csv_read = pd.read_csv(r_filename_csv)
        for index, value in enumerate(csv_read['email']):
            if value == row_value:
                location_in_csv = index
                break
        else:
            raise Exception("Can't find specified  %s. Not found in CSV %s" % (row_value, file_name))

        return csv_read[header][location_in_csv]

    # Rendom emails
    domains = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
    letters = string.ascii_lowercase[:26]

    def generate_random_emails(self):
        return \
            [self.get_one_random_name(self.letters) + '@' + self.get_one_random_domain(self.domains) for i in range(1)][
                0]

    def get_one_random_domain(self, domains):
        return random.choice(domains)

    def get_one_random_name(selff, letters):
        return ''.join(random.choice(letters) for i in range(7))
