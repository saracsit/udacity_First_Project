def adjust_results4_isadog(results_dic, dogfile):
    #Read in the dog names from dognames.txt file into a data structure (like a dictionary)
DogNames_dictionary = {}
dogs = open(dogfile)
 DogFileNames = dogs.readlines()

 #append the dog name if it is not in DogNames_dictionary
 for i in DogFileNames:

        if key.strip("\n") in DogNames_dictionary:
            print("The dog name " + key.strip("\n") + " already exists")
        else:
            DogNames_dictionary[i.strip("\n")] = 1

#to find matches
for i in results_dic:
        #print(results_dic[i][1])
        if(results_dic[i][0] in DogNames_dictionary.keys()):

                results_dic[i].append(1)
        else:

                results_dic[i].append(0)


        if(results_dic[i][1] in DogNames_dictionary.keys()):
            results_dic[i].append(1)
        else:
            results_dic[i].append(0)

# Creates dognames dictionary to determine  matching to results_dic labels

DogNames_dictionary = dict()
with open(dogfile, "f") as file:
    DogName = file.readline()
    while DogName != "":
        DogName = DogName.strip("\n")

        if DogName not  in DogNames_dictionary:
                DogNames_dictionary[DogName] = 1
                DogName = file.readline()

#add index3 and index4
for key in results_dic:
    if results_dic[key][0] in DogNames_dictionary:
        if results_dic[key][1] in DogNames_dictionary:
                results_dic[key].extend((1, 1))
        else:

                results_dic[key].extend((1, 0))
    else:
         if results_dic[key][1] in DogNames_dictionary:

                results_dic[key].extend((0, 1))
         else:

                results_dic[key].extend((0, 0))
