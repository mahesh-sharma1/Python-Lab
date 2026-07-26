import random

def get_difficulty():
    """Get game difficulty from user"""
    print("\nSelect Difficulty:")
    print("1. Easy (1-50, 10 attempts)")
    print("2. Medium (1-100, 7 attempts)")
    print("3. Hard (1-200, 5 attempts)")
    
    while True:
        choice = input("\nEnter choice (1-3): ")
        if choice == '1':
            return 50, 10
        elif choice == '2':
            return 100, 7
        elif choice == '3':
            return 200, 5
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

def give_hint(guess, secret, attempts_left):
    """Give hint to player"""
    if abs(guess - secret) <= 5:
        print("🔥 You're very close!")
    elif abs(guess - secret) <= 15:
        print("👍 You're getting warm...")
    else:
        print("❄️ You're far off...")
    
    if guess < secret:
        print("📈 Try a higher number!")
    else:
        print("📉 Try a lower number!")
    
    print(f"💡 Attempts left: {attempts_left}")

def play_game():
    """Play one round of the game"""
    max_num, max_attempts = get_difficulty()
    secret_number = random.randint(1, max_num)
    attempts = 0
    
    print(f"\n🎮 Game Started!")
    print(f"🤔 I'm thinking of a number between 1 and {max_num}")
    print(f"🎯 You have {max_attempts} attempts to guess it!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            
            if guess < 1 or guess > max_num:
                print(f"⚠️ Please enter a number between 1 and {max_num}!")
                continue
            
            attempts += 1
            
            if guess == secret_number:
                print(f"\n🎉 CONGRATULATIONS! 🎉")
                print(f"You guessed the number {secret_number} in {attempts} attempts!")
                return True
            else:
                give_hint(guess, secret_number, max_attempts - attempts)
        
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")
    
    print(f"\n😔 GAME OVER! The number was {secret_number}")
    return False

def show_statistics(games_played, games_won):
    """Display game statistics"""
    print("\n" + "="*40)
    print("GAME STATISTICS")
    print("="*40)
    print(f"Games Played: {games_played}")
    print(f"Games Won: {games_won}")
    if games_played > 0:
        win_rate = (games_won / games_played) * 100
        print(f"Win Rate: {win_rate:.1f}%")

def number_guessing_game():
    """Main game system"""
    games_played = 0
    games_won = 0
    
    print("="*50)
    print("🎲 WELCOME TO NUMBER GUESSING GAME! 🎲")
    print("="*50)
    
    while True:
        print("\n" + "="*30)
        print("MAIN MENU")
        print("="*30)
        print("1. Start New Game")
        print("2. View Statistics")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            games_played += 1
            if play_game():
                games_won += 1
        elif choice == '2':
            show_statistics(games_played, games_won)
        elif choice == '3':
            show_statistics(games_played, games_won)
            print("\n👋 Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

# Run the game
number_guessing_game()