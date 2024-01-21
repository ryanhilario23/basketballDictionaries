players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]


new_team=[]
class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

# Attempt of Ninja Bonus
    # @classmethod
    # def get_team(cls,players):
    #     new_team2 = []
    #     for i in players:
    #         new_team2.append(players)
    #     return new_team
# Player.get_team(players)

for i in players:
	test = Player(i['name'],i['age'],i['position'],i['team'])
	new_team.append(test)

for i in new_team:
    testing = [i.name, i.age, i.position,i.team]
    print(testing)