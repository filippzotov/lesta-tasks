# 2. На языке Python (2.7) реализовать минимум по 2 класса
# реализовывающих циклический буфер FIFO.
# Объяснить плюсы и минусы каждой реализации.

# Обычная версия циклической очереди со статическим размером

# Плюсы: Статический размер делает очередь предсказуемой с точки зрения выделения памяти
# Минусы: Если требуется расширить размер очереди, то придется заново её создавать с новым размером


class CircularQueue1:
    def __init__(self, size) -> None:
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    # Поулчение нового индекса для конца или начала очереди
    def next_index(self, index):
        return (index + 1) % self.size

    # Добавление нового элемента в очередь
    def enqueue(self, elem):
        if self.next_index(self.tail) == self.head:
            print("Очередь заполнена")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = elem
        else:
            self.tail = self.next_index(self.tail)
            self.queue[self.tail] = elem

    # Удаление элемента из очереди
    def dequeue(self):
        if self.head == -1:
            print("Очередь пуста")
        elif self.head == self.tail:
            pop_element = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return pop_element
        else:
            pop_element = self.queue[self.head]
            self.head = self.next_index(self.head)
            return pop_element

    # Вывод очереди в виде строки
    def __str__(self) -> str:
        return str(self.queue)


# Версия циклической очереди с динамическим выделением памяти под
# новые элементы в случае, если место в очереди кончилось

# Плюсы: Очередь автоматически выделяет память под новые элементы
# Минусы: При очистке очереди останутся пустые элементы, занимающие место в памяти


class CircularQueue2:
    def __init__(self, size) -> None:
        self.size = size
        self.queue = [None] * size
        self.head = -1
        self.tail = -1

    # Поулчение нового индекса для конца или начала очереди
    def next_index(self, index):
        return (index + 1) % self.size

    # Добавление нового элемента в очередь
    def enqueue(self, elem):
        if (
            self.next_index(self.tail) == self.head
        ):  # Расширение размера очереди при нехватке места
            self.size *= 2
            if self.head < self.tail:
                self.queue = self.queue[: self.next_index(self.tail)] + [None] * (
                    self.size // 2
                )
            else:
                self.queue = (
                    self.queue[: self.next_index(self.tail)]
                    + [None] * (self.size // 2)
                    + self.queue[self.head :]
                )
                self.head = self.head + self.size // 2
        if self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = elem
        else:
            self.tail = self.next_index(self.tail)
            self.queue[self.tail] = elem

    # Удаление элемента из очереди
    def dequeue(self):
        if self.head == -1:
            print("Очередь пуста")
        elif self.head == self.tail:
            pop_element = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return pop_element
        else:
            pop_element = self.queue[self.head]
            self.head = self.next_index(self.head)
            return pop_element

    # Вывод очереди в виде строки
    def __str__(self) -> str:
        return str(self.queue)
