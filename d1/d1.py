class RPS:
    def __init__(self, inputs):
        self.inputs = self.process_inputs(inputs)
        self.p1_round_points = []
        self.p2_round_points = []

    @property
    def p1_score(self):
        return sum(self.p1_round_points)

    @property
    def p2_score(self):
        return sum(self.p2_round_points)

    def process_inputs(self, inputs):
        """Process file of inputs into a list of tuples.
        Translate inputs to use same coding for same inputs."""

        # Initialize translations to uniform input coding
        # X: rock, Y: paper, Z: scissors
        trantab = str.maketrans("XYZ", "ABC")

        with open(f"d1/{inputs}", "r", encoding="UTF-8") as f:
            inputs_processed = []

            for line in f.readlines():
                # Translate XYZ --> ABC
                line_translated = line.translate(trantab)

                # Convert str to tuples, combine to a list of tuples
                line_trimmed_and_splitted = line_translated.strip("\n").split(" ")
                tuple_line_trimmed = tuple(line_trimmed_and_splitted)
                inputs_processed.append(tuple_line_trimmed)

        return inputs_processed

    def play(self):
        """Play a game of Rock Paper Scissors. Player choices given in inputs."""

        for choices in self.inputs:
            new_round = Round(choices)
            outcome = new_round.calculate_outcome()
            self.p1_round_points.append(outcome[0])
            self.p2_round_points.append(outcome[1])

        # print(self.p1_scores)


class Round:
    def __init__(self, choices):
        self.choices = choices
        self.points = (0, 0)

    def calculate_outcome(self):
        """Calculates the outcome of the game."""
        # {'Rock': 'A', 'Paper': 'B', 'Scissors': 'C'}
        # {'Rock': 'X', 'Paper': 'Y', 'Scissors': 'Z'}

        if self.choices[0] not in ("A", "B", "C") or self.choices[1] not in (
            "A",
            "B",
            "C",
        ):
            return f"invalid inputs: {self.choices[0]}, {self.choices[1]}"

        if self.choices[0] == self.choices[1]:
            return (3, 3)

        p1_wins = [("A", "C"), ("B", "A"), ("C", "B")]

        if self.choices in (p1_wins):
            return (6, 0)
        else:
            return (0, 6)


def main():
    game = RPS("inputs.txt")  # A: rock VS. Y: scissors --> Y: scissors wins
    game.play()

    print(game.p1_score)


if __name__ == "__main__":
    main()
