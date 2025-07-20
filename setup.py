from setuptools import find_packages, setup

package_name = 'rosPy'

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
    maintainer='faust',
    maintainer_email='Vitosik3000@gmail.com',
    description='Testing',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = rosPy.publisher_member_function:main',
                'listener = rosPy.subscriber_member_function:main',
        ],
    },
)
