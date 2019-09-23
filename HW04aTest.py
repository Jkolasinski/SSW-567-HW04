#Jakub Kolasinski
#HW04a Testing

from HW04aKolasinski import reposcommits

import unittest

class testreposcommits(unittest.TestCase):
    def testrepcommit(self):
        self.assertEqual(2, len(reposcommits("jkolasinski")))
        self.assertEqual(2, reposcommits("jkolasinski").get("SSW-567-HW01"))
        self.assertEqual(7, reposcommits("jkolasinski").get("SSW-567-HW02"))
        

        
        
        
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()