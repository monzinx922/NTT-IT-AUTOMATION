# import json for manage dictionary data
import json

# Object save a dictionary to file
# input dictionary to save, output file path
def save_dic_to_file(dic_obj,file_path):
    # open a file to save
    myfile = open(file_path, "w+")

    # convert dict to string
    json_string = json.dumps(dic_obj)

    # write data to file as string
    myfile.write(json_string)

    # close file
    myfile.close()

# Object load a file to dictionary
# input file path saved dictionary, output dictionary object
def read_file_to_dic(file_path):
    # open file for read
    myfile = open(file_path, "r")

    # check if file in read mode
    if myfile.mode == 'r':
        # read data in file to string object
        content_str = myfile.read()

    # convert data to dictionary
    data = json.loads(content_str)
    return data

# Set up iput
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
file_path = "dic_data.json"

# Try to use function
save_dic_to_file(thisdict,file_path)
retrived_dic_data = read_file_to_dic(file_path)

# Show function result
print("your dictionary data is ", retrived_dic_data)
print("data type is ", type(retrived_dic_data))
