from typing import Optional, Sequence

import pytest

from d3rlpy.algos import (
    DecisionTransformerConfig,
    DiscreteDecisionTransformerConfig,
)

from ...testing_utils import create_scaler_tuple
from .algo_test import algo_tester


@pytest.mark.parametrize("observation_shape", [(100,), (4, 84, 84)])
@pytest.mark.parametrize("scalers", [None, "min_max"])
def test_decision_transformer(
    observation_shape: Sequence[int],
    scalers: Optional[str],
) -> None:
    observation_scaler, action_scaler, reward_scaler = create_scaler_tuple(
        scalers
    )
    config = DecisionTransformerConfig(
        observation_scaler=observation_scaler,
        action_scaler=action_scaler,
        reward_scaler=reward_scaler,
    )
    dt = config.create()
    algo_tester(
        dt,  # type: ignore
        observation_shape,
    )


@pytest.mark.parametrize("observation_shape", [(100,), (4, 84, 84)])
@pytest.mark.parametrize("scalers", [None, "min_max"])
def test_discrete_decision_transformer(
    observation_shape: Sequence[int],
    scalers: Optional[str],
) -> None:
    observation_scaler, _, reward_scaler = create_scaler_tuple(scalers)
    config = DiscreteDecisionTransformerConfig(
        observation_scaler=observation_scaler,
        reward_scaler=reward_scaler,
    )
    dt = config.create()
    algo_tester(
        dt,  # type: ignore
        observation_shape,
        action_size=10,
    )
