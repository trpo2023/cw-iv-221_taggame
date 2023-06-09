.PHONY: all clean

# Компиляция и запуск программы
all: main.py
	python3 main.py

# Очистка временных файлов
clean:
	rm -rf __pycache__