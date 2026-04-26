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
      
#Make some reccommendations (fat loss, increase muscle, cardio, eating habits)
def get_goal_recommendation(goal):
    if goal == "fat_loss":
        return "Focus on calorie deficit, cardio 3-5x/week, and light strength training."
    elif goal == "muscle_gain":
        return "Increase protein intake, lift weights 4-6x/week, and progressively overload."
    elif goal == "endurance":
        return "Incorporate long cardio sessions and interval training."
    else:
        return "Set a clear fitness goal."
    
# Ask the user for a daily coloric estimate

def estimate_calories(weight, activity_level):
    base_calories = weight * 14  # simple baseline
    multiplier = get_activity_multiply (activity_level)
    return int(base_calories * multiplier)

#Provide a user summary
def generate_user_summary(user):
    calories = estimate_calories(user.weight, user.activity_level)
    recommendation = get_goal_recommendation(user.goal)

    return {
        "Profile": user.display_profile(),
        "Estimated Daily Calories": calories,
        "Recommendation": recommendation
    }

   ####### User Set is done , now its time for Logging Data#######

   #class Exercise:
    def __init__(self, name, set, reps, weight):
        self.name = name
        self.set = set
        self.reps = reps
        self.weight = weight

    def display(self):
        return {
            "exercise": self.name,
            "sets": self.sets,
            "reps": self.reps,
            "weight": self.weight
        }
#Once the information is added to the app its time to tack it
class WorkoutLogger:
    def __init__(self):
        self.workouts = []

    def log_workout(self, workout):
        self.workouts.append(workout)

    def get_all_workouts(self):
        return [w.display_workout() for w in self.workouts]

    def get_user_workouts(self, user_id):
        return [w.display_workout() for w in self.workouts if w.user_id == user_id]
    
#Performance tracking should be added to each members account
def get_exercise_progress(workouts, exercise_name):
    history = []

    for workout in workouts:
        for ex in workout.exercises:
            if ex.name == exercise_name:
                history.append({
                    "date": workout.date,
                    "weight": ex.weight,
                    "reps": ex.reps
                })

    return history

#This is important for the users because it ensures that it tracks the progress of each user, so that they can review it for later.

#Create the basic dashboard for the app
#Import Matplotlib to help with prototype charts and graphs of progression