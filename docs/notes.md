Main Idea: Gaming Community Social Platform

 

User Story: This project will be inspired by my involvement in the gaming community. This platform will allow users to create personalized profiles, connect with fellow gamers, and share gaming content. Users will have the ability to engage with user profiles and discussion posts. Stretch goals: users can upload various kinds of posts such as polls, status updates, and images to showcase any accomplishments or updates to their gaming activities as well as messaging rooms for 1 on 1 interaction or group interaction. 

 

How my project will meet project requirements:

Models - 

     Users: Store user data such as name, username, email, password, join date, and birthdate.

     Friendships: Store all connections between user id's and their respective relationships                 (friend or non-friend)

     Posts: facilitate all posts updated and their engagement/interaction data such as comments/likes

     Game Groups: facilitate users that belong to specific game communities, giving users a feed that will be based on their likes and interests 

 

Relationships - 

     Users: many-to-many relationships managing friend connections and user game groups. A connection of ID to identify a user and show their involvement in the other categories

     Friendships: many-to-many relationships between users and gaming groups using ID for games and users. what user id like what specific game id and what members are in what groups. 

     Posts: one-to-many relationship between user and game. Users owns the post and the post is owned by one user. Will user user.id and post.user_id

     Game Groups:A many-to-many relationship between users and gaming groups for membership. Users will be part of gaming groups and the gaming groups will have a correlation of many posts and many users. 

API Routes - 

     1. /api/users

     2. /api/friends

     3. /api/groups

     4. /api/discussion

Frontend Routes - 

     1. /profile

     2. /friends

     3. /home

     4. /feed

     5. /gamerooms

Forms - 

     Sign Up: Allow users to sign up if they are not a member of the current platform

     Login: Allow users to login if they are already members of the current platform

     Gaming/User posts: Allow users to post gaming feeds on the platform

     Invite/Create Rooms: Allow users to submit request to create a new gaming room or add users to an existing gaming room. 

 

User Authentication - 

     create user authentication using Flask-Login.

     use password hashing and secure login mechanisms

     Ensure that only authenticated users can access certain routes, like profile and friend management.