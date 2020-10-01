from django.test import TestCase, Client

# Create your tests here.
class TestApi(TestCase):

	def test_GET_correct_values_one(self):
		client = Client()

		response = client.get('/caso1/580600/580700/20')
		responseContent = [
		{"inicio": 580600,"final": 580620,"iri": 3.1},
		{"inicio": 580620,"final": 580640,"iri": 6.3},
		{"inicio": 580640,"final": 580660,"iri": 3.4},
		{"inicio": 580660,"final": 580680,"iri": 3.6},
		{"inicio": 580680,"final": 580700,"iri": 2.7}
		]

		self.assertEquals(response.status_code, 200)
		self.assertListEqual(response.json(), responseContent)

	def test_GET_correct_values_two(self):
		client = Client()
		response = client.get('/caso1/580600/580700/30')
		responseContent = [
		{"inicio": 580600,"final": 580630,"iri": 4.166666666666667},
		{"inicio": 580630,"final": 580660,"iri": 4.366666666666666},
		{"inicio": 580660,"final": 580690,"iri": 3.3},
		{"inicio": 580690,"final": 580700,"iri": 2.7}
		]
		self.assertEquals(response.status_code, 200)
		self.assertListEqual(response.json(), responseContent)

	def test_GET_incorrect_values_one(self):
		client = Client()

		response = client.get('/caso1/580700/580700/100')
		responseContent = {"Error":"El valor de inicio es igual al valor de fin"}

		self.assertEquals(response.status_code, 200)
		self.assertDictEqual(response.json(), responseContent)

	def test_GET_incorrect_values_two(self):
		client = Client()

		response = client.get('/caso1/580800/580700/20')
		responseContent = {"Error":"El valor de inicio es mayor al valor de fin"}

		self.assertEquals(response.status_code, 200)
		self.assertDictEqual(response.json(), responseContent)

	def test_GET_incorrect_values_three(self):
		client = Client()

		response = client.get('/caso1/580600/647001/20')
		responseContent = {"Error":"El valor de final es superior al maximo permitido"}

		self.assertEquals(response.status_code, 200)
		self.assertDictEqual(response.json(), responseContent)

	def test_GET_incorrect_values_four(self):
		client = Client()

		response = client.get('/caso1/580599/580800/20')
		responseContent = {"Error":"El valor de inicio es inferior al minimo permitido"}

		self.assertEquals(response.status_code, 200)
		self.assertDictEqual(response.json(), responseContent)

	def test_GET_incorrect_values_five(self):
		client = Client()

		response = client.get('/caso1/580600/580800/0')
		responseContent = {"Error":"El valor de paso debe ser mayor a 0"}

		self.assertEquals(response.status_code, 200)
		self.assertDictEqual(response.json(), responseContent)


