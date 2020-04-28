import pytest
import src.exercise

def test_exercise():
    input_values = ["3","6","8","2","45","45"]
    output = []

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    src.exercise.input = mock_input
    src.exercise.print = lambda s : output.append(s)

    src.exercise.main()

    assert [output[0],output[1],output[2]] == ["","","3 is smaller than 6."]
    assert [output[3],output[4],output[5]] == ["","","8 is greater than 2."]
    assert [output[6],output[7],output[8]] == ["","","45 is equal to 45."]
