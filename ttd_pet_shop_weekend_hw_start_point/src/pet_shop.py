# WRITE YOUR FUNCTIONS HERE or else
def get_pet_shop_name(pet_shop): # could be banana but pet_shop is more descriptive 
    return pet_shop["name"] # name is the key. eg "camelot of pets" is the value, ''''''name''''' is the key for it

    # line 2, pet_shop is the parameter
    # arguement passed in is self.cc_pet_shop  - line 32
    # square brackets to access value thats stored in the key. []
    
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

# would flowcharts become too complicated? maybe its a decent stepping stone
# checklist



def get_stoc






