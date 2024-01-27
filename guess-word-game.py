import random

word_list = [
    "ability", "able", "about", "above", "accept", "according", "account", "across", "action", "activity",
    "actually", "address", "administration", "admit", "adult", "affect", "after", "again", "against", "age",
    "agency", "agent", "ago", "agree", "agreement", "ahead", "air", "all", "allow", "almost",
    "alone", "along", "already", "also", "although", "always", "American", "among", "amount", "analysis",
    "and", "animal", "another", "answer", "any", "anyone", "anything", "appear", "apply", "approach",
    "area", "argue", "arm", "around", "arrive", "art", "article", "artist", "as", "ask",
    "assume", "at", "attack", "attention", "attorney", "audience", "author", "authority", "available", "avoid",
    "away", "baby", "back", "bad", "bag", "ball", "bank", "bar", "base", "be",
    "beat", "beautiful", "because", "become", "bed", "before", "begin", "behavior", "behind", "believe",
    "benefit", "best", "better", "between", "beyond", "big", "bill", "billion", "bit", "black",
    "blood", "blue", "board", "body", "book", "born", "both", "box", "boy", "break",
    "bring", "brother", "budget", "build", "building", "business", "but", "buy", "by", "call",
    "camera", "campaign", "can", "cancer", "candidate", "capital", "car", "card", "care", "career",
    "carry", "case", "catch", "cause", "cell", "center", "central", "century", "certain", "certainly",
    "chair", "challenge", "chance", "change", "character", "charge", "check", "child", "choice", "choose",
    "church", "citizen", "city", "civil", "claim", "class", "clear", "clearly", "close", "coach",
    "cold", "collection", "college", "color", "come", "commercial", "common", "community", "company", "compare",
    "computer", "concern", "condition", "conference", "Congress", "consider", "consumer", "contain", "continue", "control",
    "cost", "could", "country", "couple", "course", "court", "cover", "create", "crime", "cultural",
    "culture", "cup", "current", "customer", "cut", "dark", "data", "daughter", "day", "dead",
    "deal", "death", "debate", "decade", "decide", "decision", "deep", "defense", "degree", "Democrat",
    "democratic", "describe", "design", "despite", "detail", "determine", "develop", "development", "die", "difference",
    "different", "difficult", "dinner", "direction", "director", "discover", "discuss", "discussion", "disease", "do",
    "doctor", "dog", "door", "down", "draw", "dream", "drive", "drop", "drug", "during",
    "each", "early", "east", "easy", "eat", "economic", "economy", "edge", "education", "effect",
    "effort", "eight", "either", "election", "else", "employee", "end", "energy", "enjoy", "enough",
    "enter", "entire", "environment", "environmental", "especially", "establish", "even", "evening", "event", "ever",
    "every", "everybody", "everyone", "everything", "evidence", "exactly", "example", "executive", "exist", "expect",
    "experience", "expert", "explain", "eye", "face", "fact", "factor", "fail", "fall", "family",
    "far", "fast", "father", "fear", "federal", "feel", "feeling", "few", "field", "fight",
    "figure", "fill", "film", "final", "finally", "financial", "find", "fine", "finger", "finish",
    "fire", "firm", "first", "fish", "five", "floor", "fly", "focus", "follow", "food",
    "foot", "for", "force", "foreign", "forget", "form", "former", "forward", "four", "free",
    "friend", "from", "front", "full", "fund", "future", "game", "garden", "gas", "general",
    "generation", "get", "girl", "give", "glass", "go", "goal", "good", "government", "great",
    "green", "ground", "group", "grow", "growth", "guess", "gun", "guy", "hair", "half",
    "hand", "hang", "happen", "happy", "hard", "have", "he", "head", "health", "hear",
    "heart", "heat", "heavy", "help", "her", "here", "herself", "high", "him", "himself",
    "his", "history", "hit", "hold", "home", "hope", "hospital", "hot", "hotel", "hour",
    "house", "how", "however", "huge", "human", "hundred", "husband", "I", "idea", "identify",
    "if", "image", "imagine", "impact", "important", "improve", "in", "include", "including", "increase",
    "indeed", "indicate", "individual", "industry", "information", "inside", "instead", "institution", "interest", "interesting",
    "international", "interview", "into", "investment", "involve", "issue", "it", "item", "its", "itself",
    "job", "join", "just", "keep", "key", "kid", "kill", "kind", "kitchen", "know",
    "knowledge", "land", "language", "large", "last", "late", "later", "laugh", "law", "lawyer",
    "lay", "lead", "leader", "learn", "least", "leave", "left", "leg", "legal", "less",
    "let", "letter", "level", "lawyer" ]

random_number = random.randint(0, len(word_list) - 1)

secret_word = word_list[random_number]

incorrect_guesses = 0

maximum_gusses = 5

# Print one underscore for each letter in the word
display_word = ["_"] * len(secret_word)

while True:
    print("")
    print(" ".join(display_word))
    print("")

    user_letter = input("What do you think the next letter in the word is: ")

    if user_letter in secret_word:
        print(f"The letter '{user_letter}' is in the word.")

        for counter in range(len(secret_word)):
            if user_letter is secret_word[counter]:
                display_word[counter] = user_letter
    else:            
        incorrect_guesses = incorrect_guesses + 1
        print(f"The letter '{user_letter}' is not in the word. Incorrect guesses ({incorrect_guesses} of {maximum_gusses})")

    if secret_word == "".join(display_word):
        print("")
        print(" ".join(display_word))
        print("")
        print("Congrarulations you got the correct word")
        break

    if maximum_gusses == incorrect_guesses:
        print("you faild")
        break


