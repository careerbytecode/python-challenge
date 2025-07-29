## Scenario 31: Image Processing and Transformation  
**Problem Statement: Performing image manipulation tasks such as resizing and applying filters.**  

**Detailed Scenario: A Python application needs to process images by resizing them to fit a specific resolution and applying filters (e.g., grayscale, blur).**  

**Usecase Approach: Use Python’s Pillow library to load, resize, and apply filters to images.**  

**Tools and Modules: Pillow**  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════  

Approach:  
- Open image with PIL.Image.open  
- Resize using .resize()  
- Convert to grayscale using .convert("L")  
- Apply filter with .filter(ImageFilter.BLUR)  
- Save all outputs in a new folder  



══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════
