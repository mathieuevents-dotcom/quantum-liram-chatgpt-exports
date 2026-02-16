# REAL_ABLATIONS
- seed=42, Kmax=60, metrics rerun on ablated covariance reconstructions.
- baseline phi37=6.972598, sync37=0.560161
- A1 diag removal: phi37=11.300293, sync37=0.653764
- A2 near-diagonal (w=1..5): phi37 range [3.849287, 5.219263], sync37 range [0.475144, 0.546968]
- A3 long-range only (w=1..5): phi37 range [8.652345, 10.251292], sync37 range [0.328406, 0.444505]
- A4 rank-k sweep: core phi37 max=21.422354, residual phi37 max=8.475652
- strongest phi drop: A2_near_diagonal w=1 (delta=-3.123310)
- strongest sync drop: A3_long_range_only w=1 (delta=-0.231755)
- Guardrail: information geometry only; no physical claim.
