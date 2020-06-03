import pandas as pd
import numpy as np

file = 'Example.csv'
df = pd.read_csv(file)

#Insert necessary columns into CSV file downloaded from Infusion
def addEmptyCols():
	new_col = np.nan
	#add columns such as: df.insert(loc=37, column="Leadsource", value=new_col)
	#Save
	df.to_csv('Example.csv', index=False)

#Input Product ID's and Abbreviations based on Product Name column, export as CSV
def addProductIDs():
	#Now begin to fill the product and product type
	#Example:
	#df.loc[df["Product Names"] == 'Options Money Machine 1 Year', 'Product Type'] = "OMM 1 Year Upsell


	df.to_csv('Example.csv', index=False)



addEmptyCols()
addProductIDs()
