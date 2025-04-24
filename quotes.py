import random

quotes = [
    "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill",
    "The only way to do great work is to love what you do. — Steve Jobs",
    "Believe you can and you're halfway there. — Theodore Roosevelt",
    "Don’t watch the clock; do what it does. Keep going. — Sam Levenson",
    "Quality means doing it right when no one is looking. — Henry Ford",
    "Success usually comes to those who are too busy to be looking for it. — Henry David Thoreau",
    "Discipline is the bridge between goals and accomplishment. — Jim Rohn",
    "Opportunities don't happen. You create them. — Chris Grosser",
    "Hard work beats talent when talent doesn’t work hard. — Tim Notke",
    "Excellence is not an act, but a habit. — Aristotle",
    "What you do today can improve all your tomorrows. — Ralph Marston",
    "Dream big. Start small. Act now. — Robin Sharma",
    "Your work is going to fill a large part of your life… — Steve Jobs",
    "Great things are done by a series of small things brought together. — Vincent Van Gogh",
    "The secret of getting ahead is getting started. — Mark Twain",
    "Perseverance is not a long race; it is many short races one after the other. — Walter Elliot",
    "You don’t have to be great to start, but you have to start to be great. — Zig Ziglar",
    "Success is liking yourself, liking what you do, and liking how you do it. — Maya Angelou",
    "Make each day your masterpiece. — John Wooden",
    "Work hard in silence, let success make the noise. — Frank Ocean"
]

def get_random_quote():
    return random.choice(quotes)
