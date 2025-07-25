from pathlib import Path

# Creaing a Path object
file_path = Path(r"C:\Users\Sivar\Downloads\DNA (2025) Tamil.mkv")

# Checking if the file exists
if file_path.exists():
   print("The file exists.")

else:
   print("The file does not exist.")
