import validations

def reload_or_stop_game():
    print('\t\t\t\t     ╔═══════════ ∘◦ ☆ ◦∘ ════════════╗\
           \n\n\t\t\t\t         Do you want to play again?\
            \n\n\t\t\t\t                1 for yes\
             \n\n\t\t\t\t                0 for no\
           \n\n\t\t\t\t     ╚═══════════ ∘◦ ❉ ◦∘ ════════════╝')
    user_choice = input('\n\t\t\t\t\t\t  Type your option here: ')
    while validations.validate_user_choice(user_choice) == False:
        print('\n' * 13)
        print('\t   ⚠Invalid answer. You should choose 0 if you\n\t   want to stop and 1 if you want to continue.⚠')
        print('\t\t\t\t     ╔═══════════ ∘◦ ☆ ◦∘ ════════════╗\
               \n\n\t\t\t\t         Do you want to play again?\
                \n\n\t\t\t\t                1 for yes\
                 \n\n\t\t\t\t                0 for no\
               \n\n\t\t\t\t     ╚═══════════ ∘◦ ❉ ◦∘ ════════════╝')
        user_choice = input('\n\t\t\t\t\t\t  Type your option here: ')

    return user_choice
