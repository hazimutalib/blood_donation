# import requests

# def check_url_existence(url):
#     try:
#         # Send a GET request to the URL
#         response = requests.get(url)

#         # Check if the response status code is 2xx (indicating success)
#         if response.status_code // 100 == 2:
#             print(f"URL '{url}' exists. Status code: {response.status_code}")
#             return True
#         else:
#             print(f"URL '{url}' does not exist. Status code: {response.status_code}")
#             return False
#     except requests.RequestException as e:
#         print(f"Error while checking URL '{url}': {e}")
#         return False

# # Replace with the URL you want to check
# url_to_check = 'onsv'

# # Check if the URL exists
# url_exists = check_url_existence(url_to_check)


from datetime import datetime
# x = datetime.now().date - datetime.now().date
print(datetime.now().date())