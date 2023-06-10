.PHONY: all clean

# Компиляция и запуск программы
all: main.py
	python3 main.py

# Очистка временных файлов
clean:
	find $(CURDIR)/src -type d -name "__pycache__" -exec rm -rf {} +

