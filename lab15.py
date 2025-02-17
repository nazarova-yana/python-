import random
from typing import Dict, List, Union

# Визначення можливих дій у грі та їх перемог
ACTIONS: Dict[int, str] = {0: "Rock", 1: "Paper", 2: "Scissors"}
VICTORIES: Dict[str, str] = {
    "Rock": "Scissors",  # Камінь перемагає ножиці
    "Paper": "Rock",  # Папір перемагає камінь
    "Scissors": "Paper",  # Ножиці перемагають папір
}


def get_user_selection(actions: Dict[int, str]) -> str:
    """
    Отримує вибір користувача зі списку доступних дій.

    :param actions: Словник доступних дій (ключ - число, значення - назва дії).
    :return: Рядок, що представляє вибір користувача.
    """
    choices: List[str] = [f"{actions[action]}[{action}]" for action in actions]
    choices_str: str = ", ".join(choices)
    selection: int = int(input(f"Enter a choice ({choices_str}): "))
    action: str = actions[selection]
    return action


def get_computer_selection(actions: Dict[int, str]) -> str:
    """
    Отримує випадковий вибір комп'ютера зі списку доступних дій.

    :param actions: Словник доступних дій (ключ - число, значення - назва дії).
    :return: Рядок, що представляє вибір комп'ютера.
    """
    selection: int = random.randint(0, len(actions) - 1)
    action: str = actions[selection]
    return action


def get_determine_winner(
    victories: Dict[str, str], user_action: str, computer_action: str
) -> str:
    """
    Визначає переможця гри на основі вибору користувача та комп'ютера.

    :param victories: Словник, що визначає, яка дія перемагає іншу.
    :param user_action: Вибір користувача.
    :param computer_action: Вибір комп'ютера.
    :return: Рядок, що описує результат гри.
    """
    defeats: str = victories[user_action]
    if user_action == computer_action:
        result: str = f"Both players selected {user_action}. It's a tie!"
    elif computer_action in defeats:
        result: str = f"{user_action} beats {computer_action}! You win!"
    else:
        result: str = f"{computer_action} beats {user_action}! You lose."
    return result


if __name__ == "__main__":
    while True:
        try:
            # Отримання вибору користувача
            user_selection: str = get_user_selection(ACTIONS)
            print(f"You chose: {user_selection}")

            # Отримання вибору комп'ютера
            computer_selection: str = get_computer_selection(ACTIONS)
            print(f"Computer chose: {computer_selection}")

            # Визначення переможця та виведення результату
            determine_winner: str = get_determine_winner(
                VICTORIES, user_selection, computer_selection
            )
            print(determine_winner)
        except (KeyError, ValueError):
            # Обробка помилок у випадку невірного вводу
            range_str: str = f"[0, {len(ACTIONS) - 1}]"
            print(f"Invalid selection. Enter a value in range {range_str}")
            continue

        # Запит на повторення гри
        play_again: str = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
