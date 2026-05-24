import os, webbrowser

def run_game():
    path = os.path.join(os.path.dirname(__file__), 'pacman.html')
    webbrowser.open(f'file://{os.path.abspath(path)}')

if __name__ == '__main__':
    run_game()
