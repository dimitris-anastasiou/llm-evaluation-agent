
default: help

clean:
	@echo "Removing __pycache__ directories..."
	find . -type d -name "__pycache__" -exec rm -r {} +

help:
	@echo "clean - remove __pycache__ directories"
	@echo "help - display this help message"



