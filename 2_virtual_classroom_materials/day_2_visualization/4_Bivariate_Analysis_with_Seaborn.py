# Databricks notebook source
# MAGIC %md
# MAGIC # Bivariate Analysis with Seaborn
# MAGIC 
# MAGIC Firstly, we import necessary libraries and load penguins dataset as 'penguins'.

# COMMAND ----------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# COMMAND ----------

# Load the data
penguins = pd.read_csv('Data/penguins.csv')

# COMMAND ----------

# Take a look at the first5 rows
penguins.head()

# COMMAND ----------

# Dropping missing values
penguins.dropna(inplace = True)

# COMMAND ----------

# MAGIC %md
# MAGIC # 1. Categorical variables
# MAGIC 
# MAGIC If you want to visualize data involving categorical variables, you can choose between 2 plotting approaches as we already saw in the preceding notebook: 
# MAGIC 
# MAGIC a) `catplot()` plotting function 
# MAGIC 
# MAGIC - this is a Figure-level interface that allows you to plot categories
# MAGIC - by calling this function, `a stripplot` will be drawn by default
# MAGIC   
# MAGIC Important note: specifying data
# MAGIC 
# MAGIC - data you want to visualize must passed in a long-form DataFrame 
# MAGIC - categorical and numerical variables must be passed as strings to `x` and `y` parameters in the following way:   
# MAGIC   ```sns.catplot(data = dataset, x = 'categorical_variable', y = 'numerical_variable')```
# MAGIC   
# MAGIC 
# MAGIC - the code below won´t work:  
# MAGIC   ```sns.catplot(x = data['categorical_variable'], y = data['numerical_variable'])```
# MAGIC   
# MAGIC `catplot()` functions provides us the access to other axes-level plotting functions, that you can select by passing respective plot kind to `kind` parameter:
# MAGIC 
# MAGIC - "box", "swarm", "strip", "violin", "barplot", etc. 
# MAGIC   
# MAGIC 
# MAGIC b) axes-level plotting functions
# MAGIC - `sns.boxplot()`
# MAGIC - `sns.swarmplot()`
# MAGIC - `sns.stripplot()`
# MAGIC - `sns.violinplot()`
# MAGIC - `sns.countplot()`
# MAGIC - `sns.barplot()`, etc.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1.1 Categorical vs. Numerical variable
# MAGIC 
# MAGIC One thing you could be interested in is to find out how the distribution of the numerical variable vary accros different categories. For this purpose you can use plotting functions such `sns.boxplot()`, `sns.violinplot()`, `sns.boxenplot()`.

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1.1.1 Boxplot
# MAGIC 
# MAGIC Inside a function for creating a boxplot we specify dataset and variable names. A categorical variable 'species' will be plotted on the x-axis and respective values of 'body_mass_g' on y-axis.

# COMMAND ----------

# Boxplots of body mass of penguins based on the species
plt.figure(figsize = (13,9))
sns.boxplot(data = penguins, 
            x = 'species', 
            y = 'body_mass_g', 
            palette = 'Set3');

# COMMAND ----------

# MAGIC %md
# MAGIC Visualization of the distribution reveals us interesting differences and similarities among species. For Adelie and Chinstrap, the majority of penguins do weigh up to approximately 4000 grams, although Chinstrap weight range is smaller than Adelie penguins. These two species have also the same median value of 3700 grams (we also verified median values in the code cell below). In case of Chanstrap penguins, there are present outliers, which can indicate that some penguins weight differently less or more compared to the rest of observations. Gentoo penguins are overally heavier, while the vast majority of penguins have weight about 4700-5500 grams. this species has the highest range of recorded values.  

# COMMAND ----------

# Median values of Adelie and Chinstrap species
print('Adelie body mass-median value: ', penguins[penguins.species == 'Adelie'].body_mass_g.median(),
      '\n'
      'Chinstrap body mass-median value: ', penguins[penguins.species == 'Chinstrap'].body_mass_g.median())

# COMMAND ----------

# Boxplots of the bill length based on the species
plt.figure(figsize = (13,9))
sns.boxplot(data = penguins, 
            x = 'species', 
            y = 'bill_length_mm');

# COMMAND ----------

# MAGIC %md
# MAGIC From the boxplots we can say, that Adelie species is characteristic with the shortest length of the bill, while the most penguins have about 37-41 milimeters long bill. The bill length of Chinstrap and Gentoo species is from about 41 mm. If we do not take into account the outlier of Gentoo species, this species have shorter bills compared to Chinstrap penguins.

# COMMAND ----------

# TASK 1 >>> Create boxplots about the depth of the bills based on species
#        >>> Set a Figure size: (13,9)
#        >>> Set the title: 'Distribution of bill's depth based on species'



# COMMAND ----------

# MAGIC %md
# MAGIC > What can you say about those 3 species in term of the bill depth? How does the distribution differ ? What about the range of values? What species has the smallest bill depth range?

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1.1.2 Swarmplot
# MAGIC 
# MAGIC We can also take a closer look at three islands where penguins live. Since our dataset does not comprise too many observations, the data points are nicely plotted.

# COMMAND ----------

# Swarmplot of the flipper length based on islands

plt.figure(figsize = (13,9))
ax = sns.swarmplot(data = penguins, 
              x = 'island', 
              y = 'flipper_length_mm')
ax.set(title = 'Distribution of the flipper length', # Accessing Axes object and setting title and labels using .set()
       xlabel = 'The island',
       ylabel = 'The flipper length (mm)');

# COMMAND ----------

# MAGIC %md
# MAGIC Now we see the distribution of penguins´s flipper length on three islands, but this plot does not provide us any specific and useful information. We can say only, for example, there are penguins with either really short flippers or vast majority of penguins have long flippers about 215 milimeters on Biscoe island. 
# MAGIC 
# MAGIC Let´s explore what species are actually present on particular islands.

# COMMAND ----------

# Group data based on island and count penguins

penguins.groupby('island')['species'].value_counts()

# COMMAND ----------

# MAGIC %md
# MAGIC Interesting, Adelie species inhabit all three islands. Gentoo penguins are present only in Biscoe island and Chinstrap´s home is Dream island. Let´s filter the dataset only for Gentoo and Chinstrap penguins.
# MAGIC 
# MAGIC Filtering approach is up to you. You can create a subset of a DataFrame with specific rows based on a condition using indexing like in this example:   
# MAGIC ```subset = data['weight'] == 85```
# MAGIC 
# MAGIC This operation checks for whether the row contain value 85 and returns only those rows where this condition is fulfilled.
# MAGIC 
# MAGIC Another option is to used  `query` which we apply onto the DataFrame and I find it more straightforward. We specify that, we want to filter only those rows, where Gentoo and Chinstrap penguins are present as species. Since we filter for more than 1 condition, these species must by passed as a list. We use `in` keyword, which check whether a species is present in the list.
# MAGIC 
# MAGIC 
# MAGIC Choose a approach which the best suits you. I included both of them for comparing the code syntax.

# COMMAND ----------

# Filtering only Gentoo and Chinstrap species using Pandas query

penguins_filter = penguins.query('species in ["Gentoo","Chinstrap"]')

# COMMAND ----------

# Filtering only Gentoo and Chinstrap species using indexing

penguins_fil = penguins[penguins['species'].isin(["Gentoo","Chinstrap"])]

# COMMAND ----------

# The new DataFrame penguins_filter will be returned as an output

penguins_filter

# COMMAND ----------

# TASK 2 >>> Create a swarmplot using created penguins_filter subset
#        >>> Set a Figure size: (13,9)
#        >>> Visualize flipper length based on Chinstrap and Gentoo species
#        >>> Set the title: 'Distribution of Chinstrap and Gentoo species'using plt.title()

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1.1.3 Stripplot
# MAGIC 
# MAGIC As you already learned how to create a stripplot, try the following exercise of visualizing Adelie species flipper length distribution based on categories of the gender.

# COMMAND ----------

# Filtering only Adelie species and save it as adelie_filter
adelie_filter = penguins.query('species == "Adelie"')

# COMMAND ----------

# TASK 3 >>> Visualize Adelie´s flipper length distribution using swarmplot based on the gender
#        >>> Set a Figure size: (13,9)
#        >>> Store the output of stripplot to ax variable
#        >>> Set the following using ax.set(): 
#            title: 'The flipper length based on the gender'
#            x-axis label: 'The gender'
#            y-axis label: 'The flipper length (mm)'

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1.1.4 Violinplot
# MAGIC 
# MAGIC Categories can be nicely compared using a violinplot which shows statistics from boxplot and the shape of distribution that comes from density plot. A violinplot is a good choice for plotting the distribution when visualizing the large number of observations is not sufficient due to data points overlapping.

# COMMAND ----------

# A violinplot of 'body_mass_g' variable
plt.figure(figsize = (13,9))
sns.violinplot(data = penguins, 
               x = 'sex', 
               y = 'body_mass_g');

# COMMAND ----------

# MAGIC %md
# MAGIC A violinplot consists of boxplot that is displayed in the middle. The thick black bar represents the majority of values (IQR) and the white dot is the median value. Thin black lines represent the rest of data points. There shape of distribution is displayed on each side. The interpretation of violinplot is similar for instance to swarmplot. Wider parts represent higher frequency of observations, while thinner parts denote less observations. You can notice that most male penguings have weight about 4000 grams and are generally heavier than females.
# MAGIC 
# MAGIC ---
# MAGIC 
# MAGIC Please, see the [documentation](https://seaborn.pydata.org/generated/seaborn.violinplot.html) for specifying other parameters.

# COMMAND ----------

# A violin plot of 'body_mass_g' variable based on 'species'
color = {'Adelie':'powderblue','Chinstrap':'thistle','Gentoo':'bisque'}
plt.figure(figsize = (13,9))
ax = sns.violinplot(data = penguins, 
                    x = 'body_mass_g', 
                    y = 'species',
                    inner = 'quartile',
                    linewidth = 1.4,
                    palette = color);

# COMMAND ----------

# MAGIC %md
# MAGIC ### 1.1.5 Displot
# MAGIC 
# MAGIC We can also compare spread of the values using a histogram by specifying several approaches or other parameters.

# COMMAND ----------

# A displot of 'body_mass_g' variable based on 'species'
sns.displot(data = penguins, 
            x='body_mass_g', 
            hue = 'species', 
            kind = 'kde',
            height = 6, 
            aspect = 1.3);

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1.2 Categorical vs. categorical variable
# MAGIC 
# MAGIC With a countplot we are able to count the number of observations in each catogory and then compared how these values vary accross categories. 
# MAGIC 
# MAGIC Let´s visualize how many females and males penguins are present in each species.

# COMMAND ----------

# A countplot of male and females penguins based on species
plt.figure(figsize = (13,9))
bars = sns.countplot(data = penguins, x = 'species', hue = 'sex', palette = 'Set3')

# Annotation for bars and example customizations
for b in bars.patches:                               
    bars.annotate('{:.0f}'.format(b.get_height()),  # Showing the count and string formatting to no decimal place
                 (b.get_x() + 0.2, b.get_height()), # A tuple of the left coordinate of bar with adding some float to center it 
                                                    # and getting the height of a bar - to change the placement of numbers,
                                                    # substract some number from b.get_height() to see the change 
                  ha='center',                      # Setting horizontal alignment of text
                  va='bottom',                      # Setting vertical alingment of text
                  color= 'black',                   
                  fontsize = 10)
sns.despine(top = True, left = True)                # Removing spines from plot
bars.set(ylabel = '', yticks = [])                  # Removing y-axis labels and y-axis ticks         
bars.set_xlabel('Species', fontsize = 13);      

# COMMAND ----------

# MAGIC %md
# MAGIC # 2. Numerical vs. numerical variable
# MAGIC 
# MAGIC During bivariate analysis of two numerical variables we attempt to determine any relationship between them and how these variables relate to each other.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2.1 Relplot
# MAGIC 
# MAGIC Seaborn´s `replot()` plotting function creates a relational plot. The output of this function is a FacetGrid object which allows to extend existing plot in several ways, for instance adding another subplots or adding a subset of the data to visually display various categories. These options will be discussed in the last notebook about Multivariate analysis.
# MAGIC 
# MAGIC It is also possible to choose method of visualizing statistical relationship using `kind` parameter:
# MAGIC - `kind = 'scatter'` - by default
# MAGIC - `kind = 'line` 
# MAGIC 
# MAGIC For now let´s focus on creating a default relational plot comparing 2 numerical variables at once. We specify input dataset to `data` parameter and assign numerical variables as strings to `x` and `y`. 

# COMMAND ----------

# Relationship between body mass and the flipper length
rel = sns.relplot(data = penguins, 
                  x = 'body_mass_g', 
                  y = 'flipper_length_mm',
                  color = 'grey',
                  height = 6, 
                  aspect = 1.3)
rel.set(xlabel = 'Body mass (g)', 
        ylabel = 'Flipper length (mm)');

# COMMAND ----------

# MAGIC %md
# MAGIC The above plot shows the relationship between penguin´s body mass and the flipper length. We can see, that these two characteristics are strongly related with each other. The clear pattern indicates that with increasing body mass, there are an increase of the flipper length. 

# COMMAND ----------

# Relationship between body mass and bill length 
rel = sns.relplot(data = penguins, 
                  x = 'body_mass_g', 
                  y = 'bill_length_mm', 
                  color = 'cadetblue',
                  height = 6, 
                  aspect = 1.3)
rel.set(xlabel = 'Body mass (g)', 
        ylabel = 'The bill depth (mm)');

# COMMAND ----------

# MAGIC %md
# MAGIC Again, we can observe some kind of relationship between body mass and the bill length. You can notice that penguins that weight about 3500 grams tend to have either short bill (roughly about 35-40 mm), or longer bill (above 45 mm). After the weight about 4500 grams, the relationship becomes somewhat stronger and with increasing body mass, the bill length is longer. This is the case, when we would need to take a closer look at the relationship by implementing some kind of visual semantic to gain more information from the data.

# COMMAND ----------

# TASK 4 >>> Create a relplot to visualize the relationship between 'bill_length_mm' and 'bill_depth_mm' variables
#        >>> Set parameters: height = 6, aspect = 1.3
#        >>> Set x-axis: 'The bill length (mm)'
#        >>> Set y-axis label: 'The bill depth (mm)'

# COMMAND ----------

# MAGIC %md
# MAGIC > What can you say about this relationship ? Does the bill length relate to the bill depth? Is there some indication about a strong relationship or you barely see any patterns ?  

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2.2 Scatterplot
# MAGIC 
# MAGIC Another option to create a relational plot is using axes-level function `scaterplot()`. 

# COMMAND ----------

# Relationship between 'body_mass_g' and 'flipper_length_mm'
plt.figure(figsize = (13,9))
sns.scatterplot(data = penguins, 
                x = 'body_mass_g', 
                y = 'flipper_length_mm', 
                color = 'lightcoral');

# COMMAND ----------

# MAGIC %md
# MAGIC We can see a strong positive relationship between the body mass and the flipper length. 

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2.3 Visualizing trends

# COMMAND ----------

# MAGIC %md
# MAGIC ### 2.3.1 Regplot
# MAGIC 
# MAGIC The axes-level function`regplot()` creates a scatterplot and a line of the best fit with a default 95% confidence interval which is drawn using translucent bands around the line. A similar plotting function is `lmplot()` which take use of regplot and FacetGrid object so that you can compare several categories in a Figure.

# COMMAND ----------

# A regplot of 'body_mass' and 'flipper_length_mm' variables
plt.figure(figsize = (13,9))
sns.regplot(data = penguins, 
            x = 'body_mass_g', 
            y = 'bill_length_mm',
            color = 'indigo',
            ci = 99);           # Setting the size of confidence interval for the estimate

# COMMAND ----------

# MAGIC %md
# MAGIC # 3. Heatmap
# MAGIC 
# MAGIC Often, we want to compute correlation coefficients to see the strength and the direction of the relationship. This can be done using Pandas´s `corr()` function that take input data and compute pairwise correlation of variables.
# MAGIC 
# MAGIC Types of correlation, that can be specified as an argument to `method` parameter:
# MAGIC - pearson
# MAGIC - kendall
# MAGIC - spearman
# MAGIC 
# MAGIC Correlation matrix can be visualized using a heatmap where correlation coefficients are represented as colors. Values of correlation coefficients can take a range from -1 (a strong negative relationship) to 1 (a strong positive relationship). Since the coefficients take either high or low values, we should select a specific color palette called diverging.

# COMMAND ----------

# Computing correlation coefficients
corr = penguins.corr()

# COMMAND ----------

# A heatmap of penguins dataset
fig, ax = plt.subplots(figsize = (13,9))
sns.heatmap(corr, 
            annot = True,                 # Correlation coeficients will be displayed in each cell
            annot_kws = {'fontsize':14},  # Setting a fontsize
            cmap = 'Blues');              # Setting a color map

# COMMAND ----------

# MAGIC %md
# MAGIC # 4. Practice time
# MAGIC 
# MAGIC Let's continue exploring the "Bank marketing" dataset as in the previous notebook.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4.1 Loading data, preprocessing

# COMMAND ----------

# Load the data 

data = pd.read_csv('Data/bank_data.csv',sep = ';')
# Let´s rename some of variables
data.rename(columns = {'marital':'marital_status','default':'default_credit','housing':'house_loan',
                      'contact':'contact_type','duration':'contact_duration','campaign':'number_of_contacts',
                      'pdays':'days_passed','previous':'number_previous_contact','poutcome':'previous_campaign_outcome',
                      'emp.var.rate':'emp_variation_rate','cons.price.idx':'cpi','cons.conf.idx':
                      'cci','euribor3m':'euribor_rate','nr.employed':'no_employees','y':'target'},
           inplace = True)

# COMMAND ----------

# Remove duplicated rows

data.drop_duplicates(inplace = True)

# COMMAND ----------

# Select all variables that need to be converted

to_category = ['job','marital_status','education','default_credit','house_loan', 
               'loan','contact_type','month','day_of_week', 'previous_campaign_outcome']

# COMMAND ----------

# Convert them to category data type

for col in to_category:
    data[col] = data[col].astype('category')

# COMMAND ----------

# Create a dictionary with original values and corresponding new values for days

mapping_days = {'mon':'Monday','tue':'Tuesday','wed':'Wednesday','thu':'Thursday','fri':'Friday'}
# Map new values to column 'day_of_week'
data.day_of_week = data.day_of_week.map(mapping_days)

# COMMAND ----------

# Create a dictionary with original values and corresponding new values for months

mapping_months = {'mar':'March', 'apr':'April','may':'May','jun':'Jun','jul':'Jul','aug':'August',
                  'sep':'September','oct':'October','nov':'November','dec':'December'}
# Map new values to column 'month'
data.month = data.month.map(mapping_months)

# COMMAND ----------

# Converting seconds to minutes

data.contact_duration = data.contact_duration.apply(lambda x: x / 60)

# COMMAND ----------

# Inspect the data
data

# COMMAND ----------

# TASK 5 >>> Create a Figure object and set size to (13,9)
#        >>> Create a heatmap of data with written correlations coefficients
#        >>> Set color palette: 'RdGy'


# COMMAND ----------

# TASK 6 >>> Create a histogram of 'contact_duration' based on 'target' variable
#        >>> Set parameter: multiple = 'stack'
#        >>> Set parameters: height = 7, aspect = 1.3


# COMMAND ----------

# TASK 7 >>> Create a boxplot of 'age' variable based on 'target'
#        >>> Set a Figure size: (13,9)


# COMMAND ----------

# TASK 8 >>> Create a countplot using a Figure-level function catplot() 
#        >>> Visualize 'target' variable based on client´s job
#        >>> Specify parameters: height = 6 and aspect = 1.3
#        >>> Set the rotation of x-axis tick labels to 50 degrees


# COMMAND ----------

# TASK 9 >>> Create a countplot of 'marital_status' based on 'target' using a Figure-level function catplot() 
#        >>> Specify parameters: height = 6 and aspect = 1.3


# COMMAND ----------

# MAGIC %md
# MAGIC ## Citation request:
# MAGIC 
# MAGIC [Moro et al., 2014] S. Moro, P. Cortez and P. Rita. A Data-Driven Approach to Predict the Success of Bank Telemarketing. Decision Support Systems, Elsevier, 62:22-31, June 2014  
# MAGIC 
# MAGIC Some material adapted for RBI internal purposes with full permissions from original authors. [Source](https://github.com/zatkopatrik/authentic-data-science) 
