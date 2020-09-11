from unittest import TestCase, TestLoader, TestSuite
from selenium import webdriver
from pyunitreport import HTMLTestRunner
from assertions import AssertionTest
from searchtest import  SearchTest

assetions_test = TestLoader().loadTestsFromTestCase(AssertionTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test=TestSuite([assetions_test,search_test])


runner=HTMLTestRunner(output='reportes', report_name='smoke-report')
runner.run(smoke_test)
