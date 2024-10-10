from pathlib import Path
from setuptools import setup, find_packages

cwd = Path(__file__).resolve().parent
requirements = (cwd / 'requirements.txt').read_text().split('\n')

setup_args = dict(
    name='employee_events',
    version='0.0',
    description='SQL Query API',
    packages=find_packages(),
    package_data={'': ['employee_events.db']},
    include_package_data=True,
    install_requirements=requirements,
    )

if __name__ == "__main__":
    setup(**setup_args)