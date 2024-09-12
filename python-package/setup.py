from setuptools import setup, find_packages

setup_args = dict(
    name='employee_events',
    version='0.0',
    description='SQL Query API',
    packages=find_packages(),
    package_data={'': ['employee_events.db']},
    include_package_data=True,
    install_requires=[
        "pandas==1.5.2"
        ]
    )

if __name__ == "__main__":
    setup(**setup_args)