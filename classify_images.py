from classifier import classifier
from os import listdir
import ast

def classify_images():
filenames = []

    filename_list = listdir(pet_images)


    for file_name in range(len(filename_list)):
        filenames.append(filename_list[file_name])

    classifier_labels = []

    classifier_label_set = open("imagenet1000_clsid_to_human.txt")

    set_label = ast.literal_eval(classifier_label_set.read())

    for i in range(0,len(set_label),1):
        classifier_labels.append(set_label[i].strip().lower())

    pet_labels = []
        #Iterate through results_dic to get labels
    for idx in results_dic:
        pet_labels.append(results_dic[idx][0].strip().lower())

    pet_label_is_dog = []
    classifier_label_is_dog = []

    for i in range(len(filenames)):
        if(int(len(filenames)-len(pet_label_is_dog))==1):
            pet_label_is_dog.append(0)
        else:
            pet_label_is_dog.append(1)

    for i in range(len(filenames)):
        if(int(len(filenames)-len(classifier_label_is_dog))==1):
            classifier_label_is_dog.append(0)
        else:
            classifier_label_is_dog.append(1)

    for idx in range(0,len(filenames),1):
        if filenames[idx] in results_dic:
            results_dic[filenames[idx]] = [pet_labels[idx], classifier_labels[idx]]
        if pet_labels[idx] in classifier_labels[idx]:
            results_dic[filenames[idx]].append(1)
        else:
            results_dic[filenames[idx]].append(0)

    for idx in range(len(filenames)):
        results_dic[filenames[idx]].extend([pet_label_is_dog[idx], classifier_label_is_dog[idx]])

    # Iterates through the list to print the results for each filename
    for key in results_dic:
        print("\nFilename=", key, "\npet_image Label=", results_dic[key][0],
          "\nClassifier Label=", results_dic[key][1], "\nmatch=",
          results_dic[key][2], "\nImage is dog=", results_dic[key][3],
          "\nClassifier is dog=", results_dic[key][4])
        # Provides classifications of the results
        if sum(results_dic[key][2:]) == 3:
            print("*Breed Match*")
        if sum(results_dic[key][3:]) == 2:
            print("*Is-a-Dog Match*")
        if sum(results_dic[key][3:]) == 0 and results_dic[key][2] == 1:
            print("*NOT-a-Dog Match*")

     # Process all files in the results_dic
     for key in results_dic:
         model_label = ""
         model_label = classifier(images_dir + key, model).lower().strip()
         truth = results_dic[key][0]
         if truth in model_label:
              results_dic[key].extend([model_label,1])
        else:
            results_dic[key].extend([model_label,0])

    None
