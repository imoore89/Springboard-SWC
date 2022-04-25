#!/usr/bin/env python
# coding: utf-8

# In[98]:


import matplotlib as mpl
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
sns.set_style("darkgrid")
mpl.rcParams['figure.figsize'] = (20,5)


# In[99]:


dataframe_raw = pd.read_csv(r"C:\Users\isaia\Desktop\DF_Raw_Data.csv")
dataframe_stdev = pd.read_csv(r"C:\Users\isaia\Desktop\DF_Rolling_Stdev.csv")

print(dataframe_raw.describe())
print(dataframe_raw.info())

print(dataframe_stdev.describe())
print(dataframe_stdev.info())


# In[100]:


dataframe_raw.plot(kind="box")
dataframe_raw.plot(kind="line")

dataframe_stdev.plot(kind="box")
dataframe_stdev.plot(kind="line")

plt.show()


# In[101]:


pre_failure = dataframe_raw["PUMP FAILURE (1 or 0)"]== 0
dataframe_raw_0 = dataframe_raw[pre_failure]
dataframe_raw_0.plot(kind="box")
plt.title("Pre Failure (Raw)")

post_failure = dataframe_raw["PUMP FAILURE (1 or 0)"]== 1
dataframe_raw_1 = dataframe_raw[post_failure]
dataframe_raw_1.plot(kind="box")
plt.title("Post Failure (Raw)")

plt.show()

pre_failure_stdev = dataframe_stdev["PUMP FAILURE (1 or 0)"]== 0
dataframe_stdev_0 = dataframe_stdev[pre_failure_stdev]
dataframe_stdev_0.plot(kind="box")
plt.title("Pre Failure (stdev)")

post_failure_stdev = dataframe_stdev["PUMP FAILURE (1 or 0)"]==1
dataframe_stdev_1 = dataframe_stdev[post_failure_stdev]
dataframe_stdev_1.plot(kind="box")
plt.title("Post Failure (stdev)")

plt.show()


# In[102]:


Q1 = dataframe_raw.quantile(q=0.25, axis=0)
Q3 = dataframe_raw.quantile(q=0.75, axis=0)
IQR = Q3 - Q1
print(IQR)


# In[103]:


Lower_Limit = Q1 - 1.5*IQR
Upper_Limit = Q3 + 1.5*IQR

outliers = dataframe_raw[((dataframe_raw < Lower_Limit) | ((dataframe_raw > Upper_Limit))).any(axis=1)]
no_outliers = dataframe_raw[~((dataframe_raw < Lower_Limit) | (dataframe_raw > Upper_Limit)).any(axis=1)]
proportion_outliers = (outliers.count())/(dataframe_raw.count())

print(no_outliers.count())
print(proportion_outliers)


# In[104]:


pump_normal_0 = dataframe_raw["PUMP FAILURE (1 or 0)"] == 0
pump_fail_1 = dataframe_raw["PUMP FAILURE (1 or 0)"] == 1

no_outliers[pump_normal_0].plot(kind="box", title="No Outliers Pump Normal", rot=60)
no_outliers[pump_fail_1].plot(kind="box", title="No Outliers Pump Failure", rot=60)
plt.show()


# In[105]:


list_of_variables = ["Volumetric Flow Meter 1", "Volumetric Flow Meter 2", 
                     "Pump Speed (RPM)", "Pump Torque ", "Ambient Temperature", "Horse Power", "Pump Efficiency", "PUMP FAILURE (1 or 0)"]
print(list_of_variables)


# In[106]:


for items in list_of_variables:
    first_axis = dataframe_raw[items].plot()
    second_axis = first_axis.twinx()
    second_axis.plot(dataframe_raw["PUMP FAILURE (1 or 0)"], color="teal")
    plt.title(items)
    plt.show()


# In[111]:


dataframe_time_filtered= dataframe_stdev[(dataframe_stdev.index>= "10/12/2014 12:00") & (dataframe_stdev.index<="10/12/2014 14:30")]

for item in list_of_variables:
    first_axis = dataframe_time_filtered[item].plot()
    first_axis.xaxis.set_major_locator(plt.MaxNLocator(10))
    second_axis = first_axis.twinx()
    second_axis.plot(dataframe_time_filtered["PUMP FAILURE (1 or 0)"], color="orange")
    second_axis.xaxis.set_major_locator(plt.MaxNLocator(10))
    plt.title(item)
    plt.show()


    


# In[ ]:





# In[ ]:




