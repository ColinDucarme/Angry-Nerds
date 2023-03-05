# Angry-Nerds

Run Runner.py

External libs : Mediapipe, Pygame, Websocket


# Angry nerd - web sockets

# prerequesites
Having the websocket Pypy library installed

# How to run ?
the Listener side is integrated to the game using class function as seen in the server.py file, to run it simply launch the runner.py file witch will use the class contain in server.py.

# Changing ip adress and port of listener

If needed to change the ip adress, simply acces the server.py file and modify the "host" adress, same goes for the port. Sometime the server.py function might be called before the OS "Time_Delay" time out which result in an error saying "adress already in use". To fix this simply change the port used.
