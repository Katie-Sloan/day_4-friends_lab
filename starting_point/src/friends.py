import pdb

def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return (person["favourites"]["tv_show"])

def likes_to_eat(person, food):
    #pdb.set_trace()
    for snack in person["favourites"]["snacks"]:
        if snack == food:
            return True
        
    return False

