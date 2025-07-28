import gzip
import shutil

def compress_file(input_file, output_file):
    """Compress a file using gzip."""
    with open(input_file, 'rb') as f_in:
        with gzip.open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f" File compressed and saved as {output_file}")

def decompress_file(input_file, output_file):
    """Decompress a gzip file."""
    with gzip.open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f" File decompressed and saved as {output_file}")


# Use raw strings (r"...") or double backslashes for Windows paths
compress_file(r"C:\Users\Sivar\Downloads\Sivaraj SEO.pdf",
              r"C:\Users\Sivar\Downloads\Sivaraj SEO.pdf.gz")

decompress_file(r"C:\Users\Sivar\Downloads\Sivaraj SEO.pdf.gz",
                r"C:\Users\Sivar\Downloads\Sivaraj SEO_restored.pdf")
