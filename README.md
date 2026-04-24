# A Smart Desk inspired (mostly) by the Iron Man movies

* The Setup has a projector projecting on a flat desk and a Camera pointed at the desk.
* The Camera feed is used to perform hand tracking which will be used to interact with the projected screen
* The whole setup will be controlled by a Raspberry Pi 4
___
# How does it work

* We're using Mediapipe.js for the pose estimation/Hand Tracking
* As of now All the Apps are written in HTML so that they are standalone and can be run on a browser
We can also use the mediapipe library for python and build cool apps for the desk
___
# Apps
## Checkers
<img width="1920" height="893" alt="image" src="https://github.com/user-attachments/assets/49e15f13-254f-48d0-93de-0c8a7836f265" />

* Grab pieces by moving your hands and pinching
* release to place the piece
* The "AI" script will play its turn automatically

## Flappy Bird
<img width="1920" height="893" alt="image" src="https://github.com/user-attachments/assets/4e1b04b7-4678-4eb0-a3c1-c395c611df2a" />

* Pinching makes the bird fly higher
  
## pong
<img width="1920" height="893" alt="ScreenShot Tool -20260407081125" src="https://github.com/user-attachments/assets/79b1a5a4-00b2-425b-a006-9f3b037594d0" />

*Pinch and move your hands to move the padle upwards or Downwards

# Future
* Once I get the Desk, I'll make a custom Dashboard that kinda flushes in with the real world stuff like the keyboard, mouse pad and the penstand.
* I'll need a Music player and video player on the dashboard
* pomodoro timer
