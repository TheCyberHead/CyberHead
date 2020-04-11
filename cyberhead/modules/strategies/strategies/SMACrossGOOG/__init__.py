from . import SMACrossGOOG


def start():
    SMACrossGOOG.run_backtest()
    return 'Backtest performed', 0
