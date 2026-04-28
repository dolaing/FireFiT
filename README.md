# FireFit Workout Tracker

**Description:**  
FireFit is a powerful and easy-to-use workout tracking app designed to help users stay consistent, monitor progress, and reach their fitness goals. Whether you're training for performance or just staying active, FireFit allows you to log workouts, track improvements, and stay motivated every step of the way.

In today's society, it can be a little difficult for many individuals to consistently track their workouts, times, and progress in one place. As a student-athlete, I can definitely relate to this issue, as many athletes either forget their stats or are unable to effectively analyze and track the improvements over time. This project will thereby solve that problem by creating a simple application that allows users to log workouts, visualize progress, and track running and weight journey

As we start to build our app, I plan to create a fitness performance tracker using Python. This app will allow users to input their daily workout (time, type of workout, and distance). The data therefor will be stored and displayed through graphs, weekly, to ensure that users are given accurate data, which will enable them to evaluate their performance and provide positive feedback and possibly suggestions to their users. Some tutorials that I will possibly be using are Tutorials I may use are Python basics: https://www.w3schools.com/python/ and Matplotlib tutorial: https://matplotlib.org/stable/tutorials/index.html. 

Some features that this App will be  providing for its users that can be accessed are:
Add and save workout data
View personal records (PRs)
Graph progress 
Simple menu-based interface
editing or deleting entries
Weight watcher

*****************************
Overview of steps taken 

Step 1.
 The first thing we did was to create a user profile for our customers in which personal and fitness information can be stored. This information included name, age, weight, and height, along with their fitness goals and activity levels. These, therefore, allow the app to start with the basics needed to implement and track their workouts as it brings them closer to their goals. This ensures that a personal connection is built between technology and humans, aiming to achieve a common goal.

 Step 2:
 Next, we added the logic that makes the profile interactable. Activity levels are converted to estimate how active a person is, and their fitness goals are used to give basic recommendations. This, therefore, will help us to use the raw data 
 
 Step 3:
 Implementing a simple formula to estimate the calorie intake of a user and what they should consume on a daily basis. We will take into consideration their body weight and activity level. This, therefore, can help us to understand the nutritional intake that connects directly to our users achieving their goals

 Step 4:
  Now it's time to track and develop the workout systems for the app. With this feature, we will be able to develop an exercise class that stores the details along with the movements, such as sets and reps. A workout class groups the exercises into one session with dates, and a workoutlogger class that stores all the workouts and allows you to retrieve them. This allows us to record what is actually happening in the gym, which is critical for tracking progress.
  
Step 5.
A Progress tracker was then developed so the users will be able to look back and track their progress. These exercises will change over time with the history of the weights and reps. This app will then start to create a progress analysis, which separates the simple tracker from a normal smart fitness app.

Step 6.
Instead of just showing numbers, we also used matplotlib to display progress over time using user-friendly, visual graphs that help users better understand their progression and see improvement, plateau, and decline.

