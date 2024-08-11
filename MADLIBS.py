def load_story():
    with open('TextFiles\story.txt', 'r') as f:
        story = f.read()
    return story

def collect_words(story):
    words = []
    start_of_word = -1
    target_start, target_end = '<','>'
    for i, char in enumerate(story):
        if char == target_start:
            start_of_word = i
        if char == target_end and start_of_word != -1:
            end_of_word = i+1
            word = story[start_of_word:end_of_word].lower()
            words.append(word)
            start_of_word = -1
    return words

def collect_answers(words):
    answers = []
    vowels = ['a','e','i','o','u']
    for i in range(len(words)):
        if words[i][1] in vowels:
            answer = input(f'Give me an {words[i][1:-1]} ')
            answers.append(answer)
        else:
            answer = input(f'Give me a {words[i][1:-1]} ')
            answers.append(answer)
    return answers

def insert_answers(answers, story):
    target_start, target_end = '<','>'
    start_of_word = -1
    insert_counter = 0
    
    while insert_counter < len(answers):
        start_of_word = story.find(target_start, start_of_word + 1)
        end_of_word = story.find(target_end, start_of_word) + 1
        story = story[:start_of_word] + answers[insert_counter] + story[end_of_word:]
        insert_counter += 1

    return story

def main():
    print('\n','🎉Welcome to the Ultimate Mad Libs Adventure!🎉','\n')
    print('Ready to unleash your creativity and have a blast? Dive into our fun-filled story game where your wildest ideas will bring a whimsical tale to life! Just fill in the blanks with your chosen words, and watch as the magic unfolds.','\n')
    print('Let’s get started and see what kind of story you create!','\n')
    story = load_story()
    words = collect_words(story)
    answers = collect_answers(words)
    updated_story = insert_answers(answers, story)
    print('Here''s the story you created' + '\n' + updated_story)

if __name__ == '__main__':
    main()