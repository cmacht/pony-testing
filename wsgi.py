"""
Entry point for uwsgi
"""

from src.start import app

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
