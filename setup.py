from setuptools import setup, find_packages

setup(
    name='astro-gearbox',
    version='0.1.0',
    description='A scalar triage heuristic for exoplanet magnetohydrodynamic habitability.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'pandas>=1.3.0',
        'numpy>=1.20.0'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Programming Language :: Python :: 3',
    ],
)