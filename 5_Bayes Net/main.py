from bayesnet import BayesNet, BayesNode
from student_code import ask
import unittest

class BayesTest(unittest.TestCase):

	def makeBurglaryNet(self):
		bn = BayesNet()
		bn.add(BayesNode('Burglar',None,{'':0.001}))
		bn.add(BayesNode('Earthquake',None,{'':0.002}))
		bn.add(BayesNode('Alarm',['Burglar','Earthquake'],
			{(False,False):0.001,(False,True):0.29,(True,False):0.94,(True,True):0.95}))
		bn.add(BayesNode('JohnCalls', ['Alarm'], {True:0.9,False:0.05}))
		bn.add(BayesNode('MaryCalls', ['Alarm'], {True:0.7,False:0.01}))
		return bn

	def test1(self):
		bn = self.makeBurglaryNet()
		a = ask('Alarm', True, {'Burglar':True, 'Earthquake':True}, bn)
		print('P(a|b,e)=',a)
		self.assertAlmostEqual( 0.95, a)

	def test2(self):	
		bn = self.makeBurglaryNet()
		a = ask('Burglar', True, {'JohnCalls':True,'MaryCalls':True}, bn)
		print('P(b|j,m)=',a)
		self.assertAlmostEqual( 0.2841718, a)

	def test3(self):	
		bn = self.makeBurglaryNet()
		a = ask('Alarm', True, {}, bn)
		print('P(a)=',a)
		self.assertAlmostEqual( 0.002516442, a)

	def test4(self):	
		bn = self.makeBurglaryNet()
		a = ask('Alarm', True, {'Burglar':False}, bn)
		print('P(a|-b)=',a)
		self.assertAlmostEqual( 0.001578, a)

	def test5(self):	
		bn = self.makeBurglaryNet()
		a = ask('Earthquake', False, {'Burglar':True}, bn)
		print('P(-e)=',a)
		self.assertAlmostEqual( 0.998, a)


if __name__== "__main__":
	unittest.main()


