

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

cwc_data=pd.read_csv("/content/drive/MyDrive/cwc20data.csv")

cwc_data.head()

cwc_data.head(50)

cwc_data['Match_winner'].value_counts()

cwc_data.Match_winner[cwc_data.city=='Colombo']

cwc_data.Match_winner[cwc_data.city=='Dhaka']

cwc_data.Match_winner[cwc_data.Year==2012].value_counts()

cwc_data.Match_winner[cwc_data.Year==2016].value_counts()

cwc_data.Match_winner[cwc_data.Year==2014].value_counts()

cwc_data.Match_winner[(cwc_data.result=='Runs')&(cwc_data.Year==2012)].value_counts()

cwc_data.Match_winner[(cwc_data.result=='Wickets')&(cwc_data.Year==2016)].value_counts()

cwc_data['Match_winner'].value_counts().plot.pie(autopct='%1.1f%%',shadow=True,rotatelabels=True)
plt.title("Matches won by teams in T20 WC 2012-2016",fontweight="bold",fontsize=20)
plt.show()

cwc_data.Match_winner[(cwc_data.result=='Runs')&(cwc_data.Year==2014)].value_counts()

cwc_data.Match_winner[(cwc_data.result=='Wickets')&(cwc_data.Year==2012)].value_counts()

cwc_data.Match_winner[cwc_data.city=='Kolkata']
