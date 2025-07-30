## Scenario 19: Optimizing Database Queries  
**Problem Statement: Optimizing SQL queries for faster results.**  

**Detailed Scenario: A Python application interacts with a SQL database. The goal is to improve the performance of queries that retrieve large datasets.**  

**Usecase Approach: Use indexing, limit the number of rows fetched, or use batch processing to improve query performance.**  

**Tools and Modules: sqlite3, os**  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════  
Approach:  
- Indexing: Created on product column to speed up filter queries.  
- LIMIT clause: Reduces the load by fetching only top 10 rows.  
- Batch inserts: Done in one loop instead of repeated commits.  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════  


