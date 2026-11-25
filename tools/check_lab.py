"""Check founding artifacts and optionally rerun finite checks in a scratch copy."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / 'research/mathematics/prefix-reversal-asymptotics'


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reproduce', choices=['quick', 'full'])
    args = parser.parse_args()
    ledger = json.loads((ROOT / 'research/registry.json').read_text(encoding='utf-8'))
    ids = set()
    for project in ledger['projects']:
        ident = project['id']
        require(ident not in ids, f'Duplicate project ID: {ident}')
        ids.add(ident)
        for field in ('title', 'status', 'formal_verification', 'independent_review', 'priority'):
            require(bool(project.get(field)), f'Missing field {field}: {ident}')
        loc = project['location']
        if not loc.startswith('https://'):
            require((ROOT / loc / 'README.md').is_file(), f'Missing project: {loc}')
    manifest = PROJECT / 'ARTIFACTS.sha256'
    count = 0
    for line in manifest.read_text(encoding='utf-8').splitlines():
        digest, name = line.split(maxsplit=1)
        require(Path(name).name == name, 'Invalid manifest path')
        require(hashlib.sha256((PROJECT / name).read_bytes()).hexdigest() == digest,
                f'Archived artifact changed: {name}')
        count += 1
    require(count == 6, 'Incomplete founding manifest')
    print(f'PASS: {len(ids)} ledger entries; {count} founding artifact hashes.', flush=True)
    if not args.reproduce:
        return
    archived = json.loads((PROJECT / 'results.json').read_text())
    limits = (26, 100, 8) if args.reproduce == 'full' else (12, 30, 8)
    with tempfile.TemporaryDirectory(prefix='opl-verify-') as temp:
        dst = Path(temp) / 'research'
        shutil.copytree(PROJECT, dst)
        subprocess.run([sys.executable, str(dst / 'verify.py'), '--order-max', str(limits[0]),
                        '--identity-max', str(limits[1]), '--bfs-max', str(limits[2])], check=True)
        result = json.loads((dst / 'results.json').read_text())
    require(result['violations'] == 0, 'A finite check failed')
    if args.reproduce == 'full':
        require(result == archived, 'Full result differs from archived evidence')
    else:
        require(result['rows'] == [row for row in archived['rows'] if row['n'] <= limits[0]],
                'Quick test row differs from archived evidence')
        require(result['coefficients'] == archived['coefficients'], 'Coefficients differ')
        from math import comb
        from itertools import combinations
        require(result['exact_group_order_checks'] == sum(comb(n-2, 2) for n in range(4, limits[0]+1)), 'Unexpected group-check count')
        require(result['identity_checks'] == sum(a+b <= n-3 for n in range(4, limits[1]+1) for a,b in combinations(range(1,n-1),2)), 'Unexpected identity-check count')
        require(result['bfs_checks'] == archived['bfs_checks'], 'BFS count differs')
    print(f'PASS: {args.reproduce} reproduction matches archived records. Finite checks only; not a formal proof or independent review.')


if __name__ == '__main__':
    main()
