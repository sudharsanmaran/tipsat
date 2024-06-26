from enum import Enum
import os


class OutputHeader(Enum):
    SIGNAL = "No. of signals"
    POINTS = "Net Points"
    POINTS_PERCENT = "Net Points Percentage"
    PROBABILITY = "Probability"
    POINTS_PER_SIGNAL = "Net Points Per Signal"
    POINTS_PER_SIGNAL_PERCENT = "Net Points Per Signal Percent"
    RISK_REWARD = "Risk Reward Ratio"
    SIGNAL_DURATION = "Signal Duration (in days)"
    WEIGHTED_AVERAGE_SIGNAL_DURATION = (
        "Weighted Average Signal Duration (in days)"
    )
    RANKING = "Ranking"


class SignalColumns(Enum):
    LONG_PLUS = "Long +"
    LONG_MINUS = "Long -"
    LONG_NET = "Long (Net)"
    SHORT_PLUS = "Short +"
    SHORT_MINUS = "Short -"
    SHORT_NET = "Short (Net)"
    LONG = "Long"
    SHORT = "Short"


class ProbabilityColumns(Enum):
    LONG = "Long"
    SHORT = "Short"
    TOTAL = "Total"


class RankingColumns(Enum):
    PROBABILITY_LONG = "Probability Long"
    PROBABILITY_SHORT = "Probability Short"
    PROBABILITY_TOTAL = "Probability Total"
    NET_POINTS_PER_SIGNAL_LONG_PLUS = "Net Points Long +"
    NET_POINTS_PER_SIGNAL_LONG_MINUS = "Net Points Long -"
    NET_POINTS_PER_SIGNAL_SHORT_PLUS = "Net Points Short +"
    NET_POINTS_PER_SIGNAL_SHORT_MINUS = "Net Points Short -"
    RISK_REWARD_LONG = "R_R_L"
    RISK_REWARD_SHORT = "R_R_S"
    WEIGHTED_AVERAGE_SIGNAL_DURATION_LONG_PLUS = (
        "Weighted Average Signal Duration Long +"
    )
    WEIGHTED_AVERAGE_SIGNAL_DURATION_LONG_MINUS = (
        "Weighted Average Signal Duration Long -"
    )
    WEIGHTED_AVERAGE_SIGNAL_DURATION_SHORT_PLUS = (
        "Weighted Average Signal Duration Short +"
    )
    WEIGHTED_AVERAGE_SIGNAL_DURATION_SHORT_MINUS = (
        "Weighted Average Signal Duration Short -"
    )
    TOTAL = "Total"


TIMEFRAME_OPTIONS = sorted(
    list(
        map(
            lambda x: int(x.strip()),
            os.getenv("TIMEFRAME_OPTIONS", "").split(","),
        )
    )
)
PERIOD_OPTIONS = sorted(
    list(
        map(
            lambda x: int(x.strip()),
            os.getenv("PERIOD_OPTIONS", "").split(","),
        )
    )
)
SD_OPTIONS = sorted(
    list(map(lambda x: int(x.strip()), os.getenv("SD_OPTIONS", "").split(",")))
)


class FirstCycleColumns(Enum):
    DURATION_SIGNAL_START_TO_CYCLE_START = (
        "Duration Signal Start to Cycle Start"
    )
    CYCLE_DURATION = "Cycle Duration"
    MOVE = "Move"
    MOVE_PERCENT = "Move Percent"
    CYCLE_MAX = "Cycle Max"
    CYCLE_MIN = "Cycle Min"
    MAX_TO_MIN = "Max to Min"
    AVERAGE_TILL_MAX = "Average Till Max"
    AVERAGE_TILL_MIN = "Average Till Min"
    POINTS_FRM_AVG_TILL_MAX_TO_MIN = "Points from Avg till Max to Min"
    CLOSE_TO_CLOSE = "Close to Close"
    # DURATION_TO_MAX = "Duration to Max"
    # DURATION_ABOVE_BB = "Duration Above BB"
    # SIGNAL_START_TO_MAX_POINTS = "Signal Start to Max Points"
    # SIGNAL_START_TO_MAX_PERCENT = "Signal Start to Max Percent"
    # CATEGORY = "Category"
    # MOVE_START_TO_MAX_CYCLE_POINTS = "Move Start to Max Cycle Points"
    # MOVE_START_TO_MAX_CYCLE_PERCENT = "Move Start to Max Cycle Percent"
    # POINTS_FRM_AVG_TILL_MIN_TO_MAX = "Points from Avg till Min to Max"
    # SIGNAL_START_TO_MINIMUM_POINTS = "Signal Start to Minimum Points"
    # SIGNAL_START_TO_MINIMUM_PERCENT = "Signal Start to Minimum Percent"
    # DURATION_BETWEEN_MAX_MIN = "Duration Between Max Min"
    # AVG_OF_MAX_TO_AVG_OF_MIN = "Avg of Max to Avg of Min"
    # POSITIVE_NEGATIVE = "Positive / Negative"


class SecondCycleIDColumns(Enum):
    CTC_CYCLE_ID = "CTC Cycle ID"
    MTM_CYCLE_ID = "MTM Cycle ID"


class MTMCrossedCycleColumns(Enum):
    IS_MTM_CROSS_PNT_3 = "IS_MTM Crossed .3"
    IS_MTM_CROSS_PNT_5 = "IS_MTM Crossed .5"
    IS_MTM_CROSS_PNT_75 = "IS_MTM Crossed .75"
    IS_MTM_CROSS_1 = "IS_MTM Crossed 1"


class BB_Band_Columns(Enum):
    MEAN = "MEAN"
    UPPER = "UPPER"
    LOWER = "LOWER"
    # CLOSE = "CLOSE"
    # HIGH = "HIGH"
    # LOW = "LOW"
