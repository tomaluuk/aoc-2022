class RPS:
    """Represents a game of Rock, Paper, Scissors."""

    def __init__(self, inputs):
        self.inputs = self.process_inputs(inputs)
        self.rounds = []  # List of played rounds

    @property
    def p1_score(self):
        """Calculates score for p1 from list of Rounds."""
        scores = [r.points[0] for r in self.rounds]
        return sum(scores)

    @property
    def p2_score(self):
        """Calculates score for p2 from list of Rounds."""
        scores = [r.points[1] for r in self.rounds]
        return sum(scores)

    def process_inputs(self, inputs):
        """Process file of inputs into a list of tuples.
        Translate inputs to use same coding for same inputs."""

        # Initialize translations to uniform input coding: XYZ -> ABC
        # A: rock, B: paper, C: scissors
        trantab = str.maketrans("XYZ", "ABC")

        with open(f"d1/{inputs}", "r", encoding="UTF-8") as f:
            inputs_processed = []

            for line in f.readlines():
                line_translated = line.translate(trantab)

                # Convert str to tuples, combine to a list of tuples
                line_trimmed_and_splitted = line_translated.strip("\n").split(" ")
                tuple_line_trimmed = tuple(line_trimmed_and_splitted)
                inputs_processed.append(tuple_line_trimmed)

        return inputs_processed

    def play(self):
        """Play a game of Rock Paper Scissors. Player choices given in inputs."""

        # Loop through a list of tuples holding player choices for individual Rounds
        for choices in self.inputs:
            new_round = Round(choices)
            new_round.calculate_outcome()
            self.rounds.append(new_round)


class Round:
    """
    Represents a single round in a game of Rock, Paper, Scissors.
    A Round can end in p1 winning, p2 winning, or a draw.
    """

    # Points given for the choice made in a Round
    # A -> Rock, B -> Paper, C -> Scissors
    dict_choice_points = {"A": 1, "B": 2, "C": 3}
    p1_winning_combinations = [("A", "C"), ("B", "A"), ("C", "B")]

    def __init__(self, choices):
        self.choices = choices
        self.points = self.calculate_choice_points()

    def calculate_choice_points(self):
        """Calculates the choice points in accordance of dict_choice_points."""

        # Ensure choices are consistent with expected ABC coding
        if self.choices[0] not in ("A", "B", "C") or self.choices[1] not in (
            "A",
            "B",
            "C",
        ):
            print(f"invalid inputs: {self.choices[0]}, {self.choices[1]}")

        choice_points = [self.dict_choice_points[choice] for choice in self.choices]

        return choice_points

    def calculate_outcome(self):
        """Calculates the outcome of the game."""

        if self.choices[0] == self.choices[1]:
            self.points[0] += 3
            self.points[1] += 3
            return self

        if self.choices in (self.p1_winning_combinations):
            self.points[0] += 6
            return self
        else:
            self.points[1] += 6
            return self


def main():
    game = RPS("inputs.txt")  # A: rock VS. Y: scissors --> Y: scissors wins
    game.play()

    print("Total scores after tournament")
    print(f"Opponents score: {game.p1_score}")
    print(f"My score: {game.p2_score}")


if __name__ == "__main__":
    main()
