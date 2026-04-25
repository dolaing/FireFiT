print("Welcome to the FireFit Family!")

#Ask the user to input information upon downloading the app
class UserProfile:
  def __init__(self, name, age, weight, height, goal, activity_level):
        self.name = name
        self.age = age
        self.weight = weight  # in pounds or kg
        self.height = height  # inches or cm
        self.goal = goal  # "fat_loss", "muscle_gain", "endurance"
        self.activity_level = activity_level  # "low", "moderate", "high"

#Display the profile for the user to see
def display_profile(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Weight": self.weight,
            "Height": self.height,
            "Goal": self.goal,
            "Activity Level": self.activity_level
        }

# Ask the user what Activity Level would they like to start at
def get_activity_multiply (activity_level):
      levels= {
            "low": 1.2,
             "moderate": 1.55,
             "high": 1.9
      }
      return levels.get(activity_level, 1.2)
      
   