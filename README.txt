1. Explain every file in your release archive

Our release archive contains six main files: source_code.py, dangernoodle.py, images, music, sounds, and README.txt. 
The source_code.py file conatins our beginning code that we acquired from a link in pygamezero to github. 
dangernoodle.py contains all the python code for running our game. The images file contains .png 
images that our game uses. The music and sounds files contain .wav files our game uses for background music and sound effects.

2. Provide an overview of your project

Our project, named dangernoodle, is a recreation of the popular snake game using pygame zero. In the traditional snake game, the user moves
a snake around a game board. The snake eats food that randomly spawns on the board in order to increase in length. Every time the snake 
eats one piece of food, the snake increases in length by one unit. The snake's length is the player's score. The player’s goal is to make the snake 
as long as possible. As the snake gets longer, the game becomes more difficult. If the snake collides into itself, the player loses and the game ends. 
In our version, the user controls the snake’s direction with the arrow keys on the keyboard. However, our version employs three difficulty 
levels for the player to choose from: easy, medium, and hard. Easy mode is the traditional snake game with no obstacles. Medium mode spawns
five random obstacles on the board that cause the game to end if the snake collides. Finally, hard mode spawns five moving obstacles and
a bullet boss that the snake must avoid. These moving obstacles and the bullet boss end the game if they contact the snake's head.
Finally, medium and hard modes contain an invulnerability powerup that makes the snake invulnerable for 10 seconds. This powerup, which 
appears as a star on the board, also temporarily pauses the moving obstacles and the bullet boss. Additionally, the snake speeds up faster in medium and
hard modes, increasing the difficulty for the user. Our game also uses background music and sound effects to make the game more enjoyable for the user.

3. Explain the command to run the program and any arguments to the run command including explanation of those arguments (e.g., is there an argument to run a certain level or in easy/hard mode?, see Linux man pages for examples of this)

To run dangernoodle, simple double click on the dangernoodle.py. If this does not work, open PowerShell within the release archive and enter:

python -i dangernoodle.py 

Once the game starts, the user must use the mouse to click on "EASY", "MEDIUM", or "HARD". After selecting the game mode, use the arrow keys to guide
the snake around the board. Once the snake crashes causing the game to end, simply close the game window.

4. List any Python or other code packages or modules needed to run the program (so the user can make sure they are installed)

We only used pygame zero and random. Here is the installation command:
pip install pgzero

5. Describe any potential input that might be needed and what formats are acceptable

No input needed other than initial mouse click and movement commands.

6. Describe any output files that are created

No output files created.

Citations:
Snake image and source code:

Pope, Daniel. "pgzero -> examples -> snake". Github. 2017 https://github.com/lordmauve/pgzero/tree/master/examples/snake

We used this source as the basic snake game to which we added configurations. Easy difficulty is very similar to this documentation.

Image for stationary obstacles:
"Platformer Art: Extended Enemies". Kenny. 2020.  https://kenney.nl/assets/platformer-art-extended-enemies

Image for boss:
"Bullet Bill" YAWD. 2020. https://ya-webdesign.com/explore/vector-bullet-bill/

Image for moving obstacle:
"Green Shell". Fandom. 2020. https://supersmashbros.fandom.com/wiki/Green_Shell

Image for powerup:
"Star". Clipart. 2020. https://www.clipartkey.com/view/TTwwmR_super-mario-fire-power/