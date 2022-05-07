import random
import logging
import argparse


logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
log_format = '%(message)s'
fh = logging.FileHandler('all.log')
fh.setLevel(logging.DEBUG)
fh.setFormatter(logging.Formatter(log_format))
logger.addHandler(fh)


def save_log():
    user_file = log_input("File name:")
    with open("all.log", 'r') as file_log:
        f = file_log.read()
        with open(user_file, "w") as file_of_user:
            print(f, file=file_of_user, flush=True)
    log_print("The log has been saved.")


def log_print(msg):
    print(msg)
    logger.debug(msg)


def log_input(input_msg):
    input_log = input(input_msg + '\n')
    logger.debug(input_msg)
    logger.debug(input_log)
    return input_log


class DuplicateError(Exception):
    def __str__(self):
        return "The term already exists."


class Cards:
    dict_of_cards = {}
    terms_of_cards = []
    mistakes_of_cards = {}

    def add(self):
        card = log_input('The card:')
        while True:
            try:
                if card in self.dict_of_cards.keys():
                    raise DuplicateError
            except DuplicateError:
                card = log_input(f'The term "{card}" already exists. Try again:\n')
            else:
                self.terms_of_cards.append(card)
                break
        while True:
            definition = log_input('The definition of the card:')
            try:
                if definition in Cards.dict_of_cards.values():
                    raise DuplicateError
            except DuplicateError:
                log_print(f'The definition "{definition}" already exists. Try again:')
            else:
                log_print(f'The pair ("{card}":"{definition}") has been added.')
                self.dict_of_cards.update({card: definition})
                self.mistakes_of_cards.update({card: 0})
                break

    def remove(self):
        card = log_input('Which card?')
        try:
            self.dict_of_cards.pop(card)
            log_print('The card has been removed.')
        except KeyError:
            log_print(f'''Can't remove "{card}": there is no such card.''')
        else:
            self.terms_of_cards.remove(card)
            self.mistakes_of_cards.pop(card)

    def import_cards(self, file_name):
        try:
            cards_file = open(file_name, 'rt')
        except OSError:
            log_print('File not found.')
        else:
            cards = cards_file.readlines()
            for c in range(0, len(cards)):
                if c > len(cards):
                    break
                else:
                    card = cards[c][:cards[c].index(':')]
                    definition = cards[c][(cards[c].index(':'))+1:cards[c].index(';')]
                    mistakes = int(cards[c][(cards[c].index(';'))+1:cards[c].index('\n')])
                    if card in Cards.dict_of_cards:
                        self.dict_of_cards.pop(card)
                        self.mistakes_of_cards.pop(card)
                        self.terms_of_cards.remove(card)
                    self.terms_of_cards.append(card)
                    self.dict_of_cards.update({card: definition})
                    self.mistakes_of_cards.update({card: mistakes})
            cards_file.close()
            log_print(f'{int(len(cards))} cards have been loaded.')

    def export_cards(self, file_name):
        cards_file = open(file_name, 'wt')
        for card in self.dict_of_cards:
            cards_file.write(card + ':' + self.dict_of_cards[card] + ';' + str(self.mistakes_of_cards[card]) + '\n')
        cards_file.close()
        log_print(f'{len(self.terms_of_cards)} cards have been saved.')

    def the_flashcards_game(self):
        number_to_play = int(log_input('How many times to ask?'))
        if len(self.terms_of_cards) != 0:
            for n in range(number_to_play):
                key = random.choice(self.terms_of_cards)
                log_print(f'Print the definition of "{key}":')
                user_input = input()
                if user_input == self.dict_of_cards[key]:
                    log_print("Correct!")
                elif user_input in self.dict_of_cards.values():
                    user_definition = list(self.dict_of_cards.keys())[list(self.dict_of_cards.values()).index(user_input)]
                    log_print(f'Wrong. The right answer is "{self.dict_of_cards[key]}",'
                          f' but your definition is correct for "{user_definition}"')
                    self.mistakes_of_cards[key] = self.mistakes_of_cards[key] + 1
                else:
                    log_print(f'Wrong. The right answer is "{Cards.dict_of_cards[key]}".')
                    self.mistakes_of_cards[key] = self.mistakes_of_cards[key] + 1
        else:
            log_print('No cards')

    def reset_stats(self):
        for card in self.terms_of_cards:
            self.mistakes_of_cards.update({card: 0})

    def hardest(self):
        try:
            max_mistakes = max(self.mistakes_of_cards.values())
        except ValueError:
            log_print('There are no cards with errors.')
        else:
            list_of_mistakes = []
            if max_mistakes == 0:
                log_print('There are no cards with errors.')
            else:
                for card in self.mistakes_of_cards:
                    if self.mistakes_of_cards[card] == max_mistakes:
                        list_of_mistakes.append(card)
                    else:
                        pass
                if len(list_of_mistakes) == 0:
                    log_print("There are no cards with errors.")
                elif len(list_of_mistakes) == 1:
                    log_print(f'The hardest card is "{list_of_mistakes[0]}". You have {max_mistakes} errors answering'
                              f' it.')
                else:
                    msg = 'The hardest cards are: "'
                    for el in list_of_mistakes:
                        msg += el + '", "'
                    msg = msg[:-3] + f'. You have {max_mistakes} errors answering it.'
                    log_print(msg)


def main():
    cards = Cards()
    parser = argparse.ArgumentParser(description="This is flashcards game")
    parser.add_argument("--import_from", default=False)
    parser.add_argument("--export_to", default=False)
    args = parser.parse_args()
    if args.import_from:
        cards.import_cards(args.import_from)

    while True:
        action = log_input('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):')
        if action == 'exit':
            log_print('Bye bye!')
            break
        elif action == 'add':
            cards.add()
        elif action == 'remove':
            cards.remove()
        elif action == 'import':
            file_name = log_input('File name:')
            cards.import_cards(file_name)
        elif action == 'export':
            file_name = log_input('File name:')
            cards.export_cards(file_name)
        elif action == 'ask':
            cards.the_flashcards_game()
        elif action == 'hardest card':
            cards.hardest()
        elif action == 'log':
            save_log()
        elif action == 'reset stats':
            cards.reset_stats()
            log_print('Card statistics have been reset.')
        else:
            log_print('Wrong action')

    if args.export_to:
        cards.export_cards(args.export_to)


main()


#python Flashcards.py --import_from=cards.txt --export_to=cards.txt