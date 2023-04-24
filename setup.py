from setuptools import setup, find_packages

setup(
    name='PDFmanipulator_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'os',
        'subprocess',
        'PyPDF2', 'shutil','io'
    ],
    author='Thalia',
    author_email='xi1le7@gmail.com',
    description='Manipulation de PDF',
    url='https://github.com/thabe03/pdfmanipulator',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
