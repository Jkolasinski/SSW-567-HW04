#Jakub Kolasinski
#HW04a Testing

from HW04aKolasinski import reposcommits


import unittest
from unittest import mock

class testreposcommits(unittest.TestCase):
    @mock.patch('requests.get')
    def testrepcommit(self, mockapi):
        mockapi.return_value.json.return_value = ([{"github":1,"name":"Repo_A"},{"github":2,"name":"Repo_B"}])
        self.assertEqual(2, len(reposcommits("jkolasinski")))
        self.assertEqual(2, reposcommits("jkolasinski").get("Repo_A"))
        self.assertEqual(2, reposcommits("jkolasinski").get("Repo_B"))
        

        
        
        
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()