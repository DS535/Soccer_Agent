# Soccer_Agent
This Repo is about an Agent playing Soccer with some hardcoded strategies

For the implementation of the system, I have used pygame python library.
In this system design, I am using following assets.
1. Blue Players
2. Red Players 
3. Football
4. Football Ground

Design components:
As the game starts 4 replicas of BLUE_PLAYER, 3 replicas of RED_PLAYER, a FOOTBALL and a FOOTBALL_FIELD is rendered on the game screen.
All the objects are defined using width*height.
Football field of size (1000*700)
Players are of size (40*50)
Football is of size (25*25)
All coordinates are measured from top left corner i.e. origin(0,0) is located at top left corner.
The assets need to be transformed to take a particular size on the screen. That is done by using transform and scale.




