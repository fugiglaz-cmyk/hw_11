class GameEventException(Exception):

    def __init__(self, event_name: str, metadata: str) -> None:
        """Method fot initialization
        args: event_name: what happened
        metadata: adittional information about the event
        return: None
        """
        self.event_name = event_name
        self.metadata = metadata
        super().__init__(f"{event_name} is happened because: {metadata}")


def action() -> None:
    """Method for information about the game event
    return: what happened and why
    """
    event_name = input("Enter the action that happen: ")
    metadata = input("Enter how the action start, end, etc: ")
    print(f"{event_name} is happened because: {metadata}")
    raise GameEventException(event_name, metadata)


def save_event(event_name: str, metadata: str) -> None:
    """Method to save the event
    args: event_name: what happened
    metadata: why this happened
    return: None
    """
    with open("events_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{event_name}: {metadata}\n")


def main() -> None:
    """Func for do the main algorithm
    return: None
    """
    try:
        action()
    except GameEventException as e:
        print(f"[Game event ended] {e.event_name}")
        print(f"Details: {e.metadata}")
        save_event(e.event_name, e.metadata)
        print("Event data has been saved.")
    except Exception as e:
        print(f"Unexpected error: {e}")

main()
