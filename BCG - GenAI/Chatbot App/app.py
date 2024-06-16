import pandas as pd

df = pd.read_csv('report.csv')
df.drop(df.columns[df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)

def simple_chatbot():
    print("\nWelcome to the financial chatbot:")
    print("\nPlease select your company from the list:")
    company = input("Microsoft, Tesla, Apple: ").capitalize()

    print("\nPlease select fiscal year from the list:")
    year = int(input("2021, 2022, 2023: "))

    print("\nPlease select metric from the list:")
    metric = input("Total Revenue, Net Income, Total Assets, Total Liabilities, Cash Flow from Operating Activities, Revenue Growth (%), Net Income Growth (%), Assets Growth (%), Liabilities Growth (%), Cash Flow from Operating Activities Growth (%): ")

    if company not in ['Microsoft', 'Tesla', 'Apple']:
        print("Invalid Company Name. Please check again!")
        return  # Replace break with return
    
    if year not in [2021, 2022, 2023]:
        print("Fiscal Year details unavailable. Please check again!")
        return  # Replace break with return

    if metric not in ['Total Revenue', 'Net Income', 'Total Assets', 'Total Liabilities', 'Cash Flow from Operating Activities', 'Revenue Growth (%)', 'Net Income Growth (%)', 'Assets Growth (%)', 'Liabilities Growth (%)', 'Cash Flow from Operating Activities Growth (%)']:
        print("Metric Unavailable or Incorrect Query")
        return

    print(f"\nDisplaying {metric} for {company} for fiscal year {year} in millions:")
    answer = df[(df['Fiscal Year']==year)&(df['Company']==company)][metric].values[0]
    print (answer)

simple_chatbot()