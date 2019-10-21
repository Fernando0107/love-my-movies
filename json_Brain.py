import json

def json_Brain(x):
    try:
        # Get a file object with write permission.
        file_object = open("test.json", 'w+')

        # Save dict data into the JSON file.
        json_data = json.dump(x, file_object, indent=4, sort_keys=False)

        print("test.json" + " created. ")

    except FileNotFoundError:
        print("test.json" + " not found. ")


json_Brain(d)
