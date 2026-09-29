"""糖果厂核心逻辑：糖浆、熬糖锅、浇筑和冷却。"""

import json


def new_game():
    return {"batches": {}, "pot_load": 0, "pot_capacity": 2, "syrup": 100, "rate": 100, "batch_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["batch_id"] += 1
    return state


def feed(state, batch_id, amount):
    state["batches"][batch_id] = amount
    state["syrup"] -= amount
    return True


def boil(state, batch_id):
    state["pot_load"] += 1
    return True


def check_temp(state, temp):
    if temp < 30:
        return "over"
    return "ok"


def cancel(state, batch_id):
    return True


def pour(state, amount):
    state["syrup"] -= amount
    return True


def crack(state):
    state["rate"] -= 10
    state["rate"] -= 10
    return state["rate"]


def cool(state, batch_id):
    return True


def main():
    print("糖果厂 - 命令: feed/boil/temp/cancel/pour/crack/cool/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
