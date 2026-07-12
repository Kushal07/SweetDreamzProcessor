"""
SweetDreamzProcessor
Application Entry Point
"""

from gui import SweetDreamzApp


def main() -> None:
    """Start the application."""
    app = SweetDreamzApp()
    app.run()


if __name__ == "__main__":
    main()