# imports
import sys
from analyze import analyze

# main
def main():

    with open('./Static/hashtag.txt', 'r') as f:
        print(f'\n{f.read()}')

    def hashtag():

        hash = input('\n> ')

        hash = hash.replace('#','')
        hash = hash.replace(' ','')
        
        return hash

    def case(hash):

        match hash:
            case '-1':
                sys.exit()
            case _:
                analyze(hash)
        
        case(hashtag())

    case(hashtag())

# run
main()
