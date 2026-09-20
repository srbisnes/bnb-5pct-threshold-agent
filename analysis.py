"""
Risk Analysis + Profit Evaluator + Best Hours module
Professional layer for the BNB 5% Threshold Agent
"""
from decimal import Decimal
from dataclasses import dataclass
from typing import List, Dict
import statistics

@dataclass
class RiskReport:
    risk_level: str
    volatility_pct: float
    max_position_pct: float
    recommended_stop: float
    notes: List[str]

@dataclass
class ProfitProjection:
    capital: float
    risk_per_trade_pct: float
    trades_per_month: int
    expected_monthly_pnl: float
    expected_monthly_roi: float
    estimated_max_drawdown: float
    win_rate_assumed: float

def analyze_risk(recent_returns: List[float] = None, base_vol: float = 2.5) -> RiskReport:
    """
    Simple risk analysis.
    recent_returns: list of percentage returns (optional)
    """
    if recent_returns and len(recent_returns) > 3:
        vol = statistics.stdev(recent_returns)
    else:
        vol = base_vol

    if vol < 2.0:
        level = "Bajo"
        max_pos = 3.0
    elif vol < 3.5:
        level = "Medio"
        max_pos = 2.0
    else:
        level = "Alto"
        max_pos = 1.0

    notes = [
        f"Volatilidad estimada: {vol:.2f}%",
        f"Riesgo máximo recomendado por trade: {max_pos}%",
        "Solo una posición abierta a la vez",
        "Paper trading activo por defecto",
        "Actualización de referencia después de cada señal"
    ]

    return RiskReport(
        risk_level=level,
        volatility_pct=vol,
        max_position_pct=max_pos,
        recommended_stop=-5.0,
        notes=notes
    )

def project_profit(
    capital: float = 1000,
    risk_per_trade_pct: float = 2.0,
    trades_per_month: int = 12,
    win_rate: float = 0.55,
    reward_risk: float = 1.2
) -> ProfitProjection:
    """
    Educational profit projection based on simple expectancy model.
    """
    risk_amount = capital * (risk_per_trade_pct / 100)
    wins = trades_per_month * win_rate
    losses = trades_per_month * (1 - win_rate)

    gross_profit = wins * risk_amount * reward_risk
    gross_loss = losses * risk_amount
    net = gross_profit - gross_loss
    roi = (net / capital) * 100 if capital > 0 else 0
    max_dd = risk_per_trade_pct * 3  # conservative estimate

    return ProfitProjection(
        capital=capital,
        risk_per_trade_pct=risk_per_trade_pct,
        trades_per_month=trades_per_month,
        expected_monthly_pnl=net,
        expected_monthly_roi=roi,
        estimated_max_drawdown=max_dd,
        win_rate_assumed=win_rate
    )

def best_hours_report() -> List[Dict]:
    """
    Typical high-volatility windows for BNB (UTC).
    Educational / pattern-based.
    """
    return [
        {"window": "13:00 – 16:00 UTC", "volatility": "Alta", "reason": "Apertura USA + solapamiento Europa", "recommendation": "Mejor ventana"},
        {"window": "00:00 – 03:00 UTC", "volatility": "Media-Alta", "reason": "Sesión Asia", "recommendation": "Buena"},
        {"window": "07:00 – 10:00 UTC", "volatility": "Media", "reason": "Apertura Europa", "recommendation": "Moderada"},
        {"window": "20:00 – 23:00 UTC", "volatility": "Baja", "reason": "Cierre USA", "recommendation": "Evitar scalping"},
    ]

if __name__ == "__main__":
    print("=== Risk Analysis ===")
    risk = analyze_risk()
    print(f"Nivel: {risk.risk_level} | Vol: {risk.volatility_pct}% | Max pos: {risk.max_position_pct}%")
    for n in risk.notes:
        print(f"  - {n}")

    print("\n=== Profit Projection ===")
    proj = project_profit(capital=1000, risk_per_trade_pct=2, trades_per_month=12)
    print(f"PnL esperado/mes: {proj.expected_monthly_pnl:.0f} USDT")
    print(f"ROI mensual: {proj.expected_monthly_roi:.1f}%")
    print(f"Max DD estimado: -{proj.estimated_max_drawdown:.1f}%")

    print("\n=== Best Hours ===")
    for h in best_hours_report():
        print(f"{h['window']} | {h['volatility']} | {h['recommendation']}")
