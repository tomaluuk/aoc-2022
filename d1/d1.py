class RPS:
    def __init__(self, inputs):
        self.inputs = self.process_inputs(inputs)

    def process_inputs(self, inputs):
        """Process file of space separated round input pairs and
        newline separated rounds into a list of tuples."""

        with open(f"d1/{inputs}", "r") as f:
            inputs_processed = []

            for line in f.readlines():
                line_trimmed_and_splitted = line.strip("\n").split(" ")
                tuple_line_trimmed = tuple(line_trimmed_and_splitted)
                inputs_processed.append(tuple_line_trimmed)

        return inputs_processed

    def play(self):
        """Play a game of Rock Paper Scissors. Player choices given in inputs."""

        rps_round = Round()

        for choices in self.inputs:
            outcome = rps_round.calculate_outcome(choices)
            print(outcome)


class Round:
    def calculate_outcome(self, choices):
        # {'Rock': 'A', 'Paper': 'B', 'Scissors': 'C'}
        # {'Rock': 'X', 'Paper': 'Y', 'Scissors': 'Z'}
        self.choices = choices

        if self.choices[0] not in ("A", "B", "C") or self.choices[1] not in (
            "X",
            "Y",
            "Z",
        ):
            return f"invalid inputs: {self.choices[0]}, {self.choices[1]}"

        if self.choices[0] == self.choices[1]:
            return "draw: {}"

        p1_wins = [("A", "Z"), ("B", "X"), ("C," "Y")]

        if self.choices in (p1_wins):
            return "p1 wins"
        else:
            return "p2 wins"


def main():
    # with open('inputs.txt', 'r') as f:
    #    f.readline()
    inputs_text = "A Y\nB T\nC Z"
    inputs = [("A", "Y"), ("B", "T"), ("C", "Z")]

    game = RPS("inputs_sample.txt")  # A: rock VS. Y: scissors --> Y: scissors wins
    game.play()


if __name__ == "__main__":
    main()
