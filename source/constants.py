from enum import Enum


class TradeExitType(Enum):
    FRACTAL = "Fractal Exit"
    SIGNAL = "Signal Change"
    TRAILING = "Trailling"
    END = "Trade End Exit"


class TradeType(Enum):
    INTRADAY = "intraday"
    POSITIONAL = "positional"


class MarketDirection(Enum):
    LONG = "long"
    SHORT = "short"
    PREVIOUS = "previous"
    ALL = "all"


POSSIBLE_STRATEGY_IDS = list(range(1, 11))


fractal_columns = [
    "P_1_FRACTAL_LONG",
    "P_1_FRACTAL_SHORT",
    "P_1_FRACTAL_CONFIRMED_LONG",
    "P_1_FRACTAL_CONFIRMED_SHORT",
]

fractal_column_dict = {
    "entry": {
        MarketDirection.LONG: "entry_P_1_FRACTAL_LONG",
        MarketDirection.SHORT: "entry_P_1_FRACTAL_SHORT",
    },
    "exit": {
        MarketDirection.LONG: "exit_P_1_FRACTAL_LONG",
        MarketDirection.SHORT: "exit_P_1_FRACTAL_SHORT",
    },
}

confirm_fractal_column_dict = {
    "entry": {
        MarketDirection.LONG: "entry_P_1_FRACTAL_CONFIRMED_LONG",
        MarketDirection.SHORT: "entry_P_1_FRACTAL_CONFIRMED_SHORT",
    },
    "exit": {
        MarketDirection.LONG: "exit_P_1_FRACTAL_CONFIRMED_LONG",
        MarketDirection.SHORT: "exit_P_1_FRACTAL_CONFIRMED_SHORT",
    },
}
