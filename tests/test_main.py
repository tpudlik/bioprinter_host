"""
test_main.py: Tests of the main program.
"""

import os, sys
sys.path.append('..')

# Absolute path to this file, and to the directory that contains it.
abspath = os.path.abspath(__file__)
testdir = os.path.dirname(abspath)
maindir = os.path.dirname(testdir)

# Other paths of use in what follows
path_to_main = os.path.join(maindir, "main.py")
path_to_output = os.path.join(testdir, "test.gcodes")

import subprocess
from unittest import TestCase

class test_main(TestCase):

    def test_own_img_cross(self):
        path_to_png = os.path.join(maindir, "example_files", "own_img_cross.png")
        return_code = subprocess.call(["python", path_to_main, path_to_png,
                                        "--codes_file", path_to_output])

        # The code ran successfully
        assert return_code == 0

        # The results are correct
        with open(os.path.join(testdir, "own_img_cross.gcodes"), 'r') as f:
            expected_output = f.read()
        with open(path_to_output, 'r') as f:
            actual_output = f.read()

        assert expected_output == actual_output

    def test_heart(self):
        path_to_png = os.path.join(maindir, "example_files", "heart.png")
        return_code = subprocess.call(["python", path_to_main, path_to_png,
                                        "--codes_file", path_to_output])

        # The code ran successfully
        assert return_code == 0

        # The results are correct
        with open(os.path.join(testdir, "heart.gcodes"), 'r') as f:
            expected_output = f.read()
        with open(path_to_output, 'r') as f:
            actual_output = f.read()

        assert expected_output == actual_output

    def tearDown(self):
        # This function will be executed after every test in this class,
        # regardless of whether the test passes.
        files_to_remove = (path_to_output,
                           os.path.join(maindir, "example_files",
                                        "heart.arrayplot.png"),
                           os.path.join(maindir, "example_files",
                                        "own_img_cross.arrayplot.png"))
        for f in files_to_remove:
            try:
                os.remove(f)
            except OSError:
                # The file does not exist
                pass
