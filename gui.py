import tkinter as tk
from tkinter import messagebox


class VotingApp:
    def __init__(self, frame, vote_callback, restart_callback):
        self.frame = frame
        self.vote_callback = vote_callback
        self.restart_callback = restart_callback
        self.frame.title('Voting Menu')
        self.frame.geometry('300x300')
        self.frame.resizable(False, False)

        self.vote_frame = tk.Frame(frame)
        self.vote_frame.pack(fill='both', expand=False)
        self.label = tk.Label(self.vote_frame, text='Vote Menu', fg='blue', font=('Arial', 14))
        self.label.pack(pady=10)

        self.vote_button = tk.Button(self.vote_frame, text='Vote', command=self.show_candidates)
        self.vote_button.pack(pady=5)

        self.exit_button = tk.Button(self.vote_frame, text='Exit', command=self.frame.quit)
        self.exit_button.pack(pady=5)

        self.result_label = tk.Label(self.vote_frame, text='', fg='green')
        self.result_label.pack(pady=10)

    def show_candidates(self):
        self.vote_frame.pack_forget()
        self.candidate_frame = tk.Frame(self.frame)
        self.candidate_frame.pack(fill='both', expand=True)

        tk.Label(self.candidate_frame, text='Enter your ID:', font=('Arial', 10)).pack(pady=5)
        self.voter_id_entry = tk.Entry(self.candidate_frame)
        self.voter_id_entry.pack(pady=5)

        tk.Label(self.candidate_frame, text='Select Candidate:', font=('Arial', 10)).pack(pady=5)
        tk.Button(self.candidate_frame, text='John', command=lambda: self.vote('John')).pack(pady=5)
        tk.Button(self.candidate_frame, text='Jane', command=lambda: self.vote('Jane')).pack(pady=5)
        tk.Button(self.candidate_frame, text='Back', command=self.go_back_to_menu).pack(pady=10)

    def vote(self, candidate):
        voter_id = self.voter_id_entry.get().strip()
        if not voter_id:
            self.show_message('Error', 'You must enter an ID', 'red')
            return

        success = self.vote_callback(voter_id, candidate)
        if success:
            self.show_message('Congrats!', f'You voted for {candidate}!', 'green')
            self.go_back_to_menu()
        else:
            self.show_message('Error', 'You have already voted.', 'red')

    def update_results(self, john_votes, jane_votes):
        total_votes = john_votes + jane_votes
        self.result_label.config(
            text=f'John - {john_votes}, Jane - {jane_votes}, Total - {total_votes}'
        )

    def go_back_to_menu(self):
        self.candidate_frame.pack_forget()
        self.vote_frame.pack()

    def reset(self):
        self.restart_callback()
        self.update_results(0, 0)

    def show_message(self, title, message, color):
        messagebox.showinfo(title, message)
        self.result_label.config(text=message, fg=color)
