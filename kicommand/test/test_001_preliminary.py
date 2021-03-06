import unittest
from kicommand.kicommand import kc

class TestBasicClear(unittest.TestCase):
# conversion: mils fromsvg dict mil string list ilist index. len delist float mm pairwise int iset bool split 
# remaining:  fromsvg string ilist index. pairwise iset split 

#returnval -1 return entire stack
    def test_clear(self):
        self.assertEqual(kc('clear',returnval=-1),[])
    
    def test_BasicStack(self): # all other tests in this file need to leave the stack empty
        self.assertEqual(kc('clear 0',returnval=-1),['0'])
	
    def test_BasicstackThenClear(self):
        self.assertEqual(kc('0 clear',returnval=-1),[])

    def test_escaped(self):
        self.assertEqual(kc(r'clear 12\t34\n'),r'12\t34\n')
        self.assertEqual(kc('escaped'),'12\t34\n')

if __name__ == '__main__':
    unittest.main()
   