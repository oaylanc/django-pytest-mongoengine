from django.core import management
from django.core.management.commands import test
from django.core.management.commands import syncdb
from django.conf import settings
from django.core.management.base import BaseCommand
from optparse import make_option


class Command(test.Command):
    option_list = test.Command.option_list + (
        make_option('-k', action='store', dest='keyword', default='',
            help='Tell py.test to filter out tests that don\'t contain keyword'),
        make_option('-s', action='store_false', dest='capture', default=False,
            help='Tell py.test not to capture output. Useful for dropping to ipython shells'),
        make_option('-x', action='store_true', dest='', default=False,
            help='exit instantly on first error or failed test.'),
        make_option('--pdb', action='store_false', dest='pdb', default=False,
            help='Start the python debugger on errors'),
    )

    def run_from_argv(self, argv):
        # Separate Django command options from py.test ones with -- to ensure
        # that Django is not complaining about unknown options.
        try:
            args = argv[:argv.index('--')]
            super(Command, self).run_from_argv(args)
        except ValueError:
            super(Command, self).run_from_argv(argv)
