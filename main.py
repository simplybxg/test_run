#create new files to test commiting and pushing github
import json

# Load the JSON file
with open("enterprise_attack.json", "r", encoding="utf-8") as file: #file here is the new nickname for the json file
    data = json.load(file) #data is the json file nickname "file"

# Counting
count = 0 #starts counting at 0
nodup_name = set() #a set doesn't allow duplicated name
threat_actor =[] #an empty list to store the threat actors

#go through one by one, called item
#for every object in data (as defined above) - won’t crash even if an id is not found because the list is empty
for item in data.get("objects", []):

    #if the item retreived equals to threat-actor
    if item.get("type") == "threat-actor":
        #retrieve a threat actor's name – check for duplicate
        panda = item.get("name")

        #retrieve the id of the threat actors
        popo = item.get("id")

        #double count panda
        if panda and panda not in nodup_name:

            #count = count + 1
            count += 1

            #panda is added to the id set so it won’t be saved again
            nodup_name.add(panda)

            #save the threat actor in the threat actor list
            threat_actor.append(
                { "id": popo, "threat actor" : panda} #get the id and name
            )

#print the result here
print("Total number of threat actors:", count)

#save the threat actors' ids and names onto a seperate file
with open("threat_actor_names.json", "w", encoding="utf-8") as outfile:
    json.dump(threat_actor, outfile, indent=1)

#with: closes the file once the goal is completed
#"w": write mode | overwrite an existing file or create a new one
#"outfile": a nickname for the whole thing to simplify the code
#xinchao
