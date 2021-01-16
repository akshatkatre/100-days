import requests

input_parameters = {
    "name": "akshat"
}

response = requests.get(url="https://api.agify.io", params=input_parameters)
response.raise_for_status()
# print(response.text)
age = response.json()['age']
print(age)

response = requests.get(url="https://api.genderize.io", params=input_parameters)
response.raise_for_status()
gender = response.json()['gender']
print(gender)

