from . import SMACrossAPPL


def start():
    SMACrossAPPL.run_backtest()
    return 'Backtest performed', 0
