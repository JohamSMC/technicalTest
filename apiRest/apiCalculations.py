import pandas as pd

class ApiCalculations():
	startList = []
	endList = []
	iriList = []

	def executeCalculations(self, inicio, fin, paso):
		ApiCalculations.loadData(self)
		return ApiCalculations.iri_weighted_average(self, inicio, fin, paso)

	def loadData(self):
		data = pd.read_csv('static/datos_prueba_tecnica.csv', sep=';')
		self.startList = data.Inicio.values.tolist()
		self.endList = data.Fin.values.tolist()
		self.iriList = data.IRI.values.tolist()

		self.startList = [int(el) for el in self.startList]
		self.endList = [int(el) for el in self.endList]
		self.iriList = [float(el.replace(',','.')) for el in self.iriList]

		#return [startList, endList, iriList]

	def iri_weighted_average(self, inicio, fin, paso):
		if inicio ==  fin:
			return {"Error":"El valor de inicio es igual al valor de fin"}
		if inicio > fin:
			return {"Error":"El valor de inicio es mayor al valor de fin"}
		if fin > self.endList[-1]:
			return {"Error":"El valor de final es superior al maximo permitido"}
		if inicio < self.startList[0]:
			return {"Error":"El valor de inicio es inferior al minimo permitido"}
		if paso <= 0:
			return {"Error":"El valor de paso debe ser mayor a 0"}

		outputs = []
		startIteration = inicio
		endIteration = startIteration + paso

		while endIteration <= fin and startIteration != endIteration:
			mismatch = 0
			while not(startIteration-mismatch) in self.startList:
				mismatch +=1

			index = self.startList.index(startIteration-mismatch)
			auxStep = paso
			auxStartIteration = startIteration
			iriIteration = 0

			while not(auxStep == 0):
				stepIncrease = self.endList[index] - auxStartIteration \
							if (auxStartIteration + auxStep) >= self.endList[index] \
							else auxStep

				iriIteration += self.iriList[index] * stepIncrease
				auxStartIteration += stepIncrease
				auxStep -= stepIncrease
				index += 1

			iriIteration /= paso
			outputs.append({"inicio":startIteration, "final":endIteration , "iri":iriIteration})
			startIteration = endIteration
			endIteration = startIteration + paso \
							if (startIteration + paso) < fin \
							else fin

		#print(outputs)
		return outputs
