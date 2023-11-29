import os
import csv
from google.colab import drive
import matplotlib.pyplot as plt

def generate_winner_stats():
    drive.mount('/content/drive')

    file_path = '/content/drive/My Drive/game_result.csv'

    if not os.path.exists(file_path):
        print("No game history found.")
        return

    stats = {
        'X Win': 0,
        'O Win': 0,
        'Bot Win': 0,
        'X&O Draw': 0,
        'X&Bot Draw': 0
    }

    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            is_bot = row[0]
            winner = row[1]
            winner_type = row[2]

            if winner == 'X':
                stats['X Win'] += 1
            elif winner == 'O':
                stats['O Win'] += 1
            elif winner == 'Draw':
                if is_bot == 'Bot':
                    stats['X&Bot Draw'] += 1
                else:
                    stats['X&O Draw'] += 1

            if winner_type == 'Bot':
                stats['Bot Win'] += 1

    print(stats)

    labels = list(stats.keys())
    counts = list(stats.values())

    counts = [int(count) for count in counts]

    fig, ax = plt.subplots(figsize=(10, 5))
    bars = ax.bar(labels, counts, color=['blue', 'orange', 'green', 'red', 'purple'])

    ax.set_xlabel('Game Outcome')
    ax.set_ylabel('Number of Games')
    ax.set_title('Tic Tac Toe Game Outcomes')

    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=45)

    ax.set_ylim(0, max(counts) + 1)

    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{int(height)}',
            xy=(bar.get_x() + bar.get_width() / 2, height),
            xytext=(0, 3),
            textcoords="offset points",
            ha='center', va='bottom')

    plt.tight_layout()
    plt.show()

    return stats

if __name__ == '__main__':
    generate_winner_stats()