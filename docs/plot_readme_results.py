"""Regenerate the README charts from saved results without rerunning simulations."""
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'docs' / 'images'
SERIES = [
    ('optimal', 'Gurobi reference', '#64748b', 'D', '--'),
    ('spa', 'SPA', '#007c83', 'o', '-'),
    ('dts', 'DTS', '#c45a13', '^', '-'),
    ('improved_dts', 'Improved DTS', '#8054ae', 's', '-'),
]


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    plt.rcParams.update({'font.size': 11, 'axes.spines.top': False,
                         'axes.spines.right': False, 'figure.facecolor': 'white'})
    experiments = [
        ('ue_count_variation_plot_folder', 'profit_by_user_count.png',
         'Profit across user counts', 'Number of users',
         'Saved experiment: 100 to 700 users. Server counts vary at the 300-user point.'),
        ('bandwidth_comparison_plot_folder', 'profit_by_bandwidth.png',
         'Profit across bandwidth settings', 'Per-device bandwidth multiplier for fog servers',
         'Saved experiment: bandwidth multipliers as recorded in the source JSON.'),
    ]
    for folder, filename, title, xlabel, note in experiments:
        data = json.loads((ROOT / 'comparative_plots' / folder / 'accumulated_data.json').read_text())
        fig, ax = plt.subplots(figsize=(10, 5.8))
        fig.subplots_adjust(left=.11, right=.97, bottom=.19, top=.79)
        fig.text(.11, .94, title, fontsize=20, weight='bold', color='#172b3a')
        fig.text(.11, .885, note, fontsize=10, color='#526170')
        for key, label, color, marker, style in SERIES:
            points = sorted((float(x), y) for x, y in data[key].items())
            ax.plot([x for x, _ in points], [y for _, y in points],
                    label=label, color=color, marker=marker, linestyle=style,
                    linewidth=2.2, markersize=6)
        ax.set(xlabel=xlabel, ylabel='Total system profit (simulation units)', ylim=(0, None))
        ax.set_xticks(sorted(float(x) for x in data['spa']))
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.0f}'))
        ax.grid(axis='y', alpha=.2)
        ax.set_axisbelow(True)
        ax.legend(loc='upper left', frameon=False, ncol=2, fontsize=10)
        fig.text(.11, .045, 'Recorded values only; no repeated-trial uncertainty is available.',
                 fontsize=10, color='#526170')
        fig.savefig(OUTPUT / filename, dpi=180, facecolor='white')
        plt.close(fig)


if __name__ == '__main__':
    main()
