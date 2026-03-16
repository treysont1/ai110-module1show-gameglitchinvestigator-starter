# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

--- The game's hints are completely inaccurate, and at times, the secret number was out of the 1-100 range (for example, the secret number being -15). 
The game also doesn't allow users to start a new game using the button, and requires you to refresh the page.
If I enter an invalid input, like "", and continue to press enter, the game doesn't stop once I exhaust guesses, and the guess counter just goes negative.
Number of guesses provides one less than it should.
Difficulties does not appear to change the range of the possible answers

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One AI suggestion that was correct was the fact that on even-numbered attempts, secret was being cast to a string for no reason, so the suggestion was to remove it. I verified this by checking over the logic and seeing that answer was in fact being casted to a string with the modulo operator.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
One AI suggestion that was misleading was where I asked it about the secret ranges earlier, then changed them myself, and asked if the guesses allowed for each difficulty were fair. It then provided a response based on the previous secret ranges rather than the new ones. I then provided additional context.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I went into the app myself and did the same test that allowed me to find the bug beforehand.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
I entered an empty string and continued to press enter until guesses were exhausted. I also finished a game and pressed new game to see if it would allow me to play again. These showed me that there was some faulty logic where guesses weren't being updated when given an empty string, and the game state wasn't being updated upon the new game button press.
  
- Did AI help you design or understand any tests? How?
AI helped me design tests like making sure the guess ranges were accurate to the difficulty. It also helped me understand test by showing me the return types of certain functions and how they were incompatible with the previous tests.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The code "if secret not in st.session_state: secret =" would run whenever something changed, and could happen randomly.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit reruns the whole script whenever something changes like clicking a button. Session state is how the app remembers where you are before the rerun, or what the last thing you did was. For example, when you win a game, the state is now set to "won", so when there's a rerun, it won't treat you as though you just opened the app.
- What change did you make that finally gave the game a stable secret number?
I changed the "secret" not in st.session_state if statement to one that would only happen if the difficulty is explicitly changed.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit that I'd like to reuse in the future is learning Git commands through the terminal rather than the VS code extension. I also would like to implement better prompting, and using pytest.
- What is one thing you would do differently next time you work with AI on a coding task?
One thing I'd do differently is ensure that the model knows exactly what my intentions are with a fix, rather than just describing an issue.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
This project helped me realize the efficiency of using an AI model for unfamiliar projects. Because all the logic was in one file and I was unfamiliar with Streamlit and the program's structure. AI helped me with navigating and understanding certain choices.