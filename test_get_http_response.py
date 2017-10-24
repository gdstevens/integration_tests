import unittest
from urllib.request import Request, urlopen
from urllib.request import URLError, HTTPError
import csv


class UrlTest(unittest.TestCase):
   def test_page_avaialble_test(self):
       with open("urlListing.csv")as csvfile:
           logfile = open('test.log', 'w')

           reader = csv.DictReader(csvfile)

           for row in reader:
               req = Request(str(row["URL"]))

               try:
                   response = urlopen(req)

               except HTTPError as e:
                   logfile.write("Error code: " + str(e.code) + ' ' + row['URL'] + "\n")
               except URLError as e:
                   logfile.write("Error code: " + str(e.reason) + ' ' + row['URL'])
               else:
                   continue
       logfile.close()


if __name__ == '__main__':
   unittest.main()
