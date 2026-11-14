def move_forwards(aturtle, step):
    aturtle.forward(step)
    print("move forward")

def move_backwards(aturtle, step):
    aturtle.backward(step)
    print("move backwards")

def rotate_left(aturtle, angle=10):
    current_angle = aturtle.heading()
    aturtle.setheading(current_angle + angle)
    print("rotate left")

def rotate_right(aturtle, angle=10):
    current_angle = aturtle.heading()
    aturtle.setheading(current_angle - angle)
    print("rotate right")

# Multi-key handling
class KeyRecording:
    def __init__(self, aturtle, step=20, angle=10):
        self.aturtle = aturtle
        self.keyset = set()
        self.step = step
        self.angle = angle
        self.original_state = {'step': self.step, 'angle': self.angle}

    def print_attributes(self):
        print(
            f"Step: {self.step}\n"
            f"Angle: {self.angle}\n"
        )

    def press(self, key):
        self.keyset.add(key)

    def release(self, key):
        self.keyset.discard(key)

    def increase_angle(self):
        self.angle += 5
        self.angle = min(self.angle, 360)
        print(f"Angle: {self.angle}")

    def decrease_angle(self):
        self.angle -= 5
        self.angle = max(self.angle, 10)
        print(f"Angle: {self.angle}")

    def increase_step(self):
        self.step += 20
        self.step = self.step = min(self.step, 100)
        print(f"Step: {self.step}")

    def decrease_step(self):
        self.step -= 20
        self.step = max(self.step, 10)
        print(f"Step: {self.step}")

    def reset(self):
        self.step = self.original_state['step']
        self.angle = self.original_state['angle']
        print("Resetting parameters...")
        print(f"Step: {self.step} | Angle: {self.angle}")


    def update(self, ascreen):
        if "Up" in self.keyset:
            move_forwards(self.aturtle, step=self.step)

        if "Down" in self.keyset:
            move_backwards(self.aturtle, step=self.step)
        if "Left" in self.keyset:
            rotate_left(self.aturtle, angle=self.angle)
        if "Right" in self.keyset:
            rotate_right(self.aturtle, angle=self.angle)

        ascreen.ontimer(fun=lambda: self.update(ascreen), t=20)

def start_turning_left(aturtle, angle=10):
    rotate_left(aturtle, angle)