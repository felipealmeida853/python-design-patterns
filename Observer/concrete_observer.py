from observer import Observer

class ConcreteObserverOne(Observer):

    def update(self, args):
        self._observer_state = args
        print('dispare observe 1')
        print('args' + str(args))
        self._mult = args * args
        print(self._mult)


class ConcreteObserverTwo(Observer):

    def update(self, args):
        self._observer_state = args
        print('dispare observe 2')
        print('args' + str(args))
        self._sum = args + args
        print(self._sum)
