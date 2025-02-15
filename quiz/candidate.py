ELECTORAL_VOTES = {'AZ': 11, 'CA': 55, 'FL': 29, 'IA': 6, 'MA': 11, 'OH': 18, 'PA': 20, 'TX': 38}




class Candidate:
    """The presidential candidate"""

    def __init__(self, name, winning_states=None, votes=0):
        """Initialize candidate.
        name: string
        winning_states: a list of strings representing initial winning state(s) (even before voting).
        votes: integer, representing number of votes
        """
        self.name = name
        self.winning_states = winning_states
        self.votes = votes
        if self.winning_states is None:
            self.winning_states = ''
        for state in self.winning_states:
            self.votes += ELECTORAL_VOTES.get(state)

    def __str__(self):
        """Return a string representation of this candidate,
        including name and winning state(s).
        """
        return (f'{self.name}: {self.winning_states}')

    def __lt__(self, other):
        """return True if self's votes is lexicographically
           less than other's votes, and False otherwise""" 
        if self.votes == other.votes:
            return self.votes < other.votes
        return self.votes < other.votes

    def win_state(self, state):
        """Adds a state to winning_states and updates votes.
        state: a string of state abbreviation
        """
        self.winning_states.append(state)
        self.votes += ELECTORAL_VOTES.get(state)
        return self.winning_states

    



###########################################
# Please DO NOT change code in main method!
###########################################
def main():
    trump = Candidate('Donald Trump', winning_states=['TX', 'FL'])
    biden = Candidate('Joe Biden', winning_states=['CA', 'MA'])
    west = Candidate('Kanye West')
    print('Before voting:')
    print(trump)
    print(biden)
    print(west)
    print('Does Trump win?')
    print(trump > biden)
    print()
    print('After election day:')
    trump.win_state('OH')
    trump.win_state('IA')
    biden.win_state('PA')
    biden.win_state('AZ')
    print(trump)
    print(biden)
    print('Does Trump win?')
    print(trump > biden)


if __name__ == '__main__':
    main()