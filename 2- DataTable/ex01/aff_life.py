from load_csv import load
import matplotlib.pyplot as plt

def aff_life(row, country):
    row = row.transpose()
    row.columns = ['Life expectancy']
    
    plt.plot(row.index, row['Life expectancy'])
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title(country + ' life expectancy Projections')
    
    # Set X ticks to show every 40 years
    x_ticks = row.index[::40]
    plt.xticks(x_ticks)
    
    plt.show()



def main():
	cntry = 'Spain'
	try:
		df = load("../life_expectancy_years.csv")
		row = df.loc[df['country'] == cntry].drop(columns=['country'])
		aff_life(row, cntry)
		return (0)
	except:
		print("Error in the program")
		return (1)
        

if __name__ == "__main__":
	main()