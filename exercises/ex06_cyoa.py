"""Let's go on a camping trip!"""

__author__ = "730361113"


from random import randint

points: int = 0
player: str = "First Run"


def greet() -> None:
    """Gives player an introduction to the AT and briefs them on their first decision."""
    global player
    player = (input("What is your name? "))
    if len(player) == 0:
        player = str(input("Please input your name. "))
    print(f" === Hello, {player}, welcome to The Great Smokey Mountains! === ")
    print("The Smokies are an ancient mountain range rising to heights over 6600 feet on the NC-TN border.")
    print("They are well known for the beatiful sights and wildlife that can be seen both at summits and on the mountain-side.")
    print("People travel from all over to experience its beauty, with opportunities to leave behind civilization on a backpacking trip.")
    print("Let's try backpacking from Fontana Dam in the South to the Newfound Gap outside of Gatlinburg Tennesse.")
    print("So when do you want to start? Too early or too late in the year, and you'll risk a blizzard!")


def start(month: int) -> None:
    """Makes sure player has picked an acceptable date and tells them which month they've chosen."""
    while month >= 10 or month <= 2:
        print("Are you sure you want to start then? It'll be too cold for sure!")
        month: int = int(input("Try and picking a different start-date here: ")) 
    if month == 0:
        print(f"Hiking isn't for everyone. Goodbye {player}. ")
        quit()
    if month == 3:
        print("You have chosen to start in March.")
    if month == 4:
        print("You have chosen to start in April.")
    if month == 5:
        print("You have chosen to start in May.")
    if month == 6:
        print("You have chosen to start in June.")
    if month == 7:
        print("You have chosen to start in July.")
    if month == 8:
        print("You have chosen to start in August.")
    if month == 9:
        print("You have chosen to start in September.")
    

def weather(month: int) -> int:
    """Provides a random weather report."""
    CLEAR_SKY: str = "\U0001f31E" 
    CLEAR_COLD: str = "\U0001F976"
    SNOWY_COLD: str = "\U00002603"
    RAINY_DAY: str = "\U0001F327"
    VERY_HOT: str = "\U0001f975"
    weather: int = 0
    if month == 3:
        if randint(1, 2) == 1:
            print(f"It is cold and snowing {SNOWY_COLD}") 
            weather += 8
        else:
            print(f"The sky is clear, but it is cold {CLEAR_SKY}")
            weather += 4
    if month == 4:
        if randint(1, 3) == 1:
            print(f"It is cold and snowing {SNOWY_COLD}")
            weather += 8
        else:
            print(f"The sky is clear, but it is cold {CLEAR_SKY}")
            weather += 3
    if month == 5 or month == 6:
        if randint(1, 3) == 1:
            print(f"It is raining. {RAINY_DAY}")
            weather += 3
            if randint(1, 3) == 2:
                print(f"It is cold. {CLEAR_COLD}")
                weather += 3
        else:
            print(f"The weather is clear and it is cool. {CLEAR_COLD}")
            weather += 1
    if month == 7 or month == 8:
        if randint(1, 4) == 1:
            print(f"It is very hot. {VERY_HOT}")
            weather += 4
        else: 
            if randint(1, 2) == 1:
                print(f"It is raining. {RAINY_DAY}")
                weather += 3
            else:
                print(f"It is clear. {CLEAR_SKY}")
                weather += 1
    if month == 9:
        if randint(1, 2) == 1:
            print(f"It is clear. {CLEAR_SKY}")
            weather += 1
        else:
            if randint(1, 5) != 1:
                print(f"It is raining. {RAINY_DAY}")
                weather += 3
            else:
                print(f"Winter came early, you were caught in a freak blizzard atop Mt. Washington! {SNOWY_COLD}")
                weather += 10
    return weather


def challenge(health: int) -> int:
    """Two health checks."""
    choice: int = 0
    if randint(1, 2) == 1:
        print("You have begun to run out of water. You may:")
        print("(1) Keep hiking and hope to find water ahead.")
        print("(2) Go looking for water off trail.")
        choice = int(input("Type 1 or 2 to make your decision. "))
        if choice == 1 and randint(1, 3) == 1:
            print("No water is found for the next 4 miles, long after you've begun to feel weak.")
            health += 3
        if choice == 2 and randint(1, 2) == 1:
            print("No water is found and you have to return back to the trail even thirsty than when you started.")
            health += 5
        else:
            print("The trail provides! You find water around the next bend.")
    if randint(1, 10) == 1:
        print(" === You come across a bear! What are you going to do? === ")
        print("(1) Run and hide")
        print("(2) Yell at the bear")
        print("(3) Play dead")
        action: int = int(input("Type 1, 2, or 3 to make your decision. "))
        if action != 1 and action != 2 and action != 3:
            action: int = int(input("Please input either 1, 2, or 3. "))
        if action == 1:
            print("As soon as you catch sight of the bear, you turn and high-tail it in the opposite direction.")
            print("The bear wonders where it is you could be off too and chases you down!")
            print("The bear gives you multiple big hugs, but you don't seem to enjoy it, and soon it just walks away.")
            print("You're badly hurt, but manage to call 911 to get airlifted.")
            print(f"Thank you for playing, you lasted {points} days.")
            quit()
        if action == 2:
            print("The bear is startled, and seeing that you are no threat, trots off into the brush.")
        if action == 3:
            print("The bear sees a limp body up the trail, and trots over to investigate.")
            print("After a good whack to see if anything moves, it shrugs, and leaves unimpressed.")
            print("You've got a couple scratches on you leg, but will live to tell the tale")
            health += 5
    return health


def main() -> None:
    """Where the game is played!"""
    if player == "First Run":
        global points
        points = 0
    greet()
    print(" === When will you start? ===")
    month: int = int(input("Reply with 1 for January, 2 for February, and so on. Reply with 0 to decide not to hike. "))
    start(month)
    print("Welcome to Fontana Dam, NC, where you will start your hike. Newfound Gap lies 40.6 miles North.")
    print("You have enough food to last 6 days.")
    forecast: int = 0
    distance: int = 0
    health: int = 0
    day: int = 1
    checkpoint: int = 0
    while distance < 40.6 and day < 7:
        print(f" === Day {day} === ")
        forecast = (weather(month))
        time: int = int(input("What time do you want to start hiking in the morning? Please enter an integer between 1 and 12. "))
        challenge(health)
        distance += 15 - health - forecast + 8 - time
        if distance >= 10.2 and checkpoint == 0:
            checkpoint += 1
            print("You've made it to Mollies Ridge Shelter. Type 1 or 2 to make your decision.")
            mollies: int = 0
            mollies = int(input("(1)Stay the night in the shelter or (2)Continue on to Newfound Gap? "))
            if mollies == 1:
                distance = 10.2
                print("The shelter is warm and protects you from the wind. But the spring nearby is dry and you go to bed thirsty.")
                health = health + 2
            else:
                print("You continue on past the shelter. ")
        if distance >= 17.9 and checkpoint == 1:
            checkpoint += 1
            print("Ahoy! There's a stranger ahead. She seems to be looking for something.")
            dolly: int = 0
            dolly = int(input("Would you like to offer her help? Type (1)to help look or (2)to keep hiking. "))
            if dolly == 1:
                print("Welcome to Good ol' Rocky Top the woman says")
                print("\"Can you help you find something ma'am? you reply\"")
                print("\"You could have a little bit ago, but some other stranger already helped me find it!\"")
                print("\"But here, just for offering your time, here's some corn\"")
                print("The woman hands you a jar. Understanding, you unscrew the cap and take a drink.")
                print("The drink makes you feel alive! And you hit the trails with more vigor than you've had in years.")
                health = 0
            else:
                print("You continue on past her, wondering who that woman was...she looked a little familiar...")
        if distance >= 28.6 and checkpoint == 2:
            checkpoint += 1
            print("You've made it to Derrick Knob Shelter!")
            print("Would you like to stop here and stay in the shelter tonight?")
            derrick: int = 0
            derrick = int(input("Type (1) to stay at Derrick Knob Shelter or (2) to keep hiking: "))
            if derrick == 1:
                print("Derrick Knob Shelter's three walls provide you warmth from the wind and protection from the rain!")
                distance = 28.6
                health = health - 1
            else:
                print("You're unable to find a flat spot to pitch your tent past the Derrick Knob Selter")
                print("After several miles, and with wind and rain expected overnight, you must retrace your steps back to the shelter.")
                distance = 28.6
                health = health + 1
        if distance >= 38.9 and checkpoint == 3:
            checkpoint += 1
            print("You've made it to Clingman's Dome! The highest peak in the Smokies")
            print("Somewhat unexpectedly, the sunset is shapping up to be absolutely stunning!")
            dome: int = 0
            dome = int(input("Would you like to stay for the sunset, and camp here tonight? Type (1) for yes or (2) for no."))
            if dome == 1:
                distance = 38.9
                print("You stay overnight only to be awoken in the middle of the night by a howling wind. The wind is bone-chilling and loud.")
                health = health + 3
        if distance >= 40.6 and checkpoint == 4:
            checkpoint += 1
            print(f"Congratulations, you made it to Newfound Gap in {day} days!")
        day += 1
        points += 1
        if forecast + health >= 10:
            print("The wear and tear of the journey pushes you to your breaking point.")
            print("Thankfully, a local boyscout troop is passing by right as you begin to lose it, ")
            print("and they've been practicing their fireman-carries.")
            print("You're badly hurt, but manage to call 911 to get airlifted.")
            print(f"Thank you for playing, you lasted {points + 1} days.")
            quit()
        if distance < 40.6:
            print(f"You have hiked {distance} miles total. Newfound Gap is {40.6 - distance} miles away.")
    if distance > 40.6:
        print(f"Congratulations! You made it to Newfound Gap in {points + 1} days!")
    else:
        print("You ran out of food before you could make it to Newfound Gap. Hike faster next time!")
        print(f"Thank you for playing, {player}. You spent a total of {points + 1} days on trail. ")
        quit()
    again: int = int(input("If you would like to keep playing please type 1, otherwise, type 2: "))
    if again == 1:
        main()
    else:
        print(f"Thank you for playing, {player}. You spent a total of {points + 1} days on trail. ")
        quit()

    
if __name__ == "__main__":
    main()