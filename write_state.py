from turtle import Turtle


class Write(Turtle):
    def __init__(self, answer_state, df):
        super().__init__()
        state_data = df[df.state == answer_state]
        self.penup()
        self.hideturtle()
        self.goto(state_data.x.item(), state_data.y.item())
        self.write(answer_state, align="center")
