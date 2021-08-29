from run import main

import fileinput

class TestRuntime:
    def test_run_example_a(self, monkeypatch, capsys):
        def example():
            yield "PLACE 0,0,NORTH\n"
            yield "MOVE\n"
            yield "REPORT\n"

        monkeypatch.setattr(fileinput, 'input', example)

        main()
        out, err = capsys.readouterr()
        assert out == "0,1,NORTH\n"

    def test_run_example_b(self, monkeypatch, capsys):
        def example():
            yield "PLACE 0,0,NORTH\n"
            yield "LEFT\n"
            yield "REPORT\n"

        monkeypatch.setattr(fileinput, 'input', example)

        main()
        out, err = capsys.readouterr()
        assert out == "0,0,WEST\n"

    def test_run_example_c(self, monkeypatch, capsys):
        def example():
            yield "PLACE 1,2,EAST\n"
            yield "MOVE\n"
            yield "MOVE\n"
            yield "LEFT\n"
            yield "MOVE\n"
            yield "REPORT\n"

        monkeypatch.setattr(fileinput, 'input', example)

        main()
        out, err = capsys.readouterr()
        assert out == "3,3,NORTH\n"
