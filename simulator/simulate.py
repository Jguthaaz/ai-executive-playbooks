"""Standard-library decision support demo. All bundled data are synthetic."""
import argparse
import csv
import json
import math
from pathlib import Path

IMPACT = ['revenue', 'productivity', 'customer', 'risk', 'alignment']
EFFORT = ['data', 'integration', 'adoption', 'controls', 'resources']
SCENARIOS = {
    'Balanced': [25, 30, 20, 10, 15],
    'Growth': [45, 15, 15, 5, 20],
    'Efficiency': [10, 50, 15, 10, 15],
    'Service': [10, 20, 40, 20, 10],
}
EFFORT_WEIGHTS = [25, 25, 20, 15, 15]

def weighted(values, weights):
    if len(values) != len(weights) or not values:
        raise ValueError('Scores and weights must have equal nonzero length')
    if any(not math.isfinite(w) or w < 0 for w in weights) or sum(weights) <= 0:
        raise ValueError('Weights must be finite, nonnegative and total above zero')
    if any(not math.isfinite(v) or not 1 <= v <= 5 for v in values):
        raise ValueError('Every score must be finite and between 1 and 5')
    return sum(v * w for v, w in zip(values, weights)) / sum(weights)

def load_rows(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        reader = csv.DictReader(stream)
        required = ['id', 'name', *IMPACT, *EFFORT, 'confidence', 'ready']
        if not set(required).issubset(reader.fieldnames or []):
            raise ValueError('Missing required CSV columns')
        rows = list(reader)
    if not rows:
        raise ValueError('No opportunities supplied')
    seen = set()
    for row in rows:
        if not row['id'] or row['id'] in seen or not row['name']:
            raise ValueError('IDs must be unique and names nonempty')
        seen.add(row['id'])
        for key in IMPACT + EFFORT:
            row[key] = float(row[key])
        weighted([row[k] for k in IMPACT + EFFORT], [1] * 10)
        if row['ready'] not in ('yes', 'no') or row['confidence'] not in ('low', 'medium', 'high'):
            raise ValueError('Invalid readiness or confidence')
    return rows

def compare(rows, impact_weights, effort_weights):
    result = [dict(r, impact=weighted([r[k] for k in IMPACT], impact_weights),
                   effort=weighted([r[k] for k in EFFORT], effort_weights)) for r in rows]
    for r in result:
        # Only eligible candidates participate in the frontier comparison.
        r['frontier'] = r['ready'] == 'yes' and not any(
            o['ready'] == 'yes' and o['impact'] >= r['impact'] and o['effort'] <= r['effort']
            and (o['impact'] > r['impact'] or o['effort'] < r['effort']) for o in result)
    return result

def generate(input_path, output_dir):
    rows = load_rows(input_path)
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / 'scenario-results.csv').open('w', encoding='utf-8', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=['scenario', 'id', 'name', 'impact', 'effort', 'confidence', 'ready', 'frontier'])
        writer.writeheader()
        for scenario, weights in SCENARIOS.items():
            for r in compare(rows, weights, EFFORT_WEIGHTS):
                writer.writerow(dict(scenario=scenario, **{k: round(r[k], 4) if k in ('impact', 'effort') else r[k] for k in writer.fieldnames[1:]}))
    payload = json.dumps(dict(rows=rows, impact=IMPACT, effort=EFFORT, scenarios=SCENARIOS,
                              effortWeights=EFFORT_WEIGHTS), ensure_ascii=False).replace('<', '\\u003c')
    template = Path(__file__).with_name('viewer-template.html').read_text(encoding='utf-8')
    (output_dir / 'viewer.html').write_text(template.replace('__DATA__', payload), encoding='utf-8')
    return rows

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=Path(__file__).with_name('opportunities.csv'))
    parser.add_argument('--output', type=Path, default=Path(__file__).with_name('output'))
    args = parser.parse_args()
    try:
        generate(args.input, args.output)
    except (ValueError, OSError) as error:
        parser.exit(1, f'Unable to generate simulator: {error}\n')
    print(f'Generated {args.output / "viewer.html"} and scenario-results.csv')
