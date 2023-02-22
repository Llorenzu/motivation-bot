import random

# Define a list of motivational messages
motivational_messages = [
    "You are capable of amazing things!",
    "Believe in yourself and all that you are!",
    "You are stronger than you think!",
    "Don't let fear hold you back!",
    "Every failure is a step towards success!",
    "You have the power to change your life!",
    "Chase your dreams and never give up!",
    "You are amazing just the way you are!",
    "Take one step at a time and keep moving forward!",
    "Your potential is limitless!"
]

# Define a list of fear-overcoming messages
fear_overcoming_messages = [
    "Face your fears head on and overcome them!",
    "Believe in yourself and your ability to overcome your fears!",
    "Visualize yourself succeeding and conquering your fears!",
    "Take small steps towards overcoming your fears and build up your confidence!",
    "Seek support from family and friends to help you overcome your fears!",
    "Challenge negative thoughts and replace them with positive affirmations!",
    "Focus on the present moment and stay grounded in the here and now!",
    "Celebrate your successes, no matter how small!",
    "Remember that mistakes and failures are opportunities to learn and grow!",
    "Never give up on yourself, you are stronger than your fears!"
]

# Define a function to motivate and help overcome fear
def motivate_and_overcome_fear():
    # Choose a random message from the motivational_messages list
    motivational_message = random.choice(motivational_messages)
    
    # Choose a random message from the fear_overcoming_messages list
    fear_overcoming_message = random.choice(fear_overcoming_messages)
    
    # Print the messages
    print(motivational_message)
    print(fear_overcoming_message)

# Call the function to get motivated and overcome fear
motivate_and_overcome_fear()
