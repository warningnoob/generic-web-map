import requests

#stupid file code
list_choice = input("built in or file ").lower()
link = input("what is the base link? ")

if list_choice == "file":
    location = input("Enter the word list file path: ")
    with open(location, "r") as file:
        data_into_list = file.read().splitlines() 


else:
    data_into_list = ["/admin", "/login", "/files"]

for addon in data_into_list:
    full_url = link + addon
    try:
        x = requests.get(full_url)
        code = x.status_code

        if code == 200:
            print(f"Website {full_url} is up (status code: {200})")
        else:
            print(f"Error accessing {full_url} (status code: {code})")
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {full_url}: {e}")