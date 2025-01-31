def get_input(word_type: str) -> str:
    user_input = input(f"Enter a {word_type}: ")
    return user_input

noun1 = get_input("none 1")
verb1 = get_input("verb 1")
noun2 = get_input("none 2")
verb2 = get_input("verb 2")

story = f'''
so this is the story of the {noun1} with it's verb {verb1}
the second element of the story will be {noun2} and it also have a verb {verb2}
you cna modify the story as you want and so one 
so this is just a simple project
'''

print(story)