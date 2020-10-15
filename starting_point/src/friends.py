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


 # 4. For a given person, add a new name to their list of friends
  # (e.g. the function add_friend(self.person2, "Scrappy-Doo") should add Scrappy-Doo to the friends.)
  # (hint: This function should not return anything. 
  # After the function call, check for the length of the friends array to test it!)
  
def add_friend(person, friend):
    person["friends"] = person["friends"].append("friend")

    return len(person["friends"])