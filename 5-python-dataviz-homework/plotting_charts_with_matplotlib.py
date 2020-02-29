# 1 Still using the same DataFrame from the previous exercise insurance.csv plot the chart for charges and save it
# as charges_plot.png
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('data/insurance.csv', header=0)
plt.plot(df['charges'])
plt.title('Charges Plot')
plt.ylabel('Charges')
plt.savefig('charges_plot.png')

# 2 plot the histogram for bmi and save it as bmi_hist.png
plt.clf()
plt.hist(df['bmi'])
plt.title('BMI Histogram')
plt.ylabel('BMI')
plt.savefig('bmi_hist.png')

# 3 plot the scatterplot for age vs charges and save it as age_charge_scatter.png
plt.clf()
plt.scatter(df['age'], df['charges'])
plt.title('Age vs Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.savefig('age_charge_scatter.png')

# 4 Re-do the previous items, adding the title, x label and y label for each item.
# done above

# 5 Think about the exercise 12 from the previous section. Do the plots match what we saw with the correlation function?
# Yes, charges are going up with age
