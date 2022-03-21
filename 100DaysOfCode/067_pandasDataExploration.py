import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import csv
import pandas as pd

# Analyzing salary data by undergraduate major #######################################################################

# Selenium
PAYSCALE_URL = "https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors"
chrome_driver_path = r"C:\Users\Eunice Kim\Desktop\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Columns
major_col = []
early_career_pay_col = []
mid_career_pay_col = []
meaning_col = []

# Find the number of pages
response = requests.get(PAYSCALE_URL)
payscale_page = response.text
soup = BeautifulSoup(payscale_page, "html.parser")
page_nums = [int(x.text) for x in soup.find_all(class_="pagination__btn--inner") if x.text.isnumeric()]
pages = max(page_nums)

# Go to first page
driver.get(PAYSCALE_URL)
sleep(2)

for x in range(pages - 1):
    CURRENT_PAGE = driver.current_url

    # Beautiful Soup
    response = requests.get(CURRENT_PAGE)
    payscale_page = response.text
    soup = BeautifulSoup(payscale_page, "html.parser")

    major_data = soup.find_all(class_="data-table__cell csr-col--school-name")
    for x in major_data:
        major_col.append(x.findChild("span", {'class', 'data-table__value'}).text)

    pay_data = soup.find_all(class_="data-table__cell csr-col--right")
    for index, x in enumerate(pay_data, start=1):
        data = x.findChild("span", {'class', 'data-table__value'}).text
        if index % 3 == 1:
            early_career_pay_col.append(data)
        elif index % 3 == 2:
            mid_career_pay_col.append(data)
        else:
            meaning_col.append(data)

    next_btn = driver.find_element(By.CLASS_NAME, "pagination__next-btn")
    next_btn.click()
    sleep(2)

column_names = ["Major", "Early Career Pay", "Mid-Career Pay", "Meaning"]
rows = []

for x in range(len(major_col)):
    rows.append([major_col[x], early_career_pay_col[x], mid_career_pay_col[x], meaning_col[x]])

with open("updated_salary.csv", "w") as file:
    write = csv.writer(file)
    write.writerow(column_names)
    write.writerows(rows)

df = pd.read_csv("updated_salary.csv")
print(df.head())

df['Early Career Pay'] = df['Early Career Pay'].replace('\$|,', '', regex=True)
df['Early Career Pay'] = pd.to_numeric(df['Early Career Pay'])

df['Mid-Career Pay'] = df['Mid-Career Pay'].replace('\$|,', '', regex=True)
df['Mid-Career Pay'] = pd.to_numeric(df['Mid-Career Pay'])

df['Meaning'] = df['Meaning'].str.rstrip('%')

df.to_csv("updated_salary.csv")

# Preview Data
df.head()

# Find highest salary for early career
df.loc[df['Early Career Pay'].idxmax()]

# Find highest salary for mid career
df.loc[df['Mid-Career Pay'].idxmax()]

# Make a new column 'spread' to see difference in mid-career and early career salaries
spread = df['Mid-Career Pay'] - df['Early Career Pay']
df.insert(1, 'Spread', spread)
high_spread = df.sort_values('Spread', ascending=False)
high_spread.head()




# Analyzing the popularity of programming languages #################################################################
# https://data.stackexchange.com/stackoverflow/query/675441/popular-programming-languages-per-over-time-eversql-com
import matplotlib.pyplot as plt

df.read_csv('QueryResults.csv', names=['date', 'tag', 'posts'], header=0)

# Look at example rows in head and tail
df.head()
df.tail()

# How many rows and columns?
df.shape

# How many entries for each column?
df.count()

# Get the number of posts per language.
df.groupby('tag').sum().sort_values('posts', ascending=False)

# How many months of data for each language?
df.groupby('tag').count().sort_values('date')

# DATA CLEANING

# Converting date column to a datetime
df.date = pd.to_datetime(df.date)
df.head()

# DATA MANIPULATION

reshaped_df = df.pivot(index='date', columns='tag', values='posts')
reshaped_df.shape
reshaped_df.columns
reshaped_df.head()

# Get the number of entries per language
# The number is different because of NaN values
reshaped_df.count()
reshaped_df.fillna(0, inplace=True)

# see if there are any na values now
reshaped_df.isna().values.any()

# DATA VISUALIZATION

# Plot popularity of Python over time
plt.plot(reshaped_df.index, reshaped_df.python)

# Format the chart
plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Number of Posts', fontsize=16)
plt.ylim(0, 32000)
for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column],
             linewidth=3,
             label=reshaped_df[column].name)
plt.legend(fontsize=16)

# Java & Python on the same chart
plt.plot(reshaped_df.index, reshaped_df.java, reshaped_df.python)

# Plotting the rolling average to smooth out the time series data
roll_df = reshaped_df.rolling(window=6).mean()

plt.figure(figsize=(16, 10))
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Number of Posts', fontsize=16)
plt.ylim(0, 32000)

for column in roll_df.columns:
    plt.plot(roll_df.index,
             roll_df[column],
             linewidth=3,
             label=roll_df[column].name)

plt.legend(fontsize=16)
