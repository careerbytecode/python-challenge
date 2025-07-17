## Scenario 34: Caching API Responses for Performance  
**Problem Statement: Caching API responses to improve performance.**

**Detailed Scenario: To minimize API calls, the application needs to cache the responses for certain requests (e.g., user data) for a predefined time.**

**Usecase Approach: Use Python’s cachetools or functools.lru_cache to cache API responses in memory.**

**Tools and Modules: cachetools, functools**

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════

Approach:  
- Import cachetools and requests  
- Create a TTLCache with max size and expiry time  
- Use @cached(cache) to decorate your API function  
- On first call, fetch from API and store in cache  
- On next call (within TTL), return cached response  
- After TTL expires, fetch fresh data again  

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════
