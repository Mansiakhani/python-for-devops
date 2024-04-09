student_info = {"name":"Mansi",
                "age": 21,
                "education": "ME"}

print(student_info["education"])

for key, value in student_info.items():
    print(key,value)

x = student_info.items()
print(x)

#List of Dictionary

ec2_instance_info = [{"name": "Server_1", "Id": 123233, "type": "t2.micro"},
                     {"name": "Server_2", "Id": 656223, "type": "t2.nano"},
                     {"name": "Server_3", "Id": 1232553, "type": "t2.large"}]

print(ec2_instance_info[0]["name"])

for i in range(len(ec2_instance_info)):
    print(ec2_instance_info[i]["name"])