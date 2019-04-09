import pandas as pd
import numpy as np

file = 'Example.csv'
df = pd.read_csv(file)

#Insert necessary columns into CSV file downloaded from Infusion
def addEmptyCols():
	new_col = np.nan
	df.insert(loc=37, column="Leadsource", value=new_col)
	df.insert(38, column="The OG's", value=new_col)
	df.insert(39, column="Recent Sales Source", value=new_col)
	df.insert(40, column="Product Type", value=new_col)
	df.insert(41, column="Product", value=new_col)
	#Save
	df.to_csv('Example.csv', index=False)

#Input Product ID's and Abbreviations based on Product Name column, export as CSV
def addProductIDs():
	#Now begin to fill the product and product type
	df.loc[df["Product Names"] == 'Options Money Machine 1 Year', 'Product Type'] = "OMM 1 Year Upsell"
	df.loc[df["Product Names"] == 'Options Money Machine 1 Year', 'Product'] = "OMM"
	df.loc[df["Product Names"] == 'Options Money Machine 2 Year', 'Product Type'] = "OMM 2 Year Upsell"
	df.loc[df["Product Names"] == 'Options Money Machine 2 Year', 'Product'] = "OMM"
	df.loc[df["Product Names"] == 'Options Money Machine Monthly', 'Product Type'] = "OMM Monthly"
	df.loc[df["Product Names"] == 'Options Money Machine Monthly', 'Product'] = "OMM"

	df.loc[df["Product Names"] == 'Options Wealth Machine 1 Year', 'Product Type'] = "OWM 1 Year"
	df.loc[df["Product Names"] == 'Options Wealth Machine 1 Year', 'Product'] = "OWM"
	df.loc[df["Product Names"] == 'Options Wealth Machine  (2-year)', 'Product Type'] = "OMM 2 Year"
	df.loc[df["Product Names"] == 'Options Wealth Machine  (2-year)', 'Product'] = "OWM"
	df.loc[df["Product Names"] == 'Options Wealth Machine  (Monthly)', 'Product Type'] = "OWM Monthly"
	df.loc[df["Product Names"] == 'Options Wealth Machine  (Monthly)', 'Product'] = "OWM"
	df.loc[df["Product Names"] == 'OWM 2 Year Discount (1995)', 'Product Type'] = "OMM 2 Year"
	df.loc[df["Product Names"] == 'OWM 2 Year Discount (1995)', 'Product'] = "OWM"

	df.loc[df["Product Names"] == 'The Ultimate Options Trading Strategy', 'Product Type'] = "Ultimate Options Trading Strategy"
	df.loc[df["Product Names"] == 'The Ultimate Options Trading Strategy', 'Product'] = "UOTSG"

	df.loc[df["Product Names"] == 'Marijuana Insider Report', 'Product Type'] = "Marijuana Insider Report"
	df.loc[df["Product Names"] == 'Marijuana Insider Report', 'Product'] = "MIR"

	df.loc[df["Product Names"] == 'Marijuana Insider Report - Lifetime', 'Product Type'] = "Marijuana Insider Report"
	df.loc[df["Product Names"] == 'Marijuana Insider Report - Lifetime', 'Product'] = "MIR"


	df.loc[df["Product Names"] == 'YOLO Legacy', 'Product Type'] = "O360"
	df.loc[df["Product Names"] == 'YOLO Legacy', 'Product'] = "O360"

	df.loc[df["Product Names"] == 'Adam Mesh Coaching Program', 'Product Type'] = "Coaching"
	df.loc[df["Product Names"] == 'Adam Mesh Coaching Program', 'Product'] = "Coaching"

	df.loc[df["Product Names"] == 'Christian/Adam Group Call', 'Product Type'] = "Christian Group Call"
	df.loc[df["Product Names"] == 'Adam Mesh Coaching Program', 'Product'] = "Group Call"

	df.loc[df["Product Names"] == 'Earnings 360 Package', 'Product Type'] = "E360"
	df.loc[df["Product Names"] == 'Earnings 360 Package', 'Product'] = "E360"
	df.loc[df["Product Names"] == 'Earnings360 Quarterly', 'Product Type'] = "E360"
	df.loc[df["Product Names"] == 'Earnings360 Quarterly', 'Product'] = "E360"

	df.loc[df["Product Names"] == 'ETF Accelerator FC', 'Product Type'] = "ETF FC"
	df.loc[df["Product Names"] == 'ETF Accelerator FC', 'Product'] = "ETF"

	df.loc[df["Product Names"] == 'ETF Money Cycle 1 Year', 'Product Type'] = "ETF 1 Year"
	df.loc[df["Product Names"] == 'ETF Money Cycle 1 Year', 'Product'] = "ETF"

	df.loc[df["Product Names"] == 'ETF Money Cycle 2 Year', 'Product Type'] = "ETF 2 Year"
	df.loc[df["Product Names"] == 'ETF Money Cycle 2 Year', 'Product'] = "ETF"

	df.loc[df["Product Names"] == 'Friday Profit', 'Product Type'] = "Friday Profit"
	df.loc[df["Product Names"] == 'Friday Profit', 'Product'] = "Friday Profit"

	df.loc[df["Product Names"] == 'Full Contact Trading', 'Product Type'] = "FCTS"
	df.loc[df["Product Names"] == 'Full Contact Trading', 'Product'] = "FCTS" 
	df.loc[df["Product Names"] == 'Full Contact Trading System', 'Product Type'] = "FCTS"
	df.loc[df["Product Names"] == 'Full Contact Trading System', 'Product'] = "FCTS" 

	df.loc[df["Product Names"] == 'Mesh Insider Monthly', 'Product Type'] = "Mesh Insider"
	df.loc[df["Product Names"] == 'Mesh Insider Monthly', 'Product'] = "Mesh Insider"
	df.loc[df["Product Names"] == 'Mesh Insider', 'Product Type'] = "Mesh Insider"
	df.loc[df["Product Names"] == 'Mesh Insider', 'Product'] = "Mesh Insider"

	df.loc[df["Product Names"] == 'Mesh Private Portfolio', 'Product Type'] = "MPP"
	df.loc[df["Product Names"] == 'Mesh Private Portfolio', 'Product'] = "MPP"

	df.loc[df["Product Names"] == 'Mesh Private Portfolio - Payment Plan', 'Product Type'] = "Mesh Private"
	df.loc[df["Product Names"] == 'Mesh Private Portfolio - Payment Plan', 'Product'] = "Mesh Private"

	df.loc[df["Product Names"] == 'The Next Big Profit', 'Product Type'] = "Next Big Profit"
	df.loc[df["Product Names"] == 'The Next Big Profit (pretty)', 'Product Type'] = "Next Big Profit Pretty"
	df.loc[df["Product Names"] == 'Next Big Profit Upsell', 'Product Type'] = "Next Big Profit Upsell"
	df.loc[df["Product Names"] == 'The Next Big Profit', 'Product'] = "NBP"
	df.loc[df["Product Names"] == 'The Next Big Profit (pretty)', 'Product'] = "NBP"
	df.loc[df["Product Names"] == 'Next Big Profit Upsell', 'Product'] = "NBP"
	df.loc[df["Product Names"] == 'Next Big Profit Lifetime', 'Product Type'] = "Next Big Profit Lifetime"
	df.loc[df["Product Names"] == 'Next Big Profit Lifetime', 'Product'] = "NBP"

	df.loc[df["Product Names"] == 'Phoenix Monthly', 'Product Type'] = "Phoenix Monthly"
	df.loc[df["Product Names"] == 'Phoenix Yearly', 'Product Type'] = "Phoenix Yearly"
	df.loc[df["Product Names"] == 'Phoenix $19 Trial', 'Product Type'] = "Phoenix $19 Trial"
	df.loc[df["Product Names"] == 'Phoenix Monthly', 'Product'] = "Phoenix"
	df.loc[df["Product Names"] == 'Phoenix Yearly', 'Product'] = "Phoenix"
	df.loc[df["Product Names"] == 'Phoenix $19 Trial', 'Product'] = "Phoenix"

	df.loc[df["Product Names"] == 'ProfitPoint', 'Product Type'] = "ProfitPoint"
	df.loc[df["Product Names"] == 'ProfitPoint', 'Product'] = "ProfitPoint"

	df.loc[df["Product Names"] == 'Smart Money Prime', 'Product Type'] = "Smart Money Prime"
	df.loc[df["Product Names"] == 'Smart Money Prime', 'Product'] = "SMP" 
	df.loc[df["Product Names"] == 'Smart Money Elite', 'Product Type'] = "Smart Money Elite"
	df.loc[df["Product Names"] == 'Smart Money Elite', 'Product'] = "SME" 

	df.loc[df["Product Names"] == 'Smart Trades', 'Product Type'] = "Smart Trades"
	df.loc[df["Product Names"] == 'Smart Trades', 'Product'] = "Smart Trades"

	df.loc[df["Product Names"] == 'The 2019 & Beyond Success Formula', 'Product Type'] = "Beyond Success Formula"
	df.loc[df["Product Names"] == 'The 2019 & Beyond Success Formula', 'Product'] = "Beyond Success Formula"

	df.loc[df["Product Names"] == 'The Profit Machine 2 Year', 'Product Type'] = "Profit Machine 2 Year"
	df.loc[df["Product Names"] == 'The Profit Machine 2 Year', 'Product'] = "TPM"
	df.loc[df["Product Names"] == 'The Profit Machine 1 Year', 'Product Type'] = "Profit Machine 1 Year"
	df.loc[df["Product Names"] == 'The Profit Machine 1 Year', 'Product'] = "TPM"

	df.loc[df["Product Names"] == 'Thursday Profit', 'Product Type'] = "Thursday Profit"
	df.loc[df["Product Names"] == 'Thursday Profit', 'Product'] = "Thursday Profit"

	df.loc[df["Product Names"] == 'Options360 Experience', 'Product Type'] = "O360"
	df.loc[df["Product Names"] == 'Options360 Experience', 'Product'] = "O360"

	df.loc[df["Product Names"] == 'The Trade Architect', 'Product Type'] = "Trade Architect"
	df.loc[df["Product Names"] == 'The Trade Architect', 'Product'] = "Trade Architect"


	df.to_csv('Example.csv', index=False)



addEmptyCols()
addProductIDs()
