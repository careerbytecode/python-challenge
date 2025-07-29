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

<img width="795" height="87" alt="image" src="https://github.com/user-attachments/assets/30bbfc3d-894d-44cf-a4fa-7173305dd8d9" />

<img width="550" height="197" alt="image" src="https://github.com/user-attachments/assets/4fec4361-7ad5-4467-8941-c7a1feca7b0d" />
