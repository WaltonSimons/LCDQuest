
class Control:

    def __init__(self):
        self.input = None

    def clear_input(self):
        self.input = ''

    def wait_for_input(self):
        self.input = raw_input('>')

    def A_button(self):
        return self.input == 'f'

    def B_button(self):
        return self.input == 'g'

    def left_arrow(self):
        return self.input == 'a'

    def right_arrow(self):
        return self.input == 'd'

    def up_arrow(self):
        return self.input == 'w'

    def down_arrow(self):
        return self.input == 's'

    def ESC_button(self):
        return self.input == 'quit'