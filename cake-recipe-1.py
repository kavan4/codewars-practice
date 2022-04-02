def cakes(recipe, available):
    
    # make sure all the ingredients from recipe are available - convert to set and ensure recipe is subset of avail
    recipe_set = set(recipe.keys())
    available_set = set(available.keys())
    
    if not(recipe_set <= available_set) :
        return 0

    #init list 
    ratios_list = []

    #check if qty is sufficient
    for qty in available:
        if qty in recipe:
            ratios_list.append(available[qty]//recipe[qty])
        
    print(ratios_list)

    if min(ratios_list)>=1:
        return min(ratios_list)
    else : 
        return 0