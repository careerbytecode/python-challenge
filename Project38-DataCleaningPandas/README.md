## Scenario 38: Data Cleaning with Pandas  
**Problem Statement:** Cleaning and preprocessing data from a raw dataset.

**Detailed Scenario:** The dataset contains missing values, outliers, and incorrect formats that need to be cleaned before further analysis.

**Use Case Approach:** Use Python’s pandas module to clean and preprocess the dataset, fill missing values, and remove outliers.

**Tools and Modules:**  
- `pandas` for data manipulation and cleaning.

**Approach Overview:**  
1. Load the dataset into a pandas DataFrame.  
2. Inspect the data for missing values, outliers, and incorrect formats.  
3. Clean the data by filling or removing missing values, handling outliers, and correcting data types.  
4. Export the cleaned dataset for further analysis.

**What this script does**
- Replaces missing VM statuses with "UNKNOWN"
- Drops entries without IP addresses
- Removes outliers in RAM (e.g., 999999)
- Normalizes string columns (names, flavors, images)
- Converts creation timestamps to datetime

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

**Reference:**  
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Small YouTube tutorial](https://www.youtube.com/watch?v=bDhvCp3_lYw)