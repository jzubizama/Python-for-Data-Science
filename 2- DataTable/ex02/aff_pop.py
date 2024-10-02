from load_csv import load
import matplotlib.pyplot as plt
import numpy as np

def aff_pop(rows, cntry1, cntry2):
    rows = rows.transpose()
    
    plt.plot(rows.index, rows[cntry1], label=cntry1)
    plt.plot(rows.index, rows[cntry2], label=cntry2)
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.title('Population Projections')
    plt.legend()
    
    # Set X ticks to show every 40 years
    x_ticks = rows.index[::40]
    plt.xticks(x_ticks)
    
    # Set Y ticks to show every 20 million
    #max_y = max(rows[cntry1].max(), rows[cntry2].max())
    #y_ticks = np.arange(0, max_y + 20000000, 20000000)
    #plt.yticks(y_ticks)
    
    plt.show()


def get_values(rows):
	"""
		Take pandas.DataFrame and changes all Sries values to be represented
		as float (replacing human readable format)
	"""
	for cntry, row in rows.iterrows():
		for col in row.index:
			rows.at[cntry, col] = float(
				row[col].replace('k', 'e3').replace('M', 'e6')
			)


def main():
	cntry1 = 'Spain'
	cntry2 = 'France'
	try:
		df = load("../population_total.csv")
		df.set_index('country', inplace=True)
		rows = df.loc[[cntry1 , cntry2]]
		get_values(rows)
		aff_pop(rows, cntry1, cntry2)
		return (0)
	except:
		print("Error in the program")
		return (1)
        

if __name__ == "__main__":
	main()