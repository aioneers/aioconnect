import shutil
import os
from pathlib import Path
import subprocess


def test_make_html(capsys):
    def _run_process_func(exe: str, cwd=None):
        p = subprocess.Popen(
            exe, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, cwd=cwd
        )
        while True:
            # returns None while subprocess is running
            retcode = p.poll()
            line = p.stdout.readline().decode("utf8")
            yield line
            if retcode is not None:
                break

    def run_process(exe: str, cwd=None):
        """Run a command line task with real-time output

        The function outputs the results as soon as they are available

        Parameters
        ----------
        exe : str
            The string that should be executed by the local shell
        cwd : str = None
            Working directory where the command should be executed

        Examples
        --------
        >>> import aio_data_science_py as aio
        >>> def test_run_process(capsys):
        >>>     aio.run_process(exe = "az --version")
        >>>     captured = capsys.readouterr()
        """
        print(f"running cmd: {exe}")

        for line in _run_process_func(exe, cwd=cwd):
            print(line, end="", flush=True)

    path_to_docs = str(Path(os.path.abspath(__file__)).parent.parent) + "/doc"
    run_process(exe="make html", cwd=path_to_docs)

    captured = capsys.readouterr().out
    print(captured.split("\n"))

    assert captured.find("WARNING:") == -1
    assert captured.find("build succeeded") != -1

    # For some reason this does not work on the pipeline
    shutil.rmtree(path_to_docs + "/build")
