# Translation Dataset

* Company XYZ is a worldwide e-commerce site with localized versions of the site.
* A data scientist at XYZ noticed that Spain-based users have a much higher conversion rate than any other Spanish-speaking country. She therefore went and talked to the international team in charge of Spain And LatAm to see if they had any ideas about why that was happening.
* Spain and LatAm country manager suggested that one reason could be translation. All Spanish- speaking countries had the same translation of the site which was written by a Spaniard. They agreed to try a test where each country would have its one translation written by a local.
* That is, Argentinian users would see a translation written by an Argentinian, Mexican users by a Mexican and so on. Obviously, nothing would change for users from Spain.
* After they run the test however, they are really surprised cause the test is negative. I.e., it appears that the non-localized translation was doing better!

**Goal**

The goal of this challenge is to build a machine learning model that predicts the probability that the first transaction of a new user is fraudulent.

* Confirm that the test is actually negative. That is, it appears that the old version of the site with just one translation across Spain and LatAm performs better
* Explain why that might be happening. Are the localized translations really worse?
* If you identified what was wrong, design an algorithm that would return FALSE if the same problem is happening in the future and TRUE if everything is good and the results can be trusted.


**Data**

We have 2 tables.

**Table 1: "test_table" - general information about the test results**

Columns:

* user_id : the id of the user. Unique by user. Can be joined to user id in the other table. For each user, we just check whether conversion happens the first time they land on the site since the test started.
* date : when they came to the site for the first time since the test started
* source : marketing channel: Ads, SEO, Direct . Direct means everything except for ads and SEO. Such as directly typing site URL on the browser, downloading the app w/o coming from SEO or Ads, referral friend, etc.
* device : device used by the user. It can be mobile or web
* browser_language : in browser or app settings, the language chosen by the user. It can be EN, ES, Other (Other means any language except for English and Spanish)
* ads_channel : if marketing channel is ads, this is the site where the ad was displayed. It can be: Google, Facebook, Bing, Yahoo ,Other. If the user didn't come via an ad, this field is NA
* browser : user browser. It can be: IE, Chrome, Android_App, FireFox, Iphone_App, Safari, Opera
* conversion : whether the user converted (1) or not (0). This is our label. A test is considered successful if it increases the proportion of users who convert.
* test : users are randomly split into test (1) and control (0). Test users see the new translation and control the old one. For Spain-based users, this is obviously always 0 since there is no change there.


**Table 2: "user_table" - some information about the user**

Columns:

* user_id : the id of the user. It can be joined to user id in the other table
* sex : user sex: Male or Female
* age : user age (self-reported)
* country : user country based on ip address

### Question 1

#### Write a function to convert given CSV file to Dataframe

* Define function with name `csv_to_dataframe` which should accept `filepath` as a parameter.
* Function should return a dataframe.
* As we require a dataframe, type of return variable should be pandas dataframe.
* In case if we pass `filepath` which does not exist, function should raise FileNotFoundError.

### Question 2

#### Write a function to merge two dataframes on given column name

* Define function with name `merge_dataframe` which should accept `dataframe1`, `dataframe2`(dataframes to be merged), `column_name`(as string) as a parameter.
* Function should return a dataframe.
* As we require a dataframe, type of return variable should be pandas dataframe.
* In case if we pass `column_name` which does not exist, function should raise KeyError.

### Question 3

#### Write a function to convert datatype of given variables to "category"

* Define function with name `dtype_category` which should accept `dataframe` and `list of columns` as parameters.
* Function should return a dataframe with type of given columns changed to "category".
* As we require a dataframe, type of return variable should be `pandas dataframe`.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 4

#### Write a function to to center and scale numerical variables.

* Define function with name `centre_and_scale` which should accept `dataframe` and `column_list` as parameters.
* Function should return a dataframe given columns of numerical variables being centred and scaled.
* As we require a dataframe, type of return variable should be `pandas dataframe`.
* In case if we pass column name which does not exist, function should raise KeyError

### Question 5

#### Write a function to encode all nominal categorical variables using label encoding

* Define function with name `label_encoder` which should accept `dataframe`, `column_list` (of variables to be encoded) as parameters.
* Function should return dataframe with encoded variables.
* As we require dataframe, type of return variable should be pandas dataframe.
* In case if we pass column name which does not exist or is not categorical type, function should raise KeyError

### Question 6

#### Write a function to encode nominal categorical variables using one hot encoding

* Define function with name `one_hot_encoder` which should accept `dataframe`, `column_list` (of variables to be encoded) as parameters.
* Function should return dataframe with encoded variables.
* As we require dataframe, type of return variable should be pandas dataframe.
* In case if we pass column name which does not exist or is not categorical type, function should raise KeyError

### Question 7

#### Write a function to return skewness of numerical variables:

* Define function with name `skewness` which should accept `dataframe`, `column_list` (of variables whose skewness is to be determined) as parameters.
* Function should return list of skewness of given columns
* As we require list of values, type of return variable should be list
* In case if we pass column name which does not exist or is categorical type, function should raise KeyError

### Question 8

#### Write a function to return sqrt transform of numerical variables

* Define function with name `sqrt_transform` which should accept `dataframe`, `column_list` (of variables which are to be sqrt transformed) as parameters.
* Function should return dataframe of sqrt transformed columns of given columns
* As we require list of values, type of return variable should be list
* In case if we pass column name which does not exist or is categorical type, function should raise KeyError

### Question 9

#### Write a function to plot  histogram and box plot of transformed  vs original numerical variables:

* Define function with name `plots` which should accept `dataframe`, `column_list` (of variables to be plotted) as parameters.
* Function should return subplots of histogram and boxplots for the numeric variables.
* As we require plot, type of return variable should be matplotlib object.
* In case if we pass column name which does not exist, function should raise KeyError