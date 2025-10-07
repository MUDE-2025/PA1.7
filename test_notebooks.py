from testbook import testbook


def test_debug_notebook_runs():
    # Execute the bundled notebook end-to-end and ensure it runs without errors.
    with testbook('debug_notebook.ipynb', execute=True):
        pass
