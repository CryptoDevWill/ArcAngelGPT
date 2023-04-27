

class WorkMode:
    def __init__(self):
        self.value = False

    def set(self, state):
        self.value = state

    def get(self):
        return self.value

work_mode = WorkMode()


class Loading:
    def __init__(self):
        self.value = True

    def set(self, state):
        self.value = state

    def get(self):
        return self.value

loading = Loading()
