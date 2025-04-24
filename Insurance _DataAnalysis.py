#!/usr/bin/env python
# coding: utf-8

# # Insurance Data Analysis
# 
# 
# 

# __Step 1.	Import libraries such as Pandas, matplotlib, NumPy, and seaborn and load the insurance dataset__

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# __Load Data__

# In[3]:


insurance_data =pd.read_csv("insurance.csv")


# In[4]:


insurance_data


# In[9]:


#print first five rows of the datasets
insurance_data.head()


# In[7]:


#print first five rows of the datasets
insurance_data.tail()


# __Step: 2, To check the shape of the data along with the data types of the column__

# In[10]:


insurance_data.shape 


# List of Columns

# In[11]:


insurance_data.columns


# __Columns Data Type__

# In[14]:


insurance_data.dtypes


# **Data Information**

# In[15]:


insurance_data.info()


# __Check for duplicate records__

# In[17]:


insurance_data.duplicated().any()


# In[18]:


insurance_data[insurance_data.duplicated()]


# In[19]:


insurance_data1= insurance_data.drop_duplicates()


# In[21]:


insurance_data1.shape


# __Check for Missing Valuess__

# In[24]:


insurance_data1.isnull().any()
insurance_data1.isnull().sum()


# **List of Categorical and Numerical Columns**:

# In[28]:


Numerical_columns = insurance_data1.select_dtypes(include="number").columns.to_list()
Categorical_columns =  insurance_data1.select_dtypes(exclude="number").columns.to_list()
print(f"Numerical columns in the data : {Numerical_columns}")
print(f"Categorical_columns in the data : {Categorical_columns}")



# **Step 3.	Check missing values in the dataset and find the appropriate measures to fill in the missing values:**

# Statistical Measure of Numeric Columns:

# In[29]:


insurance_data1.describe()


# In[33]:


insurance_data1.describe(exclude="number")


# In[34]:


insurance_data1.sex.unique()


# In[35]:


insurance_data1.sex.nunique()


# In[37]:


insurance_data1.sex.value_counts()


# In[39]:


print(insurance_data1.smoker.unique())
print()
print(insurance_data1.smoker.nunique())
print()
print(insurance_data1.smoker.value_counts())


# In[40]:


print(insurance_data1.region.unique())
print()
print(insurance_data1.region.nunique())
print()
print(insurance_data1.region.value_counts())


# In[41]:


Numerical_columns


# In[43]:


insurance_data1['age'].plot(kind='hist')
plt.title("Age Distribution")
plt.show()


# In[48]:


insurance_data1['bmi'].plot(kind='hist')
plt.title("BMI Distribution")
plt.show()


# In[46]:


insurance_data1['children'].plot(kind='hist')
plt.title("children Distribution")
plt.show()        


# In[49]:


insurance_data1['charges'].plot(kind ='hist')
plt.title("charges Distribution")
plt.show()


# Bar Graph-Categorial Coloumn

# In[51]:


insurance_data1["children"].value_counts().plot(kind="bar")


# In[52]:


insurance_data1["sex"].value_counts().plot(kind="bar")


# In[53]:


insurance_data1["region"].value_counts().plot(kind="bar")


# In[56]:


insurance_data1["charges"].plot(kind="box")
plt.title("charges Distribution")
plt.show()


# *THESE SMALL CIRCLES INDICATESS OUTLIERS*

# In[57]:


insurance_data1["bmi"].plot(kind="box")
plt.title("BMI Distribution")
plt.show()


# In[58]:


insurance_data1["age"].plot(kind="box")
plt.title("Age Distribution")
plt.show()


# In[99]:


# HERE IS NO OUTLIERS


# Pie Chart-Region

# In[62]:


region_count = insurance_data1["region"].value_counts()
region_count


# In[66]:


plt.pie(labels=region_count.index,
        x=region_count.values,
        shadow=True,
        autopct = '%.2f%%',
        explode = (0,0.1,0,0))
plt.title("Distribution of region")
plt.show()


# In[72]:


corr_data  = insurance_data1[["age","bmi","charges"]]. corr()
plt.figure(figsize =(8,6))
sns.heatmap(round(corr_data,2), annot=True, cmap="Blues", cbar=False)
plt.title("Correlation Heatmap : Age, BMI and Charges")
plt.show()


# **Scatter Plot**

# In[73]:


plt.scatter(data = insurance_data1, x="age", y= "charges")


# In[100]:


#HERE WE CAN SEE THE POSITIVE RELATIONSHIP BETWEEN AGE AND CHARGES


# In[74]:


plt.scatter(data = insurance_data1, x="bmi", y= "charges")


# In[75]:


plt.scatter(data = insurance_data1, x="bmi", y= "age")


# increase cost for Smoker and Non Smoker:

# In[79]:


smoker_df =insurance_data1.groupby("smoker")["charges"].mean().reset_index()
smoker_df


# In[81]:


smoker_df.plot(kind ='bar',x='smoker', y= 'charges')


# In[101]:


#INSURANCE COST INCREASES IF THE PERSON IS SMOKER


# insurance cost for Male and Female

# In[84]:


gender_df = insurance_data1.groupby("sex")["charges"].mean().reset_index()
gender_df


# Region wise insurance cost

# In[85]:


region_df = insurance_data1.groupby("region")["charges"].mean().reset_index()
region_df


# In[86]:


region_df.plot(kind="bar", x="region", y ="charges")


# In[102]:


#VERY LESS OR WE CAN SAY NO IMPACT OF lOCATION ON CHARGES


# Region wise BMI

# In[90]:


region_bmi_df = insurance_data1.groupby("region")["bmi"].mean().reset_index()
region_bmi_df


# In[91]:


region_bmi_df.plot(kind="bar", x="region", y ="bmi")


# **Region wise Male and Female and cost:**

# In[96]:


insurance_data1.groupby(["region","sex"])['sex'].count()


# In[ ]:




