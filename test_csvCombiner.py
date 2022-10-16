import unittest
import csvCombiner as combiner



class TestCombiner(unittest.TestCase):
    
    def test_clg(self):

        self.assertRaises(FileNotFoundError, combiner.command_line_grab)



if __name__ == "__main__":
    unittest.main()
