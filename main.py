import castle
import user

if __name__ == "__main__":

    game_castle = castle.parse_castle_file("CastleBook.csv")

    user = user.User(game_castle)

    user_input = ''

    while user_input != 'quit':

        user.print_location()

        user_input = input("Please choose direction 'nesw' or type 'quit' to exit\n")

        if user_input in 'nesw':
            user.move(user_input)
        elif user_input == 'quit':
            break;
        else:
            print("Don't understand direction %s" % user_input)