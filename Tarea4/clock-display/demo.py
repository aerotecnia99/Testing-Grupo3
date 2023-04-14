from src.clock_factory import ClockFactory

factory = ClockFactory()
clock = factory.create("hh:mm")

for i in range(10000):
    clock.increment()
    print(clock.str())