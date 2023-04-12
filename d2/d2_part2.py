import pathlib


class RPS:
    """Represents a game of Rock, Paper, Scissors."""

    def __init__(self, input_file_name):
        self.inputs = self.process_inputs(input_file_name)
        self.rounds = []  # List of played rounds

    def process_inputs(self, input_file_name):
        """Process file of inputs into a list of tuples."""
        pwd = pathlib.Path(__file__).parent.resolve()

        with open(f"{pwd}/{input_file_name}", "r", encoding="UTF-8") as f:
            inputs_processed = []

            for line in f.readlines():
                # Convert str to tuples, combine to a list of tuples
                line_trimmed_and_splitted = line.strip("\n").split(" ")
                line_tuple = tuple(line_trimmed_and_splitted)
                inputs_processed.append(line_tuple)

        return inputs_processed

    @property
    def opponent_score(self):
        """Calculates score for opponent from list of Rounds."""
        scores = [r.points[0] for r in self.rounds]
        return sum(scores)

    @property
    def own_score(self):
        """Calculates own score from list of Rounds."""
        scores = [r.points[1] for r in self.rounds]
        return sum(scores)

    def play(self):
        """Play a game of Rock Paper Scissors. Player round_inputs given in inputs."""

        # Loop through a list of tuples holding player round_inputs for individual Rounds
        for round_inputs in self.inputs:
            new_round = Round(round_inputs)
            new_round.calculate_outcome()
            self.rounds.append(new_round)


class Round:
    """
    Represents a single round in a game of Rock, Paper, Scissors.
    A Round can end in win for either participant or a draw.
    """

    # Points given for the choice made in a Round
    # A -> Rock, B -> Paper, C -> Scissors
    dict_choice_points = {"A": 1, "B": 2, "C": 3}
    opponent_winning_combinations = [("A", "C"), ("B", "A"), ("C", "B")]
    winning_answers_to_opponent_input = {"A": "B", "B": "C", "C": "A"}
    losing_answers_to_opponent_input = {"A": "C", "B": "A", "C": "B"}

    def __init__(self, round_inputs):
        self.round_inputs = self.determine_round_inputs(round_inputs)
        self.points = self.calculate_choice_points()

    def determine_round_inputs(self, round_inputs):
        """Choose round inputs based on coding in round_inputs"""
        opponent_input, desired_outcome = round_inputs
        own_input = opponent_input

        if desired_outcome == "X":  # Lose round
            own_input = self.losing_answers_to_opponent_input[opponent_input]
        if desired_outcome == "Z":  # Win round
            own_input = self.winning_answers_to_opponent_input[opponent_input]

        return (opponent_input, own_input)

    def calculate_choice_points(self):
        """Calculates the choice points in accordance of dict_choice_points."""

        # Ensure round_inputs are consistent with expected ABC coding
        if self.round_inputs[0] not in ("A", "B", "C") or self.round_inputs[1] not in (
            "A",
            "B",
            "C",
        ):
            print(
                f"invalid inputs: {self.round_inputs[0]}, {self.round_inputs[1]}")

        choice_points = [self.dict_choice_points[choice]
                         for choice in self.round_inputs]

        return choice_points

    def calculate_outcome(self):
        """Calculates the outcome of the game."""

        if self.round_inputs[0] == self.round_inputs[1]:  # Draw
            self.points[0] += 3
            self.points[1] += 3
            return self

        if self.round_inputs in (self.opponent_winning_combinations):  # Opponent wins
            self.points[0] += 6
            return self
        else:  # I win
            self.points[1] += 6
            return self


def main():
    game = RPS("inputs.txt")  # A: rock VS. Y: scissors --> Y: scissors wins
    game.play()

    print("Total scores after tournament")
    print(f"Opponents score: {game.opponent_score}")
    print(f"My score: {game.own_score}")


if __name__ == "__main__":
    main()
