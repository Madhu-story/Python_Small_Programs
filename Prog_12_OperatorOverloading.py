
class Score:
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    def __str__(self):
        return f'{self.name} : {self.points}'
    
    def __add__(self, other):
        return Score('Total score', self.points + other.points)
    
    def __lt__(self, other):
        return self.points < other.points
  
player1 = Score('Rahul', 40)
player2 = Score('Sanjay', 60)

# To get the total score:
total_score = player1 + player2

print(player1)
print(player2)
print(total_score)

# To get the winner or high scorer
if player1 < player2:
    print(f"{player2.name} wins!")
else:
    print(f"{player1.name} wins!")

