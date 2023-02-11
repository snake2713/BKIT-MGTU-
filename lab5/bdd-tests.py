import builtins
import pathlib
from pathlib import Path
from pytest_bdd import scenario, scenarios, given, when, then, parsers
from main import get_D, get_D2, get_roots

featureFileDir = 'my_features'
featureFile = 'calculation1.feature'
BASE_DIR = Path(__file__).resolve().parent
FEATURE_FILE = BASE_DIR.joinpath(featureFileDir).joinpath(featureFile)

#scenarios("calculation2.feature")

@given(parsers.parse("I have the numbers {num1:d}, {num2:d} and {num3:d}"))
def constants(num1, num2, num3):
    const = [num1, num2, num3]
    return const

@when("I count discriminant")
def counting(const):
    res = const[1] * const[1] - 4 * const[0] * const[2]
    return res

@then(parsers.parse("I expect the result to be {result:d}"))
def comparison(result):
    assert get_D(1, 1, 1) == result

if __name__ == "__main__":
    scenarios("calculation2.feature")