
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import leadzero
import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from os import listdir
from os.path import isfile, join

from pathlib import Path

class TestLeadzero(unittest.TestCase):

    def test_parser_reverse(self):
        parser = leadzero.parse_args(['-r'])
        self.assertTrue(parser.remove)

    def test_parser_length(self):
        parser = leadzero.parse_args(['-l', '3'])
        self.assertTrue(parser.length)
        self.assertEqual(parser.length, '3')

    def test_parser_type(self):
        parser = leadzero.parse_args(['-t', 'png'])
        self.assertTrue(parser.type)
        self.assertEqual(parser.type, 'png')

    def test_main(self):
        files_to_create = ["1.jpg", "2.jpg", "a.jpg", "10.jpg", "100.jpg"]
        setup(files_to_create)
        expected_file_list = ["01.jpg", "02.jpg", "0a.jpg", "10.jpg", "100.jpg"]
        expected_file_list.sort()
        del sys.argv[1:]
        leadzero.main()
        result_list = results()
        cleanup(expected_file_list)
        self.assertEqual(expected_file_list, result_list)

    def test_main_remove(self):
        files_to_create = ["01.jpg", "02.jpg", "0a.jpg", "10.jpg", "100.jpg"]
        setup(files_to_create)

        expected_file_list = ["1.jpg", "2.jpg", "a.jpg", "10.jpg", "100.jpg"]
        expected_file_list.sort()

        sys.argv.append("-r")
        
        leadzero.main()

        result_list = results()

        cleanup(expected_file_list)
        self.assertEqual(expected_file_list, result_list)

    def test_not_lead_other_file_types(self):
        files_to_create = ["1.png", "2.png"]
        setup(files_to_create)

        leadzero.main()

        result_list = results([".png"])
        cleanup(files_to_create)
        self.assertEqual(result_list, files_to_create)

    def test_lead_other_file_types(self):
        files_to_create = ["1.png", "2.png", "1.jpg", "02.jpg"]
        expected_files = ["01.png", "02.png", "1.jpg", "02.jpg"]
        expected_files.sort()
        setup(files_to_create)

        sys.argv.append("-t")
        sys.argv.append("png")
        leadzero.main()

        result_list = results([".png", ".jpg"])

        cleanup(expected_files)
        self.assertEqual(expected_files, result_list)

    def test_the_same_file_after_remove(self):
        files_to_create = ["1.jpg", "01.jpg"]
        setup(files_to_create)
        self.assertRaises(ValueError, leadzero.main)
        cleanup(files_to_create)

    def test_the_same_file_after_lead(self):
        files_to_create = ["1.jpg", "01.jpg"]
        setup(files_to_create)
        sys.argv.append("-r")
        self.assertRaises(ValueError, leadzero.main)
        cleanup(files_to_create)

def results(extensions=[".jpg"]):
    result_list = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f)) ]
    result_list = [f for f in result_list if f[-4:] in extensions]
    result_list.sort()
    return result_list

def setup(files_to_create):
    for f in files_to_create:
        Path(f).touch()

def cleanup(files_to_clean):
    """

    :rtype: object
    """
    for f in files_to_clean:
        try:
            os.remove(f)
        except:
            pass

if __name__ == '__main__':
    unittest.main()
    #print(results(".png"))
