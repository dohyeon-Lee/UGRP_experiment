from setuptools import find_packages, setup

package_name = 'reading_sensor'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='dohyeon',
    maintainer_email='dohyeon@postech.ac.kr',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'reading_sensor = reading_sensor.reading_sensor:main',
       	 	'sign_pub = reading_sensor.pub_sign:main',
        ],
    },
)
