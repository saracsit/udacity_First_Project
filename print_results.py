def print_results (results, results_stats, model,
                  print_incorrect_dogs = False, print_incorrect_breed = False):
                  #print summary
                  print("\n Results Summary for CNN Model used",model.upper())

                  #print number of Images
                  print("{:20}: {:3d}".format('Number of total Images', results_stats['n_images']))

                  #print number of dog Images
                  print("{:20}: {:3d}".format('Number of Dog Images', results_stats['n_dog_images']))

                  #print Number of "Not-a" Dog Images
                  print("{:20}: {:3d}".format('Number of Not-a Dog Images', results_stats['n_notdog_images']))

                  #Percentage Calculations:

                    #% Match (optional - this includes both dogs and not-a dog)
                    #% Correct Dogs
                    #% Correct Breed
                    #% Correct "Not-a" Dog
                    for key in results_stats:
                        if key.startswith('p'):
                            print(key,results_stats[key])

                #Printing Misclassifications:

                #1-incorrect dogs

                if (print_incorrect_dogs and
                ( (results_stats['n_correct_dogs'] + results_stats['n_correct_notdogs'])
                != results_stats['n_images'] )):
                    print("\n incorrect  Dog or NOT Dog classification:")
                    for key in results:
                        if sum(results[key][3:]) == 1:
                            print("Pet Label = ",results[key][0] ,"Classifier Label= ",results_dic[key][1] )
                #2-incorrect breeds

                if (print_incorrect_breed and
        (results_stats['n_correct_dogs'] != results_stats['n_correct_breed'])
       ):
        print("\nincorrect Dog Breed classification:")

        for key in results:

            if ( sum(results[key][3:]) == 2 and
                results[key][2] == 0 ):
                    print("Real= " results[key][0],  "Classifier= ",results[key][1])
