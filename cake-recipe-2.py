def cakes(recipe, available):
    try:
        return min(available[qty]//recipe[qty] for qty in recipe)
    except:
        return 0