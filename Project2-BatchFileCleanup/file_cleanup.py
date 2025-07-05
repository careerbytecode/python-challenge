import os
import sys
import re
import argparse

def clean_text(text):
    pattern = re.compile(r'[^A-Za-z0-9\s\n]')
    cleaned = pattern.sub('', text)
    cleaned = re.sub(r'\s+', ' ', cleaned)
    return cleaned.strip()

def process_files(input_folder, output_folder):
    if not os.path.exists(input_folder):
        print(f"The folder {input_folder} does not exist.")
        sys.exit(1)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            try:
                with open(input_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                cleaned_content = clean_text(content)
                with open(output_path, 'w', encoding='utf-8') as outfile:
                    outfile.write(cleaned_content)
                print(f"Processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Clean up text files in a folder.")
    parser.add_argument("input_folder", help="Input folder containing files to be corrected")
    parser.add_argument("output_folder", help="Output folder for cleaned files")
    args = parser.parse_args()
    process_files(args.input_folder, args.output_folder)

if __name__ == "__main__":
    main()