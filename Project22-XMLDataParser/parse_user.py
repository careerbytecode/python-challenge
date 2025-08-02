import xml.etree.ElementTree as ET

def parse_users(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        print("User Details:\n" + "-" * 30)
        for user in root.findall('user'):
            user_id = user.get('id')
            name = user.find('name').text
            email = user.find('email').text
            role = user.find('role').text

            print(f"ID: {user_id}")
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Role: {role}")
            print("-" * 30)
    except Exception as e:
        print(f"Failed to parse XML: {e}")

if __name__ == "__main__":
    parse_users("users.xml")

