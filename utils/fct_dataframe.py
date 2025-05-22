import pandas as pd
from IPython.display import display, HTML
from scipy.signal import argrelextrema
import numpy as np



def drop_outliers_IQR(df):
    """
    Input : DF
    Return : un DF où les valeurs en dehors des [Q];Q3] sont retirées
    """
    q1=df.quantile(0.25)
    q3=df.quantile(0.75)
    IQR=q3-q1
    not_outliers = df[~((df<(q1-1.5*IQR)) | (df>(q3+1.5*IQR)))]
    outliers_dropped = not_outliers.dropna().reset_index()
    return outliers_dropped



def analyse_df(df, corr_limit = 0.75):
	"""
    Analyse any dataframe and print results
	* Print df Shape, duplicate rows qnt, memory usage, data types and call DataFrame.describe()
	* Check Missing values in each columns, returning qnt. and percentage
	* Check Linear Correlation between columns, return Pearson number
	
	Keyword arguments:
	df -- Any DataFrame
	corr_limit -- Correlation Limit (Pearson) to define if relationship exists (default 0.75)
	"""
    
	print('General Info:')
	print(f'{df.shape[0]} Rows {df.shape[1]} Columns'
		f'\n{df.columns.duplicated().sum()} Duplicated Rows'
		f'\nMemory Usage: {df.memory_usage().sum()/(1024*1024):.2f}Mb')
	
	# Checking Data Types
	
	int_list, float_list,object_list,bool_list,other_list =[[] for i in range(5)]
	for col in df.columns:
		if df[col].dtype == 'int64':
			int_list.append(col)
		elif df[col].dtype == 'float64':
			float_list.append(col)
		elif df[col].dtype == 'object':
			object_list.append(col)
		elif df[col].dtype == 'boolean':
			bool_list.append(col)
		else:
			other_list.append(col)
	
	for type_list,data_type in zip([int_list, float_list,object_list,bool_list,other_list],
	['int64','float64','object','boolean','other']):
		if len(type_list)>0:
			print(f'\nColumns {data_type}: {type_list}\n')
	
	# General statistics
	display(df.describe())
	
	# Checking Missing Values in each columns
	print('\nCheking Missing Values:')
	col_with_missing_counter = 0
	for col in df.columns:
		qnt_missing = df[col].isna().sum()
		if qnt_missing > 0:
			col_with_missing_counter +=1
			print(f'Column "{col}" has {qnt_missing} missing values ({qnt_missing/df.shape[0]:.2%})')
	
	if col_with_missing_counter ==0 :
		print('Analyzed DataFrame has no missing values')
	
	# Checking linear correlation between columns
	print('\nChecking Linear Correlation:')
	df_corr = df.corr() # Correlation DataFrame
	ckecked_list =[] # Ensure that we won't print the same information twice
	cols_with_correlation_counter = 0
	for col in df_corr.columns:
		ckecked_list.append(col)
		for i in range(len(df_corr)):
			if ((df_corr[col][i] > corr_limit or df_corr[col][i] < -corr_limit) and
				(df_corr.index[i] not in ckecked_list)):
				cols_with_correlation_counter += 1
				print(f'Linear Correlation found between columns '
					f'{df_corr.index[i]} and {col} -> Pearson coef. = {df_corr[col][i]:.2f}')
	if cols_with_correlation_counter == 0:
		print('No linear correlation was found') 
		
	

def df_get_min_max(df, col, n):
    df["min"] = df.iloc[argrelextrema(df[col].values, np.less_equal, order=n)[0]][col]
    df["max"] = df.iloc[argrelextrema(df[col].values, np.greater_equal, order=n)[0]][
        col
    ]
    return df


def pretreat_df(df, time_col = 'timestamp' , mode=None):
	if mode is not None :
		df[mode] = (df[mode].ffill().bfill())
	df[time_col] = pd.to_datetime(df[time_col]).dt.floor("s").dt.tz_localize(None)
	df.set_index(time_col, inplace=True)
	df = df.sort_index()
	return df

def time_elapsed(df):
    """
    Calculate the time elapsed since the first timestamp in the dataframe.
    """
    df.index = (df.index - df.index[0]).total_seconds()
    df.index.name = "time_elapsed [s]"  
    return df