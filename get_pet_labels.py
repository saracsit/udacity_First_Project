from os import listdir,path
def get_pet_labels(pet_images):
    filename_list = listdir(pet_images)

    filenames=[]
    pet_labels = []

    for file_name in range(len(filename_list)):
        filenames.append(filename_list[file_name])



    for i in  range(len(filenames)):
        filename = filenames[i]
        splited_file_name = filename.split("_")
        splitted_length = 0
        label_string = []
        while splitted_length < int(len(splited_fn)-1):
            label_string.append(splited_file_name[splitted_length])
            splitted_length++

        pet_labels.append(" ".join(label_string))



    results_dic = dict()

    for idx in range (0,len(filenames),1):
        if filenames[idx] not in results_dic:
            results_dic[filenames[idx]] = [pet_labels[idx]]
        else:
            print("*** Warning: Keys=", filenames[idx], "already exists in results_dic with value=", results_dic[filenames[idx])

#Iterating through a dictionary printing all keys & their associated values

print("\nPrinting all key-value pairs in dictionary results_dic:")
for key in results_dic:
    print("Filename=", key, "   Pet Label=", results_dic[key][0])


#extracting only the words # of the file that contain the pet image label
    for idx in range(0, len(in_files), 1):
        if filename_list[idx][0] != ".":
            pet_label = " "

    #Split the filename_list[idx] list, then convert the list to string and remove whitespaces to the end of the string while converting to lowercase
            splited_root_ext = path.splitext(filename_list[idx])

    #Conditiobal statement for assigning the splited list values and then append the results to pet_label
            if type(splited_root_ext[0])!='str' and len(splited_root_ext[0])!=1:
                pet_label = pet_label.join(splited_root_ext[0].split("_")[:-1]).lower().strip()
            else:
                 pet_label = pet_label.join(splited_root_ext[0]).lower().strip()

        if filename_list[idx] not in results_dic:
               results_dic[filename_list[idx]] = [pet_label]

            else:
                print("** Warning: Duplicate files exist in directory:",
                     filename_list[idx])


     return results_dic
