# highest-profit-challenge

This solution was built for this challenge: https://github.com/bobbae/gcp/tree/main/challenges/highest-profit

### Tasks
The tasks were understood as:
1. Read CSV data into memory and print number of rows in CSV data
2. Filter out rows with non-numeric Profit value and print new number of rows in filtered CSV data
3. Output filtered CSV data as `data2.json`
4. Order CSV data to find top 20 highest profit values and print the top 20 rows

### Solution
Environment:
- Python 3.6.9
- pandas 1.1.4

To run:
1. Download the files or clone the repository (`data2.json` file is not needed to run the solution)
2. `./run.sh` or `python3 highest-proft.py` in command line

## Solution Design and Decisions
#### Programming Language
I had chosen to use **Python** due to its quickness in writing code (versus Java's Object-Oriented structure) and its efficiency in list and tabular data manipulation.
#### pandas
My initial thought on reading a csv file with Python was to use the `csv` library. However, that route would've required a few additional steps to read the csv into memory. 

I decided to use the `pandas` library instead and to read the csv file into a dataframe. This allowed the csv file to be read into memory with one line of code.
pandas also allows for easy tabular data manipulation and has a built in method to output the data as a json, which would help in the other tasks.
#### Filtering the data
Because the Profit column had both numeric and non-numeric values, the column's data type was intepreted as string when it was read. To filter out the rows with non-numeric Profit values, I used the `pandas.DataFrame.apply` function on the Profit column and passed the values through a `is_float` function that would return whether the value could be converted into a float or not. This would return the dataframe with only the rows with a numeric Profit value.

#### JSON Format
Since the Profit column was read in as a string, it should be converted to a float before outputting as a JSON to be more accurate. I converted the Profit column into a float by getting the column, applying `astype(float)`, and setting the Profit column as the new converted column. This line of code prompted a `SettingWithCopy` warning, which I had chosen to suppress (will be explained later in this document).

pandas has a built in JSON converter, `pandas.Dataframe.to_json`. The default is to format the dataframe as a JSON by columns. I had chosen to format the dataframe as records instead to retain the structure of the row data. The output is a `data2.json` file written to the current directory.

##### SettingWithCopy Warning Analysis
The following line had produced a SettingWithCopy warning:
```
filtered_df[profit_feat] = filtered_df[profit_feat].astype(float)
```
I had looked up what this warning meant and utilized this page as my resource: https://www.dataquest.io/blog/settingwithcopywarning/

The common issues that produces the warning can be summarized as: a chaining of get and/or set operations on the dataframe may produce unwanted results due to unintended dependency/independency between the operations. 

To analyze whether that issue is applicable here, the line of code can be broken down as 

(set: (get: `filtered_df[profit_feat]`), (copy: (get: `filtered_df[profit_feat]`), `.astype(float)`))

where the outermost function is the set, and it sets a copy created from the right hand side of the function to the get-view of the left hand side. That is exactly the intention the above line of code and it does not produce any unwanted results. Therefore I had chosen to suppress the warning to keep the output clean.

#### Printing the top 20 Profit rows
This task was fairly simple. I had sorted the filtered dataframe by the Profit column in a descending order and printed the first 20 rows. To exclude the indexing that was included with the dataframe structure in efforts to retain the original data schema, I had chosen to print a `to_string` version of the filtered dataframe and had set `Index=false`.

#### Checking the solutions
I had opted for what I thought was the simpliest way to check my answers for the number of rows and top 20 Profit rows, which was to import the CSV file into my Google Drive and open it as a Google Sheets, where I can easily see the indexed rows and sort by column values.
