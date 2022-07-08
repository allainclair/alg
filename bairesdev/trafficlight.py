import asyncio

# Some terminal colors help to create a Traffic Light view.
RED = '\033[1;31m'
GREEN = '\033[92m'
YELLOW = '\033[33m'
REVERSE = '\033[;7m'
RESET = '\033[0;0m'

# Some easy to print traffic light format.
COLOR_RED = f'{REVERSE}{RED}R {RESET}'
COLOR_GREEN = f'{REVERSE}{GREEN}G {RESET}'
COLOR_YELLOW = f'{REVERSE}{YELLOW}Y {RESET}'
COLOR_ALERT1 = f'{REVERSE}{YELLOW}A {RESET}'
COLOR_ALERT2 = f'{YELLOW}A {RESET}'

# Some states to help us in the traffic light logic and to print.
STATE_CLOSED = 'CLOSED'
STATE_OPEN = 'OPEN'
STATE_ATTENTION = 'ATTENTION'
STATE_ALERT = 'ALERT'

# Some times needed to:
TIME_ALERT = 0.5  # Alert animation turned off/on (blinking yellow)
TIME_ATTENTION = 2  # Yellow time for the traffic light to close.
TIME_DEADLINE = 1  # Deadline for the exiting task to set the exit event.

# Move the cursor to help to keep the Traffic Light in the same place when printed.
POSITION_LOG = '\033[1H'
POSITION_COLOR = '\033[2H'


async def main():
    # await test_event_wait()

    tl = TrafficLight()
    task_alert = asyncio.create_task(tl.transition(STATE_ALERT))
    await asyncio.sleep(5)
    task_close = asyncio.create_task(tl.transition(STATE_CLOSED))
    await asyncio.sleep(5)
    task_open = asyncio.create_task(tl.transition(STATE_OPEN))
    await asyncio.sleep(5)
    task_close = asyncio.create_task(tl.transition(STATE_CLOSED))
    await asyncio.sleep(5)
    task_alert = asyncio.create_task(tl.transition(STATE_ALERT))
    await asyncio.sleep(5)
    task_open = asyncio.create_task(tl.transition(STATE_OPEN))
    await asyncio.sleep(5)


def printcolor(color):
    print(POSITION_COLOR)
    print(color)


def printlog(message):
    if message:
        print(POSITION_LOG)
        print(message)


class TrafficLight:
    def __init__(self):
        self._exit_event = asyncio.Event()
        self._running_event = asyncio.Event()
        self._running_event.set()  # No task running.
        # This map helps us getting the functions according to the state.
        # We can avoid some ifs, for example.
        self._task_map = {
            STATE_ALERT: self.alert,
            STATE_CLOSED: self.close,
            STATE_OPEN: self.open,
        }

    async def _sync_in(self):
        """Can we improve it?"""
        if not self._running_event.is_set():  # If some task is running.
            self._running_event.set()
            self._exit_event.clear()

            # self._exit_event must be set as fast as possible
            # when self._running_event is set.
            if await event_wait(self._exit_event, TIME_DEADLINE, ''):
                pass  # The current task has exited.
            else:
                pass  # Probably a bad behavior (timeout). Take care here!
        else:  # No running task. A new task is going to start.
            pass
        self._running_event.clear()

    def _sync_out(self):
        """Necessary events to tell new tasks that there is no running task."""
        self._exit_event.set()
        self._running_event.set()

    async def alert(self):
        color_control = 0
        # We print the alert right away.
        printcolor(f'Traffic Light: {COLOR_ALERT2}')
        while not await event_wait(self._running_event, TIME_ALERT, ''):
            color_control %= 2
            color_control += 1
            if color_control == 1:
                printcolor(f'Traffic Light: {COLOR_ALERT1}')
            else:
                printcolor(f'Traffic Light: {COLOR_ALERT2}')
        # self._running_event has been set.

    async def transition(self, state):
        printlog(f'Move state to: {state}   ')
        # We wait for some sync logic before starting a new task.
        await self._sync_in()

        task = self._task_map[state]
        await task()

        # We need some sync before finishing the task.
        self._sync_out()

    async def close(self, attention_time=TIME_ATTENTION):
        printcolor(f'Traffic Light: {COLOR_YELLOW}')
        # If no task sets the event,
        # it means the change to red can proceed.
        if not await event_wait(self._running_event, attention_time, ''):
            printcolor(f'Traffic Light: {COLOR_RED}')
        else:
            pass  # self._running_event has been set in another task.

    async def open(self):
        """The open task is just a green color printed on the screen."""
        printcolor(f'Traffic Light: {COLOR_GREEN}')


async def event_wait(evt, timeout, timeout_message='Event timed out!'):
    """Perform an event.wait(timeout) like in the thread library."""
    try:
        await asyncio.wait_for(evt.wait(), timeout)
    except asyncio.exceptions.TimeoutError:
        # We just print a log message in case of timeout.
        printlog(timeout_message)

    return evt.is_set()


async def test_event_wait():
    # The event starts False.
    event = asyncio.Event()
    # event_wait waits for 1 second before returning the False event.
    assert not await event_wait(event, 1, timeout_message='')

    # The task waits for 2 seconds before timeout.
    task = asyncio.create_task(event_wait(event, 2))
    await asyncio.sleep(1)  # We sleep for for 1 second.
    event.set()  # The event is set after 1 second.
    assert await task  # The task must return True.


if __name__ == '__main__':
    asyncio.run(main())
