# -*- coding: utf-8 -*-
#
# run_tests.py
#
# Test framework using 
# unitest (https://docs.python.org/3/library/unittest.html)
# and
# Coverage.py (https://coverage.readthedocs.io/)
#
# Runs all test cases in the Add-on's scripts/tests/ folder and its subfolders.
# Test cases must be named test_*.py or *_test.py.
#
# Carl Zeiss GOM Metrology GmbH, 2024
# 
# ---

import gom
import sys
import os
import unittest
import coverage
import tempfile
import zipfile
import inspect
import glob
import importlib

####################################################################################
# User defined options
####################################################################################

# Analyze coverage
COVERAGE = True

# Generate HTML coverage report 
HTML = True

####################################################################################

def collect_tests(path):
	"""Collect and add test cases to the test suite
	
	Parameters:
		path (string): absolute path of test case folder
		
	Returns:
		test suite
	"""
	# Get a list of all Python files in the folder
	python_files = glob.glob(os.path.join(path, "test_*.py"))
	python_files += glob.glob(os.path.join(path, "*_test.py"))
	
	suite = unittest.TestSuite()
	
	# Loop through the list of files, import each one as a module and
	# add each function with the same name as the module to the test suite
	for file in python_files:
		file_name = os.path.splitext(os.path.basename(file))[0]
		module_name = 'tests.' + file_name
		module = importlib.import_module(module_name)
		test_function = getattr(module, file_name)
		suite.addTest(unittest.FunctionTestCase(test_function))
	
	return suite
		
	
def main():
	'''Run tests and generate coverage report'''
	
	# Get test case folder
	addon_path = gom.api.addons.get_current_addon().get_file()
	tests_path = os.path.join(addon_path, 'scripts', 'tests')
	print(f'Test case folder: {tests_path}')
	
	if COVERAGE:
		# Init coverage
		cov = coverage.Coverage(data_file=os.path.join(tests_path, '.coverage'))
		cov.erase()
		cov.start()
	
	# Run unittest with test folder
	suite = collect_tests(tests_path)
	unittest.TextTestRunner().run(suite)
	
	if COVERAGE:
		# Finalize coverage
		cov.stop()
		cov.save()
	
		# Create coverage report (text)
		cov.report(
			file=sys.stdout,
			omit=['*/gom_script_server/*', '*/gom_python_wheel_cache/*'],
			ignore_errors=True
		)


		if HTML:
			# Create coverage report (HTML) 
			html_path = os.path.join(tests_path, 'coverage_html')
			try:
				cov.html_report(
					directory=html_path, 
					omit=['*/gom_script_server/*', '*/gom_python_wheel_cache/*'],
					ignore_errors=True
				)
			except:
				pass
			
			print('\nHTML coverage report:')
			print(f'{os.path.join(html_path, "index.html")}')



if __name__ == "__main__":
	'''Check if the Add-on is in editing mode as required'''
	if sys.argv[0][0] == ':':
		# Inside a packed Add-on
		print("ERROR: Add-on must be in editing mode!")
		sys.exit(0)
	else:
		main()

