## Scenario 42: Developing a REST API with Flask  
**Problem Statement: Building a simple REST API to handle GET and POST requests.**

**Detailed Scenario: A Python application needs to expose an API to handle requests for retrieving and posting data to/from**

**Usecase Approach: Use Python’s Flask framework to create RESTful endpoints and handle JSON data.**

**Tools and Modules: Flask**

══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════  
Approch:  
Set up Flask app and use a list (items) to store data temporarily.  
Create /items route for GET to return all items and POST to add a new one.  
Use request.get_json() to read data, validate name and price, and avoid duplicates.  
Send JSON responses using jsonify() and run the app with app.run(debug=True).  


══════════════ ⭑ ⭑ ⭑ ⭑ ⭑ ══════════════  
Refrence:
-[Flask Intro](https://python-adv-web-apps.readthedocs.io/en/latest/flask.html#deconstruct-the-code-in-a-small-flask-app)

<img width="1912" height="1033" alt="image" src="https://github.com/user-attachments/assets/edf1e7be-1c95-462a-b33d-709f4abe8164" />
