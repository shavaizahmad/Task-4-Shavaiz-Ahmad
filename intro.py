

questions = [
    ["What does CPU stand for?",
     "Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing User", "None", 1],

    ["Which device is used to type text?",
     "Mouse", "Keyboard", "Monitor", "Printer", "None", 2],

    ["Which device displays output on a screen?",
     "Keyboard", "Scanner", "Monitor", "Microphone", "None", 3],

    ["What does RAM stand for?",
     "Read Access Memory", "Random Access Memory", "Run Access Module", "Random Active Machine", "None", 2],

    ["Which device is used to print documents?",
     "Scanner", "Mouse", "Printer", "Speaker", "None", 3],

    ["Which of these is an input device?",
     "Monitor", "Printer", "Speaker", "Mouse", "None", 4],

    ["Which of these is an operating system?",
     "Windows", "Google", "Facebook", "YouTube", "None", 1],

    ["What does WWW stand for?",
     "World Wide Web", "World Web Window", "Wide World Website", "Web World Work", "None", 1],

    ["Which device is used to store data permanently?",
     "RAM", "Hard Disk", "Cache", "Register", "None", 2],

    ["Which of these is a web browser?",
     "MS Word", "Windows", "Google Chrome", "Excel", "None", 3],
]
score = 0 
for i in range(len(questions)):
    q = questions[i]

    print(f"\nQuestion {i + 1}: {q[0]}")
    print(f"a. {q[1]}        b. {q[2]}")
    print(f"c. {q[3]}        d. {q[4]}")

    reply = input("Enter your answer (a/b/c/d): ").strip().lower()
    correct_letter = "abcd"[q[-1] - 1]

    if reply == correct_letter:
        score += 1
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_letter}. {q[q[-1]]}")

print(f"\nQuiz finished! Your final score: {score}/{len(questions)}")