📝 CSV Writer with Mixed Rows in Python
This script demonstrates how to write structured data (a mix of lists and tuples) into a CSV file using Python’s built-in csv module.

✅ Highlights
- Supports both list and tuple row formats
- Writes cleanly to a CSV file (saved_data.csv)
- Useful for combining dynamic sources of tabular data

📚 Notes
- csv.writerows() supports iterables like both list and tuple, so mixing them works fine.
- newline='' ensures no extra blank lines on Windows.
- You can change the delimiter to ;, \t, etc., for different formatting needs.



