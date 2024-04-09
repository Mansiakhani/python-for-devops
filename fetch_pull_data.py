import requests

response = requests.get("https://api.github.com/repos/iam-veeramalla/python-for-devops/pulls")
if response.status_code == 200:
    details =response.json()
    print(details)
    print(type(details))
    information ={}
    print("information before loop", information)
    for detail in details:
        username = detail['user']['login']
        print(username)
        print(type(username))
        if username in information:
            print("Information before increment",information)
            information[username] +=1
            print("information value after increment" ,information)
        else:
            information[username]=1
            print(information)
    print("The Pull request username and count:")
    for username, count in information.items():
        print(f"{username} did {count} pull request ")

    #print(len(details))
    #print("details of user 3", details[2]["user"]["login"])
    #for i in range(len(details)):
        #print(f"username for user  {i}  is :" ,details[i]["user"]["login"])
else:
    print(f"failed to fetch data. Status code : {response.status_code}")

