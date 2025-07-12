##Scenario 21: Multi-Threading for Performance Optimization
**Problem Statement: Speeding up a computationally intensive task by using multiple threads.**

**Detailed Scenario: An application performs a computationally intensive task that needs to be optimized using multi-threading to handle multiple tasks concurrently.**

**Usecase Approach: Use Python’s threading module to execute tasks in parallel.**

**Tools and Modules: threading, time**

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approch:  
Use Python's `threading` module to make our program faster by running parts of the work at the same time.

1. **Split the Work:** Break the big task into smaller, independent pieces.
2. **Create Threads:** Make a thread for each piece using `threading.Thread`.
3. **Start Threads:** Start all threads so they run together.
4. **Wait for Threads:** Use `thread.join()` to wait until all threads finish.
5. **Combine Results:** Gather the results from each thread if needed.

This way, the program can finish faster by doing several things at once.


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Refrence:  
- [Python Threading Explained in 8 Minutes](https://www.youtube.com/watch?v=A_Z1lgZLSNc)
- [Python threading — Official Documentation](https://docs.python.org/3/library/threading.html)
- [Real Python: An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)
- [Python time — Official Documentation](https://docs.python.org/3/library/time.html)
