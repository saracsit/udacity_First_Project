def calculates_results_stats(results):
    results_stats=dict()

    results_stats['n_dog_images'] = 0
    results_stats['n_match'] = 0
    results_stats['n_correct_dogs'] = 0
    results_stats['n_correct_notdogs'] = 0
    results_stats['n_correct_breed'] = 0
    results_stats['n_notdog_images'] =0

    results_stats['n_images'] = len(results)

#loop through results dictionary toi increment counters

for key in results:
         #Pet Label is a dog
         if results[key][3] == 1:
            results_stats['n_dog_images'] += 1

            #both labels are of dogs
            if results[key][4] == 1:
                results_stats['n_correct_dogs'] += 1
        #pet label ia not a dogs
         if results[key][3]==0:
            results_stats['n_notdog_images'] +=1
            #Both labels are NOT of dogs
            if results[key][4]==0:
                results_stats['n_correct_notdogs']
        #Pet Label is a dog & Labels match
    else if results[key][3]==1:
            if results[key][2]==1:
                results_stats['n_correct_breed'] +=1


        # Labels Match
    if results[key][2] == 1:
            results_stats['n_match'] += 1


results_stats['pct_match'] = results_stats['n_match']/ results_stats_dic['n_images']*100

results_stats['pct_correct_dogs'] = results_stats['n_correct_dogs']/ results_stats['n_dog_images']*100

 results_stats['pct_correct_breed'] = results_stats['n_correct_breed']/ results_stats['n_dog_images']*100

if results_stats['n_notdog_images'] > 0:
        results_stats['pct_correct_notdogs'] = (results_stats['n_correct_notdogs'] /
                                                results_stats_dic['n_notdogs_images'])*100.0
    else:
        results_stats['pct_correct_notdogs'] = 0

return results_stats
