def show_skills(skills):
    print("Your Skill:")
    for i, skill in enumerate(skills,start=1):
        print(f"{i}. {skill}")

def main():
    skills = [
        "Communication - skills",
        "Python - Programming",
        "Web develoment",
        "E-Commerce",
        "Graph-Design",
        "Canva-school",
        "How to learn e-commerce",
        "Free code camp",
        "Google python Class",
        "how to talk only",
    ]

    show_skills(skills)

if __name__ == "__main__":
    main()