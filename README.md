🎮 Hangman Game - CodeAlpha Task 1

Overview  
This project is a simple Python-based implementation of the classic Hangman game.  
The player must guess the hidden word by suggesting letters or the entire word within 6 wrong attempts.  
With each incorrect guess, a part of the hangman is drawn until the game is lost.  

Features  
• Random word selection  
• Guess letters or the full word  
• Tracks wrong guesses and remaining attempts  
• ASCII hangman drawing for each mistake  
• Prevents duplicate guesses  
• Beginner-friendly command-line interface  

How to Play  
1. Clone this repository  
   git clone https://github.com/abdulraffayrazaq/CodeAlpha_TaskAutomation-TASK-1.git  
2. Open the project folder  
3. Run the game  
   python hangmangame.py  

Sample Gameplay  
Word: _ _ _ _ _  
Chances left: 6/6  
👉 Guess a letter: a  
✅ Correct!  

Word: a _ _ _ e  
Chances left: 6/6  
👉 Guess a letter: b  
❌ Wrong! Chances left: 5/6  

Concepts Used  
• random – to select words  
• while loop – to run the game until win/lose  
• set – to track guessed letters  
• if/else – to check guesses and update progress  
• string formatting – to display word state  

Author  
Abdul Raffay Razaq  
GitHub: https://github.com/abdulraffayrazaq
