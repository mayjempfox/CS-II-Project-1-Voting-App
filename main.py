import tkinter as tk
from gui import VotingApp
import csv
import os

class VotingLogic:
    def __init__(self, vote_file='votes.csv'):
        self.john_votes = 0
        self.jane_votes = 0
        self.vote_file = vote_file
        self.voters = set() 
        if os.path.exists(self.vote_file):
            with open(self.vote_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    voter_id, candidate = row
                    self.voters.add(voter_id)
                    if candidate == 'John':
                        self.john_votes += 1
                    elif candidate == 'Jane':
                        self.jane_votes += 1

    def vote_for_candidate(self, voter_id, candidate):
        if voter_id in self.voters:
            return False  #if there is duplicates
        self.voters.add(voter_id)
        if candidate == 'John':
            self.john_votes += 1
        elif candidate == 'Jane':
            self.jane_votes += 1
        self.save_vote(voter_id, candidate)
        return True

    def save_vote(self, voter_id, candidate):
        with open(self.vote_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([voter_id, candidate])

    def get_results(self):
        return self.john_votes, self.jane_votes

    def restart_votes(self):# clear
        self.john_votes = 0
        self.jane_votes = 0
        self.voters.clear()
        with open(self.vote_file, 'w'):
            pass
def main():
    logic = VotingLogic()
    def handle_vote(voter_id, candidate):
        if logic.vote_for_candidate(voter_id, candidate):
            update_results()
            return True
        return False
    def update_results():
        john, jane = logic.get_results()
        app.update_results(john, jane)

    def handle_restart():
        logic.restart_votes()
        update_results()
    frame = tk.Tk()
    app = VotingApp(frame, handle_vote, handle_restart)
    frame.mainloop()


if __name__ == '__main__':
    main()
