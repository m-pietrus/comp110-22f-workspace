"""Let's go on a camping trip!"""

__author__ = "730361113"


from random import randint


def greet(name: str) -> None:
    """Gives player an introduction to the AT and briefs them on their first decision."""
    print(f" === Hello, {name}, welcome to The Great Smokey Mountains! === ")
    print("The Smokies are a an old mountain range rising to heights over 6600 feet on the NC-TN border.")
    print("They are well known for the beatiful sights and wildlife that can be seen both at summits and on the mountain-side.")
    print("People travel from all over to experience its beauty, and some even venture into the backcountry on multi-day backpacking trips.")
    print("Let's try hiking from Fontana Dam in the South to the Newfound Gap outside of Gatlinburg Tennesse.")
    print("So when do you want to start? Too early or too late in the year, and you'll risk a blizzard!")


def start(month: int, name: str) -> None:
    """Makes sure player has picked an acceptable date and tells them which month they've chosen."""
    while month >= 10 or month <= 2:
        print("Are you sure you want to start then? It'll be too cold for sure!")
        month: int = int(input("Try and picking a different start-date here: ")) 
    if month == 0:
        print(f"Hiking isn't for everyone. Goodbye {name}. ")
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
    """Provides a random weather report. """
    weather: int = 0
    if month == 3:
        if randint(1, 2) == 1:
            print("It is cold and snowing.")
            weather += 8
        else:
            print("The sky is clear, but it is cold.")
            weather += 4
    if month == 4:
        if randint(1, 3) == 1:
            print("It is cold and snowing.")
            weather += 8
        else:
            print("The sky is clear, but it is cold.")
            weather += 3
    if month == 5 or month == 6:
        if randint(1, 3) == 1:
            print("It is raining.")
            weather += 3
            if randint (1, 3) == 2:
                print("It is cold.")
                weather += 3
        else:
            print("The weather is clear and it is cool.")
            weather += 1
    if month == 7 or month == 8:
        if randint (1, 4) == 1:
            print("It is very hot.")
            weather += 4
        else: 
            if randint (1, 2) == 1:
                print("It is raining.")
                weather += 3
            else:
                print("It is clear.")
                weather +=1
    if month == 9:
        if randint (1, 2) == 1:
            print("It is clear.")
            weather += 1
        else:
            if randint (1, 10) == 1:
                print("Winter came early, you were caught in a freak blizzard atop Mt. Washington!")
                weather += 10
    return weather


def challenge(health: int, points: int) -> int:
    """Two health checks"""
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
    name: str = str(input("What is your name? "))
    if len(name) == 0:
        name: str = str(input("Please input your name. "))
    (greet(name))
    print(" === When will you start? ===")
    month: int = int(input("Reply with 1 for January, 2 for February, and so on. Reply with 0 to decide not to hike. "))
    start(month, name)
    print(f"Welcome to Fontana Dam, NC, where you will start your hike. Newfound Gap lies 40.6 miles North")
    print("You have enough food to last 6 days.")
    forecast: int = 0
    distance: int = 0
    health: int = 0
    day: int = 1
    points: int = 0
    while distance < 40.6 and day < 7:
        print(f" === Day {day} === ")
        forecast = (weather(month))
        time: int = int(input("What time do you want to start hiking in the morning? Please enter an integer between 1 and 12. "))
        (challenge(health, points))
        distance += 15 - health - forecast + 8 - time
        if distance >= 10.2:
            print("You've made it to Mollies Ridge Shelter. Type 1 or 2 to make your decision.")
            mollies: int = int(input("(1)Stay the night in the shelter or (2)Continue on to Newfound Gap? "))
            if mollies == 1:
                distance = 10.2
                print("The shelter is warm and protects you from the wind. But the spring nearby is dry and you go to bed thirsty.")
                health = health + 2
        print(f"You've hiked {distance} miles total. Newfound Gap is {40.6 - distance} miles away.")
            else:
                print("You continue on past the shelter and find the perfect place to pitch your tent on ")
                print(f"You've hiked {distance} miles total. Newfound Gap is {40.6 - distance} miles away.")
        else:
            print(f"You've hiked {distance} miles total. Newfound Gap is {40.6 - distance} miles away.")
        if distance >= 17.9:
            print("Ahoy! There's a stranger ahead. She seems to be looking for something.")
            dolly: int = int("Would you like to offer her help? Type (1)to help look or (2)to keep hiking. ")
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
        if distance >= 28.6:
            print("You've made it to Derrick Knob Shelter!")
        if distance >= 38.9:
            print("You've made it to Clingman's Dome!")
        if distance >= 40.6:
            print(f"Congratulations, you made it to Newfound Gap in {day} days!")
        day += 1
        points += 1
        if forecast + health >= 15:
            print("The wear and tear of the journey pushes you to your breaking point.")
            print("Thankfully, a local boyscout troop is passing by right as you begin to lose it, ")
            print("and they've been practicing their fireman-carries.")
            print("You're badly hurt, but manage to call 911 to get airlifted.")
            print(f"Thank you for playing, you lasted {points + 1} days.")
            quit()
    if distance >= 40.6:
        print(f"Congratulations, you made it to Newfound Gap in {day} days!")
        print(f"You've spent a total of {points + 1} on trail.")
    again: int = int(input("If you would like to keep playing please type 1, otherwise, type 2: "))
    if again == 1:
        print("Run again?")
    else:
        print(f"Thank you for playing, {name}. You spent a total of {points + 1} days on trail. ")
        quit()

    
if __name__ == "__main__":
  main()