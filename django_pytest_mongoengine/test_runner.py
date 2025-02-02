def run_tests(test_labels, verbosity=1, interactive=True, extra_tests=[]):
    import sys
    from pkg_resources import load_entry_point
    sys.argv[1:] = sys.argv[2:]

    # Remove stop word (--) from argument list again. This separates Django
    # command options from py.test ones.
    try:
        del sys.argv[sys.argv.index('--')]
    except ValueError:
        pass

    sys.exit(
        load_entry_point('pytest>=2.0', 'console_scripts', 'py.test')()
    )
