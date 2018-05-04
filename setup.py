import os
from setuptools import setup, Command


class CleanCommand(Command):
    """
    Custom clean command to tidy up the project root
    """
    user_options = []

    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')

setup(
    entry_points = {
        'console_scripts': [
            'fp = python_tools.example_python_tool:main', # this file will go to --> ~/my_virtual_env/bin
        ]
    },
    scripts=[

    ],
    include_package_data = True,
    zip_safe=False,
    cmdclass={
        'clean': CleanCommand,
    }
)
