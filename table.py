from utils import convert_to_ordinal

class Table:
    def __init__:
        pass

    def announce_round(self, round_num):
        round_num_out = convert_to_ordinal(round_num)
        print(f"==== {round_num_out} round of table ====")

    def announce_war(self):
        pass

    def table_start_end(self):
        print("======================")

    def user_cards(self):
        pass

    def computer_cards(self):
        pass


    def vizualize_table(self):
        if war:
            self.announce_war()
        else:
            self.announce_round()
        self.table_start_end()
        ...
        self.table_start_end()