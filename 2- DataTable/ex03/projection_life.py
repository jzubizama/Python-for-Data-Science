from load_csv import load
import matplotlib.pyplot as plt
import numpy as np

def  projection_life(valsx, valsy, year):
    
    plt.scatter(valsx, valsy)
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')
    plt.title(year)   
    
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    
    plt.show()

def main():
	year = '1900'
	try:
		dfx = load("../income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
		dfy = load("../life_expectancy_years.csv")
		dfx.set_index('country', inplace=True)
		dfy.set_index('country', inplace=True)
		valsx = dfx[year]
		valsy = dfy[year]
		projection_life(valsx, valsy, year)
		return (0)
	except:
		print("Error in the program")
		return (1)
        

if __name__ == "__main__":
	main()