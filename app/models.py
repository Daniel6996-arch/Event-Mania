class Event:
    '''
    Pitch class to define Pitch Objects
    '''

    def __init__(self,name,time,location,price,owner,followers,category ):
        self.name = name
        self.time = time
        self.location = location
        self.price = price
        self.owner = owner
        self.followers = followers
        self.category = category
        