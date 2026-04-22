#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ollama


MODEL = "enterprise-assistant"


def main():
    messages = [
        {
            "role": "system",
            "content": "Ты корпоративный AI-помощник. Отвечай кратко и по делу.",
        }
    ]

    print("Чат-бот запущен. Напиши 'exit' для выхода.\n")

    while True:
        user_text = input("Ты: ").strip()
        if not user_text:
            continue

        if user_text.lower() in {"exit", "quit", "выход"}:
            print("Завершение.")
            break

        messages.append({"role": "user", "content": user_text})

        response = ollama.chat(
            model=MODEL,
            messages=messages,
            options={"temperature": 0.7},
        )

        assistant_text = response["message"]["content"]
        print(f"\nБот: {assistant_text}\n")

        messages.append({"role": "assistant", "content": assistant_text})


if __name__ == "__main__":
    main()