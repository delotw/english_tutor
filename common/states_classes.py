from aiogram.fsm.state import StatesGroup, State


class Reg(StatesGroup):
    name = State()
    grade = State()
    sex = State()


class BalanceDeposit(StatesGroup):
    amount = State()
    wait_confirm = State()


class CheckMail(StatesGroup):
    check_type = State()
    task_type = State()
    confirmed = State()
    check_done = State()


class SolveTasks(StatesGroup):
    solve_audio = State()
    solve_reading = State()
    sovle_grammar = State()
    solve_mails = State()

    # немного другая и более страшная хуйня
    solve_main_content = State()
    solve_TFNS_search = State()
    solve_full_understanding = State()
    solve_match = State()
    solve_insert = State()
    solve_choice_right = State()
    solve_grammar = State()
    solve_vocabulary = State()
    solve_mail = State()
    solve_essay = State()
