#drawing game using turtle module
import turtle
import random
import time
class TurtleGame:
    def __init__(self, player_name):
         self.player_name = player_name
         self.score = 0
         self.level = 1
    # เริ่มเกม
    
    def start_game(self):
        print(f"Welcome {self.player_name} to the Turtle Game!")
        self.play_level()
    # เล่นเลเวล
    
    def play_level(self):
        print(f"Starting Level {self.level}...")
        # Logic for playing the level goes here
        time.sleep(2)  # Simulate time taken to play the level
        self.score += random.randint(10, 100)  # Simulate scoring points
        print(f"Level {self.level} completed! Your score is now {self.score}.")
        self.level += 1
        self.ask_to_continue()
    # ถามผู้เล่นว่าจะเล่นต่อหรือไม่
    
    def ask_to_continue(self):
        choice = input("Do you want to continue to the next level? (yes/no): ")
        if choice.lower() == 'yes':
            self.play_level()
        else:
            self.end_game()
    # จบเกม
    
    def end_game(self):
        print(f"Thank you for playing, {self.player_name}! Your final score is {self.score}.")  