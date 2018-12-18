	def test6(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map1, 'Campus', 'Campus')
		self.assertEqual(path, ['Campus'])
		self.assertEqual(expand.expand_count, 0)

	def test7(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map1, 'Campus', 'Waldalgesheim')
		self.assertEqual(path, [])
		self.assertEqual(expand.expand_count, 0)

	def test8(self):
		expand.expand_count = 0
		path = sc.a_star_search(dis_map, time_map1, 'Frankfurt', 'Cinema')
		self.assertEqual(path, [])
		self.assertEqual(expand.expand_count, 0)