# Reality Sources

- Source: NIST ASD Line List query endpoint `https://physics.nist.gov/cgi-bin/ASD/lines1.pl`
- Fetch date (UTC): `2026-02-14`
- Query pattern per element: `spectra=<symbol> I`, `format=3`, `unit=1(nm)`, `line_out=0`, `remove_js=on`
- Rate limit: `0.35` sec per request
- Timeout per request: `20` sec
- Elements queried: `118`
- Parsed lines written: `0`
- Output file: `data/external/raw/nist_lines.csv`

## Notes
- Some or all requests failed (network or endpoint format constraints).
- Failures: 118
  - Z=1 H: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=2 He: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=3 Li: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=4 Be: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=5 B: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=6 C: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=7 N: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=8 O: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=9 F: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=10 Ne: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=11 Na: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=12 Mg: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=13 Al: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=14 Si: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=15 P: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=16 S: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=17 Cl: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=18 Ar: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=19 K: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - Z=20 Ca: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>
  - ... (98 additional failures)
