from subject import *
from observer import *
from concrete_observer import *



def main():
    subject = Subject()
    concrete_observer_one = ConcreteObserverOne()
    concrete_observer_two = ConcreteObserverTwo()
    subject.attach(concrete_observer_one)
    subject.attach(concrete_observer_two)
    subject.subject_state = 123

if __name__ == "__main__":
    main()