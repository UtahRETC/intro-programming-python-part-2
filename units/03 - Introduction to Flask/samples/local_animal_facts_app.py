import flask
import random

app = flask.Flask(__name__)

animal_facts = [
    "A group of flamingos is called a 'flamboyance' because, well, look at them.",
    "Octopuses have three hearts, and two of them stop beating when they swim. No pressure.",
    "Cows have best friends and get stressed when they're separated. Bovine bromance is real.",
    "Sloths can hold their breath longer than dolphins. They slow their heart rate to a near standstill!",
    "A shrimp’s heart is in its head. That’s one way to keep love on your mind.",
    "Wombat poop is cube-shaped so it doesn’t roll away. Nature’s little bricklayers.",
    "Male seahorses are the ones that get pregnant. Talk about a role reversal!",
    "Butterflies taste with their feet. Imagine stepping in pizza and knowing exactly how good it is.",
    "A cat’s purr has a frequency that can promote healing. Basically, they are tiny, fluffy doctors.",
    "Elephants can 'hear' with their feet by picking up vibrations from the ground. Nature’s wireless network.",
    "Tigers have striped skin, not just striped fur. The pattern is like a fingerprint—unique to each tiger!",
    "Ducks can sleep with one eye open to stay alert for danger. Built-in security system.",
    "Some turtles can breathe through their butts. Not the superpower anyone asked for, but hey, it works.",
    "A narwhal's 'horn' is actually a tooth that grows through its lip. Talk about a serious dental issue.",
    "Frogs can freeze solid in the winter and thaw out just fine in the spring. Frogcicles are a real thing!",
    "The mantis shrimp punches so fast it creates a tiny explosion in the water. Underwater boxing champion.",
    "Goats have rectangular pupils, giving them a 320-degree field of vision. They see almost everything—except why humans find them funny.",
    "Cows produce more milk when they listen to calming music. So yes, they have playlists.",
    "A jellyfish is 95% water. Basically, a floating, slightly aggressive Jell-O blob.",
    "Rats can laugh when tickled. Science spent time figuring that out, and honestly, respect."
]

@app.route("/")
def index():
    fact = random.choice(animal_facts)
    return flask.render_template("animal_facts_homepage.html", fact=fact)

app.run(debug=True)
