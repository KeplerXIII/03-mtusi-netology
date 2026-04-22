#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def run_benchmark():
    try:
        from benchmark_ollama import main as run
        run()
    except ImportError as e:
        print(f"[ERR] benchmark: {e}")


def run_structured():
    try:
        from structured_output_demo import main as run
        run()
    except ImportError as e:
        print(f"[ERR] structured_output: {e}")


def run_chat():
    try:
        from chat_bot import main as run
        run()
    except ImportError as e:
        print(f"[ERR] chat_bot: {e}")


def print_menu():
    print("\n" + "=" * 50)
    print("ВЫБЕРИ РЕЖИМ")
    print("=" * 50)
    print("1 — Benchmark моделей")
    print("2 — Structured Outputs (тональность)")
    print("3 — Чат-бот (с памятью)")
    print("0 — Выход")
    print("=" * 50)


def main():
    while True:
        print_menu()
        choice = input("Ввод: ").strip()

        if choice == "1":
            print("\n>>> Benchmark\n")
            run_benchmark()

        elif choice == "2":
            print("\n>>> Structured Output\n")
            run_structured()

        elif choice == "3":
            print("\n>>> Chat Bot\n")
            run_chat()

        elif choice == "0":
            sys.exit(0)

        else:
            print("Неверный выбор")


if __name__ == "__main__":
    main()